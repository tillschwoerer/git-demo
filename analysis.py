import pandas as pd
import seaborn as sns

# Load data
df = sns.load_dataset('iris')
df.to_csv('iris.csv')

# Analysis
df.value_counts('species')
df.columns
