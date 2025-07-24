# ---- Base Image ----
FROM python:3.10-slim

# ---- Set Environment Variables ----
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ---- Set Work Directory ----
WORKDIR /app

# ---- Install System Dependencies ----
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libxml2 \
    libxslt1-dev \
    chromium-driver \
    tesseract-ocr \
    wget \
    unzip \
    && apt-get clean

# ---- Install Python Dependencies ----
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# ---- Copy Project Files ----
COPY . .

# ---- Expose Port & Run ----
EXPOSE 5000

# ---- Start Flask App ----
CMD ["python", "app/app.py"]
