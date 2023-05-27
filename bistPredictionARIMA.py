# import pandas as pd
# import numpy as np
# from statsmodels.tsa.arima.model import ARIMA
# import datetime

# # Veri setini yükleme veya oluşturma
# data = pd.read_csv('bist100_degerler.csv')
# dates = pd.to_datetime(data.iloc[:, 0])  # Tarih sütununu datetime formatına dönüştürme

# # Prompt the user to enter the stock symbol for prediction
# symbol = input("Enter the stock symbol: ")

# # Kapanış fiyatlarını seçme
# prices = data[symbol]  # Replace 'symbol' with the column name of the desired stock

# # ARIMA modelini oluşturma ve eğitme
# p, d, q = 1, 1, 1  # ARIMA order parameters
# model = ARIMA(prices, order=(p, d, q))
# model_fit = model.fit()

# # Gelecekteki değerleri tahmin etme
# end_date = dates.iloc[-1] + pd.DateOffset(months=24)  # Add 3 months to the last date in the data
# prediction_dates = pd.date_range(start=dates.iloc[-1], end=end_date, freq='D')  # Sonraki 3 ayın tahmin tarihlerini oluşturma
# future_predictions = model_fit.predict(start=len(prices), end=len(prices) + len(prediction_dates) - 1)  # Tahmin yapma

# # Tahminleri bir DataFrame'e dönüştürme
# predictions_df = pd.DataFrame({'Date': prediction_dates, 'Predicted Price': future_predictions})

# # Excel tablosuna kaydetme
# predictions_df.to_excel('tahminler.xlsx', index=False)

# print("Tahminler başarıyla Excel tablosuna kaydedildi.")


import pandas as pd
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
import datetime

# Veri setini yükleme veya oluşturma
data = pd.read_csv('bist100_degerler.csv')
dates = pd.to_datetime(data.iloc[:, 0])  # Tarih sütununu datetime formatına dönüştürme

# Prompt the user to enter the stock symbol for prediction
symbol = input("Enter the stock symbol: ")

# Kapanış fiyatlarını seçme
prices = data[symbol]  # Replace 'symbol' with the column name of the desired stock

# ARIMA modelini oluşturma ve eğitme
p, d, q = 1, 1, 1  # ARIMA order parameters
model = ARIMA(prices, order=(p, d, q))
model_fit = model.fit()

# Gelecekteki değerleri tahmin etme
end_date = dates.iloc[-1] + pd.DateOffset(days=3)  # Add 2 months to the last date in the data
prediction_dates = pd.date_range(start=dates.iloc[-1], end=end_date, freq='D')  # Sonraki 2 ayın tahmin tarihlerini oluşturma
future_predictions = model_fit.predict(start=len(prices), end=len(prices) + len(prediction_dates) - 1)  # Tahmin yapma

# Tahminleri bir DataFrame'e dönüştürme
predictions_df = pd.DataFrame({'Date': prediction_dates, 'Predicted Price': future_predictions})

# Excel tablosuna kaydetme
predictions_df.to_excel('tahminler.xlsx', index=False)

print("Tahminler başarıyla Excel tablosuna kaydedildi.")
