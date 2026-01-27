"""
Pandas (Intermediate)
A DataFrame contains student_id, course_id, login_date, and minutes_spent.
Task:
    Identify inactive students (no login in last 7 days)
    Calculate average session duration per course
    Find top 3 courses with highest engagement
"""
from helper.generator import generator_student_df
import pandas as pd

def inactive_student(df):
    most_recent_date = df['login_date'].max()
    most_recent_seven_days = most_recent_date - pd.Timedelta(days = 7)
    filter_mask = df['login_date'] < most_recent_seven_days
    filter_df = df[filter_mask]
    filter_student_df = filter_df["student_id"].unique()

    return filter_student_df

def avg_session_duration(df):
    crs_mean_values = df.groupby('course_id')['minutes_spent'].mean()
    return crs_mean_values

def top_three_courses(df):
    net_crs_duration = df.groupby('course_id')['minutes_spent'].sum()
    top_three_crs = net_crs_duration.sort_values(ascending = False).head(3)
    return top_three_crs
if __name__ == "__main__":
    sample_data = generator_student_df()
    print(f"sample data:\n{sample_data}")
    print(f"inactive_student\n{inactive_student(sample_data)}")
    print(f"Avg_session_duration\n{avg_session_duration(sample_data)}")
    print(f"top_three_courses\n{top_three_courses(sample_data)}")























#
#
#
#
#
#
#
#
# from helper.generator import generator_student_df
# import pandas as pd
#
# def inactive_students(df):
#
#     most_recent_date = df['login_date'].max()
#     most_recent_seven_date = most_recent_date - pd.Timedelta(days=7)
#
#     filter_mask = df['login_date'] < most_recent_seven_date
#     filtered_df = df[filter_mask]
#
#     filtered_student_df = filtered_df["student_id"].unique()
#
#     return filtered_student_df
#
# def avg_session_duration(df):
#     course_mean_vals = df.groupby('course_id')['minutes_spent'].mean()
#     return course_mean_vals
#
# def top_three_courses(df):
#     net_course_durations = df.groupby('course_id')['minutes_spent'].sum()
#
#     top_three_crs = net_course_durations.sort_values(ascending=False).head(3)
#
#     return top_three_crs
#
# if __name__=="__main__":
#     sample_data = generator_student_df()
#     print(f"SAMPLE DATA:\n{sample_data}")
#     print(f"INACTIVE STUDENTS:\n{inactive_students(sample_data)}")
#     print(f"AVG SESSION DURATION:\n{avg_session_duration(sample_data)}")
#     print(f"TOP 3 COURSES:\n{top_three_courses(sample_data)}")

