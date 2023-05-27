import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import datetime

# Veri setini yükleme veya oluşturma
data = pd.read_csv('bist100_degerler.csv')
dates = pd.to_datetime(data.iloc[:, 0])  # Tarih sütununu datetime formatına dönüştürme

# Prompt the user to enter the stock symbol for prediction
symbol = input("Enter the stock symbol: ")

# Kapanış fiyatlarını seçme
prices = data[symbol]  # Replace 'symbol' with the column name of the desired stock

# Veri kümesini X ve y olarak ayırma
X = np.array(range(len(prices))).reshape(-1, 1)  # Tarihlerin sıralı sayılarını X olarak kullanma
y = prices.values  # Kapanış fiyatlarını y olarak kullanma

# Lineer regresyon modelini oluşturma ve eğitme
model = LinearRegression()
model.fit(X, y)

# Gelecekteki değerleri tahmin etme
end_date = dates.iloc[-1] + pd.DateOffset(months=3)  # Add 3 months to the last date in the data
prediction_dates = pd.date_range(start=dates.iloc[-1], end=end_date, freq='D')  # Sonraki 3 ayın tahmin tarihlerini oluşturma
future_predictions = model.predict(np.array(range(len(prices), len(prices) + len(prediction_dates))).reshape(-1, 1))  # Tahmin yapma

# Tahminleri bir DataFrame'e dönüştürme
predictions_df = pd.DataFrame({'Date': prediction_dates, 'Predicted Price': future_predictions})

# Excel tablosuna kaydetme
predictions_df.to_excel('tahminler.xlsx', index=False)

print("Tahminler başarıyla Excel tablosuna kaydedildi.")
