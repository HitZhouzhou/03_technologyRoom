from math import sin
k=1
sum=0
while k<=10000000:
    sum+=sin(k)/k+sin(k+2)/(k+2)-2*sin(k+1)/(k+1)
    k+=1
print(sum)
print(sin(1)-sin(2)/2)
print(sin(1)-sin(2)/2-sum)