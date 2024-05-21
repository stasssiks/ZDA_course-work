import os

import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.pyplot as plt
import joblib


def load_processed_data(filename='crashes-processed.csv'):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    return pd.read_csv(file_path)


data = load_processed_data()
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

yearly_crashes = data.resample('YE').size()
model = ARIMA(yearly_crashes, order=(1, 1, 1))
model_fit = model.fit()

joblib.dump(model_fit, 'crashes_predictor_model.pkl')


forecast = model_fit.forecast(steps=10)

plt.figure(figsize=(12, 6))
plt.plot(yearly_crashes.index, yearly_crashes, label='Historical Crash Counts')
forecast_index = pd.date_range(start=yearly_crashes.index[-1], periods=11, freq='YE')[1:]
plt.plot(forecast_index, forecast, label='Forecasted Crash Counts', color='red')
plt.title('Forecast of Total Crashes Over the Next 10 Years')
plt.legend()
plt.grid(True)
plt.show()

