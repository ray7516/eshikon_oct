list_1=[1,2,3,4,5]
print(list_1)

list_2=["ab","cd","ef"]
print(list_2)

list_1=[1,2,3,4,5]
print(len(list_1))

list_2=["ab","cd","ef"]
print(len(list_2))

list_2=["ab","cd","ef"]
print(list_1[0])

list_1=[1,2,3,4,5]
print(list_1[1:3])
print(list_1[4])
print(list_1[1])
print(list_1[0])

list_2=["ab","cd","ef"]
print(list_2[0])

list_1=[1,2,3,4,5]
for i in range(len(list_1)):
  print(i) 

list_2=["ab","cd","ef"]
for i in range(len(list_2)):
 print(i,list_2[i])

list_1=[10,20,30,40,50]
for i in list_1:
 print(i)

list_1=[10,20,30,40,50]
sum=0
for i in list_1:
 sum=sum+i
print(sum) 

list_1=[10,20,30,40,50]
print("before append",list_1)
list_1.append(60)
print("after append",list_1)

list_1=[10,20,30,40,50]
list_1.clear()
print("after clear",list_1)

list_1=[10,20,30,40,50]
list_2=list_1.copy()
print("after copy",list_2)

list_1=[10,20,30,50,40,50]
cnt=list_1.count(50)
print("number:",cnt)

count=0
for i in list_1:
 if(i==50):
  count=count+1
 else:
  count=count
print(count)   

list_1=[10,11,22,32,51,42,40,22,53]
even_list=[]
odd_list=[]
for i in list_1:
 if(i%2==0):
  even_list.append(i)
 else:
  odd_list.append(i)
print(even_list)
print(odd_list)

list_1=[10,11,22,32,51,42,40,22,53]
list_1.insert(0,100)
print("after insert",list_1)

list_2=["abcd","efgh"]
sum=0
for i in list_2:
 sum=sum+len(i)
print(sum)

