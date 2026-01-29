from helper.helper import helper
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#pandas task
def generate_department_wise_salary(df):
    # df['result'] = df.groupby('department')('salary','performance_score')
    # return df['result']
    df['department'] = df['department'].apply(
        lambda x :x[0] if isinstance(x,list) else x
    )
    summary = df.groupby('department').agg({
        'salary':'mean',
        'performance_score' : 'mean'
    }).rename(columns = {
        'salary':'avg_salary',
        'performance_score':'avg_performance'
    })
    return summary

def categorize_employee_salary_bands(df):
    bins = [15000,25000,35000,50000]
    labels = ['low','medium','high']
    df['salary band'] = pd.cut(df['salary'],bins=bins,labels=labels)
    return df

#numpy tasks
def normalization(df):
    x = df['salary'].to_numpy(dtype=float)
    normalized = (x-np.min(x))/(np.max(x)-np.min(x))
    df['salary_normalized'] = normalized
    return df

def corelation(df):
    salary = df['salary'].to_numpy()
    performance = df['performance_score'].to_numpy()

    corelation = np.corrcoef(salary,performance)[0,1]
    return corelation

#matplotlib
def histogram(df):
    df['department'] = df['department'].apply(
        lambda x:x[0] if isinstance(x,list)else x
    )
    df.boxplot(column = 'salary',by = 'department',figsize =(10,6))
    plt.title("Salary Distribution by Department")
    plt.suptitle("")
    plt.xlabel('department')
    plt.ylabel('salary')
    plt.show()

def scatterplot(df):
    plt.scatter(df['experience_year'],df['salary'],color = 'skyblue')
    plt.title("Visualize experience vs salary relation")
    plt.xlabel('experience')
    plt.ylabel('salary')
    plt.grid()
    plt.show()
if __name__ == '__main__':
    sample_data = helper()
    print(f'Sample Data\n{sample_data}')
    # print(f'generate department wise salary:\n{generate_department_wise_salary(sample_data)}')
    # print(f'categorize employee into salary band:\n{categorize_employee_salary_bands(sample_data)}')
    # print(f'Normalization:\n{normalization(sample_data)}')
    # print(f'corelation:\n{corelation(sample_data)}')
    # histogram(sample_data)
    scatterplot(sample_data)
