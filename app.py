import os
import pandas as pd
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime, timedelta
import yfinance as yf
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt
import joblib
import numpy as np
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def getLiveUpdates(url, model_name):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        soup = BeautifulSoup(response.content, "html.parser")

        title_elem = soup.find("h2", class_="liveTitle")
        title = title_elem.get_text(strip=True) if title_elem else "No Title Available"

        live_updates = []
        for div in soup.find_all("div", class_="liveSec"):
            timestamp_elem = div.find("span", class_="timeStamp")
            content_elem = div.find("p")

            Date = timestamp_elem.get_text(strip=True) if timestamp_elem else "No Timestamp Available"
            content = content_elem.get_text(strip=True) if content_elem else "No Content Available"

            live_updates.append({
                "Title": title,
                "Date": Date,
                "Content": content,
            })

        save_to_csv(live_updates, model_name)
    except requests.RequestException as e:
        print("Error fetching data:", e)

def save_to_csv(live_updates, model_name):
    news_data_paths = {
        "tata": r"D:\my_flask_app\models\tata power model\tatapowernews.csv",
        "rpower": r"D:\my_flask_app\models\rpower\live_updates_updated_2new.csv",
        "jswsteel": r"D:\my_flask_app\models\JSW STEEL MODEL\jswnewssteel.csv"
    }
    news_data_path = news_data_paths.get(model_name.lower())
    
    if not news_data_path:
        print(f"No path found for model: {model_name}")
        return

    try:
        # Read the existing CSV file if it exists, otherwise create an empty DataFrame
        try:
            combined_df = pd.read_csv(news_data_path)
        except FileNotFoundError:
            combined_df = pd.DataFrame()

        # Convert the live updates to a DataFrame
        new_df = pd.DataFrame(live_updates)

        if combined_df.empty:
            combined_df = new_df
        else:
            new_content = set(new_df['Content'])
            existing_content = set(combined_df['Content'])
            unique_content = new_content - existing_content

            if unique_content:
                new_unique_entries = new_df[new_df['Content'].isin(unique_content)]
                combined_df = pd.concat([combined_df, new_unique_entries], ignore_index=True)
                print(f"New unique entries added to {news_data_path}")
            else:
                print("No new unique entries to add")

        combined_df.to_csv(news_data_path, index=False)
    except Exception as e:
        print("Error:", e)

def load_model(model_name):
    model_paths = {
        "tata": r"D:\my_flask_app\models\tata power model\mlp_modelTATAPOWER.pkl",
        "rpower": r"D:\my_flask_app\models\rpower\mlp_modelRPOWER.pkl",
        "jswsteel": r"D:\my_flask_app\models\JSW STEEL MODEL\mlp_modelJSWSTELL.pkl"
    }
    model_path = model_paths.get(model_name.lower())
    if model_path and os.path.exists(model_path):
        try:
            with open(model_path, 'rb') as f:
                model = joblib.load(f)
            return model
        except Exception as e:
            print(f"Error loading model: {e}")
            return None
    else:
        print("Model path not found for the selected stock.")
        return None

def load_news_data(model_name):
    news_data_paths = {
        "tata": r"D:\my_flask_app\models\tata power model\tatapowernews.csv",
        "rpower": r"D:\my_flask_app\models\rpower\live_updates_updated_2new.csv",
        "jswsteel": r"D:\my_flask_app\models\JSW STEEL MODEL\jswnewssteel.csv"
    }
    news_data_path = news_data_paths.get(model_name.lower())
    if news_data_path and os.path.exists(news_data_path):
        try:
            news_df = pd.read_csv(news_data_path)
            news_df['Date'] = news_df['Date'].apply(parse_date)
            news_df = news_df.dropna(subset=['Date'])
            news_df['Sentiment'] = news_df['Content'].apply(get_sentiment)
            print("News data loaded successfully")
            return news_df
        except Exception as e:
            print(f"Error loading news data: {e}")
            return None
    else:
        print("News data path not found for the selected model.")
        return None

def parse_date(date_str):
    try:
        return pd.to_datetime(date_str, errors='coerce')
    except Exception as e:
        print(f"Error parsing date: {e}")
        return pd.NaT

def get_sentiment(text):
    try:
        analyzer = SentimentIntensityAnalyzer()
        sentiment = analyzer.polarity_scores(text)
        return sentiment['compound']
    except Exception as e:
        print(f"Error analyzing sentiment: {e}")
        return 0

def get_stock_data(model_name):
    stock_symbols = {
        "tata": "TATAPOWER.NS",
        "rpower": "RPOWER.NS",
        "jswsteel": "JSWSTEEL.NS"
    }
    stock_symbol = stock_symbols.get(model_name.lower())
    if stock_symbol:
        try:
            current_date = datetime.today().strftime('%Y-%m-%d')
            stock_df = yf.download(stock_symbol, start='2023-08-29', end=current_date, progress=False)
            stock_df.reset_index(inplace=True)
            print("Stock data fetched successfully")
            return stock_df
        except Exception as e:
            print(f"Error fetching stock data: {e}")
            return None
    else:
        print("Stock symbol not found for the selected model.")
        return None

def calculate_100_day_mean_close(data):
    data['100_Day_Mean_Close'] = data['Close'].rolling(window=100).mean()
    return data

def calculate_support_resistance(data, window=20):
    data['Support'] = data['Low'].rolling(window=window).min()
    data['Resistance'] = data['High'].rolling(window=window).max()
    return data

def get_merged_df(model_name):
    news_df = load_news_data(model_name)
    if news_df is None:
        print("Failed to load news data.")
        return None

    stock_df = get_stock_data(model_name)
    if stock_df is None:
        print("Failed to fetch stock data.")
        return None

    try:
        stock_df = calculate_100_day_mean_close(stock_df)
        news_df['Date'] = pd.to_datetime(news_df['Date'])
        merged_df = pd.merge(stock_df, news_df[['Date', 'Sentiment']], on='Date', how='left')
        merged_df['Sentiment'].fillna(method='ffill', inplace=True)
        merged_df = calculate_support_resistance(merged_df)
        merged_df['Previous_Close'] = merged_df['Close'].shift(1)
        merged_df.dropna(inplace=True)
        return merged_df
    except Exception as e:
        print(f"Error merging dataframes: {e}")
        return None
# heatmap
@app.route('/api/sentiment-heatmap')
def sentiment_heatmap():
    stock_models = ['tata', 'rpower', 'jswsteel']
    heatmap_data = []

    for model in stock_models:
        df = load_news_data(model)
        if df is not None and not df.empty:
            # Group by date and get mean sentiment
            grouped = df.groupby(df['Date'].dt.date)['Sentiment'].mean().reset_index()
            # Sort by date descending and take last 7 days
            grouped = grouped.sort_values('Date', ascending=False).head(7)
            # Sort again ascending for display
            grouped = grouped.sort_values('Date')
            for _, row in grouped.iterrows():
                heatmap_data.append({
                    'stock': model.upper(),
                    'date': row['Date'].strftime('%Y-%m-%d'),
                    'sentiment': round(row['Sentiment'], 3)
                })

    return {'data': heatmap_data}




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enter_news', methods=['POST'])
def enter_news():
    model_name = request.form['model_name']
    return render_template('option.html', model_name=model_name)

@app.route('/manual_entry')
def manual_entry():
    model_name = request.args.get('model_name')
    return render_template('manual_entry.html', model_name=model_name)

@app.route('/web_scraping')
def web_scraping():
    model_name = request.args.get('model_name')
    return render_template('web_scraping.html', model_name=model_name)

@app.route('/predict', methods=['POST'])
def predict():
    model_name = request.form['model_name']
    news_data = []

    # Collect the news data from the form
    for i in range(7):
        title = request.form.get(f'title_{i}')
        date = request.form.get(f'date_{i}')
        content = request.form.get(f'content_{i}')
        if title and date and content:
            news_data.append({'title': title, 'date': date, 'content': content})

    if news_data:
        # Save the news data to the corresponding CSV file
        news_df = pd.DataFrame(news_data)
        news_df['Date'] = pd.to_datetime(news_df['Date'])
        news_df['Sentiment'] = news_df['Content'].apply(get_sentiment)
        
        news_data_paths = {
            "tata": r"D:\my_flask_app\models\tata power model\tatapowernews.csv",
            "rpower": r"D:\my_flask_app\models\rpower\live_updates_updated_2new.csv",
            "jswsteel": r"D:\my_flask_app\models\JSW STEEL MODEL\jswnewssteel.csv"
        }
        news_data_path = news_data_paths.get(model_name.lower())
        
        if news_data_path:
            try:
                existing_news_df = pd.read_csv(news_data_path)
                combined_news_df = pd.concat([existing_news_df, news_df]).drop_duplicates(subset=['Content'])
                combined_news_df.to_csv(news_data_path, index=False)
                print(f"News data saved to {news_data_path}")
            except Exception as e:
                print(f"Error saving news data: {e}")

    mlp_model = load_model(model_name)
    if mlp_model is None:
        return render_template('result.html', result="Failed to load the model for the selected stock.")

    merged_df = get_merged_df(model_name)
    if merged_df is None:
        return render_template('result.html', result="Failed to create the merged DataFrame.")

    today = datetime.today().date()
    next_seven_days_dates = [today + timedelta(days=i) for i in range(7)]

    last_7_days = merged_df.iloc[-7:][['Previous_Close', 'Sentiment', 'Support', 'Resistance']].values

    if last_7_days.shape[0] == 0:
        return render_template('result.html', result="Not enough data to make predictions. Please ensure there is sufficient historical data.")

    predicted_close_prices = []
    predicted_price_changes = []

    for i in range(7):
        X_next_day = pd.DataFrame(last_7_days, columns=['Previous_Close', 'Sentiment', 'Support', 'Resistance'])
        # Defensive: check if X_next_day has at least one row
        if X_next_day.shape[0] == 0:
            return render_template('result.html', result="Not enough data to make predictions. Please ensure there is sufficient historical data.")
        next_day_close = mlp_model.predict(X_next_day.iloc[[-1]])[0]

        predicted_close_prices.append(next_day_close)
        price_change = next_day_close - last_7_days[-1][0]
        predicted_price_changes.append(price_change)

        last_7_days = np.append(last_7_days[1:], [[next_day_close, last_7_days[-1][1], last_7_days[-1][2], last_7_days[-1][3]]], axis=0)

    predicted_df = pd.DataFrame({
        'Date': next_seven_days_dates,
        'Predicted_Close': predicted_close_prices,
        'Predicted_Price_Change': predicted_price_changes
    })

    output_dir = os.path.join('D:\\my_flask_app\\models', model_name.lower())
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    predicted_prices_path = os.path.join(output_dir, 'predicted_prices.csv')
    predicted_df.to_csv(predicted_prices_path, index=False)
    print("Predicted prices saved.")

    try:
        merged_df['Actual_Price_Change'] = merged_df['Close'] - merged_df['Previous_Close']
        predicted_close_df = merged_df[['Date', 'Close']].copy()
        predicted_close_df['Predicted_Close'] = mlp_model.predict(merged_df[['Previous_Close', 'Sentiment', 'Support', 'Resistance']])

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 14), sharex=True)

        ax1.plot(merged_df['Date'], merged_df['Close'], label='Actual Close Price', color='blue')
        ax1.plot(predicted_close_df['Date'], predicted_close_df['Predicted_Close'], label='Predicted Close Price', color='red', linestyle='--')
        ax1.plot(predicted_df['Date'], predicted_df['Predicted_Close'], label='Next 7 Days Predicted Close Price', color='green', linestyle='--')
        ax1.set_ylabel('Close Price')
        ax1.set_title('Actual vs Predicted Close Price')
        ax1.legend()

        ax2.plot(merged_df['Date'], merged_df['Actual_Price_Change'], label='Actual Price Change', color='blue')
        ax2.plot(predicted_df['Date'], predicted_df['Predicted_Price_Change'], label='Predicted Price Change', color='green', linestyle='--')
        ax2.set_xlabel('Date')
        ax2.set_ylabel('Price Change')
        ax2.set_title('Actual vs Predicted Price Change')
        ax2.legend()

        fig.tight_layout()
        plot_path = os.path.join('static', 'prediction_plot.png')
        plt.savefig(plot_path)
        plt.close()
        print("Prediction plot saved.")
    except Exception as e:
        print(f"Error generating plot: {e}")
        plot_path = None

    return render_template('result.html', result="Prediction complete", plot_path=plot_path)


@app.route('/heatmap')
def heatmap():
    return render_template('heatmap.html')


if __name__ == '__main__':
    app.run(debug=True)
