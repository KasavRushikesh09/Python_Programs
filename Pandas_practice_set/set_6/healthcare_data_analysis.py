'''
Pandas (Intermediate)
 A DataFrame contains patient_id, timestamp, heart_rate, and ward.
Task:
Compute average heart rate per ward


Identify patients with sudden spikes in heart rate


Extract data for critical cases

'''
from helper.helper import healthcare_data
import pandas as pd

def avg_hr_per_ward(df):
    avg_heart_per_ward = df.groupby('ward')['heart_rate'].mean()
    return avg_heart_per_ward

def sudden_spikes(df):

    df['heart_rate_diff'] = df.groupby('patient_id')['heart_rate'].diff()

    filter_mask = df['heart_rate_diff']>20
    filtered_df = df[filter_mask]

    return filtered_df

def critical_cases_data(data):

    spike_filtered_data = sudden_spikes(data)

    filter_mask = (spike_filtered_data['heart_rate'] > 120) | (spike_filtered_data['heart_rate'] < 60 )

    filtered_data = spike_filtered_data[filter_mask]
    return filtered_data[['patient_id','heart_rate']]

if __name__ == '__main__':
    sample_data = healthcare_data()
    print(f'Sample Data\n{sample_data}')
    print(f'Average heart rate:\n{avg_hr_per_ward(sample_data)}')
    print(f'Patients with sudden heart rate spikes:\n{sudden_spikes(sample_data)}')
    print(f"Critical Cases:\n{critical_cases_data(sample_data)}")

