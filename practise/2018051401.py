# -- coding: utf-8 --
# data = {
# 	'name': 'zhou',
# 	'age': '18'
# }
# for k,v in data.items():
# 	print('key ====' + k)
# 	print('value ====' + v)
# for k in data:
# 	print(k)
# for k in data.keys():
# 	print(k)
# arr = [];
# for index in range(5):
# 	print(index)
# 	arr.append(index)
# print(arr)
# for index in arr[:3]:
# 	print(index)


# 第七章
# message = input('请输入你的名字');
# print(message)
# age = '18'
# print(age > 17)

# for index in range(20):
# 	if index % 3 == 6:
# 		break
# 	else:
# 	 print(index)

#


# 第八章 函数
# def printName():
# 	""" 描述注释 """
# 	print('atie')
# # printName()
# def printName(name):
# 	print(name)

# printName("zhou")


# def printFullName(first, last):
# 	print("first" +first)
# 	print('last'+last)

# printFullName(last='atie',first='zhou')


# def printNames(*arr):
# 	print(arr)

# printNames("atie")

# def fn(a, **arr):
# 	print(a)
# 	print(arr)


# fn(1,c=2)

# def fn(a, *arr):
# 	print(a)
# 	print(arr)

# fn(1,2,3,4)

# def make_car(a,b,**items):
# 	obj = {}
# 	obj['first'] = a;
# 	obj['last'] = b;
# 	for key,value in items.items():
# 		obj[key] = value;
# 	return obj;

# car = make_car('subaru','oub',color="blue",age="10")
# print(car)
# import fn
# fn.fn(1)


# import fn
# print(fn.arr)

# from fn import printStr,arr
# printStr(1)
# for item in arr:
# 	printStr(item)






























