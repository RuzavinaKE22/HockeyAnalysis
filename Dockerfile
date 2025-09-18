# ---------- Базовый образ ----------
FROM python:3.11-slim

# ---------- Переменные окружения ----------
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

# ---------- Рабочая директория ----------
WORKDIR /app

# ---------- Установка зависимостей ----------
COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

# ---------- Копируем проект ----------
COPY . .

# ---------- Порт (Streamlit по умолчанию использует 8501) ----------
EXPOSE 8501

# ---------- Команда запуска ----------
CMD ["streamlit", "run", "streamlit_app.py", "--server.address=0.0.0.0"]
