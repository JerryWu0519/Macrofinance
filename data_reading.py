import yfinance as yf
import pandas as pd
from functions import clean_data

# Dictionary of assets with readable names
def get_assets():
    return {    
    'NVDA': 'NVIDIA',
    'AMZN': 'Amazon',
    'GOOGL': 'Google',
    'BABA': 'Alibaba',
    'GS': 'Goldman Sachs',
    'ARM': 'ARM Holdings',          # May not be available on Yahoo Finance
    '1211.HK': 'BYD',
    'BRK-B': 'Berkshire Hathaway',
    'RR.L': 'Rolls-Royce',          # .L = London Stock Exchange
    'RHM.DE': 'Rheinmetall',        # .DE = Germany
    'COIN': 'Coinbase',
    '1810.HK': 'Xiaomi',
    'NKE': 'Nike',
    'GC=F': 'Gold Futures',
    'BND': 'US Total Bond Market ETF',
    'BTC-USD': 'Bitcoin',
    '^N225': 'Japan 225',
    '^NDX': 'USA Tech 100',
    '^GDAXI': 'Germany 40',
    '^FTSE': 'UK 100',
    '^HSI': 'Hong Kong 50',
    '^SSMI': 'Switzerland 20',
    'EPOL': 'iShares MSCI Poland ETF',
    'PLTR': 'Palantir',
    'FXI': 'iShares China Large-Cap ETF',
    'CL=F': 'Crude Oil Futures',
    'KO': 'Coca-Cola',
    'COST': 'Costco',
    'LULU': 'Lululemon',
    'BIRK': 'Birkenstock',
    'BP': 'BP',
    'MC.PA': 'LVMH',                      # Paris Stock Exchange
    'AIR.PA': 'Airbus',                   # Paris Stock Exchange
    'MAR': 'Marriott International',
    'GE': 'General Electric',
    'STZ': 'Constellation Brands',
    'NVO': 'Novo Nordisk',
    'TSLA': 'Tesla',
    'AAPL': 'Apple',
    'JNJ': 'Johnson & Johnson',
    'PG': 'Procter & Gamble'
}

def load_price_data(start="2023-01-01", end="2025-05-02", interval="1d"):
    assets = get_assets()
    df = yf.download(list(assets.keys()), start=start, end=end, interval=interval)['Close']
    df.columns = [assets[ticker] for ticker in df.columns]
    df = clean_data(df)
    return df

