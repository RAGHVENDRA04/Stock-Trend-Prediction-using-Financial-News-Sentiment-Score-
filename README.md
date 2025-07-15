# 📈 Stock Trend Prediction using Financial News Sentiment Score  
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
- ✅ MongoDB Atlas for storing predictions/logs
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

4. **Model Training**  
   - Trains MLP Regressor using scikit-learn  
   - Evaluates using MSE, MAE, R²

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
| MAE            | 14.21       |
| MSE            | 308.77      |

---

## 🧰 Tech Stack

- **Languages:** Python, HTML, CSS, JavaScript  
- **ML & NLP:** Scikit-learn, VADER, NumPy, Pandas  
- **Web Scraping:** BeautifulSoup, Selenium  
- **Deployment:** Flask, Docker, Vercel, Render  
- **Database:** MongoDB Atlas  
- **Visualization:** Matplotlib  

---


---

## 🧠 Resume-Aligned Highlights

- Integrated **real-time financial sentiment** with stock forecasting  
- Trained and deployed a **neural network model (MLP)** for time-series prediction  
- Calculated **support/resistance levels** for technical market analysis  
- Used **MongoDB Atlas** to manage over 1 lakh+ financial records  
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
📍 Pune, India  
📧 [raghvendrarajivasingh07@gmail.com](mailto:raghvendrarajivasingh07@gmail.com)  
🔗 [LinkedIn Profile](https://linkedin.com/in/Raghvendra-Singh04)

---







![Uploading Stock Prediction System Architecture_page-0001.jpg…]()







![Uploading Stock Prediction System Architecture_page-0002.jpg…]()


















