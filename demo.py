# PROBLEM STATEMENT
# Write a pandas logic to do data analysis on the data set. 
# Also generate a report on the data set.

































# PROMPTS
# Create a dummy data set of 1000 rows and 10 columns.
# The data set should contain only integers between 1-10.
# The data set should contain one column with date type.
# The data set should contain one column with categorical type.
# The data set should contain one column with string type.
# The data set should contain one column with boolean type.
# The data set should contain one column with float type.
# The data set should contain one column with complex type.
# The data set should contain one column with object type.
# The data set should contain one column with timedelta type.
# The data set should contain one column with interval type.
# The data set should contain one column with sparse type.
# The data set should contain one column with duplicate values.
# The data set should contain one column with missing values.
# The data set should contain one column with negative values.
# The data set should contain one column with positive values.
# The data set should contain one column with zero values.
# The data set should contain one column with infinite values.
# The data set should contain one column with null values.
# The data set should contain one column with NaN values.
# The data set should contain one column with NaT values.

# Path: analysis.py
# Read the data set created in demo.py.
# Write a pandas code to do data analysis on the data set.
# Also generate a report on the data set.

import pandas as pd
import numpy as np
import random
import datetime
import string
import math
import sys


def generate_dummy_data():
    data = {}
    data['integers'] = [random.randint(1, 10) for i in range(1000)]
    data['date'] = [datetime.date(random.randint(1900, 2020), random.randint(1, 12), random.randint(1, 28)) for i in
                    range(1000)]
    data['categorical'] = [random.choice(string.ascii_letters) for i in range(1000)]
    data['string'] = [random.choice(string.ascii_letters) for i in range(1000)]
    data['boolean'] = [random.choice([True, False]) for i in range(1000)]
    data['float'] = [random.uniform(1, 10) for i in range(1000)]
    data['complex'] = [complex(random.randint(1, 10), random.randint(1, 10)) for i in range(1000)]
    data['object'] = [random.choice(string.ascii_letters) for i in range(1000)]
    data['timedelta'] = [datetime.timedelta(random.randint(1, 10)) for i in range(1000)]
    data['interval'] = [random.randint(1, 10) for i in range(1000)]
    data['sparse'] = [random.randint(1, 10) for i in range(1000)]
    data['duplicate'] = [random.randint(1, 10) for i in range(1000)]
    data['missing'] = [random.randint(1, 10) for i in range(1000)]
    data['negative'] = [random.randint(-10, -1) for i in range(1000)]
    data['positive'] = [random.randint(1, 10) for i in range(1000)]
    data['zero'] = [0 for i in range(1000)]
    data['infinite'] = [math.inf for i in range(1000)]
    data['null'] = [None for i in range(1000)]
    data['NaN'] = [np.nan for i in range(1000)]
    data['NaT'] = [pd.NaT for i in range(1000)]
    return data;


def create_dataframe(data):
    df = pd.DataFrame(data)
    return df


def write_to_csv(df):
    df.to_csv('data.csv', index=False)
    
    
def read_from_csv():
    df = pd.read_csv('data.csv')
    return df


def data_analysis(df):
    print(df.describe())
    print(df.info())
    print(df.isnull().sum())
    print(df.isna().sum())
    print(df.duplicated().sum())
    print(df.corr())
    print(df.cov())
    print(df.count())
    print(df.max())
    print(df.min())
    print(df.mean())
    print(df.median())
    print(df.mode())
    print(df.std())
    print(df.var())
    print(df.sum())
    print(df.abs())
    print(df.cumsum())
    print(df.cummax())
    print(df.cummin())
    print(df.cumprod())
    print(df.diff())
    print(df.pct_change())
    print(df.rank())
    print(df.round())
    print(df.clip())
    print(df.clip_lower())
    print(df.clip_upper())
    print(df.clip_axis())
    print(df.clip_lower(axis=1))
    print(df.clip_upper(axis=1))
    print(df.clip_axis(axis=1))
    print(df.abs())
    print(df.corrwith(df['integers']))
    print(df.corrwith(df['integers'], axis=1))
    print(df.corrwith(df['integers'], axis=0))
    print(df.corrwith(df['integers'], axis=1, drop=True))
    print(df.corrwith(df['integers'], axis=0, drop=True))
    print(df.corrwith(df['integers'], axis=1, drop=False))
    print(df.corrwith(df['integers'], axis=0, drop=False))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs())
    print(df.corrwith(df['integers'], axis=0, drop=False).abs())
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False))
    print(df.corrwith(df['integers'], axis=0, drop=False).abs().sort_values(ascending=False))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False).head(1))
    print(df.corrwith(df['integers'], axis=0, drop=False).abs().sort_values(ascending=False).head(1))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False).tail(1))
    print(df.corrwith(df['integers'], axis=0, drop=False).abs().sort_values(ascending=False).tail(1))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False).head(2))
    print(df.corrwith(df['integers'], axis=0, drop=False).abs().sort_values(ascending=False).head(2))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False).tail(2))
    print(df.corrwith(df['integers'], axis=0, drop=False).abs().sort_values(ascending=False).tail(2))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False).head(3))
    print(df.corrwith(df['integers'], axis=0, drop=False).abs().sort_values(ascending=False).head(3))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False).tail(3))
    print(df.corrwith(df['integers'], axis=0, drop=False).abs().sort_values(ascending=False).tail(3))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False).head(4))
    print(df.corrwith(df['integers'], axis=0, drop=False).abs().sort_values(ascending=False).head(4))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False).tail(4))
    print(df.corrwith(df['integers'], axis=0, drop=False).abs().sort_values(ascending=False).tail(4))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False).head(5))
    print(df.corrwith(df['integers'], axis=0, drop=False).abs().sort_values(ascending=False).head(5))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False).tail(5))
    print(df.corrwith(df['integers'], axis=0, drop=False).abs().sort_values(ascending=False).tail(5))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False).head(6))
    print(df.corrwith(df['integers'], axis=0, drop=False).abs().sort_values(ascending=False).head(6))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False).tail(6))
    print(df.corrwith(df['integers'], axis=0, drop=False).abs().sort_values(ascending=False).tail(6))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False).head(7))
    print(df.corrwith(df['integers'], axis=0, drop=False).abs().sort_values(ascending=False).head(7))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False).tail(7))
    print(df.corrwith(df['integers'], axis=0, drop=False).abs().sort_values(ascending=False).tail(7))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False).head(8))
    print(df.corrwith(df['integers'], axis=0, drop=False).abs().sort_values(ascending=False).head(8))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False).tail(8))
    print(df.corrwith(df['integers'], axis=0, drop=False).abs().sort_values(ascending=False).tail(8))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False).head(9))
    print(df.corrwith(df['integers'], axis=0, drop=False).abs().sort_values(ascending=False).head(9))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False).tail(9))
    print(df.corrwith(df['integers'], axis=0, drop=False).abs().sort_values(ascending=False).tail(9))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False).head(10))
    print(df.corrwith(df['integers'], axis=0, drop=False).abs().sort_values(ascending=False).head(10))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False).tail(10))
    print(df.corrwith(df['integers'], axis=0, drop=False).abs().sort_values(ascending=False).tail(10))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False).head(11))
    print(df.corrwith(df['integers'], axis=0, drop=False).abs().sort_values(ascending=False).head(11))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False).tail(11))
    print(df.corrwith(df['integers'], axis=0, drop=False).abs().sort_values(ascending=False).tail(11))
    print(df.corrwith(df['integers'], axis=1, drop=False).abs().sort_values(ascending=False).head(12))
    
    