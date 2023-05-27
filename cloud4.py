import boto3
import pandas as pd
import matplotlib.pyplot as plt

# Конфігурація доступу до Amazon S3
s3 = boto3.client('s3')
s3.download_file('bucketcloud2', 'dataaa.csv', 'downloaded.csv')

df = pd.read_csv('downloaded.csv')

# Фільтрування даних за потрібними валютами
usd = df.loc[df['cc'] == 'USD']
eur = df.loc[df['cc'] == 'EUR']

# Побудова графіка
plt.plot(usd['exchangedate'], usd['rate'], label='USD')
plt.plot(eur['exchangedate'], eur['rate'], label='EUR')
plt.xlabel('Дата')
plt.ylabel('Курс')
plt.title('Курс валют за 2021 рік')
plt.legend()
plt.show()

# Збереження графіка у бакеті
plt.savefig('sched.png')
s3.upload_file('sched.png', 'bucketcloud2', 'sched.png')
