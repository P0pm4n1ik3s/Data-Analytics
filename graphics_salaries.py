import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#THE CODE BELOW ALLOW YOU TO READ THE 'SALARIES.CSV' FILE, FILTER DATA PER 'YEAR', 'EXPERIENCE LEVEL', 'EMPLOYMENT TYPE' AND 'COMPANY SIZE'.
#IT GROUPS RESULTS BY 'JOB TITLE' AND 'WORK YEAR' AND PROVIDE THE AVERAGE 'SALARY IN USD'.
#EVENTUALLY A BAR GRAPHIC GET CREATED SHOWING THE FINAL RESULT

file = pd.read_csv(r"C:\Users\yuz3741\Desktop\Webucator\Python\Data_Analysis\salaries.csv")
file_columns = file[['work_year', 'experience_level', 'employment_type', 'job_title', 'salary_in_usd', 'company_size']]
file_filter = file_columns[(file_columns['work_year'] == 2023) & (file_columns['experience_level'] == 'EN') & (file_columns['employment_type'] == 'FT') & (file_columns['company_size'] == 'M')]
file_agg = file_filter.groupby(['job_title', 'work_year']).agg({"salary_in_usd":'mean'})

plot_order = file_agg.sort_values(by='salary_in_usd', ascending=False)

ax = sns.catplot(x="job_title", y="salary_in_usd", kind='bar', data=plot_order)
sns.set(rc = {'figure.figsize':(20, 12)})
plt.xticks(rotation=90)
plt.ylabel('Average Salary in USD')
plt.grid('darkgrid')
ax.set_xticklabels(size = 5)
plt.show()
