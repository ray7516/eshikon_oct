name=""
if(len(name)==0):
    print("true")
else:
    print("false")

a=""
if(len(a)==0):
    print("success")
else:
    print("failed")

name="Dhononjoy"
if(len(name)==0):
    print(failed)
else:
    if(len(name)>=5):
        print("the name length must be better than 5")
    else:
        print("success")

name="Sree"
if(len(name)==0):
    print(failed)
else:
    if(len(name)>=5):
        print("the name length must be minimum 5")
    else:
        print("success")

name="Sree"
if(len(name)==0):
    print(failed)
else:
    if(len(name)<=4):
        print("the name length must be minimum 5")
    else:
        print("success")

email_number="124"
name=""
phone_number="1457"
if(len(name)==0 or len(phone_number)==0 or len(email_number)==0):
    print("true")

email_number="124"
name="sree"
phone_number="12"
if(len(name)==0 or len(phone_number)==0 or len(email_number)==0):
    print("false")
else:
    if(len(name)<=3):
        print("the name length must be minimum 3")
    elif(len(email_number)>=4):
        print("the email_number must be maximus 4")    
    elif(len(phone_number)<=2):
        print("the phone_number must be minimum 2")
    else:
        print("success")

