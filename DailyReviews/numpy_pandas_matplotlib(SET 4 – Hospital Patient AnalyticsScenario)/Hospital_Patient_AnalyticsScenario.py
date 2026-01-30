'''SET 4 – Hospital Patient AnalyticsScenario
A hospital wants to analyze patient stay patterns and treatment costs.
Problem Statement
Create a dataset of at least 400 patients containing:

patient_id, age, gender, diagnosis, hospital_days, treatment_cost

Using Pandas:

Compute average hospital stay per diagnosis.

Segment patients into age groups.

Using NumPy:

Identify treatment cost anomalies.

Apply suitable transformations to normalize cost data.

Using a visualization library:

Compare hospital stay across diagnoses.

Visualize cost patterns across age groups.'''

from helper.helper import helper
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#pandas task
def avg_day(df):
    avg_days = df.groupby('diagnosis')['hospital_days'].mean()
    return avg_days

def segment_patients(df):
    bins = [0, 25, 35, 45, 100]
    labels = ['18-25', '26-35', '36-45', '46+']

    df['age_group'] = pd.cut(
        sample_data['age'],
        bins=bins,
        labels=labels
    )
    return df
#numpy task
def anomalies(df):
   anomal = 80000
   return df[df["treatment_cost"]>anomal]


def normalize_cost_data(df):
    # df['treatment_cost'] = np.to_numpy('treatment_cost')
    x = df['treatment_cost'].values
    normalize = (x - np.min(x))/(np.max(x)-np.min(x))
    df['normalize'] = normalize
    return df

#matplotlib
def box_plot(df):
    avg_days = df('diagnosis')['hospital_days'].mean()
    plt.boxplot(avg_days)
    plt.title('Avg Days')
    plt.show()


def box_plots(df):
    data = [
        df[df['age_group'] == group]['treatment_cost']
        for group in df['age_group'].dropna().unique()
    ]

    labels = df['age_group'].dropna().unique()

    plt.boxplot(data, labels=labels)
    plt.title('Treatment Cost Patterns Across Age Groups')
    plt.xlabel('Age Group')
    plt.ylabel('Treatment Cost')
    plt.show()


if __name__ == '__main__':
    sample_data = helper()
    print(f'sample_data\n{sample_data}')
    # print(f'avg days\n{avg_day(sample_data)}')
    print(f'segment patients\n{segment_patients(sample_data)}')
    # print(f'Anomailies patients\n{anomalies(sample_data)}')
    # print(f'normalize:\n{normalize_cost_data(sample_data)}')

    #CALL NORMALIZATION FUNCTION
    # sample_data = normalize_cost_data(sample_data)
    # print(sample_data)

    # box_plot(sample_data)
    box_plots(sample_data)