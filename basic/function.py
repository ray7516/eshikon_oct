str1="binapani"
count=0
for i in str1:
    count=count+1
print(count)    

str2="mother"
def custom_len():
    count=0
    for i in str2:
        count=count+1
    print(count)
custom_len()

str3="father1"
def custom_len():
    count=0
    for i in str3:
        count=count+1
    return count
a=custom_len()
print(a)

str4="gopal"
a=len(str4)
print(a)

def custom_len(x):
    count=0
    for i in x:
        count=count+1
    return count
str5="pitasree1"
a=custom_len(str5)
print(a)

def custom_len(x,y,z):
    count1=0
    count2=0 
    count3=0
    for i in x:
        count1=count1+1
    for j in y:
        count2=count2+1     
    for k in z:
        count3=count3+1
    return  count1,count2,count3   
str1="joy11"
str2="ramdev"
str3="sitadevi"
a,b,c=custom_len(str1,str2,str3)
print(a,b,c)

def custom_len(x,y):
    count1=0
    count2=0
    for i,j in zip(x,y):
         count1=count1+1
         count2=count2+1
    return count1,count2
str1="sultan"
str2="salman"
a,b= custom_len(str1,str2)
print(a,b)





