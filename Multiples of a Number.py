#Multiples of a Number
#Write a function that prints all multiples of a given number up to a specified limit. For example, for num = 3 and limit = 20, the output should be 3, 6, 9, 12, 15, 18.
n,Lim = input("enter the number and limit with gap of space :").split()
n = int(n)
Lim = int(Lim)
s = []
for i in range(1,Lim+1):
    if i%n == 0:
        s.append(str(i))
s = ", ".join(s)
print(s)
