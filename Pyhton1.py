


import pymc as pm
import numpy as np
import pandas as pd
import seaborn as sns
import arviz as az
from nhanes.load import load_NHANES_data
import matplotlib.pyplot as plt

# Load NHANES data for the 2017-2018 cycle
demo_df = load_NHANES_data(year='2017-2018', component='DEMO')
bpx_df = load_NHANES_data(year='2017-2018', component='BPX')

# Merge the datasets on the sequence number (SEQN)
nhanes_df = pd.merge(demo_df, bpx_df, on='SEQN')

# Rename columns for easier use
nhanes_df.rename(columns={'RIDAGEYR': 'Age', 'RIAGENDR': 'Gender', 'BMXBMI': 'BMI', 'BPXSY1': 'SBP'}, inplace=True)

# Select relevant columns and drop rows with missing data
data = nhanes_df[['Age', 'Gender', 'BMI', 'SBP']].dropna()

# Encode Gender as a dummy variable (1 for Male, 2 for Female)
data['Gender_Male'] = data['Gender'].apply(lambda x: 1 if x == 1 else 0)

# Print the first few rows to confirm data is ready
print(data.head())
