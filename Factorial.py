#Write a function to compute the factorial of a given number using a loop. For example, factorial(5) should return 120
n = int(input())
s = 1
for i in range(1,n+1):
  s *= i 
print(f"factorial of {n} is {s}")
