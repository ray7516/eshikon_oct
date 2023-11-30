a=10
b=10
if(a==b):
    print("a is equal to b")
else:print("something went wrong")

total_prise=500
discount=5
if(total_prise>=500):
    total_after_discount=total_prise-(total_prise*discount)/100
    print(total_after_discount)
else:
    print(total_prise)

age=18
if(age<=17):
    print("you are not able to register for NID")
else:
    print("you are eligible")

phone_number=("01747862417")

if(len(phone_number)!=11):
    print("The phone number must be 11 digits")
else:
    print("success")    

phone_number="01747862417"
if(len(phone_number)==11):
    print("the phone_number must be 11 digits")
else:
    print("failed")

phone_number="01475"
if(len(phone_number)!=11):
    print("the phone_number must be 11 digits")
else:
    print("success")



