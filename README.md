

# Frontend & Backend Enhancements (July 2025)

- Updated `style.css` with improved, modern styles for forms, buttons, selects, and layout, including subtle animations for a more interactive user experience.
- All previous styles are preserved and enhanced for better consistency and usability.
- Backend: Added/updated the `/api/sentiment-heatmap` endpoint in `app.py` to provide the "Sentiment Score Heatmap (Last 7 Days)" feature, aggregating sentiment scores for the last 7 days per stock.
- These changes improve both the look and functionality of the Enter News and Heatmap features.
=======
#  Stock Trend Prediction using Financial News Sentiment Score  
> ML-powered forecasting system that integrates real-time news sentiment and historical stock data for stock price prediction.

![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-Production--Ready-brightgreen)
![Deployment](https://img.shields.io/badge/deployed-Vercel%20%7C%20Render-blue)

---

## 🧠 Overview

This project demonstrates an end-to-end machine learning pipeline that predicts stock prices by combining sentiment analysis of financial news with historical market data. A Multi-Layer Perceptron (MLP) Regressor is trained on engineered features to forecast trends and visualize price movement over the next 7 days.

The project uses:
- Real-time web scraping (LiveMint, MoneyControl)
- Sentiment analysis using VADER
- Stock data from Yahoo Finance (`yfinance`)
- Feature engineering with technical indicators (support/resistance)
- MLP model for predictions
- MongoDB Atlas for data storage
- Flask + Docker for deployment

---

## 🚀 Features

- ✅ Live news scraping via BeautifulSoup/Selenium
- ✅ VADER sentiment scoring with compound score (-1 to 1)
- ✅ yFinance-based stock price collection (Open, Close, High, Low)
- ✅ Data cleaning, normalization, Min-Max scaling
- ✅ Feature engineering: Previous Close, Price Change, Support/Resistance
- ✅ MLP Regressor with evaluation metrics: MSE, MAE, R²
- ✅ Visualization with Matplotlib
- ✅ Flask web interface
- ✅ Docker-ready deployment with Render & Vercel

---

## 🧪 Workflow

1. **Data Collection**  
   - Scrapes news from LiveMint, MoneyControl  
   - Pulls stock data using `yfinance`

2. **Preprocessing & Sentiment Analysis**  
   - Applies VADER sentiment scoring  
   - Aggregates sentiment on 7-day rolling window  
   - Cleans and normalizes data
3. **Feature Engineering**  
   - Merges sentiment and stock data  
   - Adds Previous Close, Price Change, Support, Resistance

5. **Prediction & Visualization**  
   - Forecasts next 7-day stock trends  
   - Plots actual vs predicted data

6. **Deployment**  
   - Dockerized Flask API  
   - Deployed using Vercel + Render  
   - MongoDB Atlas stores predictions
---

## 📊 Results

| Metric         | Value       |
|----------------|-------------|
| R² Score       | 0.72        |
- **Languages:** Python, HTML, CSS, JavaScript  
- **Web Scraping:** BeautifulSoup, Selenium  
- **Deployment:** Flask, Docker, Vercel, Render  
- **Database:** MongoDB Atlas  
- **Visualization:** Matplotlib  
- Calculated **support/resistance levels** for technical market analysis  
- Deployed on **Render + Vercel** using Docker  
- Built with **modular architecture** and tested under multi-user load  

---

## 🔮 Future Enhancements

- [ ] Add LSTM for temporal forecasting  
- [ ] Integrate finBERT for domain-specific sentiment  
- [ ] Add Twitter-based sentiment scraping  
- [ ] Enable email alerts for high-confidence predictions  
- [ ] Real-time chart dashboard with user watchlists

---

## 📁 Missing Files Notice

Some model files (`.pkl`), datasets, or API keys may be excluded due to size or security policies. Use the report and available codebase for testing and replication.

---

## 📜 Report

👉 Full technical documentation and project report is available in the repository under `Project Report.pdf`.

---

## 👨‍💻 Author

**Raghvendra Singh**  
📧 [raghvendrarajivasingh07@gmail.com](mailto:raghvendrarajivasingh07@gmail.com)  
🔗 [LinkedIn Profile](https://linkedin.com/in/Raghvendra-Singh04)

---

---



![Stock Prediction System Architecture_page-0001](https://github.com/user-attachments/assets/e816aecf-e885-4ed3-8f5f-7d69fda7694b)



![Stock Prediction System Architecture_page-0002](https://github.com/user-attachments/assets/75ef9748-fd63-4ad8-873d-b9906814e0a7)





