import math
def number(n,k):
    x=math.factorial(n)/ (math.factorial(k) * math.factorial(n-k))
    return x

def pascal(n):
    rows=[]
    for row in range(n):
        for k in range(row+1):
            x=number(row,k)
            rows.append(int(x))
        print(rows)
        rows.clear()

n=int(input("Please enter row number: "))
pascal(n)
