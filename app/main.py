import pandas as pd
import numpy as np
import joblib
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from io import StringIO
import os

app = FastAPI()

# Ścieżka do modelu w folderze 'model'
model_path = os.path.join("model", "random_forest_model.pkl")

# Wczytanie zapisanego modelu
model_rf = joblib.load(model_path)  # Zmienna dla modelu RandomForest


# Funkcja do przetwarzania danych CSV
def process_data(csv_data: str):
    df = pd.read_csv(StringIO(csv_data))  # Wczytanie CSV z danych wejściowych

    # Upewnijmy się, że kolumny są w takim samym formacie jak wcześniej
    # Przykład: usunięcie kolumny 'car' i zastąpienie brakujących wartości
    df.drop("car", axis=1, inplace=True)
    for column in [
        "Bar",
        "CarryAway",
        "CoffeeHouse",
        "RestaurantLessThan20",
        "Restaurant20To50",
    ]:
        df[column] = df[column].fillna(df[column].mode()[0])

    # Modyfikacja kolumny Time
    time_to_part_of_day = {
        "2PM": "popołudnie",
        "10AM": "rano",
        "6PM": "wieczór",
        "7AM": "wczesny_ranek",
        "10PM": "noc",
    }
    df["time"] = df["time"].map(time_to_part_of_day)

    # Zakodowanie danych kategorycznych (Label Encoding)
    from sklearn.preprocessing import LabelEncoder

    for column in df.select_dtypes(include=["object"]).columns:
        le = LabelEncoder()
        df[column] = le.fit_transform(df[column])

    return df


# Endpoint do predykcji z pliku CSV
@app.post("/predict-file/")
async def predict_file(file: UploadFile = File(...)):
    content = await file.read()
    csv_data = content.decode("utf-8")  # Zdekodowanie danych w pliku CSV
    df = process_data(csv_data)  # Przetwarzanie danych

    # Upewnij się, że mamy te same kolumny co w oryginalnym zbiorze
    X = df.drop("Y", axis=1)  # Otrzymujemy dane bez kolumny 'Y'

    # Predykcja za pomocą modelu
    predictions = model_rf.predict(X)  # Predykcja na przetworzonych danych
    return {"predictions": predictions.tolist()}  # Zwróć predykcje w formie listy
