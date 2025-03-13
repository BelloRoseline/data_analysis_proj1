import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv(r"C:\Users\user\Desktop\DHEX-TECH TRAINING\Dhex_Project\data\Dhex_Financial Record-Project 2.csv")

#Check for duplicates
print(data.duplicated().sum())

#Check for missing values
print(data.isnull().sum())

#fill missing data with NAN
#data.fillna("NAN", inplace=True)
data.dropna(inplace=True)
#check again for missing data
print(data.isnull().sum())

#data cleaning
data["Client"]= data["Client"].astype(str).str.replace("\s*\(.*?\)","",regex=True)
data["Contact"] =data["Contact"].str.title().str.replace("\s+"," ",regex=True)

# Convert "Revenue" to numeric
data["Revenue"] = pd.to_numeric(data["Revenue"], errors="coerce")

# Pivot table for revenue by department
revenue_by_dept = data.pivot_table(values="Revenue", columns="Department", aggfunc="sum").squeeze()


# Plot the bar chart
plot= revenue_by_dept.plot(kind="bar")

# Add labels to each bar
for bars in plot.containers:  
    plot.bar_label(bars, fmt="%.2f")

# Show plot
plt.show()


#profit by department
profit_by_dept=data.groupby("Department")["Profit"].sum()
pf_by_d=profit_by_dept.plot(kind= "bar")
#add labels
for bars in pf_by_d.containers:
    pf_by_d.bar_label(bars,fmt="%d")
#show plot 
plt.show()


#highest revenue by client
print(data.sort_values(["Revenue","Client"],ascending=[False,True]))

#count the payment type
payment= data["Payment"].value_counts()


plt.pie(payment, labels=payment.index,autopct="%.2f%%")
plt.show()
