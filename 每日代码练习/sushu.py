from math import sqrt       # 导入求平方根函数


n = int(input("Please input number: "))
for i in range(2,int(sqrt(n))):
    if n % i ==0:
        print(f"{n} is not a prime number.")
        break
else:
    print(f"{n} is a prime number.")