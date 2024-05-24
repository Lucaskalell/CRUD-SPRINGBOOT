import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
import numpy as np


np.random.seed(0)
data = pd.DataFrame({
    'order_date': pd.date_range(start='2022-01-01', end='2022-12-31', freq='D'),
    'customer_id': np.random.randint(1000, 2000, size=365),  # IDs de clientes fictícios
    'category': np.random.choice(['Eletrônicos', 'Roupas', 'Livros'], size=365),
    'region': np.random.choice(['Norte', 'Sul', 'Leste', 'Oeste'], size=365),
    'order_value': np.random.normal(100, 20, size=365)
})
print(data.head())

data.drop_duplicates(inplace=True)
data['order_date'] = pd.to_datetime(data['order_date'])
data['order_value'].fillna(data['order_value'].mean(), inplace=True)
data.dropna(subset=['customer_id', 'order_date', 'category'], inplace=True)

plt.figure(figsize=(10, 6))
sns.histplot(data['order_value'], bins=30, kde=True)
plt.title('Distribuição do valor dos pedidos')
plt.xlabel('Valor do pedido')
plt.ylabel('Frequência')
plt.show()

sales_by_category = data.groupby('category')['order_value'].sum().sort_values(ascending=False)
print("Vendas por categoria:\n" , sales_by_category)

plt.figure(figsize=(10, 6))
sales_by_category.plot(kind= 'bar')
plt.title('Vendas por categoria')
plt.xlabel('categoria')
plt.ylabel('total de vendas')
plt.xticks(rotation=45)
plt.show()

sales_by_region = data.groupby('region')['order_value'].sum().sort_values(ascending=False)
print("\nVendas por Regiao:\n", sales_by_region)

plt.figure(figsize=(10, 6))
sales_by_region.plot(kind='bar')
plt.title('Vendas por regiao')
plt.xlabel('regiao')
plt.ylabel('Total de vendas')
plt.xticks(rotation=45)
plt.show()

data['order_date'] = pd.to_datetime(data['order_date'])

monthly_sales = data.set_index('order_date').resample('M')['order_value'].sum()

plt.figure(figsize=(12, 6))
monthly_sales.plot()
plt.title('Vendas Mensais')
plt.xlabel('mes')
plt.ylabel('Total de vendas')
plt.grid(True)
plt.show()

clv = data.groupby('customer_id')['order_value'].sum().sort_values(ascending=False)
print("\nTop 10 clientes por valor total de pedidos:\n", clv.head(10))

plt.figure(figsize=(10, 6))
clv.head(10).plot(kind= 'bar')
plt.title('Top 10 clientes por valor total de pedidos')
plt.xlabel('Id do cliente')
plt.ylabel('Valor do cliente')
plt.show()

now = dt.datetime(2023, 1, 1)

rfm = data.groupby('customer_id').agg({
    'order_date': lambda x: (now - x.max()).days,
    'customer_id': 'count' ,
    'order_value': 'sum'

})

rfm.columns = ['recency', 'frequency', 'monetary']

print("\nRFM:\n" , rfm.head())

rfm['R_Score'] = pd.qcut(rfm['recency'], 4, labels=[4, 3, 2, 1 ])
rfm['F_Score'] = pd.qcut(rfm['frequency'].rank(method='first'),4 , labels=[1, 2, 3,4])
rfm['M_Score'] = pd.qcut(rfm['monetary'], 4, labels=[1, 2, 3, 4])

rfm['RFM_Score'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)
print("\nRFM com Score:\n", rfm.head())
