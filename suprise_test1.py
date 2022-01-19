a = eval(input())
e = len(a)
c =[]
for i in range(e-1):
    b = a[i+1]-a[i]
    c.append(abs(b))

p = 0
for j in range(len(c)-1):
    if c[j+1]>c[j]:
        p+=1
    

if p==len(c)-1:
    print("True")

else:
    print("False")