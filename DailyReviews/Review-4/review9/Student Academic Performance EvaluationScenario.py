import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from helper.helper import helper
def total_avg_score(df):
    df['total_score']= df[['math','science','english']].sum(axis=1)
    df['average_score']= df[['math','science','english']].mean(axis=1)
    return df.head()

def classify_stu(avg_score):
    if avg_score >=75:
        return "Excellent"

    elif avg_score >= 60:
        return 'Good'

    elif avg_score >= 40:
        return 'average'

    else:
        return "poor"

# numpy tasks
def Apply_weighted(df):
    weights = np.array([0.4,0.35,0.25])
    marks_array = df[['math','science','english']].values
    df['weighted_score'] = np.dot(marks_array,weights)
    return df

def standardize_scores(df):
    subjects = ['math','science','english']
    df[['math','science','english']] = (
        df[subjects] - df[subjects].mean())/df[subjects].std()
    return df

def stud_wise_avg(df):
    subject_avg = df[['math', 'science', 'english']].mean()

    plt.bar(subject_avg.index,subject_avg.values)
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")
    plt.show()

def attend_performance(df):
    plt.scatter(df['attendance_per'], df['average_score'])
    plt.xlabel("Attendance Percentage")
    plt.ylabel("Average Score")
    plt.title("Attendance vs Academic Performance")
    plt.show()
if __name__ == '__main__':
    sample_data = helper()
    # print(sample_data)
    # print(f'Sum:\n{total_avg_score(sample_data)}')
    sample_data = total_avg_score(sample_data)
    sample_data['Performance'] = sample_data['average_score'].apply(classify_stu)
    # print(sample_data.head())
    sample_data = Apply_weighted(sample_data)
    # print(sample_data.head())
    sample_data = standardize_scores(sample_data)
    # print(sample_data.head())
    # subject_avg = sample_data[['math', 'science', 'english']].mean()
    #
    # plt.bar(subject_avg.index, subject_avg.values)
    # plt.xlabel("Subjects")
    # plt.ylabel("Average Marks")
    # plt.title("Subject-wise Performance Comparison")
    # plt.show()
    #stud_wise_avg(sample_data)
    attend_performance(sample_data)