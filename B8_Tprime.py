n=int(input("Nhập n: "))
def check_divisor(n):
    d=2
    for i in range(2,(n//2)+1):
        if(n%i==0):
            d+=1
    return d==3
if(n<=3):   print("No")
for i in range(n+1):
    if(check_divisor(i)==1):
        print(i)
        