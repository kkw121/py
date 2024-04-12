Data Visualization Using Python Programming 
Case Study-02 Data Visualization Using Seaborn 
Q1 Read all product sales data and show it using stack plot use the seaborn Python library for data visualisation import seaborn and load data sets # Importing required libraries and dataset 
import pandas as pd 
import numpy as np 
from matplotlib import pyplot as plt 
import seaborn as sns 
%matplotlib inline 
import warnings 
warnings.filterwarnings("ignore") 
df = pd.read_csv("titanic.csv") 
df 
Pclass Sex Age SibSp Parch Fare Embarked Survived 0 3 male 22.0 1 0 7.2500 S 0 1 1 female 38.0 1 0 71.2833 C 1 2 3 female 26.0 0 0 7.9250 S 1 3 1 female 35.0 1 0 53.1000 S 1 4 3 male 35.0 0 0 8.0500 S 0 .. ... ... ... ... ... ... ... ... 886 2 male 27.0 0 0 13.0000 S 0 887 1 female 19.0 0 0 30.0000 S 1 888 3 female 21.5 1 2 23.4500 S 0 889 1 male 26.0 0 0 30.0000 C 1 890 3 male 32.0 0 0 7.7500 Q 0 
[891 rows x 8 columns] 
print(sns.get_dataset_names()) 
['anagrams', 'anscombe', 'attention', 'brain_networks', 'car_crashes', 'diamonds', 'dots', 'dowjones', 'exercise', 'flights', 'fmri', 'geyser', 'glue', 'healthexp', 'iris', 'mpg', 'penguins', 'planets', 'seaice', 'taxis', 'tips', 'titanic', 'anagrams', 'anagrams', 'anscombe', 'anscombe', 'attention', 'attention', 'brain_networks', 'brain_networks', 'car_crashes', 'car_crashes', 'diamonds', 'diamonds', 'dots', 'dots', 'dowjones', 'dowjones', 'exercise', 'exercise', 'flights', 'flights', 'fmri', 'fmri', 'geyser', 'geyser', 'glue', 'glue', 'healthexp', 'healthexp', 'iris', 'iris', 'mpg', 'mpg', 'penguins', 'penguins', 'planets', 'planets', 'seaice', 'seaice', 'taxis', 'taxis', 'tips', 'tips', 'titanic', 'titanic', 'anagrams', 'anscombe', 'attention', 'brain_networks', 'car_crashes', 'diamonds', 'dots', 'dowjones', 'exercise', 'flights', 'fmri', 'geyser', 'glue', 'healthexp', 'iris', 'mpg', 'penguins', 'planets', 'seaice', 'taxis', 'tips', 'titanic']
a) Consider and use Titanic data set for data visualisation below display the column sex which contains categorical value and in the Titanic data set that is male and female and visualise it using count plot 
# Python code 
colors = ['red', 'blue', 'green'] 
sns.countplot(x=df['Sex'],palette=colors,width=0.8) 
plt.title("Gender Distribution") 
plt.ylabel('Number of Passengers') 
plt.show() 
# Output: 

1 b) display the cloud is which contains containers data in Titanic data set draw kernel density estimate plot the distribution of continuous data is using kdeplot() 
# Python code 
sns.kdeplot(df['Age']) 
plt.title('Kernel Density Destribution of Age ') 
plt.show() 
# Output:

c) Display the plot of distribution countinuous data 'age' using displot(). Set kde=true bins= 5 # Python code 
sns.displot(df['Age'], kde=True, bins=5, color=(0, 102/255, 1)) plt.title('Distribution of Age') 
plt.ylabel('Number of Passengers') 
plt.show() 
#Output:

Q2 Consider and use the Iris data set for data visualisation below iris = sns.load_dataset('iris') 
iris.head(5) 
sepal_length sepal_width petal_length petal_width species 0 5.1 3.5 1.4 0.2 setosa 1 4.9 3.0 1.4 0.2 setosa 2 4.7 3.2 1.3 0.2 setosa 3 4.6 3.1 1.5 0.2 setosa 4 5.0 3.6 1.4 0.2 setosa 
a) Display scatter plot of iris flowers features 'sepal_length' vs 'petal_length' and set hue = 'species' using scatterplot 
# Python code 
sns.scatterplot(data=iris, x='sepal_length', y='petal_length', hue='species', palette=colors) 
plt.title('Distribution of Sepal Length vs Petal Length') 
plt.ylabel('Petal Length')
plt.xlabel('Sepal Length') 
plt.show() 
#Output: 

b) Display a jointplot is to plot the correlation between Iris data of features 'sepal_length' vs 'petal_length'.Set kind = 'reg' using jointplot 
# Python code 
sns.jointplot(data=iris, x='sepal_length', y='petal_length', palette=colors,kind='reg') 
plt.ylabel('Petal Length') 
plt.xlabel('Sepal Length') 
plt.suptitle('Distribution of Sepal Length vs Petal Length', y=0) plt.show() 
#Output:

c) Display pair plot of iris data set using pairplot 
# Python code 
sns.pairplot(data=iris,hue="species",palette=colors) 
plt.suptitle('Sepal Length vs Petal Length',y=0) 
plt.show() 
#Output:


