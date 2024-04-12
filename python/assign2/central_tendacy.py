from statistics import mean, fmean, geometric_mean, harmonic_mean, median,
median_low, median_high, median_grouped, mode, multimode, quantiles

Page 1 of 4

PRN: 123M1H010
Name of Student: Harshal Sanjay Bhamare

def get_user_input():
nums = input("Enter a list of numbers separated by commas: ")
num_list = [float(x) if '.' in x else int(x) for x in nums.split(',')]
return num_list
def main():
data = get_user_input()
print("a) Arithmetic mean:", mean(data))
print("b) Floating point arithmetic mean:", fmean(data))
print("c) Geometric mean:", geometric_mean(data))
print("d) Harmonic mean:", harmonic_mean(data))
print("e) Median:", median(data))
print("f) Low median:", median_low(data))
print("g) High median:", median_high(data))
print("h) Median (50th percentile) of grouped data:",
median_grouped(data))
try:
print("i) Single mode:", mode(data))
except Exception:
print("i) No single mode found.")
modes = multimode(data)
if modes:
print("j) List of modes:", modes)
else:
print("j) No modes found.")
num_intervals = int(input("Enter the number of intervals for quantiles:
"))
quantile_values = quantiles(data, n=num_intervals)
print("k) Quantiles:", quantile_values)
# Calling the main function:
main()