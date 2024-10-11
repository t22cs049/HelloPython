print("hello")

#コメント
"""
複数行
コメント
"""

#for文の書き方は二種類
for x in {1,2,3}:
    print(x)
    
n=11
for i in range(n):
    print(i)
    
#if文には:を忘れずに
if 0 < x < 10:
    print("0<x<10")
elif x<0:
    print("x<0")
else:
    print(x>10)
    
p=0
while p<10:
    print('p=',p)
    p+=1
    
def fibo(n):
    if n==0 or n==1:
        return 1
    return fibo(n-1) + fibo(n-2)