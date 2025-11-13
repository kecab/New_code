#"第二天：30天Python编程"

name = "shi"
name_full = "kecab"
country = "china"
city = "suzhou"
age = 23
year = 2023
is_married = True
is_true = False
is_light_on = "no"
rad_fruit,green_fruit,yellow_fruit,black_fruit = "apple","pear","banana","blueberry"

print(type(name))
print(type(name_full))
print(type(country))
print(type(age))
print(type(year))
print(type(is_married))
print(len(name+name_full))
if len(name)>len(name_full):
    print("you name longer")
elif len(name)<len(name_full):
    print("you name_full longer")
else:
    print("saame")

num_one = 5
num_two = 4
total = (num_one + num_two)
diff = (num_one - num_two)
product = (num_two * num_one)
division = (num_one/num_two)
remainder = (num_two % num_one)
exp = (num_one ** num_two)
floor_division = (num_one // num_two)

import math
radius = 30
area_of_circle = (math.pi * radius **2)
circum_of_circle = (2 *math.pi * radius)

user_radius = (float(input("请输入圆的半径（米）：")))
area_of_circle = (math.pi * user_radius **2)
circum_of_circle = (2 *math.pi * user_radius)

name = (input('what is you name:'))
country_place = (input("what is u country"))
place = (input("where u place"))
