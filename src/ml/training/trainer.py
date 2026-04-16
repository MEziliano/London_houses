import pandas as pd
import numpy as np
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from src.data.data_processor import build_preprocessing_pipeline

def train_and_save_model(data_path, model_type="xgboost"):
    """
    Carrega dados, treina um modelo de regressão e salva o modelo e o preprocessor.
    """
    print(f"Lendo dados de {data_path}...")
    df = pd.read_csv(data_path)
    
    X = df.drop("median_house_value", axis=1)
    y = df["median_house_value"].copy()
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print("Construindo pipeline de pré-processamento...")
    preprocessor = build_preprocessing_pipeline()
    X_train_prepared = preprocessor.fit_transform(X_train)
    X_test_prepared = preprocessor.transform(X_test)
    
    if model_type == "xgboost":
        print("Treinando XGBoost...")
        model = XGBRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
    elif model_type == "random_forest":
        print("Treinando RandomForest...")
        model = RandomForestRegressor(n_estimators=100, random_state=42)
    else:
        raise ValueError(f"Modelo {model_type} não suportado.")
        
    model.fit(X_train_prepared, y_train)
    
    # Avaliação
    predictions = model.predict(X_test_prepared)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)
    
    print(f"Modelo {model_type} treinado com sucesso!")
    print(f"RMSE: {rmse:,.2f}")
    print(f"R2 Score: {r2:.4f}")
    
    # Salvar
    os.makedirs('models/trained_models', exist_ok=True)
    joblib.dump(model, f'models/trained_models/{model_type}_model.pkl')
    joblib.dump(preprocessor, 'models/trained_models/preprocessor.pkl')
    print("Artefatos salvos em models/trained_models/")
    
    return model, preprocessor

if __name__ == "__main__":
    train_and_save_model("data/housing.csv", model_type="xgboost")
