import pandas as pd
import matplotlib.pyplot as plt
data= pd.read_csv(r"C:\Users\user\Desktop\DHEX-TECH TRAINING\Dhex_Project\data\E-commerce Customer Behavior -Project 1.csv")
print(data.columns)

#Check for duplicates
print(data.duplicated().sum())

#Check for missing values
print(data.isnull().sum())

#drop missing data 
data.dropna(inplace=True)

#check again for missing data
print(data.isnull().sum())

#total spent by city
tot_by_city=data.pivot_table(values="Total Spend",index="City",aggfunc="sum").squeeze()
print(tot_by_city)
#graph
plt.pie(tot_by_city, labels=tot_by_city.index,autopct="%.2f%%")
plt.show()


#total spent by gender
tot_by_gender=data.pivot_table(values="Total Spend",index="Gender",aggfunc="sum")
print(tot_by_gender)

#total average rating by gender
data["Average Rating"]= data["Average Rating"].astype(int)
avg_rating=data.pivot_table(values="Average Rating",index="Gender",aggfunc="sum")
print(avg_rating)

#satisfaction level by gender
print(data.loc[:,["Gender","Satisfaction Level"]])
satisfaction_level= (data.groupby(["Gender","Satisfaction Level"]).size())
print(satisfaction_level)

#highest item purchased by city
print(data.sort_values(["Items Purchased","City"], ascending=[False,True]))

#highest item purchased by gender
item_gender= (data.pivot_table(values="Items Purchased",index="Gender",aggfunc=max))
print(item_gender)

#plot of city versus gender
item_gender.plot(kind="bar")
plt.show()

plt.pie(satisfaction_level, labels=satisfaction_level.index,autopct="%.2f%%")
plt.show()
