# ==============================
# 🧪 Wine Quality Regression Comparison
# Models: ElasticNetCV, RidgeCV, LassoCV
# ==============================

# 1️⃣ Import libraries
import pandas as pd
from ucimlrepo import fetch_ucirepo
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import ElasticNetCV, RidgeCV, LassoCV
from sklearn.metrics import mean_squared_error, r2_score

# 2️⃣ Load the dataset
wine_quality = fetch_ucirepo(id=186)

X = wine_quality.data.features
y = wine_quality.data.targets.squeeze()

df  = pd.concat([X, y.rename('quality')], axis =1)
print(df.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

result = {}

models = {
    "ElasticNetCV": ElasticNetCV(cv=10, random_state=42),
    "RidgeCV": RidgeCV(cv=10),
    "LassoCV": LassoCV(cv=10, random_state=42),
}

for name, model in models.items():
    model.fit(X_train_scaled, y_train)
    y_pred = model.predict(X_test_scaled)

    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    data = {
        "mse":mse,
        "r2":r2,
    }
    result[name]=data


# print("\n===== FORMATTED SUMMARY =====")
print(f"ElasticNetCV  → MSE: {result["ElasticNetCV"]["mse"]:.4f}, R²: {result["ElasticNetCV"]["r2"]:.4f}")
print(f"RidgeCV  → MSE: {result["RidgeCV"]["mse"]:.4f}, R²: {result["RidgeCV"]["r2"]:.4f}")
# print(f"RidgeCV       → MSE: {mse_ridge:.4f}, R²: {r2_ridge:.4f}")
# print(f"LassoCV       → MSE: {mse_lasso:.4f}, R²: {r2_lasso:.4f}")
