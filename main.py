# This entrypoint file to be used in development. Start by reading README.md
import demographic_data_analyzer
from unittest import main

# Test your function by calling it here
demographic_data_analyzer.calculate_demographic_data()

# Run unit tests automatically
main(module='test_module', exit=False)



# import pandas as pd
# df = pd.read_csv('adult.data.csv')
# print(df.head())

# #print(df.value_counts('race'))

# #print(round(df[df['sex'] == 'Male']['age'].mean(), 1))

# # print(df.value_counts('education'))
# # print(df.value_counts('education').sum())
# # print(df.shape[0])
# # print(df.value_counts('education').loc['Bachelors'])


# no_of_records = df.shape[0]
# no_of_bachelors = df.value_counts('education').loc['Bachelors']
# percentage_bachelors = round(no_of_bachelors / no_of_records * 100, 1)
# print(percentage_bachelors)

#print(df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')])

#print(df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])])

#df_with_ad_ed = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
#no_with_ad_ed = df_with_ad_ed.shape[0]
#no_with_ad_ed_gt_50k = df_with_ad_ed.value_counts('salary').loc['>50K']
#higher_education = round(no_with_ad_ed_gt_50k / no_with_ad_ed * 100, 1)
#print(higher_education)
#print(df_with_ad_ed.value_counts('salary').loc['>50K'])


# higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
# lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

# higher_education_no = higher_education.shape[0]
# lower_education_no = lower_education.shape[0]

# higher_education_no_rich = higher_education.value_counts('salary').loc['>50K']
# lower_education_no_rich = lower_education.value_counts('salary').loc['>50K']

# higher_education_rich = round(higher_education_no_rich / higher_education_no * 100, 1)
# lower_education_rich = round(lower_education_no_rich / lower_education_no * 100, 1)
# print(higher_education_rich)

# print(df['hours-per-week'].min())
# min_work_hours = df['hours-per-week'].min()

# print(df[df['hours-per-week'] == min_work_hours])
# min_workers = df[df['hours-per-week'] == min_work_hours]

# num_min_workers = min_workers.shape[0]

# num_min_workers_rich = min_workers.value_counts('salary').loc['>50K']

# rich_percentage = round(num_min_workers_rich / num_min_workers * 100, 1)
# print(rich_percentage)

# What country has the highest percentage of people that earn >50K?
# print(df['native-country'])
# print(df.value_counts('native-country'))


# print(df[df['salary'] == '>50K'])

# all_over_50k = df[df['salary'] == '>50K']
# print(all_over_50k.value_counts('native-country'))

# print(round(all_over_50k.value_counts('native-country') / df.value_counts('native-country') * 100, 1))

# country_pcnts = round(all_over_50k.value_counts('native-country') / df.value_counts('native-country') * 100, 1)
# print(country_pcnts.max())
# print(country_pcnts.idxmax())

# highest_earning_country = None
# highest_earning_country_percentage = None

# print(df[(df['salary'] == '>50K') & (df['native-country'] == 'India')].value_counts('occupation').idxmax())