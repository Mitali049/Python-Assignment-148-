(b) Factorial and Binomial Co-efficient
n = int(input("Enter the value of n: "))
r = int(input("Enter the value of r: "))
# Finding factorial using functions (recursive)
if n == 0 or n == 1:
return 1
else:
return n * fact(n-1)
n_minus_r = fact(n-r)
r_fact = fact(r)
print("Factorial: ", fact(n))
def fact(n):

print("Binomial Co-efficient: ", fact(n)/(n_minus_r*r_fact))

(a)Fibonacci Series
n = int(input("Enter the value of n: "))
a = 0
b = 1
count = 0
if n <= 0:
print("Please enter a valid integer")
elif n == 1:
print("Fibonacci series upto 1")
print(a)
else:
