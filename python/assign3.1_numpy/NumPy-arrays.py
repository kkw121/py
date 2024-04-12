

Python Programs based on Python libraries - NumPy ---------------------------------------------------------------------------------------------------------------------- - 
Q1) Write a Python Program to Create the following NumPy arrays. 
## a) A 1-D array called zeros having 10 elements and all the elements are  set to zero. 
# Python code import 
numpy as np  
zeros = np.zeros(10)  
print("Zeros array:")  
print(zeros)  
# Output: 
Zeros array: 
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.] 
Page 1 of 15 
## b) A 1-D array called vowels having the elements ‘a’, ‘e’, ‘i’, ‘o’ and  ‘u’. 
# Python code vowels = np.array(['a', 'e',  
'i', 'o', 'u']) print("Vowels array:")  
print(vowels)  
# Output: 
Vowels array: 
['a' 'e' 'i' 'o' 'u']  
## c)A 2-D array called ones having 2 rows and 5 columns and all the  elements 
## are set to 1 and dtype as int. 
# Python code ones = np.ones((2,  
5), dtype=int) print("Ones  
array:") print(ones)  
# Output: 
Ones array: 
[[1 1 1 1 1]  
[1 1 1 1 1]]  
## d) Use nested Python lists to create a 2-D array called myarray1 having  3 
## rows and 3 columns and store the following data: (use table given in  the 
## assignment for this question) 
# Python code data =  
[[2.7, -2, -19],  
[0, 3.4, 99.9],  
[10.6, 0, 13]] myarray1 =  
np.array(data)  
print("myarray1 array:")  
print(myarray1)  
# Output: 
myarray1 array: 
[[ 2.7 -2. -19. ]  
[ 0. 3.4 99.9]  
[ 10.6 0. 13. ]] 
Page 2 of 15 
## e) A 2-D array called myarray2 using arange() having 3 rows and 5  columns 
## with start value = 4, step size 4 and dtype as float. 
# Python code 
myarray2 = np.arange(4, 4 + 3 * 5 * 4, 4, dtype=float).reshape(3, 5)  print("myarray2 array:") print(myarray2)  
# Output: 
myarray2 array: 
[[ 4. 8. 12. 16. 20.]  
[24. 28. 32. 36. 40.]  
[44. 48. 52. 56. 60.]] 
Q2) Using the arrays created in Question 1 above, write NumPy  commands for the following.
Page 3 of 15 
## a) Find the dimensions, shape, size, data type of the items and itemsize  of 
## arrays zeros, vowels, ones, myarray1 and myarray2. 
# Python code import numpy as np  
print("Array 'zeros':")  
print("Dimensions:", zeros.ndim)  
print("Shape:", zeros.shape)  
print("Size:", zeros.size)  
print("Data Type:", zeros.dtype)  
print("Item Size:", zeros.itemsize)  
print("\nArray 'vowels':")  
print("Dimensions:", vowels.ndim)  
print("Shape:", vowels.shape)  
print("Size:", vowels.size)  
print("Data Type:", vowels.dtype)  
print("Item Size:", vowels.itemsize)  
print("\nArray 'ones':")  
print("Dimensions:", ones.ndim)  
print("Shape:", ones.shape)  
print("Size:", ones.size)  
print("Data Type:", ones.dtype)  
print("Item Size:", ones.itemsize)  
print("\nArray 'myarray1':")  
print("Dimensions:", myarray1.ndim)  
print("Shape:", myarray1.shape)  
print("Size:", myarray1.size)  
print("Data Type:", myarray1.dtype)  
print("Item Size:", myarray1.itemsize)  
print("\nArray 'myarray2':")  
print("Dimensions:", myarray2.ndim)  
print("Shape:", myarray2.shape)  
print("Size:", myarray2.size) print("Data  
Type:", myarray2.dtype) print("Item  
Size:", myarray2.itemsize)  
# Output: 
Array 'zeros': 
Dimensions: 1  
Shape: (10,)  
Size: 10  
Data Type: float64  
Item Size: 8 
Page 4 of 15 
Array  
'vowels':  
Dimensions: 1  
Shape: (5,)  
Size: 5  
Data Type: <U1  
Item Size: 4  
Array 'ones':  
Dimensions: 2  
Shape: (2, 5)  
Size: 10  
Data Type: int64  
Item Size: 8  
Array 'myarray1':  
Dimensions: 2  
Shape: (3, 3)  
Size: 9  
Data Type: float64  
Item Size: 8  
Array 'myarray2':  
Dimensions: 2  
Shape: (3, 5)  
Size: 15  
Data Type: float64  
Item Size: 8  
## b) Reshape the array ones to have all the 10 elements in a single row. 
# Python code ones_reshaped =  
ones.reshape(1, -1)  
print("\nReshaped 'ones' array:")  
print(ones_reshaped)  
# Output: 
Reshaped 'ones' array: 
[[1 1 1 1 1 1 1 1 1 1]]  
## c) Display the 2nd and 3rd element of the array vowels. 
# Python code print("\n2nd and 3rd elements  
of 'vowels':") print(vowels[1:3])  
# Output: 
2nd and 3rd elements of 'vowels': 
['e' 'i'] 
Page 5 of 15 
##d) Display all elements in the 2nd and 3rd row of the array myarray1. 
# Python code print("\nElements in the 2nd and 3rd row of  'myarray1':") print(myarray1[1:3, :])  
# Output: 
Elements in the 2nd and 3rd row of 'myarray1': 
[[ 0. 3.4 99.9]  
[10.6 0. 13. ]]  
## e) Display the elements in the 1st and 2nd column of the array myarray1. 
# Python code print("\nElements in the 1st and 2nd column of  'myarray1':") print(myarray1[:, 0:2])  
# Output: 
Elements in the 1st and 2nd column of 'myarray1': 
[[ 2.7 -2. ]  
[ 0. 3.4]  
[10.6 0. ]]  
## f) Display the elements in the 1st column of the 2nd and 3rd row of the ## array myarray1. 
# Python code print("\nElements in the 1st column of the 2nd and 3rd row of  'myarray1':") print(myarray1[1:3, 0])  
# Output: 
Elements in the 1st column of the 2nd and 3rd row of 'myarray1': [ 0. 10.6]  
## g) Reverse the array of vowels. 
# python code vowels_reversed = np.flip(vowels) print("\nReversed 'vowels'  array:") print(vowels_reversed)  
# Output: 
Reversed 'vowels' array:  
['u' 'o' 'i' 'e' 'a']
Page 6 of 15 
Q3) Using the arrays created in Question 1 above, write NumPy  commands for the following 
## a) Divide all elements of array ones by 3. 
# Python code ones_divided_by_3 =  
ones / 3 print("\nArray 'ones'  
divided by 3:")  
print(ones_divided_by_3)  
# Output: 
Array 'ones' divided by 3:  
[[0.33333333 0.33333333 0.33333333 0.33333333 0.33333333]  
[0.33333333 0.33333333 0.33333333 0.33333333 0.33333333]]  
## b) Add the arrays myarray1 and myarray2. 
# Python code data = [[2, 9, -19],  
[6, 3.4, 10.9], [10.6, 50, 3]]  
myarray2A = np.array(data)  
sum_myarray1_myarray2 = myarray1 + myarray2A  
print("\nSum of 'myarray1' and 'myarray2':")  
print(sum_myarray1_myarray2)  
# Output: 
Sum of 'myarray1' and 'myarray2': 
[[ 4.7 7. -38. ]  
[ 6. 6.8 110.8]  
[ 21.2 50. 16. ]]  
## c) Subtract myarray1 from myarray2 and store the result in a new array. 
# Python code subtract_myarray2_myarray1 = myarray2 - 
myarray1 print("\nSubtraction of 'myarray1' from  
'myarray2':") print(subtract_myarray2_myarray1)  
# Output: 
Subtraction of 'myarray1' from 'myarray2':  
[[ -0.7  11.    0. ]  
[  6.    0.  -89. ]  
[  0.   50.  -10. ]] 
Page 7 of 15 
## d) Multiply myarray1 and myarray2 element-wise. 
# Python code multiply_elementwise_myarray1_myarray2 = myarray1 *  myarray2 print("\nElement-wise multiplication of 'myarray1' and  'myarray2':") print(multiply_elementwise_myarray1_myarray2)  
# Output: 
Element-wise multiplication of 'myarray1' and 'myarray2': [[ 5.4 -18. 361. ]  
[ 0. 11.56 1088.91] 
[ 112.36 0. 39. ]] 
## e) Do the matrix multiplication of myarray1 and myarray2 and store the  result in a new array myarray3. 

# Python code 
myarray3 = np.dot(myarray1, myarray2) 
print("\nMatrix multiplication of 'myarray1' and 'myarray2' (result in  'myarray3'):") 
print(myarray3) 

# Output: 
Matrix multiplication of 'myarray1' and 'myarray2' (result in 'myarray3'): [[-208. -932.5 -130.1 ] 
[1079.34 5006.56 336.76]
[ 159. 745.4 -162.4 ]]  
## f) Divide myarray1 by myarray2. 
# Python code divide_myarray1_myarray2 =  
myarray1 / myarray2 print("\nDivision of  
'myarray1' by 'myarray2':")  
print(divide_myarray1_myarray2)  
# Output: 
Division of 'myarray1' by 'myarray2': 
[[ 1.35 -0.22222222 1. ]  
[ 0. 1. 9.16513761]  
[ 1. 0. 4.33333333]]  
Page 8 of 15 
## g) Find the cube of all elements of myarray1 and divide the resulting  array by 2. 
# Python Code 
cube_and_divide_myarray1 = (myarray1 ** 3) / 2 print("\nCube  of 'myarray1' elements divided by 2:")  
print(cube_and_divide_myarray1)  
# Output:  
Cube of 'myarray1' elements divided by 2: 
[[ 9.841500e+00 -4.000000e+00 -3.429500e+03]  
[ 0.000000e+00 1.965200e+01 4.985015e+05]  
[ 5.955080e+02 0.000000e+00 1.098500e+03]] 
## h) Find the square root of all elements of myarray2 and divide the  resulting 

## array by 2.  
The result should be rounded to two places of decimals. 

# Python Code sqrt_and_divide_myarray2 = np.round( print("\nSquare root  of 'myarray2' elements divided by 2 (rounded to two decimal places):")  
np.sqrt(myarray2) / 2, 2)  
print(sqrt_and_divide_myarray2)  
# Output: 
Square root of 'myarray2' elements divided by 2 (rounded to two decimal places):  [[0.71 1.5   nan]  
[1.22 0.92 1.65]  
[1.63 3.54 0.87]]  
<ipython-input-23-ee416346d922>:5: RuntimeWarning: invalid value encountered in sqrt    sqrt_and_divide_myarray2 = np.round(np.sqrt(myarray2) / 2, 2) 
Page 9 of 15 
Q4) Using the arrays created in Question 1 above, write NumPy  commands for the following 
## a) Find the transpose of ones and myarray2. 
# Python code ones_transpose =  
ones.T myarray2_transpose =  
myarray2.T  
print("\nTranspose of  
'ones':") print(ones_transpose)  
print("\nTranspose of 'myarray2':") print(myarray2_transpose)  
# Output: 
Transpose of 'ones': 
[[1 1]  
[1 1]  
[1 1]  
[1 1]  
[1 1]]  
Transpose of 'myarray2':  
[[ 2. 6. 10.6]  
[ 9. 3.4 50. ]  
[-19. 10.9 3. ]]  
## b) Sort the array vowels in reverse. 
# Python code vowels_sorted_reverse =  
np.sort(vowels)[::-1] print("\nSorted  
'vowels' in reverse:")  
print(vowels_sorted_reverse)  
# Output: 
Sorted 'vowels' in reverse: 
['u' 'o' 'i' 'e' 'a']  
##c) Sort the array myarray1 such that it brings the lowest value of the  column in the first row and so on. 
# Python code myarray1_sorted =  
np.sort(myarray1, axis=0) print("\nSorted  
'myarray1' column-wise:")  
print(myarray1_sorted)  
# Output:
Page 10 of 15 
Sorted 'myarray1' column-wise: 
[[ 0. -2. -19. ]  
[ 2.7 0. 13. ]  
[ 10.6 3.4 99.9]]  
Q5) Using the arrays created in Question 1 above, write NumPy  commands for the following 
## a) Use NumPy.split() to split the array myarray2 into 5 arrays  columnwise. 
## Store the resulting arrays in myarray2A, myarray2B, myarray2C,  myarray2D 
## and myarray2E. Print the arrays myarray2A, myarray2B, myarray2C,  myarray2D 
## and myarray2E. 
# Python code 
myarray2A, myarray2B, myarray2C, myarray2D, myarray2E = np.split(myarray2,  5, axis=1)  
print("\nmyarray2A:") print(myarray2A) 
Page 11 of 15 
print("\nmyarray2B:")  
print(myarray2B)  
print("\nmyarray2C:")  
print(myarray2C)  
print("\nmyarray2D:")  
print(myarray2D)  
print("\nmyarray2E:")  
print(myarray2E)  
# Output: 
myarray2A: 
[[ 4.]  
[24.]  
[44.]]  
myarray2B:  
[[ 8.]  
[28.]  
[48.]]  
myarray2C:  
[[12.]  
[32.]  
[52.]]  
myarray2D:  
[[16.]  
[36.]  
[56.]]  
myarray2E:  
[[20.]  
[40.]  
[60.]]  
## b) Split the array zeros at array index 2, 5, 7, 8 and store the ## resulting arrays in zerosA, zerosB, zerosC and zerosD and print them. 
# Python code zerosA, zerosB, zerosC, zerosD, zeroE = np.split(zeros,  [2, 5, 7, 8]) print("zerosA:\n", zerosA) print("zerosB:\n", zerosB)  print("zerosC:\n", zerosC) print("zerosD:\n", zerosD)  
# Output: 
zerosA: 
[0. 0.]  
zerosB:  
[0. 0. 0.]  
zerosC:  
[0. 0.]  
zerosD:  
[0.] 
Page 12 of 15 
##c) Concatenate the arrays myarray2A, myarray2B and myarray2C into an  array 
# having 3 rows and 3 columns. 
# Python code concatenated_myarrays = np.concatenate((myarray2A,  myarray2B, myarray2C), axis=0) reshaped_concatenated_myarrays =  concatenated_myarrays.reshape(3, 3)  
print("\nConcatenated and reshaped  
array:")  
print(reshaped_concatenated_myarrays)  
# Output: 
Concatenated and reshaped array: 
[[ 4. 24. 44.]  
[ 8. 28. 48.]  
[12. 32. 52.]] 
Q6) Create a 2-D array called myarray4 using arange() having 14 rows  and 3 columns with start value = -1, step size 0.25 having. Split this  array row wise into 3 equal parts and print the result 
# Python Code: 
import numpy as np  
myarray4 = np.arange(-1, -1 + 14 * 3 * 0.25, 0.25).reshape(14,  3)  
split_parts = np.array_split(myarray4, 3,  
axis=0)  
for i, part in enumerate(split_parts):  
print(f"Part {i + 1}:\n{part}\n")  
# Output: 
Part 1: 
[[-1. -0.75 -0.5 ]  
[-0.25 0. 0.25]  
[ 0.5 0.75 1. ]  
[ 1.25 1.5 1.75]  
[ 2. 2.25 2.5 ]]  
Part 2:  
[[2.75 3. 3.25]  
[3.5 3.75 4. ] 
Page 13 of 15 
[4.25 4.5 4.75]  
[5. 5.25 5.5 ]  
[5.75 6. 6.25]]  
Part 3:  
[[6.5 6.75 7. ]  
[7.25 7.5 7.75]  
[8. 8.25 8.5 ]  
[8.75 9. 9.25]] 
Q7) Using the myarray4 created in the above question 6, write  commands for the following: 
## a) Find the sum of all elements. 
# Python Code sum_all_elements = np.sum(myarray4)  
print("Sum of all elements:", sum_all_elements)  
# Output: 
Sum of all elements: 173.25  
## b) Find the sum of all elements row wise. 
# Python Code sum_row_wise =  
np.sum(myarray4, axis=1) print("\nSum of  
all elements row-wise:")  
print(sum_row_wise)  
# Output: 
Sum of all elements row-wise: 
[-2.25 0. 2.25 4.5 6.75 9. 11.25 13.5 15.75 18. 20.25 22.5  24.75 27. ]  
## c) Find the sum of all elements column wise.  
# Python Code  
sum_column_wise = np.sum(myarray4, axis=0) 
print("\nSum of all elements column-wise:") 
print(sum_column_wise)  
# Output:  
account_circle  
Sum of all elements column-wise:  
[54.25 57.75 61.25]  
## d) Find the max of all elements.
Page 14 of 15 
# Python Code max_element = np.max(myarray4)  
print("\nMax of all elements:", max_element)  
# Output: 
Max of all elements: 9.25 
## e) Find the min of all elements in each row. 
# Python Code min_row_wise =  
np.min(myarray4, axis=1) print("\nMin of  
all elements in each row:")  
print(min_row_wise)  
# Output: 
Min of all elements in each row: 
[-1. -0.25 0.5 1.25 2. 2.75 3.5 4.25 5. 5.75 6.5 7.25  8. 8.75]  
## f) Find the mean of all elements in each row. 
# Python Code mean_row_wise =  
np.mean(myarray4, axis=1) print("\nMean of  
all elements in each row:")  
print(mean_row_wise)  
# Output: 
Mean of all elements in each row: 
[-0.75 0. 0.75 1.5 2.25 3. 3.75 4.5 5.25 6. 6.75 7.5  8.25 9. ]  
## g) Find the standard deviation column wise. 
# Python Code std_dev_column_wise = np.std(myarray4, axis=0)  print("\nStandard deviation column-wise:") print(std_dev_column_wise)  
# Output: 
Standard deviation column-wise:  
[3.02334666 3.02334666 3.02334666]  
CodeText 
Page 15 of 15 
