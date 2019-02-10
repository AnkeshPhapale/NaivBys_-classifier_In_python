import csv
import numpy as np
d1=d2=0
def probabilityfinder(a,datavar,Total_data,clas,N_yes):
    increyes=0
    increno=0
    global d1,d2
    N_no=Total_data-N_yes
    for i in range(Total_data):
        if(a[i]==datavar and clas[i]=="yes" ):
            increyes+=1
    
    d1=increyes/N_yes
   
    for i in range(Total_data):
        if(a[i]==datavar and clas[i]=="no" ):
            increno+=1
   
    d2=increno/N_no
   
    
    
age=[]	
income=[]
student=[]
credit_rat=[]
clas=[]

a=[]
with open('naive_bayse_dataset.csv', 'r') as benFile:
    benReader = csv.reader(benFile)
    for row2 in benReader:
        a.append(row2)
benFile.close()
n=len(a)
k=d1=d2=0
z=0
for i in range(1,n):
    for j in range(0,5):
        if(j==0):
            age.append(a[i][j])
        elif(j==1):
            income.append(a[i][j])
        elif(j==2):
            student.append(a[i][j])
        elif(j==3):
            credit_rat.append(a[i][j])
        else:
            clas.append(a[i][j])
Total_data= len(clas)
N_yes=0
P_age=0
for i in range(len(clas)):
    if(clas[i]=="yes"):
        N_yes+=1
N_no =(Total_data)-(N_yes)
probablity_yesClass= N_yes/Total_data
print("total probablity of yes class",probablity_yesClass)
probablity_noClass= N_no/Total_data
print("total probablity of no class",probablity_noClass)

U_age=input("enter age youth/middle/senior -->")
U_income=input("enter the income low/high/medium-->")
U_Isstudent=input("Is a student yes/no?-->")
User_credit=input("enter the credit fair/excel-->")
probabilityfinder(age,U_age,Total_data,clas,N_yes)
usagepryes=d1
usageprno=d2
probabilityfinder(income,U_income,Total_data,clas,N_yes)
usincomepryes=d1
usincomeprno=d2
probabilityfinder(student,U_Isstudent,Total_data,clas,N_yes)
usstudentpryes=d1
usstudentprno=d2
probabilityfinder(credit_rat,User_credit,Total_data,clas,N_yes)
uscreditpryes=d1
uscreditprno=d2
print("probablity are==>>")
print()
print( "age probablity for yes=",usagepryes)
print("age probablity for no=",usageprno)
print()
print("income probablity for yes=",usincomepryes)
print("income probablity for no=",usincomeprno)
print()
print("Is student probablity for yes=",usstudentpryes)
print("Is student probablity for no=",usstudentprno)
print()
print("Credit_rating probablity for yes=",uscreditpryes)
print("credit_ratig probablity for no=",uscreditprno)
print()
probablity_yesClass=probablity_yesClass*usagepryes*usincomepryes*usstudentpryes*uscreditpryes
probablity_noClass=probablity_noClass*usageprno*usincomeprno*usstudentprno*uscreditprno
print( "Total probablity of yesClass",probablity_yesClass)
print()
print("total probablity of no class",probablity_noClass)
print()
print("-----------------------Result----------------------------------------")
if(probablity_yesClass > probablity_noClass):
    print(" hence the tuple belongs to yes class therefore user will buy computer")
else:
    print("Hence the tuple belongs to no class therefore user will not buy computer")