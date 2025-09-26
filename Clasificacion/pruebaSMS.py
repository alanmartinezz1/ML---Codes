import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import AdaBoostClassifier, GradientBoostingClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA # Se mantiene solo para los otros datasets

# ===================== FUNCIÓN GENÉRICA DE ENTRENAMIENTO Y MÉTRICAS =====================
def run_classifier_and_plot(X, y, dataset_name, classifier_type="GB"):
    """Entrena el clasificador y muestra la matriz de confusión y el reporte."""
    print(f"\n========== {dataset_name} - {classifier_type} ==========")

    # Imputación y Escalado (para consistencia, aunque no sea crucial para TF-IDF)
    if not isinstance(X, np.ndarray):
        X = X.toarray() if hasattr(X, 'toarray') else X
    
    imputer = SimpleImputer(strategy="mean")
    X = imputer.fit_transform(X)
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Train/Test Split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

    # Inicializar y entrenar el clasificador
    if classifier_type == "GB":
        clf = GradientBoostingClassifier(n_estimators=100, random_state=42)
    elif classifier_type == "AB":
        clf = AdaBoostClassifier(n_estimators=100, random_state=42)
    else:
        raise ValueError("Clasificador no reconocido. Use 'GB' o 'AB'.")

    clf.fit(X_train, y_train)

    # Predicciones y métricas
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))
    
    # Matriz de Confusión
    cm = confusion_matrix(y_test, y_pred)
    ConfusionMatrixDisplay(cm).plot(cmap="Blues")
    plt.title(f"Matriz de Confusión - {dataset_name} ({classifier_type})")
    plt.show()

    return clf

# ===================== BLOQUE ESPECÍFICO PARA SMS SPAM =====================

# 1. Carga de Datos y Vectorización
df_sms = pd.read_csv("SMSSpamCollection", sep="\t", names=["label", "msg"])
df_sms["label"] = df_sms["label"].map({"ham": 0, "spam": 1})
y_sms = df_sms["label"]

vec = TfidfVectorizer()
X_sms = vec.fit_transform(df_sms["msg"])
feature_names = vec.get_feature_names_out()

# 2. Entrenar y obtener métricas para ambos clasificadores (Alta Dimensión)
# NOTA: Los clasificadores aquí se entrenan en ALTA DIMENSIÓN, lo cual es correcto.
clf_gb_hd = run_classifier_and_plot(X_sms, y_sms, "SMS Spam", classifier_type="GB")
clf_ab_hd = run_classifier_and_plot(X_sms, y_sms, "SMS Spam", classifier_type="AB")


# 3. Preparación de Datos 2D (Usando Top 2 Features de GB para la visualización)
# Usamos las importancias de GB ya que suele ser más estable.
importances = clf_gb_hd.feature_importances_
top_2_indices = np.argsort(importances)[-2:]
top_2_names = feature_names[top_2_indices]

# Crear el nuevo dataset 2D con SOLO esas 2 features
X_2d_best = X_sms.toarray()[:, top_2_indices]
y_2d = y_sms

# 4. Entrenar Clasificadores en 2D (solo para la gráfica de frontera)
X_train2d, _, y_train2d, _ = train_test_split(X_2d_best, y_2d, test_size=0.3, random_state=42)

clf_gb_2d = GradientBoostingClassifier(n_estimators=100, random_state=42)
clf_gb_2d.fit(X_train2d, y_train2d)

clf_ab_2d = AdaBoostClassifier(n_estimators=100, random_state=42)
clf_ab_2d.fit(X_train2d, y_train2d)


# 5. Función de Graficado de Frontera (para ambos modelos)
def plot_decision_boundary(clf, X_2d, y_2d, title, feature_names):
    x_min, x_max = X_2d[:, 0].min() - 0.05, X_2d[:, 0].max() + 0.05
    y_min, y_max = X_2d[:, 1].min() - 0.05, X_2d[:, 1].max() + 0.05
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.005),
                         np.arange(y_min, y_max, 0.005))
    
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.figure(figsize=(8, 6))
    # Usamos cmap=plt.cm.RdYlBu para que el rojo/azul sean claros
    plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.RdBu) 
    
    # Graficar los puntos de datos reales
    scatter = plt.scatter(X_2d[:, 0], X_2d[:, 1], c=y_2d, cmap=plt.cm.RdBu, edgecolor='k', alpha=0.7)
    
    # Crear leyenda manual para las clases
    legend1 = plt.legend(*scatter.legend_elements(), title="Clases")
    plt.gca().add_artist(legend1)
    
    plt.xlabel(f"Feature 1: {feature_names[0]} (TF-IDF)")
    plt.ylabel(f"Feature 2: {feature_names[1]} (TF-IDF)")
    plt.title(title)
    plt.show()


# 6. Graficar para AdaBoost y Gradient Boosting
plot_decision_boundary(clf_ab_2d, X_2d_best, y_2d, 
                       f"Frontera de Decisión (AdaBoost) - SMS Spam (Top 2 Features)", 
                       top_2_names)

plot_decision_boundary(clf_gb_2d, X_2d_best, y_2d, 
                       f"Frontera de Decisión (Gradient Boosting) - SMS Spam (Top 2 Features)", 
                       top_2_names)