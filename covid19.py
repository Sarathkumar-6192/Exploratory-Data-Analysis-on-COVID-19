import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime


cases_url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/' \
            'csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
vacc_url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv'

cases_df = pd.read_csv(cases_url)
vacc_df = pd.read_csv(vacc_url)


cases_long = cases_df.melt(
    id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], 
    var_name='Date', 
    value_name='ConfirmedCases'
)

cases_long['Date'] = pd.to_datetime(cases_long['Date'])

countries = ['US', 'India', 'United Kingdom', 'Brazil']
cases_filtered = cases_long[cases_long['Country/Region'].isin(countries)]

cases_agg = cases_filtered.groupby(['Country/Region', 'Date'])['ConfirmedCases'].sum().reset_index()
cases_agg['NewCases'] = cases_agg.groupby('Country/Region')['ConfirmedCases'].diff().fillna(0)


vacc_filtered = vacc_df[vacc_df['location'].isin(countries)].copy()
vacc_filtered['date'] = pd.to_datetime(vacc_filtered['date'])

merged_df = pd.merge(cases_agg, vacc_filtered, 
                     left_on=['Country/Region', 'Date'], 
                     right_on=['location', 'date'], 
                     how='left')

merged_df['people_vaccinated_per_hundred'] = merged_df['people_vaccinated_per_hundred'].fillna(0)
merged_df['people_fully_vaccinated_per_hundred'] = merged_df['people_fully_vaccinated_per_hundred'].fillna(0)


plt.figure(figsize=(14,8))
for country in countries:
    subset = merged_df[merged_df['Country/Region'] == country]
    plt.plot(subset['Date'], subset['NewCases'], label=f'{country} New Cases')
    # Scale vaccination rate for better visualization
    plt.plot(subset['Date'], subset['people_fully_vaccinated_per_hundred'] * 1000, label=f'{country} Vaccinated (scaled)')

plt.title('Daily New COVID-19 Cases and Vaccination Rate (Scaled)')
plt.xlabel('Date')
plt.ylabel('Count / Vaccination Rate (scaled)')
plt.legend()
plt.show()


print("Correlation between New Cases and Fully Vaccinated Rate:")
for country in countries:
    subset = merged_df[merged_df['Country/Region'] == country]
    corr = subset['NewCases'].corr(subset['people_fully_vaccinated_per_hundred'])
    print(f"{country}: {corr:.3f}")


corr_list = []
for country in countries:
    subset = merged_df[merged_df['Country/Region'] == country]
    corr = subset['NewCases'].corr(subset['people_fully_vaccinated_per_hundred'])
    corr_list.append({'Country': country, 'Correlation': corr})

corr_df = pd.DataFrame(corr_list)

sns.barplot(data=corr_df, x='Country', y='Correlation')
plt.title('Correlation between New Cases and Vaccination Rate by Country')
plt.show()


print("\nSummary:")
print(" - Negative correlation suggests vaccination rollout contributed to reducing new COVID-19 cases.")
print(" - Variations across countries indicate other factors like policy, variants, and testing rates.")
print(" - Visualizations show how vaccination rates and case counts evolved over time.")
