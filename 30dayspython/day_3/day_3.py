list = ['apple','pear','banana']
print(list[0])
print(list[-1])

colour = ['rad','green','blue','white']
batter_colour = f"我最喜欢的颜色是:{colour[0].title()}."
print(batter_colour)

colour[0] = 'yellow'
print(colour)
colour.append('rad')
colour.insert(3,'black')
print(colour)

del colour[0]
print(colour)

new_colour = colour.pop(0)
print(colour.pop())
print(colour)
print(new_colour)

bad_colour = 'blue'
colour.remove(bad_colour)
print(colour)
print(f"\n the {bad_colour.title} is too bad")

nums = [4,3,6,8,9]
print (nums)
nums.sort()
print(nums)
nums.sort(reverse = True)
print(nums)

num = [9,5,6,3,2]
num.reverse()
print(num)
print(len(num))
print(num[4])

friend_name = ['kecab','moba','suka','asa']
print(friend_name)
print(f"nice to meet you{friend_name[0]}")
print(f"nice to meet you{friend_name[1]}")
print(f"nice to meet you{friend_name[2]}")
print(f"nice to meet you{friend_name[3]}")

my_list = ['car','plane','rocket']
print("i would like to own a "+ my_list[0])
print("i would like to own a "+ my_list[1])
print("i would like to own a "+ my_list[2])

invate_name = ['马云','马化腾','马斯克']
print("尊敬的："+ invate_name[0] +","+invate_name[1]+","+invate_name[2]+"请来参加我的慈善晚宴！")
invate_name_absent = invate_name.pop(1)
invate_name.insert(1,"马蓉")
print("尊敬的:" +invate_name[0]+","+invate_name[1]+","+invate_name[2]+",请参加我的慈善晚会")
print("由于"+ invate_name_absent + "帮我打怪去了,所以宴会邀请了"+ invate_name[1])

invate_name.insert(0,"马斯克")
invate_name.insert(1,"马东敏")
invate_name.append("马拉多纳")

for new_name in invate_name:
    print("尊敬的："+ new_name +"参加我的慈善晚会")

#缩减人员名单
print(invate_name)
print(invate_name.pop()+"，很抱歉哦，位置不够你不能进来")
print(invate_name.pop()+"，很抱歉哦，位置不够你不能进来")
print(invate_name.pop()+"，很抱歉哦，位置不够你不能进来")
print(invate_name.pop()+"，很抱歉哦，位置不够你不能进来")

for new_name in invate_name:
    print("尊敬的:"+new_name+"，请来参加我的慈善晚会")
del invate_name [1]
del invate_name [0]

print(invate_name)

places = ["longdon","paris","hong kong","beijing","shnaghai"]
print(places)

#原始排序打印
print(sorted(places))
print(places)#核实

print(sorted(places,reverse=True))
print(places)#倒叙

places.reverse()
print(places)

places.reverse()
print(places)

places.sort()
print(places)

