#task1
"""name=input("enter your name:")
age=int(input("enter your age:"))
if(age>=13 and age<60):
    print("adult ticket")
elif(age>60):
    print("hello ",name)
    print("ticket type:senior citizen ticket")
else:
    print("child ticket")"""
    

#task2
"""temp=int(input("enter degree"))
if(temp<20):
    print("cold")
elif(temp>30):
    print("weather type : hot")
else:
    print("pleasant")"""
    
    
#task3

"""emp_name=input("enter name:")
exp=int(input("years of experience:"))
salary=int(input("salary?:"))
if(salary>=50000 and salary>=5):
    bonous=salary*20/100
    final_salary=bonous+salary
    print("bonous",bonous)
    print("final salary",final_salary)
elif(salary>=30000 and exp>=3):
    bonous=salary*10/100
    final_salary=salary+bonous
    print("bonous",bonous)
    print("final salary",salary)
else:
    bonous=salary*5/100
    final_salary=salary+bonous
    print("bonous",bonous)
    print("final salary",final_salary)"""
    
#task4
"""percent=int(input("enter your percentage:"))
score=int(input("enter score:"))
if(percent>=70 and score>=80):
    print("admission confirmed")
elif(percent>=60 and score>=60):
    print("waiting list")
else:
    print("rejected")"""
    
#task5
"""customer_name=input("enter name:")
units=int(input("units:"))
if(units<=100):
    bill_amount=units*2
    print(bill_amount)
    discount=bill_amount-0.10
    print("final amount:",bill_amount)
elif(units>=101 and units<=300):
    bill_amount=units*4
    print(bill_amount)
    print("final amount:",bill_amount)
elif(units>300):
    bill_amount=units*6
    print(bill_amount)
    if(bill_amount>1000):
      discount=bill_amount-(bill_amount*0.10)
      print("final_amount",discount)"""
      
#task6
age=int(input("enterage:"))
salary=int(input("enter salary:"))
exp=int(input("enter experience:"))
loan=input("y/n")
if(age<21):
  print("rejected:under age")
elif(salary<30000):
    print("rejected:not enough salary")
elif(exp<2):
    print("rejected:not enough experience")
elif(loan=="n"):
    print("rejected:loan exist found")
else:
    print("loan approved")
  


 
    

    
        

    