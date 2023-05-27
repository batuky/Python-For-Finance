import pandas as pd
import yfinance as yf
import datetime

start = datetime.datetime.now() - datetime.timedelta(days=730)  # Bugünden itibaren 180 gün önce
end = datetime.datetime.now()

symbols = ['KONTR.IS', 'FROTO.IS', 'EUPWR.IS', 'SISE.IS', 'TUPRS.IS', 'AKBNK.IS', 'AGHOL.IS', 'BIOEN.IS', 'PETKM.IS', 'ALARK.IS', 'KUTPO.IS']  # İlgilendiğiniz hisse senedi sembolleri

data = yf.download(symbols, start=start, end=end)['Adj Close']

# Verileri DataFrame olarak oluşturun
df = pd.DataFrame(data)

# Excel tablosuna kaydetme
df.to_excel('bist100_degerler.xlsx', sheet_name='BIST 100', index=True)

# CSV dosyasına kaydetme
df.to_csv('bist100_degerler.csv', index=True)

print("Veriler başarıyla Excel tablosu ve CSV dosyası olarak kaydedildi.")
