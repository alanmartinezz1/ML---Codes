import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.datasets import load_diabetes
import seaborn as sns

# interfaz
def clear_frame():
    for widget in frame.winfo_children():
        widget.destroy()

def show_menu():
    clear_frame()
    tk.Label(frame, text="Selecciona un dataset", font=("Arial", 14)).pack(pady=10)

    datasets = ["Car Price", "Concrete Compressive", "Diabetes", "Wine Quality (red)", "Iris", "Boston House"]
    for ds in datasets:
        ttk.Button(frame, text=ds, command=lambda d=ds: train_and_plot(d)).pack(pady=5)
        

def load_and_preprocess_data(dataset_name):
    try:
        if dataset_name == 'Car Price':
            df = pd.read_csv('car data.csv')
            df.dropna(inplace=True)
            X = df.drop(['Car_Name', 'Selling_Price'], axis=1)
            y = df['Selling_Price']
            X = pd.get_dummies(X, columns=['Fuel_Type', 'Seller_Type', 'Transmission'], drop_first=True)
            
        elif dataset_name == 'Concrete Compressive':
            df = pd.read_csv('Concrete_Data.csv')
            df.columns = df.columns.str.strip()
            df.dropna(inplace=True)
            
            strength_column = None
            for col in df.columns:
                if 'strength' in col.lower():
                    strength_column = col
                    break
            
            if strength_column is None:
                raise ValueError("Dataset no disponible.")
            
            y = df[strength_column]
            X = df.drop(strength_column, axis=1)
        
        elif dataset_name == 'Diabetes':
            data = load_diabetes()
            X, y = pd.DataFrame(data.data, columns=data.feature_names), pd.Series(data.target)
            
        elif dataset_name == "Wine Quality (red)":
            df = pd.read_csv("winequality-red.csv", sep=";")
            X, y = df.drop("quality", axis=1), df["quality"]
            
        elif dataset_name == 'Iris':
            df = pd.read_csv('Iris.csv')
            df.dropna(inplace=True)
            X = df.drop(['PetalLengthCm', 'Species', 'Id'], axis=1, errors='ignore')
            y = df['PetalLengthCm']
            if 'Species' in df.columns:
                species_dummies = pd.get_dummies(df['Species'], drop_first=True)
                X = pd.concat([X, species_dummies], axis=1)
            
        elif dataset_name == 'Boston House':
            column_names = [
                "CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS",
                "RAD","TAX","PTRATIO","B","LSTAT","MEDV"
            ]
            df = pd.read_csv("housing.csv", delim_whitespace=True, header=None, names=column_names)
            df.dropna(inplace=True)

            X = df.drop("MEDV", axis=1)
            y = df["MEDV"]
            
        else:
            raise ValueError("Dataset no disponible.")

        # Escalar los datos si no son un arreglo de NumPy (como los de Diabetes)
        if not isinstance(X, np.ndarray):
            scaler = StandardScaler()
            X = scaler.fit_transform(X)
        
        return X, y
    
    except FileNotFoundError:
        messagebox.showerror("Error de Archivo", f"No se encontró el archivo de datos para '{dataset_name}'.")
        return None, None
    except Exception as e:
        messagebox.showerror("Error de Procesamiento", f"Ocurrió un error al procesar el dataset:\n{e}")
        return None, None

def train_and_plot(dataset_name):
    clear_frame()


    canvas = tk.Canvas(frame)
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    
    # Paso 2: Ajustar parámetros del modelo
    models = {
        "Regresión Lineal": LinearRegression(),
        "Random Forest": RandomForestRegressor(n_estimators=200, random_state=42),
        "KNN": KNeighborsRegressor(n_neighbors=5),
        "MLP": MLPRegressor(hidden_layer_sizes=(100,50), max_iter=2000, random_state=42)
    }

        #  Paso 3: Preparar datos para alimentar al modelo 
    X, y = load_and_preprocess_data(dataset_name)
    
    if X is None or X.size == 0:
        messagebox.showerror("Error", "No se pudieron cargar los datos. Volviendo al menú.")
        show_menu()
        return
        
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


    results = {}
    best_model, best_r2 = None, -999

    for name, model in models.items():


        
        # Paso 4: Ajuste del modelo 
        model.fit(X_train, y_train)
        
        # Paso 5: Predecir resultados 
        y_pred = model.predict(X_test)
        
    # Paso 6: Evaluar modelo 
        mse = mean_squared_error(y_test, y_pred)
        rmse = np.sqrt(mse)  
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        results[name] = {
            'mse': mse,
            'rmse': rmse,
            'mae': mae,
            'r2': r2,
            'y_test': y_test,
            'y_pred': y_pred
        }
        
        if r2 > best_r2:
            best_r2, best_model = r2, name

    #  Mostrar resultados y gráficas
    tk.Label(scrollable_frame, text=f"Resultados para el dataset: {dataset_name}", font=("Arial", 14, "bold")).pack(pady=10)

    for name, metrics in results.items():
        tk.Label(scrollable_frame, text=f"{name}:\nMAE={metrics['mae']:.2f}\nMSE={metrics['mse']:.2f}\nRMSE={metrics['rmse']:.2f}\nR²={metrics['r2']:.3f}", font=("Arial", 12), fg="green").pack(pady=5)
        
        y_test = metrics['y_test']
        y_pred = metrics['y_pred']

    
        fig, ax = plt.subplots(figsize=(5, 4))
        sns.regplot(x=y_test, y=y_pred, scatter_kws={'alpha':0.6}, line_kws={'color':'red', 'linestyle':'--'}, ax=ax)
        ax.set_title(name)
        ax.set_xlabel("Valor real")
        ax.set_ylabel("Valor predicho")
        ax.grid(True)
        plt.tight_layout()

        canvas_fig = FigureCanvasTkAgg(fig, master=scrollable_frame)
        canvas_fig.draw()
        canvas_fig.get_tk_widget().pack(pady=10)

    # mejor modelo
    msg = f"El mejor modelo fue: {best_model} (R²={best_r2:.3f})."
    tk.Label(scrollable_frame, text=msg, fg="blue", font=("Arial", 12, "bold")).pack(pady=10)

    ttk.Button(scrollable_frame, text="Volver al menú", command=show_menu).pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Modelos de Regresión")
    root.geometry("900x700")

    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)

    show_menu()
    root.mainloop()