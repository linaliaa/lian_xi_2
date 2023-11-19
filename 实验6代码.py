# #8.1
# def display_message():
#     print('本章的主题：def(函数)')
# display_message()

# #8.2
# def favorite_book(title):
#     print('One of my favorite books is: '+title)
# favorite_book('Python编程')

# #8.3
# def make_shirt(size,message):
#     if message=='':
#         print('尺寸为：'+size+'; 印花为：'+'空')
#     else:
#         print('尺寸为：'+size+'; 印花为：'+message)
# make_shirt('XS','')
# make_shirt('XXL',message='Hello Python!')

# #8.4
# def make_shirt(size,message='I love Python'):
#     print('尺寸为：'+size+'; 印花为：'+message)
# make_shirt('大号T恤')
# make_shirt('中号T恤')
# make_shirt('小号T恤',message='Hello Python!')

# #8.5
# def describe_city(name,contry='China'):
#     print(name+' is in '+contry)
# describe_city('BeiJing')
# describe_city('ShangHai')
# describe_city('Florence','Italy')

# #8.6
# def city_country(name,country):
#     city_country1=name+','+country
#     return city_country1
# a=city_country('BeiJing','China')
# b=city_country('ShangHai','China')
# c=city_country('florence','Italy')
# print(a)
# print(b)
# print(c)

# #8.7
# def make_ablum(gsname,zjname,count=None):
#     if count:
#         k={'gsname':gsname,'zjname':zjname,'count':count}
#     else:
#         k={'gsname':gsname,'zjname':zjname}
#     return k
# a=make_ablum('A','a','1')
# b=make_ablum('B','b')
# c=make_ablum('C','c','3')
# print(a)
# print(b)
# print(c)

# #8.8
# def make_ablum(gsname,zjname,count=''):
#     if count:
#         k={'gsname':gsname,'zjname':zjname,'count':count}
#     else:
#         k={'gsname':gsname,'zjname':zjname}
#     return k
# k1='请输入歌手名：(输入quit退出)'
# k2='请输入专辑名：(输入quit退出)'
# ac=True
# while ac:
#     a=input(k1)
#     b=input(k2)
#     if a=='quit' or b=='quit':
#         break
#     else:
#         c=make_ablum(a,b)
#         print(c)

# #8.9
# message=['a','b','c']
# def show_message():
#     for name in message:
#         print(name)
# show_message()

# #8.10
# message=['a','b','c']
# sent_messages=[]
# def send_messages():
#     for name in message:
#         print(name)
#         sent_messages.append(name)
# send_messages()
# print('message:',message)
# print('sent_messages:',sent_messages)

# #8.11
# message=['a','b','c']
# sent_messages=[]

# def send_messages(messages):
#     for name in messages:
#         print(name)
#         sent_messages.append(name)

# message_copy = message.copy()
# send_messages(message_copy)

# print('message:', message)
# print('sent_messages:', sent_messages)

# #8.12
# def sandwich(*food):
#     print('添加的食材有：')
#     for i in food:
#         print(i)

# sandwich('a','b','c')
# sandwich('d','e')
# sandwich('f')

# #8.13
# def user_profile(first,last,**else_info):
#     name_file={}
#     name_file['first_name']=first
#     name_file['last_name']=last
#     for i,j in else_info.items():
#         name_file[i]=j
#     return name_file
# a=user_profile('A','1',company='2',sex='3')
# print(a)
# b=user_profile('B','1',sex='2')
# print(b)

# #8.14
# def make_car(manufacture,type,**else_info):
#     cars={}
#     cars['manufacture']=manufacture
#     cars['type']=type
#     for i,j in else_info.items():
#         cars[i]=j
#     return cars

# car=make_car('subaru','outback',color='blue',tow_package=True)
# print(car)

#codewars
# #第一题
# def count_developers(developers):  
#     count = 0  
#     for developer in developers:  
#         if developer['continent'] == 'Europe' and developer['language'] == 'JavaScript':  
#             count += 1  
#     return count

# #第二题
# def zero(fun=None): return fun(0) if fun else 0
# def one(fun=None): return fun(1) if fun else 1
# def two(fun=None): return fun(2) if fun else 2
# def three(fun=None): return fun(3) if fun else 3
# def four(fun=None): return fun(4) if fun else 4
# def five(fun=None): return fun(5) if fun else 5
# def six(fun=None): return fun(6) if fun else 6
# def seven(fun=None): return fun(7) if fun else 7
# def eight(fun=None): return fun(8) if fun else 8
# def nine(fun=None): return fun(9) if fun else 9

# def plus(y): return lambda x: x + y
# def minus(y): return lambda x: x - y
# def times(y): return lambda x: x * y
# def divided_by(y): return lambda x: x // y

# #第三题
# def shorten_number(suffixes, base):
#     def my_filter(data):
#         try:
#             number = int(data)
#         except (TypeError, ValueError):
#             return str(data)
#         else:
#             i = 0
#             while number//base > 0 and i < len(suffixes)-1:
#                 number //= base
#                 i += 1
#             return str(number) + suffixes[i]
#     return my_filter

# #第四题
# def find_senior(lst): 
#     mage = max(a['age'] for a in lst)
#     return [a for a in lst if a['age']==mage]

# #第五题
# from inspect import signature
# from functools import partial

# def curry_partial(main_func, *args):
    
#     if not(callable(main_func)):
#         return main_func
    
#     p = len(signature(main_func).parameters)
#     func = partial(main_func)
    
#     for a in args:
#         if len(func.args) == p: break
#         func = partial(func, a)
    
#     if len(func.args) < p:
#         return partial(curry_partial, main_func, *func.args)

#     return func()
