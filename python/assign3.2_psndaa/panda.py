

Case Study: Data Analysis using pandas : Experiential Learning  Assignment-01 
---------------------------------------------------------------------------------------------------------------------- - 
Q.1) Write Python Programs based on pandas Series data structure. ## a) Create a pandas Series S1 of elements [2, 5, 6, 8, 5, -10, 2, -2]. 
# Python code 
import pandas as pd 
import numpy as np 
S1 = pd.Series([2, 5, 6, 8, 5, -10, 2, -2]) 
## b) Recreate a pandas Series S1, include the index option and assign an  array 
## of strings containing the labels. 
# Python code 
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] 
S1_with_index = pd.Series([2, 5, 6, 8, 5, -10, 2, -2], index=labels) 
## c) Display two arrays individually that make up the Series data  structure 
## in Pandas using index and values attributes.
Page 1 of 16 
# Python code 
print("S1 Index:", S1_with_index.index) 
print("S1 Values:", S1_with_index.values) 
# Output: 
S1 Index: Index(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], dtype='object') S1 Values: [ 2 5 6 8 5 -10 2 -2] 
## d) Select individual elements of a Series S1 by specifying the Key and  Label 
## corresponding to the position of the index. 
# Python code 
print("Element at index 'c':", S1_with_index['c']) 
# Output: 
Element at index 'c': 6 
## e) Select multiple elements of a Series S1 by specifying the Key and  Label 
## corresponding to the position of the index using slicing. 
# Python code 
print("Elements from index 'c' to 'f':", S1_with_index['c':'f']) 
# Output: 
Elements from index 'c' to 'f': c 6 
d 8 
e 5 
f -10 
dtype: int64 
## f) Create a Series S2 and S3 from NumPy Arrays and any other Series. 
# Python code 
S2 = pd.Series(np.array([10, 20, 30, 40, 50])) 
S3 = pd.Series(S1 * 2) 
# Output: 
## g) Select all elements of Series S1 which are less than 8, Series S2  which 
## are greater than 5 and Series S3 which are less than 0. 
# Python Code 
print("S1 < 8:", S1[S1 < 8]) 
print("S2 > 5:", S2[S2 > 5])
Page 2 of 16 
print("S3 < 0:", S3[S3 < 0]) 
# Output: 
S1 < 8: 0 2 
1 5 
2 6 
4 5 
5 -10 
6 2 
7 -2 
dtype: int64 
S2 > 5: 0 10 
1 20 
2 30 
3 40 
4 50 
dtype: int64 
S3 < 0: 5 -20 
7 -4 
dtype: int64 
## h) Perform operations using operators such as (+, -, *, and /) on  Series 
## S1, S2 and S3, and any three mathematical functions on each Series. 
# Python Code 
print("S1 + S2:", S1 + S2) 
print("S1 - S2:", S1 - S2) 
print("S1 * S2:", S1 * S2) 
print("S1 / S2:", S1 / S2) 
print("Square root of S1:", np.sqrt(S1)) 
print("Absolute values of S2:", np.abs(S2)) 
print("Exponential of S3:", np.exp(S3)) 
#Output: 
S1 + S2: 0    12.0 
1    25.0 
2    36.0 
3    48.0 
4    55.0 
5     NaN 
6     NaN 
7     NaN 
dtype: float64 
S1 - S2: 0    -8.0 
1   -15.0 
2   -24.0 
3   -32.0 
4   -45.0 
5     NaN 
6     NaN 
7     NaN 
dtype: float64 
S1 * S2: 0     20.0 
1    100.0
Page 3 of 16 
2    180.0 
3    320.0 
4    250.0 
5      NaN 
6      NaN 
7      NaN 
dtype: float64 
S1 / S2: 0    0.20 
1    0.25 
2    0.20 
3    0.20 
4    0.10 
5     NaN 
6     NaN 
7     NaN 
dtype: float64 
Square root of S1: 0    1.414214 
1    2.236068 
2    2.449490 
3    2.828427 
4    2.236068 
5         NaN 
6    1.414214 
7         NaN 
dtype: float64 
Absolute values of S2: 0    10 
1    20 
2    30 
3    40 
4    50 
dtype: int64 
Exponential of S3: 0    5.459815e+01 
1    2.202647e+04 
2    1.627548e+05 
3    8.886111e+06 
4    2.202647e+04 
5    2.061154e-09 
6    5.459815e+01 
7    1.831564e-02 
dtype: float64 
/usr/local/lib/python3.10/dist-packages/pandas/core/arraylike.py:402: RuntimeWarning: invalid value  encountered in sqrt 
  result = getattr(ufunc, method)(*inputs, **kwargs) 
## i) Select all the values contained in the Series S1, excluding  duplicate. 
# Python Code 
print("Unique values in S1:", S1.unique()) 
# Output: 
Unique values in S1: [ 2 5 6 8 -10 -2] 
## j) Select all the values contained in the Series S1, excluding  duplicates 
## and count the occurrences of each unique value. 
# Python Code
Page 4 of 16 
print("Value counts in S1:", S1.value_counts()) 
# Output: 
Value counts in S1:  2     2 
5     2 
6     1 
8     1 
-10    1 
-2     1 
dtype: int64 
## k) Demonstrate the use of isin() membership function on each of the  Series 
## S1, S2 and S3. 
# Python Code 
print("S1 isin [2, 5, 10]:", S1.isin([2, 5, 10])) 
print("S2 isin [20, 30, 40]:", S2.isin([20, 30, 40])) 
print("S3 isin [-5, 0, 5]:", S3.isin([-5, 0, 5])) 
# Output: 
S1 isin [2, 5, 10]: 0 True 
1 True 
2 False 
3 False 
4 True 
5 False 
6 True 
7 False 
dtype: bool 
S2 isin [20, 30, 40]: 0 False 
1 True 
2 True 
3 True 
4 False 
dtype: bool 
S3 isin [-5, 0, 5]: 0 False 
1 False 
2 False 
3 False 
4 False 
5 False 
6 False 
7 False 
dtype: bool 
## l) Create a Series S4 of elements [2, 5, 6, np.NaN, 5, np.NaN, 2, -2]  and 
## demonstrate the use of isnull() and notnull() functions on Series  S4. 
# Python Code 
S4 = pd.Series([2, 5, 6, np.NaN, 5, np.NaN, 2, -2]) 
print("S4 isnull:", S4.isnull())
Page 5 of 16 
print("S4 notnull:", S4.notnull()) 
# Output: 
S4 isnull: 0 False 
1 False 
2 False 
3 True 
4 False 
5 True 
6 False 
7 False 
dtype: bool 
S4 notnull: 0 True 
1 True 
2 True 
3 False 
4 True 
5 False 
6 True 
7 True 
dtype: bool 
## m) Create a Series S5 from a previously defined dictionary and display  it. 
# Python Code 
dict_data = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5} 
S5 = pd.Series(dict_data) 
print("S5 from dictionary:", S5) 
# Output: 
S5 from dictionary: a 1 
b 2 
c 3 
d 4 
e 5 
dtype: int64 
Q.2) Write Python Programs based on pandas DataFrame data  structure. 
## a) Read the data stored as a csv file into a pandas DataFrame titanic  using 
## read_csv(). 
# Python code 
import pandas as pd 
url = 'https://raw.githubusercontent.com/pandas 
dev/pandas/main/doc/data/titanic.csv' 
titanic = pd.read_csv(url)
Page 6 of 16 
## b) Display top 5 and bottom 5 rows of the DataFrame titanic. 
# Python code 
print("Top 5 rows:") 
print(titanic.head()) 
print("\nBottom 5 rows:") 
print(titanic.tail()) 
# Output: 
Top 5 rows: 
 PassengerId Survived Pclass \ 
0 1 0 3  
1 2 1 1  
2 3 1 3  
3 4 1 1  
4 5 0 3  
 Name Sex Age SibSp  \ 
0 Braund, Mr. Owen Harris male 22.0 1  1 Cumings, Mrs. John Bradley (Florence Briggs Th... female 38.0 1  2 Heikkinen, Miss. Laina female 26.0 0  3 Futrelle, Mrs. Jacques Heath (Lily May Peel) female 35.0 1  4 Allen, Mr. William Henry male 35.0 0  
 Parch Ticket Fare Cabin Embarked  
0 0 A/5 21171 7.2500 NaN S  
1 0 PC 17599 71.2833 C85 C  
2 0 STON/O2. 3101282 7.9250 NaN S  
3 0 113803 53.1000 C123 S  
4 0 373450 8.0500 NaN S  
Bottom 5 rows: 
 PassengerId Survived Pclass  
Name \ 
886 887 0 2 Montvila, Rev.  Juozas  
887 888 1 1 Graham, Miss. Margaret  Edith  
888 889 0 3 Johnston, Miss. Catherine Helen  "Carrie"  
889 890 1 1 Behr, Mr. Karl  Howell  
890 891 0 3 Dooley, Mr.  Patrick  
 Sex Age SibSp Parch Ticket Fare Cabin Embarked  886 male 27.0 0 0 211536 13.00 NaN S  887 female 19.0 0 0 112053 30.00 B42 S  888 female NaN 1 2 W./C. 6607 23.45 NaN S  889 male 26.0 0 0 111369 30.00 C148 C  890 male 32.0 0 0 370376 7.75 NaN Q 
## c) Check the column data types of all the columns of DataFrame titanic.
Page 7 of 16 
# Python code 
print("\nColumn data types:") 
print(titanic.dtypes) 
# Output: 
Column data types: 
PassengerId      int64 
Survived         int64 
Pclass           int64 
Name            object 
Sex             object 
Age            float64 
SibSp            int64 
Parch            int64 
Ticket          object 
Fare           float64 
Cabin           object 
Embarked        object 
dtype: object 
[ ] 
## d) Save (store) Titanic dataset (DataFrame) as a spreadsheet (.xlsx) usi ng 
## to_excel(). 
# Python code 
titanic.to_excel('titanic_dataset.xlsx', index=False) 
## e) Display the technical summary of a DataFrame titanic. 
# Python code 
print("\nTechnical summary:") 
print(titanic.info()) 
# Output: 
Technical summary: 
<class 'pandas.core.frame.DataFrame'> 
RangeIndex: 891 entries, 0 to 890 
Data columns (total 12 columns): 
# Column Non-Null Count Dtype  
--- ------ -------------- -----  
0 PassengerId 891 non-null int64  
1 Survived 891 non-null int64  
2 Pclass 891 non-null int64  
3 Name 891 non-null object  
4 Sex 891 non-null object  
5 Age 714 non-null float64 
6 SibSp 891 non-null int64  
7 Parch 891 non-null int64  
8 Ticket 891 non-null object  
9 Fare 891 non-null float64
Page 8 of 16 
10 Cabin 204 non-null object  
11 Embarked 889 non-null object  
dtypes: float64(2), int64(5), object(5) 
memory usage: 83.7+ KB 
None 
## f) Select a single column of a DataFrame titanic and also check the  type() 
## and shape of that column. 
# Python code 
single_column = titanic['Name'] 
print("\nType of single column:", type(single_column)) 
print("Shape of single column:", single_column.shape) 
# Output: 
Type of single column: <class 'pandas.core.series.Series'> Shape of single column: (891,) 
## g) Select multiple columns of a DataFrame titanic and also check the  type() 
## and shape of those columns. 
# Python code 
multiple_columns = titanic[['Name', 'Age', 'Fare']] 
print("\nType of multiple columns:", type(multiple_columns)) print("Shape of multiple columns:", multiple_columns.shape) 
# Output: 
Type of multiple columns: <class 'pandas.core.frame.DataFrame'> Shape of multiple columns: (891, 3) 
## h) Select all the passengers from the titanic DataFrame who are not  older 
## than than 50 years. 
# Python code 
young_passengers = titanic[titanic['Age'] <= 50] 
# Output: 
 PassengerId Survived Pclass \ 
0 1 0 3  
1 2 1 1  
2 3 1 3  
3 4 1 1  
4 5 0 3 
Page 9 of 16 
.. ... ... ...  
885 886 0 3  
886 887 0 2  
887 888 1 1  
889 890 1 1  
890 891 0 3  
 Name Sex Age SibSp  \ 
0 Braund, Mr. Owen Harris male 22.0 1  1 Cumings, Mrs. John Bradley (Florence Briggs Th... female 38.0 1  2 Heikkinen, Miss. Laina female 26.0 0  3 Futrelle, Mrs. Jacques Heath (Lily May Peel) female 35.0 1  4 Allen, Mr. William Henry male 35.0 0  .. ... ... ... ...  885 Rice, Mrs. William (Margaret Norton) female 39.0 0  886 Montvila, Rev. Juozas male 27.0 0  887 Graham, Miss. Margaret Edith female 19.0 0  889 Behr, Mr. Karl Howell male 26.0 0  890 Dooley, Mr. Patrick male 32.0 0  
 Parch Ticket Fare Cabin Embarked  
0 0 A/5 21171 7.2500 NaN S  
1 0 PC 17599 71.2833 C85 C  
2 0 STON/O2. 3101282 7.9250 NaN S  
3 0 113803 53.1000 C123 S  
4 0 373450 8.0500 NaN S  
.. ... ... ... ... ...  
885 5 382652 29.1250 NaN Q  
886 0 211536 13.0000 NaN S  
887 0 112053 30.0000 B42 S  
889 0 111369 30.0000 C148 C  
890 0 370376 7.7500 NaN Q  
[650 rows x 12 columns] 
## i) Select all titanic passengers from cabin class 1 and 3. 
# Python code 
cabin_class_1_3 = titanic[titanic['Pclass'].isin([1, 3])] 
# Output: 
 PassengerId Survived Pclass \ 
0 1 0 3  
1 2 1 1  
2 3 1 3  
3 4 1 1  
4 5 0 3  
.. ... ... ...  
885 886 0 3  
887 888 1 1  
888 889 0 3  
889 890 1 1  
890 891 0 3 
Page 10 of 16 
 Name Sex Age SibSp  \ 
0 Braund, Mr. Owen Harris male 22.0 1  1 Cumings, Mrs. John Bradley (Florence Briggs Th... female 38.0 1  2 Heikkinen, Miss. Laina female 26.0 0  3 Futrelle, Mrs. Jacques Heath (Lily May Peel) female 35.0 1  4 Allen, Mr. William Henry male 35.0 0  .. ... ... ... ...  885 Rice, Mrs. William (Margaret Norton) female 39.0 0  887 Graham, Miss. Margaret Edith female 19.0 0  888 Johnston, Miss. Catherine Helen "Carrie" female NaN 1  889 Behr, Mr. Karl Howell male 26.0 0  890 Dooley, Mr. Patrick male 32.0 0  
 Parch Ticket Fare Cabin Embarked  
0 0 A/5 21171 7.2500 NaN S  
1 0 PC 17599 71.2833 C85 C  
2 0 STON/O2. 3101282 7.9250 NaN S  
3 0 113803 53.1000 C123 S  
4 0 373450 8.0500 NaN S  
.. ... ... ... ... ...  
885 5 382652 29.1250 NaN Q  
887 0 112053 30.0000 B42 S  
888 2 W./C. 6607 23.4500 NaN S  
889 0 111369 30.0000 C148 C  
890 0 370376 7.7500 NaN Q  
[707 rows x 12 columns] 
## j) Select all titanic passengers data for which the age is known using ## notna() function. 
# Python code 
passengers_with_known_age = titanic[titanic['Age'].notna()] 
# Output: 
 PassengerId Survived Pclass \ 
0 1 0 3  
1 2 1 1  
2 3 1 3  
3 4 1 1  
4 5 0 3  
.. ... ... ...  
885 886 0 3  
886 887 0 2  
887 888 1 1  
889 890 1 1  
890 891 0 3  
 Name Sex Age SibSp  \ 
0 Braund, Mr. Owen Harris male 22.0 1  1 Cumings, Mrs. John Bradley (Florence Briggs Th... female 38.0 1  2 Heikkinen, Miss. Laina female 26.0 0  3 Futrelle, Mrs. Jacques Heath (Lily May Peel) female 35.0 1  4 Allen, Mr. William Henry male 35.0 0  .. ... ... ... ... 
Page 11 of 16 
885 Rice, Mrs. William (Margaret Norton) female 39.0 0  886 Montvila, Rev. Juozas male 27.0 0  887 Graham, Miss. Margaret Edith female 19.0 0  889 Behr, Mr. Karl Howell male 26.0 0  890 Dooley, Mr. Patrick male 32.0 0  
 Parch Ticket Fare Cabin Embarked  
0 0 A/5 21171 7.2500 NaN S  
1 0 PC 17599 71.2833 C85 C  
2 0 STON/O2. 3101282 7.9250 NaN S  
3 0 113803 53.1000 C123 S  
4 0 373450 8.0500 NaN S  
.. ... ... ... ... ...  
885 5 382652 29.1250 NaN Q  
886 0 211536 13.0000 NaN S  
887 0 112053 30.0000 B42 S  
889 0 111369 30.0000 C148 C  
890 0 370376 7.7500 NaN Q  
[714 rows x 12 columns] 
## k) Select the names of the titanic passengers not older than 50 years. 
# Python code 
young_passengers_names = titanic.loc[titanic['Age'] <= 50, 'Name'] 
# Output: 
0 Braund, Mr. Owen Harris 
1 Cumings, Mrs. John Bradley (Florence Briggs Th... 
2 Heikkinen, Miss. Laina 
3 Futrelle, Mrs. Jacques Heath (Lily May Peel) 
4 Allen, Mr. William Henry 
 ...  
885 Rice, Mrs. William (Margaret Norton) 
886 Montvila, Rev. Juozas 
887 Graham, Miss. Margaret Edith 
889 Behr, Mr. Karl Howell 
890 Dooley, Mr. Patrick 
Name: Name, Length: 650, dtype: object 
## l) Select rows 25 till 37 and columns 2 to 6 from a titanic DataFrame. 
# Python code 
selected_data = titanic.iloc[24:36, 1:6] 
# Output: 
 Survived Pclass Name \ 24 0 3 Palsson, Miss. Torborg Danira  25 1 3 Asplund, Mrs. Carl Oscar (Selma Augusta Emilia...  26 0 3 Emir, Mr. Farred Chehab  27 0 1 Fortune, Mr. Charles Alexander  28 1 3 O'Dwyer, Miss. Ellen "Nellie"  29 0 3 Todoroff, Mr. Lalio  30 0 1 Uruchurtu, Don. Manuel E 
Page 12 of 16 
31 1 1 Spencer, Mrs. William Augustus (Marie Eugenie)  32 1 3 Glynn, Miss. Mary Agatha  33 0 2 Wheadon, Mr. Edward H  34 0 1 Meyer, Mr. Edgar Joseph  35 0 1 Holverson, Mr. Alexander Oskar  
 Sex Age  
24 female 8.0  
25 female 38.0  
26 male NaN  
27 male 19.0  
28 female NaN  
29 male NaN  
30 male 40.0  
31 female NaN  
32 female NaN  
33 male 66.0  
34 male 28.0  
35 male 42.0  
## m) Display the average age of the titanic passengers. 
# Python code 
average_age = titanic['Age'].mean() 
print("\nAverage age of passengers:", average_age) 
# Output: 
Average age of passengers: 29.69911764705882 
## n) Display median age and ticket fare price of the titanic passengers. 
# Python code 
median_age = titanic['Age'].median() 
median_fare = titanic['Fare'].median() 
print("Median age of passengers:", median_age) 
print("Median fare price:", median_fare) 
# Output: 
Median age of passengers: 28.0 
Median fare price: 14.4542 
## o) Demonstrate the use of describe() on Age and Fare columns of the  titanic 
## DataFrame. 
# Python code 
age_fare_description = titanic[['Age', 'Fare']].describe()
Page 13 of 16 
# Output: 
             Age        Fare 
count  714.000000  891.000000 
mean    29.699118   32.204208 
std     14.526497   49.693429 
min      0.420000    0.000000 
25%     20.125000    7.910400 
50%     28.000000   14.454200 
75%     38.000000   31.000000 
max     80.000000  512.329200 
## p) Display the average age for male versus female titanic passengers. 
# Python code 
average_age_by_sex = titanic.groupby('Sex')['Age'].mean() 
# Output: 
Sex 
female 27.915709 
male 30.726645 
Name: Age, dtype: float64 
## q) Display the mean ticket fare price for each of the sex and cabin  class 
## combinations of titanic DataFrame. 
# Python code 
fare_by_sex_class = titanic.groupby(['Sex', 'Pclass'])['Fare'].mean() 
# Output: 
Sex Pclass 
female 1 106.125798 
 2 21.970121 
 3 16.118810 
male 1 67.226127 
 2 19.741782 
 3 12.661633 
Name: Fare, dtype: float64 
## r) Display the number of passengers in each of the cabin classes of ## titanic DataFrame. 
# Python code 
passengers_in_each_class = titanic['Pclass'].value_counts() 
# Output: 
3    491
Page 14 of 16 
1    216 
2    184 
Name: Pclass, dtype: int64 
## s) Sort the titanic data according to the age of the passengers. 
# Python code 
titanic_sorted_by_age = titanic.sort_values(by='Age') 
# Output: 
 PassengerId Survived Pclass Name  \ 
803 804 1 3 Thomas, Master. Assad  Alexander  
755 756 1 2 Hamalainen, Master.  Viljo  
644 645 1 3 Baclini, Miss.  Eugenie  
469 470 1 3 Baclini, Miss. Helene  Barbara  
78 79 1 2 Caldwell, Master. Alden  Gates  
.. ... ... ...  
...  
859 860 0 3 Razi, Mr.  Raihed  
863 864 0 3 Sage, Miss. Dorothy Edith  "Dolly"  
868 869 0 3 van Melkebeke, Mr.  Philemon  
878 879 0 3 Laleff, Mr.  Kristo  
888 889 0 3 Johnston, Miss. Catherine Helen  "Carrie"  
 Sex Age SibSp Parch Ticket Fare Cabin Embarked  803 male 0.42 0 1 2625 8.5167 NaN C  755 male 0.67 1 1 250649 14.5000 NaN S  644 female 0.75 2 1 2666 19.2583 NaN C  469 female 0.75 2 1 2666 19.2583 NaN C  78 male 0.83 0 2 248738 29.0000 NaN S  .. ... ... ... ... ... ... ... ...  859 male NaN 0 0 2629 7.2292 NaN C  863 female NaN 8 2 CA. 2343 69.5500 NaN S  868 male NaN 0 0 345777 9.5000 NaN S  878 male NaN 0 0 349217 7.8958 NaN S  888 female NaN 1 2 W./C. 6607 23.4500 NaN S  
[891 rows x 12 columns]
Page 15 of 16 
## t) Sort the titanic data according to the cabin class and age in  descending 
## order. 
# Python code 
titanic_sorted_by_class_age = titanic.sort_values(by=['Pclass', 'Age'],  ascending=[True, False]) 
print(titanic_sorted_by_class_age) 
# Output: 
 PassengerId Survived Pclass Name  \ 
630 631 1 1 Barkworth, Mr. Algernon Henry  Wilson  
96 97 0 1 Goldschmidt, Mr. George  B  
493 494 0 1 Artagaveytia, Mr.  Ramon  
745 746 0 1 Crosby, Capt. Edward  Gifford  
54 55 0 1 Ostby, Mr. Engelhart  Cornelius  
.. ... ... ...  
...  
859 860 0 3 Razi, Mr.  Raihed  
863 864 0 3 Sage, Miss. Dorothy Edith  "Dolly"  
868 869 0 3 van Melkebeke, Mr.  Philemon  
878 879 0 3 Laleff, Mr.  Kristo  
888 889 0 3 Johnston, Miss. Catherine Helen  "Carrie"  
 Sex Age SibSp Parch Ticket Fare Cabin Embarked  630 male 80.0 0 0 27042 30.0000 A23 S  96 male 71.0 0 0 PC 17754 34.6542 A5 C  493 male 71.0 0 0 PC 17609 49.5042 NaN C  745 male 70.0 1 1 WE/P 5735 71.0000 B22 S  54 male 65.0 0 1 113509 61.9792 B30 C  .. ... ... ... ... ... ... ... ...  859 male NaN 0 0 2629 7.2292 NaN C  863 female NaN 8 2 CA. 2343 69.5500 NaN S  868 male NaN 0 0 345777 9.5000 NaN S  878 male NaN 0 0 349217 7.8958 NaN S  888 female NaN 1 2 W./C. 6607 23.4500 NaN S  
[891 rows x 12 columns]
Page 16 of 16 
