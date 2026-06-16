#nested if
"""mark=int(input("enter your mark"))
if(mark>80):
    print("you are eligible to recieve certificates")
elif(mark>70):
        print("you are eligible for silver certificates")
if(mark>60):
        print("you are eligible for bronze certificates")
else:
    print("you are not eligible")"""


age=int(input("enter your age"))
if(age>=18):
   has_license=input("do you have a license (y/n)?:")
   if(age>18 and has_license=="y"):
       print("you can drive")
   elif(age>18 and has_license=="n"):
       print("you can't drive")
else:
    print("you are under age.you can't drive")


