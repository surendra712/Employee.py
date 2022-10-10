n=int(input("ENTER NO.OF EMPLOYEES:"))
l=[]
bonus=100
total=0
names=[]
print("-----------------------------------")
for i in range(n):
    name=input("ENTER EMPLOYEE NAME:")
    names.append(name)
    sal=int(input("ENTER EMPLOYEE SALARY:"))
    l.append(sal)
    emp_id=int(input("ENTER EMPLOYEE ID:"))
    exp=int(input("ENTER EMPLOYEE EXPERIENCE:"))
    if exp<=2:
        print("NO BONUS")
    else:
        net_sal=sal+bonus
        print("NET SALARY IS:",net_sal)
    print("-----------------------------------")
print("NAME:SALARY")
for i in range(n):
    print("names[i]:",l[i])
l=sorted(l)
print("HIGHEST SALARY:",l[-1])
print("LOWEST SALARY:",l[0])
for i in range(n):
    total=total+l[i]
avg=total/n
print("AVERAGE SALARY IS:",avg)
    
