
Q1 Consider the following company sales data for data visualisation. Use the following  CSV file for the exercise read this files using Pandas or NumPy or using built in matplotlib  functions 
# Importing required libraries and  
dataset import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt  
import seaborn as sns %matplotlib  
inline 
df = pd.read_csv("company_sales_data.csv") 
df 
month_number facecream facewash toothpaste bathingsoap shampoo \ 0 1 2500 1500 5200 9200 1200 1 2 2630 1200 5100 6100 2100 2 3 2140 1340 4550 9550 3550 3 4 3400 1130 5870 8870 1870 4 5 3600 1740 4560 7760 1560 5 6 2760 1555 4890 7490 1890 6 7 2980 1120 4780 8980 1780 7 8 3700 1400 5860 9960 2860 8 9 3540 1780 6100 8100 2100 9 10 1990 1890 8300 10300 2300 10 11 2340 2100 7300 13300 2400 11 12 2900 1760 7400 14400 1800 
moisturizer total_units total_profit 
0 1500 21100 211000 
1 1200 18330 183300 
2 1340 22470 224700 
3 1130 22270 222700 
4 1740 20960 209600 
5 1555 20140 201400
6 1120 29550 295500 
7 1400 36140 361400 
8 1780 23400 234000 
9 1890 26670 266700 
10 2100 41280 412800 
11 1760 30020 300200 
a) Read total profit of all months and show it using line plot. Generated line plot must  include the following properties 
x label name = month number d y label name = total profit location # Python code 
plt.figure(figsize=(10,6)) 
months=np.arange(1,13) 
plt.plot(months,df['total_profit']) 
plt.title("Company Profit Per Month") 
plt.xlabel('month_number') 
plt.xticks(np.arange(0,13,1)) 
plt.ylabel('total_profit') 
plt.yticks(np.arange(0,600000,100000)) 
plt.show() 
# Output:

b)Get total profit of all months and show lineplot using following style propertie.  Generated line plot must include following style properties 
linestyle dotted and line colour should be Red show Legend at lower right  location x label name = month number y label name = sold units number add a  circle marker line marker colour as Red linewidth should be three 
# Python code 
plt.figure(figsize=(10,6)) 
plt.plot(months,df['total_profit'],color='r',linestyle='dashdot',linewidth=3, marker='o',markerfacecolor='maroon') 
plt.title("Company Sales Data Last Year") 
plt.xlabel('month_number') 
plt.ylabel('total_profit') 
plt.legend(['profit of data last year'],loc='lower right') plt.xticks(np.arange(0,13,1)) 
plt.yticks(np.arange(0,600000,100000)) 
plt.show() 
# Output: 

c) Read all product sales data and show it using multiline plot that is display the number  of units sold per month for each product using multiline plots 
# Python code 
plt.figure(figsize=(10,8)) 
colors=['blue','orange','green','red','purple','brown']
legends = ['facecream', 'facewash', 'toothpaste', 'bathingsoap','shampoo', 'moisturizer'] 
plt.plot(months,df['facecream'],color=colors[0],marker='o',linewidth=2) plt.plot(months,df['facewash'],color=colors[1],marker='o',linewidth=2) plt.plot(months,df['toothpaste'],color=colors[2],marker='o',linewidth=2) plt.plot(months,df['bathingsoap'],color=colors[3],marker='o',linewidth=2) plt.plot(months,df['shampoo'],color=colors[4],marker='o',linewidth=2) plt.plot(months,df['moisturizer'],color=colors[5],marker='o',linewidth=2) plt.title("Sales Data") 
plt.xlabel('month_number') 
plt.xticks(np.arange(0,13,1)) 
plt.ylabel('Sales unit in numbers') 
plt.xticks(np.arange(0,13,1)) 
plt.yticks(np.arange(0,16000,1000)) 
plt.legend(labels=legends) 
plt.show() 
# Output:

d) Read toothpaste sales data of each month and show it using scatterplot also add a grid  to plot. Gridline style should be "-" 
# Python code 
plt.figure(figsize=(10, 8)) 
plt.scatter(months, df['toothpaste'], color='blue', alpha=0.5) plt.grid(linestyle='--') 
plt.title("Toothpaste Sales Data") 
plt.xlabel("Month Number") 
plt.ylabel("Number of Units Sold") 
plt.xticks(np.arange(0,13,1)) 
plt.yticks(np.arange(0,10000,1000)) 
plt.ylim(4000, 9000) 
plt.legend(labels=['Toothpaste Sales Data'],loc='upper left') plt.show() 
# Output:

e) Read facecream and facewash products sales data and show it using barchart. The  barchart should display the number of unit sold per month for each product. Add a separate  bar for each product in the same chart 
# Python code 
plt.bar(months-0.2,df['facecream'],0.4,color='blue') 
plt.bar(months+0.2,df['facewash'],0.4,color='orange') 
plt.title("Facewash and Facecream Sales Data") 
plt.xlabel("Month Number") 
plt.ylabel("Sales Units in Numbers") 
plt.xticks(np.arange(0,13,1)) 
plt.yticks(np.arange(0,5000,500)) 
plt.grid(linestyle='--') 
plt.legend(labels=['facecream','facewash'],loc='upper left') plt.show() 
# Output: 

f)Read sales data of bathing soap all months and show it using a barchart save this plot  to your hard disk 
# Python code
plt.bar(months,df['bathingsoap'],color='blue') 
plt.title(" Bathingsoap Sales Data") 
plt.xlabel("Month Number") 
plt.ylabel("Sales Units in Numbers") 
plt.xticks(np.arange(0,13,1)) 
plt.yticks(np.arange(0,15000,1000)) 
plt.grid(linestyle='--') 
plt.legend(labels=['bathingsoap sales']) 
plt.show() 
plt.savefig('bathing_soap_sales.png') 
# Output: 
<Figure size 640x480 with 0 Axes> 
g) Read the total profit of each month and show it using histogram to see the most  common profit ranges 
# Python code 
plt.figure(figsize=(8, 8)) 
plt.hist(df['total_profit'],color='blue') 
plt.title("Profit data")
plt.xlabel("Profit range in dollar") 
plt.ylabel("Number of companies") 
plt.xticks(rotation=45) 
plt.xticks(np.arange(0,450000,25000)) 
plt.xlim(150000,450000) 
plt.show() 
# Output: 

h) Calculate total sales data for last year for each product and show it using pie chart note  in pie chart display number of units sold per year for each product in percentage # Python code 
columns = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo',
'moisturizer'] 
total_profit = df['total_profit'].sum() 
total_profit_by_products = [df[x].sum() for x in columns] 
plt.figure(figsize=(8, 8)) 
plt.pie(total_profit_by_products, labels=columns, autopct="%1.1f%%") plt.title('Sales Data') 
plt.legend(loc='lower right') 
plt.show() 
# Output: 

i) Read bathing soap and face wash of all months and display it using subplots # Python code
fig, axes = plt.subplots(2, 1, figsize=(12, 6)) 
axes[0].plot(df['month_number'], df['bathingsoap'],  
marker='o', color='black', linewidth=3) 
axes[0].set_title('Sales Data for Bathing Soap') 
axes[0].set_ylabel("Sales Unit in Number") 
axes[1].plot(df['month_number'], df['facewash'], marker='o',  color='red', linewidth=3) 
axes[1].set_title('Sales Data for Facewash') 
axes[1].set_ylabel("Sales Unit in Number") 
plt.xlabel("Month Number") 
plt.xticks(np.arange(1, 13, 1)) 
plt.tight_layout() 
plt.show() 
# Output: 

j) Read all product sales data and show it using stack plot 
# Python code 
columns = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer'] 
sales_data = df[columns].values.T 
color = ['purple', 'turquoise', 'red', 'black', 'green', 'yellow'] 
plt.figure(figsize=(10, 6)) 
plt.stackplot(df['month_number'], sales_data, labels=columns,colors=color) plt.title('Stack Plot of Sales Data') 
plt.xlabel('Month')
plt.xticks(np.arange(0,13,1)) 
plt.ylabel('Sales Units in Numbers') 
plt.legend(loc='upper left') 
plt.show() 
# Output:

