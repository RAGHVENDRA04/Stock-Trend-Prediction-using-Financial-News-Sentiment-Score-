# Stock-Trend-Prediction-using-Financial-News-Sentiment-Score-
Machine learning model predicting stock prices by integrating sentiment analysis of financial news with historical stock data. Utilizes VADER for sentiment scoring, MLP for trend prediction, and web scraping for real-time news updates. Achieves a 72 accuracy for stock trends over 7 days.

Project Overview: This project integrates sentiment analysis of news articles with historical stock data to predict the closing prices of Reliance Power’s stock. By leveraging NLP techniques and machine learning, the objective was to create a model that could anticipate stock price movements based on sentiment derived from relevant news. The approach demonstrates how sentiment analysis can enhance the predictive capabilities of financial models.

Steps Involved:

Data Collection:

Stock Price Data:
Source: Yahoo Finance (using the yfinance library).
Data period: August 29, 2023, to the present.
Columns utilized: Date, Open, High, Low, Close, Adjusted Close, and Volume.
News and Sentiment Data:
News updates were obtained from the LiveMint website.
Sentiment analysis was performed using VADER, generating scores ranging from -1 to 1.
Data collected: 764 rows with columns such as Title, Date, and Content.
Data Preprocessing:

The stock data was cleaned, null values removed, and normalized using Min-Max scaling.
Sentiment data was aggregated over 7-day windows for better analysis.
Data Merging & Feature Engineering:

Stock data was merged with sentiment data based on the Date column.
New columns like Previous Close, Price Change, and Sentiment Label were introduced.
Feature selection: Previous Close, Sentiment, Support, and Resistance values were used.
Target: Closing prices.
Model Training:

The dataset was split into training and testing sets using an 80-20 ratio.
An MLP (Multi-Layer Perceptron) Regressor was trained on the features.
Evaluation metrics used were Mean Squared Error (MSE), Mean Absolute Error (MAE), and R-squared (R²).
Prediction:

The model was used to predict stock prices for the next 7 days.
The results showed a highest accuracy of 72%, with actual versus predicted price change visualized.
Saving the Model:

The trained MLP Regressor was saved as a pickle file for future use.
Predictions were saved into CSV files for analysis.
Evaluation Results:

The MSE, MAE, and R-squared metrics provided insights into the model's accuracy and performance.
The model achieved an accuracy of 0.72, indicating good predictive power but room for improvement.
Support and Resistance Levels:

The stock data was further analyzed to calculate support and resistance levels using rolling windows, which provided insights into price trends.
Final Dataset Description:

Stock Price Data Size: 1.6 MB.
News Sentiment Data Size: 4.2 MB (with 764 rows).
Final Merged Dataset Size: 16 KB with 7 rows, including Date, Predicted Close, and Predicted Price Change.
Tools & Libraries Used:

Web Scraping: BeautifulSoup, Selenium for gathering live news updates.
Data Handling: Pandas, NumPy for processing and manipulation.
Visualization: Matplotlib for plotting stock trends and sentiment analysis results.
ML Model: MLPRegressor from the scikit-learn library.
Sentiment Analysis: VADER for sentiment scoring of news articles.
This project highlights how combining real-time sentiment analysis from news articles with stock price data can improve predictive models in financial markets. By utilizing various machine learning techniques and performing extensive data preprocessing, the project was able to capture market dynamics influenced by sentiment, achieving a respectable prediction accuracy.





![Stock Prediction System Architecture_page-0001](https://github.com/user-attachments/assets/406615be-59c2-4fd4-af01-3226585de9fb)





![Stock Prediction System Architecture_page-0002](https://github.com/user-attachments/assets/4f20befe-995c-4b1f-a0b4-d79498bbd83a)



