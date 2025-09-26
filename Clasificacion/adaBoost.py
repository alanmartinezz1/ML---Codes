import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris, load_digits
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
import idx2numpy

# ===================== FUNCIÓN GENÉRICA =====================
def run_adaboost(X, y, dataset_name="Dataset"):
    print(f"\n========== {dataset_name} ==========")

    # ==================== Imputación de NaN ====================
    imputer = SimpleImputer(strategy="mean")
    X = imputer.fit_transform(X)

    # ==================== Escalado ====================
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # ==================== PCA 2D para visualización ====================
    pca = PCA(n_components=2)
    X_2d = pca.fit_transform(X_scaled)

    # ==================== Visualización inicial ====================
    plt.figure(figsize=(6,5))
    plt.scatter(X_2d[:,0], X_2d[:,1], c=y, cmap="tab10", alpha=0.7)
    plt.title(f"Visualización inicial (PCA) - {dataset_name}")
    plt.show()

    # ==================== Train/Test ====================
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

    # ==================== Modelo AdaBoost ====================
    clf = AdaBoostClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)

    # ==================== Predicciones y métricas ====================
    y_pred = clf.predict(X_test)
    print(classification_report(y_test, y_pred))
    cm = confusion_matrix(y_test, y_pred)
    ConfusionMatrixDisplay(cm).plot(cmap="Blues")
    plt.title(f"Matriz de Confusión - {dataset_name}")
    plt.show()

    # ==================== Frontera de decisión (2D) ====================
    X_train2d, X_test2d, y_train2d, y_test2d = train_test_split(X_2d, y, test_size=0.3, random_state=42)
    clf2d = AdaBoostClassifier(n_estimators=100, random_state=42)
    clf2d.fit(X_train2d, y_train2d)

    x_min, x_max = X_2d[:, 0].min() - 1, X_2d[:, 0].max() + 1
    y_min, y_max = X_2d[:, 1].min() - 1, X_2d[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.05),
                         np.arange(y_min, y_max, 0.05))
    Z = clf2d.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.figure(figsize=(6,5))
    plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.Set1)
    plt.scatter(X_2d[:,0], X_2d[:,1], c=y, cmap="tab10", edgecolor="k", alpha=0.7)
    plt.title(f"Frontera de decisión (AdaBoost) - {dataset_name}")
    plt.show()


# ===================== USO CON LOS DATASETS =====================

# 1) IRIS
iris = load_iris()
run_adaboost(iris.data, iris.target, "Iris")

# 2) DIGITS
digits = load_digits()
run_adaboost(digits.data, digits.target, "Digits")

# 3) BREAST CANCER (CSV)
df_bc = pd.read_csv("data.csv")  # ruta correcta
X_bc = df_bc.drop(["id", "diagnosis"], axis=1, errors="ignore")
y_bc = df_bc["diagnosis"].map({"M":1, "B":0})
run_adaboost(X_bc, y_bc, "Breast Cancer")

# 4) HEART
df_heart = pd.read_csv("heart.csv")
X_h = df_heart.drop("target", axis=1)
y_h = df_heart["target"]
run_adaboost(X_h, y_h, "Heart Disease")

# 5) ADULT
df_adult = pd.read_csv("adult.csv")
df_adult = pd.get_dummies(df_adult)
target_col = [col for col in df_adult.columns if "income_>50K" in col][0]
X_a = df_adult.drop(target_col, axis=1)
y_a = df_adult[target_col]
run_adaboost(X_a, y_a, "Adult Census")

# 6) BANK
df_bank = pd.read_csv("bank.csv", sep=",")
df_bank.columns = df_bank.columns.str.strip()
print(df_bank.columns)  # Verificar nombres de columnas
df_bank['deposit'] = df_bank['deposit'].map({'no':0, 'yes':1})
y_b = df_bank['deposit']
X_b = df_bank.drop('deposit', axis=1)
X_b = pd.get_dummies(X_b)
run_adaboost(X_b, y_b, "Bank Marketing")

# 7) TITANIC
df_titanic = pd.read_csv("titanic.csv")
df_titanic = df_titanic.drop(columns=["PassengerId","Name","Ticket","Cabin"], errors="ignore")
df_titanic = pd.get_dummies(df_titanic)
X_t = df_titanic.drop("Survived", axis=1)
y_t = df_titanic["Survived"]
run_adaboost(X_t, y_t, "Titanic")

# 8) MNIST
# t10k-images.idx3-ubyte -> imágenes de prueba
# t10k-labels.idx1-ubyte -> etiquetas de prueba
X_mnist = idx2numpy.convert_from_file('t10k-images.idx3-ubyte')
y_mnist = idx2numpy.convert_from_file('t10k-labels.idx1-ubyte')

# X viene como (num_samples, 28,28), aplanamos a 2D (num_samples, 784)
num_samples = X_mnist.shape[0]
X_mnist = X_mnist.reshape(num_samples, -1)

# ===================== Ejecutar AdaBoost =====================
run_adaboost(X_mnist, y_mnist, "MNIST")

# 9) SPAM vs HAM
df_sms = pd.read_csv("SMSSpamCollection", sep="\t", names=["label","msg"])
df_sms["label"] = df_sms["label"].map({"ham":0, "spam":1})
from sklearn.feature_extraction.text import TfidfVectorizer
vec = TfidfVectorizer()
X_sms = vec.fit_transform(df_sms["msg"])
y_sms = df_sms["label"]
run_adaboost(X_sms.toarray(), y_sms, "SMS Spam")
