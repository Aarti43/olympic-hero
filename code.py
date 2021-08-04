# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Path of the file
path

#Code starts here
data = pd.read_csv(path)
data.rename(columns={"Total" : "Total_Medals"}, inplace = True)
data.head()


# --------------
#Code starts here
data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', (np.where(data['Total_Summer'] < data['Total_Winter'], 'Winter', 'Both')))
better_event = data['Better_Event'].value_counts().index.tolist()[0]
print('Better Event Performace:', better_event)


# --------------
#Code starts here
top_countries = data[['Country_Name', 'Total_Summer', 'Total_Winter', 'Total_Medals']]
top_countries.drop(top_countries.index[-1], inplace= True)
def top_ten(df, col):
    country_list = []
    country_list = list(df.nlargest(10, col).Country_Name)
    return country_list
top_10_summer = top_ten(top_countries,'Total_Summer')
print("Top 10 Summer Team", top_10_summer)
print('----------------------------------------')

top_10_winter = top_ten(top_countries,'Total_Winter')
print("Top 10 Winter Team", top_10_winter)
print('----------------------------------------')

top_10 = top_ten(top_countries,'Total_Medals')
print("Overall Top 10 Team", top_10)
print('----------------------------------------')

set1 =  set(top_10_summer)
set2 = set(top_10_winter)
set3 = set(top_10)

common = list((set1.intersection(set2)).intersection(set3))

print("Common Teams", common)
print('----------------------------------------')



# --------------
#Code starts here
summer_df = data[data['Country_Name'].isin(top_10_summer)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]
top_df = data[data['Country_Name'].isin(top_10)]
plt.bar(summer_df['Country_Name'], summer_df['Total_Summer'], color ='maroon', width = 0.4)
plt.xlabel("Country")
plt.xticks(rotation=75)
plt.ylabel("Winners")
plt.title("Top 10 Olympic medal winner countries in Summer")
plt.show()
print('--------------------------------------------------')
plt.bar(winter_df['Country_Name'], winter_df['Total_Summer'], color ='orange', width = 0.4)
plt.xlabel("Country")
plt.xticks(rotation=75)
plt.ylabel("Winners")
plt.title("Top 10 Olympic medal winner countries in Winter")
plt.show()
print('--------------------------------------------------')
plt.bar(top_df['Country_Name'], top_df['Total_Summer'], color ='pink', width = 0.4)
plt.xlabel("Country")
plt.xticks(rotation=75)
plt.ylabel("Winners")
plt.title("Top 10 Olympic medal winner countries Overall")
plt.show()


# --------------
#Code starts here
summer_df['Golden_Ratio'] = summer_df['Gold_Summer'] / summer_df['Total_Summer']
summer_max_ratio = summer_df['Golden_Ratio'].max()
summer_country_gold = summer_df.loc[summer_df['Golden_Ratio'] == summer_max_ratio, 'Country_Name'].iloc[0]
print("Maximum Gold Medal winner Country in Summer is:", summer_country_gold)
print("-------------------------------------------")
winter_df['Golden_Ratio'] = winter_df['Gold_Winter'] / winter_df['Total_Winter']
winter_max_ratio = winter_df['Golden_Ratio'].max()
winter_country_gold = winter_df.loc[winter_df['Golden_Ratio'] == winter_max_ratio, 'Country_Name'].iloc[0]
print("Maximum Gold Medal winner Country in Winter is", winter_country_gold)
print("-------------------------------------------")
top_df['Golden_Ratio'] = top_df['Gold_Total'] / top_df['Total_Medals']
top_max_ratio = top_df['Golden_Ratio'].max()
top_country_gold = top_df.loc[top_df['Golden_Ratio'] == top_max_ratio, 'Country_Name'].iloc[0]
print("Maximum Gold Medal winner Country in Winter is", top_country_gold)



# --------------
#Code starts here


#Removing the last column of the dataframe
data_1=data[:-1]

#Creating a new column 'Total_Points'
data_1['Total_Points']= data_1['Gold_Total']*3 + data_1['Silver_Total']*2 + data_1['Bronze_Total']*1  # Use of position index to handle the ambiguity of having same name columns
print("total Points:", data_1['Total_Points'] )
print("------------------------------------------------------------------")


#Finding the maximum value of 'Total_Points' column
most_points=max(data_1['Total_Points'])
print("Most points earned:", most_points)
print("------------------------------------------------------------------")

#Finding the country assosciated with the max value of 'Total_Column' column
best_country=data_1.loc[data_1['Total_Points'].idxmax(),'Country_Name']
print('The maximum points achieved is ', most_points, ' by ', best_country )

#Code ends here


# --------------
#Code starts here
best = data[data['Country_Name'] == best_country]
best = best[['Gold_Total','Silver_Total','Bronze_Total']]
best.plot.bar(stacked=True)
plt.xlabel('United States')
plt.ylabel('Medals Tally')
plt.xticks(rotation=45)


