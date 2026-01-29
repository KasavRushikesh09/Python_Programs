import pandas as pd
from helper.helper import helper
import numpy as np
import random
import matplotlib.pyplot as plt
#pandas task
def poor_completion(df):
    courses = df.groupby('course_name')['completion_days'].min()
    return courses

def avg_completion_time(df):
    avg_time = df.groupby('course_name')['completion_days'].mean()
    return avg_time

#numpy task
def statistical_analysis(df):
    days = df['completion_days'].to_numpy()

    stat = {
        'mean' : np.mean(days),
        'min' : np.min(days),
        'max' : np.max(days),
        'median' :np.median(days),
        'std' : np.std(days)
    }
    return stat

def progress_scenarios(df):
    progress = df['progress_percent'].to_numpy()

    improvement = np.random.uniform(10,20,size=len(progress))
    df['new_progress'] = np.clip(progress+improvement,0,100)
    return df
#matplotlib
def histogram(df):
    plt.hist(df['completion_days'],bins = 20)
    plt.title('Visualize completion time distribution')
    plt.xlabel("time")
    plt.show()
def bar_chart(df):
    rating = df.groupby('course_name')['rating'].mean()
    rating.plot(kind ='bar')
    plt.title("Average Course Ratings")
    plt.xlabel("Course Name")
    plt.ylabel("Average Rating")
    plt.xticks(rotation=45)
    plt.show()
if __name__ == '__main__':
    sample_data = helper()
    print(f'sample_data\n{sample_data}')
    # print(f'poor completion:\n{poor_completion(sample_data)}')
    # print(f'avg completion of time:\n{avg_completion_time(sample_data)}')
    # print(f'statistical analysis on completion duration.\n{statistical_analysis(sample_data)}')
    # print(f'progress\n{progress_scenarios(sample_data)}')
    # histogram(sample_data)
    bar_chart(sample_data)