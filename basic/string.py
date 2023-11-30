name="mahadev"
size=len(name)
print(size)
print(name[0])
print(name[0:7])
print(name[0:6])
print(name[0:])
print(name[:7])

number="12547"
print(number[2])
print(number[0])
print(number[0:])
print(number[0:6])
print(number[:])

name="biNapani"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name[0].isupper())
print(name[0:].isupper())
print(name[0:].islower())
print(name[2].isupper())

check_upper=name[0].isupper()
if(check_upper):
    print('the first letter is capitall')
else:
    print("the first letter is not capitall")

txt="hello, wellcome to my world."
x=txt.endswith(".")

txt="hello, wellcome to my world."
x=txt[0:6].endswith(",")


