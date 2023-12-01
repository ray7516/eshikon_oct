car={"model":"m1","clour":"red","price":100}
print(car["model"])

car={"model":"m1","clour":"red","price":100}
print(car["clour"])

car={"model":"m1","clour":"red","price":100}
print(car["price"])

car={"model":"m1","clour":"red","price":100}
print(car.get("price"))

car={"model":"m1","clour":"red","price":100}
print(car.keys())

car={"model":"m1","clour":"red","price":100}
print(car.values())

car={"model":"m1","clour":"red","price":100}
for i in car:
 print(i)

car={"model":"m1","clour":"red","price":100}
for i in car.values():
 print(i)

car={"model":"m1","clour":"red","price":100}
for i,j in car.items():
 print(i,j)

car={"model":["m1","m2"],"clour":["red","white"],"price":[100,200]}
for i,j in car.items():
 print(i,j)

cars={"car1":{"model":["m1","m2"],"clour":["red","white"],"price":[100,200]},
      "car2":{"model":["m3","m4"],"clour":["black","green"],"price":[100,200]}}
for i,j in cars.items():
 for k in j.items():
  print(i,k)
 













