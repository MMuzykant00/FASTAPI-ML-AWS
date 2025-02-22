# Pobranie oficjalnego obrazu Pythona
FROM python:3.10

# Ustawienie katalogu roboczego w kontenerze
WORKDIR /app

# Skopiowanie plików projektu
COPY . /app

# Instalacja zależności
RUN pip install --no-cache-dir -r requirements.txt

# Otworzenie portu 8000
EXPOSE 8000

# Uruchomienie aplikacji
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
