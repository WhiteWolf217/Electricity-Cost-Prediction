import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
import os

os.makedirs('../results', exist_ok=True)
os.makedirs('processed_graphs', exist_ok=True)

df = pd.read_csv('../data/archive/electricity_cost_dataset.csv')

imputer = SimpleImputer(strategy='mean')
numeric_cols = df.select_dtypes(include=np.number).columns
df[numeric_cols] = imputer.fit_transform(df[numeric_cols])

print(df.columns)
cat_cols = ['structure type']
encoder = OneHotEncoder(sparse_output=False, handle_unknown='ignore')
encoded = encoder.fit_transform(df[cat_cols])
encoded_df = pd.DataFrame(encoded, columns=encoder.get_feature_names_out(cat_cols))
df = pd.concat([df.drop(cat_cols, axis=1), encoded_df], axis=1)

scaler = StandardScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

df.to_csv('../results/electricity_cost_processed.csv', index=False)
