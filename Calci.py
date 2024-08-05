n = input("ENTER THE EXPRESSION: ").split()
a = int(n[0])
b = int(n[2])
if n[1] == "+":
    print(a + b)
elif n[1] == "-":
    print(a-b)
elif n[1] == "*":
    print(a*b)
elif n[1] == "/":
    print(a/b)