import statistics
def get_user_input():
try:
n = int(input("Enter the number of elements in the list: "))
numbers = []
for i in range(n):
element = float(input(f"Enter element {i + 1}: "))
numbers.append(element)
return numbers
except ValueError:
print("Invalid input. Please enter valid numbers.")
return get_user_input()
def calculate_statistics(numbers):

Page 3 of 4

if len(numbers) < 2:
print("At least two numbers are required for statistical

calculations.")
return
population_std_dev = statistics.pstdev(numbers)
population_var = statistics.pvariance(numbers)
sample_std_dev = statistics.stdev(numbers)
sample_var = statistics.variance(numbers)
data_range = max(numbers) - min(numbers)
# Quartiles
numbers.sort()
q1 = statistics.quantiles(numbers, n=4)[0]
q3 = statistics.quantiles(numbers, n=4)[-1]
interquartile_range = q3 - q1
print("\nStatistical Measures of Spread:")
print(f"a) Population Standard Deviation: {population_std_dev:.4f}")
print(f"b) Population Variance: {population_var:.4f}")
print(f"c) Sample Standard Deviation: {sample_std_dev:.4f}")
print(f"d) Sample Variance: {sample_var:.4f}")
print(f"e) Range: {data_range:.4f}")
print(f"f) Interquartile Range: {interquartile_range:.4f}")
numbers = get_user_input()
calculate_statistics(numbers)