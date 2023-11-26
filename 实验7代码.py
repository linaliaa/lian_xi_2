# 教材练习
# #练习9.1
# class Restaurant:
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#     def describe_restaurant(self):
#         print(self.restaurant_name)
#         print(self.cuisine_type)
#     def open_restaurant(self):
#         print('Restaurant is open')
# restaurant = Restaurant('A','B')
# print(restaurant.restaurant_name,'',restaurant.cuisine_type)
# restaurant.describe_restaurant()
# restaurant.open_restaurant()

#练习9.2
# class Restaurant:
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#     def describe_restaurant(self):
#         print(self.restaurant_name)
#         print(self.cuisine_type)
#     def open_restaurant(self):
#         print('Restaurant is open')
# r1=Restaurant('A1','B1')
# r1.describe_restaurant()
# r2=Restaurant('A2','B2')
# r2.describe_restaurant()
# r3=Restaurant('A3','B3')
# r3.describe_restaurant()

#练习9.3
# class User():
#     def __init__(self, first_name,last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#     def describe_user(self):
#         print('用户：' + self.first_name + self.last_name)
#     def greet_user(self):
#         print('你好！ ' + self.first_name + self.last_name)
# user_a = User('A','a')
# user_b = User('B','b')
# user_c = User('C','c')
# user_a.describe_user()
# user_b.describe_user()
# user_c.describe_user()
# user_a.greet_user()
# user_b.greet_user()
# user_c.greet_user()

#练习9.4
# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 1
#     def describe_restaurant(self):
#         print(self.restaurant_name)
#         print(self.cuisine_type)
#     def open_restaurant(self):
#         print('Restaurant is open')
#     def number_served_info(self):
#         print('[' + self.restaurant_name + '] 餐馆每天可能接待的就餐人数: ' + str(self.number_served))
#         print('来 [' + self.restaurant_name + '] 吃 [' + self.cuisine_type + '] 的人有：'+str(self.number_served)+' 人！')
#     def set_number_served(self,number_info):
#         self.number_served = number_info
#     def increment_number_served(self,name_add):
#         self.number_served += name_add
        
# restaurant = Restaurant('A','b')
# restaurant.number_served = 30
# restaurant.set_number_served(0)
# restaurant.increment_number_served(100)
# restaurant.increment_number_served(10)
# restaurant.increment_number_served(100)
# restaurant.number_served_info()

#练习9.5
# class User():
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.login_attempts = 0
#     def describe_user(self):#打印用户名称方法
#         print('用户名称为：' + self.first_name + self.last_name)
#         print('共登录用户量：(重置中……)'+str(self.login_attempts))
#     def greet_user(self):#打印问候
#         print('你好！ ' + self.first_name + self.last_name)
#     def increment_login_attempts(self,number):
#         self.login_attempts += number
#         print('共登录用户量：' + str(self.login_attempts))
#     def reset_login_attempts(self):
#         self.login_attempts = 0
# user_a = User('A','a')
# user_a.increment_login_attempts(1)
# user_a.increment_login_attempts(1)
# user_a.increment_login_attempts(1)
# user_a.reset_login_attempts()
# user_a.describe_user()

#练习9.6
# class Restaurant():
#     def __init__(self,restaurant_name,cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#     def describe_restaurant(self):
#         print(self.restaurant_name)
#         print(self.cuisine_type)
#     def open_restaurant(self):
#         print('Restaurant is open')
# class IceCreamStand(Restaurant):
#     def __init__(self,restaurant_name,cuisine_type):
#         super().__init__(restaurant_name,cuisine_type)
#         self.favorite = ['1','2']
#     def show_ice(self):
#         for i in self.favorite:
#             print(i)
            
# IceCreamStand1 = IceCreamStand('A','a')
# IceCreamStand1.show_ice()

#练习9.7
# class User():
#     def __init__(self, first_name,last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#     def describe_user(self):
#         print('用户名称为：' + self.first_name + self.last_name)
#     def greet_user(self):
#         print('你好！ ' + self.first_name + self.last_name)
        
# class Admin(User):
#     def __init__(self,first_name,last_name):
#         super().__init__(first_name,last_name)
#         self.privileges = ['can add post','can del post','can ban user']
#     def show_privileges(self):
#         for i in self.privileges:
#             print("管理员权限有：" + i)
# Admin1 = Admin('A','a')
# Admin1.show_privileges()

#练习9.8
# class User():
#     def __init__(self, first_name,last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#     def describe_user(self):
#         print('用户名称为：' + self.first_name + self.last_name)
#     def greet_user(self):
#         print('你好！ ' + self.first_name + self.last_name)
        
# class Admin(User):
#     def __init__(self,first_name,last_name):
#         super().__init__(first_name,last_name)
#         self.b=Privileges()
# class Privileges():
#     def __init__(self):
#         self.privileges = ['can add post','can del post','can ban user']
#     def show_privileges(self):
#         for i in self.privileges:
#             print("管理员权限有：" + i)

# Admin1 = Admin('A','a')
# Admin1.b.show_privileges()

#练习9.9
# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0
#     def get_descriptive_name(self):
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name
#     def read_odometer(self):
#         print("This car has " + str(self.odometer_reading) + " miles on it.")
#     def update_odometer(self, milegeage):
#         if milegeage >= self.odometer_reading:
#             self.odometer_reading = milegeage
#         else:
#             print("You can't roll back an odometer!")
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
        
# class Battery():
#     def __init__(self, battery_size=70):
#         self.battery_size = battery_size
#     def describe_battery(self):
#         print("This car has a " + str(self.battery_size) + "-kWh battery")
#     def upgrade_battery(self):
#         if self.battery_size != 85:
#             self.battery_size = 85
#     def get_range(self):
#         if self.battery_size == 70:
#             range = 240
#         elif self.battery_size == 85:
#             range = 270
#         message = "This car can go approximately " + str(range)
#         message += "miles on a full charge."
#         print(message)
#         self.upgrade_battery()

# class ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery_size = Battery()
#     def describe_battery(self):
#         self.battery_size.battery_size()
#     def get_range(self):
#         self.battery_size.get_range()
# my_tesla = ElectricCar('tesla', 'model s', 2016)
# my_tesla.get_range()
# my_tesla.get_range()


# codewars练习

# # 第一题
# class Ship:
#     def __init__(self, draft, crew):
#         self.draft = draft
#         self.crew = crew
#     def is_worth_it(self):
#         total_crew_weight = self.crew * 1.5
#         adjusted_draft = self.draft - total_crew_weight 
#         return adjusted_draft > 20

# # 第二题
# class Block:
#     def __init__(self, dimensions):
#         self.dimensions = dimensions
#     def get_width(self):
#         return self.dimensions[0]
#     def get_length(self):
#         return self.dimensions[1]
#     def get_height(self):
#         return self.dimensions[2]
#     def get_volume(self):
#         return self.dimensions[0] * self.dimensions[1] * self.dimensions[2]
#     def get_surface_area(self):
#         width = self.get_width()
#         length = self.get_length()
#         height = self.get_height()
#         return 2 * (width * length + width * height + length * height)

# 第三题
# # TODO: complete this class
# class PaginationHelper:
    
#     # The constructor takes in an array of items and an integer indicating
#     # how many items fit within a single page
#     def __init__(self, collection, items_per_page):
#         self.collection=collection
#         self.items_per_page=items_per_page
#         pass
    
#     # returns the number of items within the entire collection
#     def item_count(self):
#         return len(self.collection)
#         pass
    
#     # returns the number of pages
#     def page_count(self):
#         a=self.item_count()
#         b=a/self.items_per_page
#         if a%self.items_per_page!=0:
#             b=b+1
#         return int(b)
#         pass
    
#     # returns the number of items on the given page. page_index is zero based
#     # this method should return -1 for page_index values that are out of range
#     def page_item_count(self, page_index):        
#         if page_index>self.page_count()-1 or page_index<0:
#             return -1
#         if page_index==self.page_count()-1:
#             if self.item_count()==self.items_per_page:
#                 return self.items_per_page
#             if self.items_per_page==1:
#                 return self.items_per_page
#             if self.item_count()%self.items_per_page==0:
#                 return self.items_per_page
#             return self.item_count()%self.items_per_page
        
#         if page_index<self.page_count()-1:
#             return self.items_per_page
#         pass
    
#     # determines what page an item at the given index is on. Zero based indexes.
#     # this method should return -1 for item_index values that are out of range
#     def page_index(self, item_index):
#         if (item_index+1)>self.item_count() or item_index<0:
#             return -1
#         else:
#             a=(item_index+1)/self.items_per_page-1
#             if (item_index+1)%self.items_per_page!=0:
#                 a=a+1
#         return int(a)
#         pass

# # 第四题
# import math  
# class Vector:
#     def __init__(self, components):
#         self.components = list(components)
        
#     def add(self, other):
#         if len(self.components) != len(other.components):
#             raise ValueError("Vectors must be of the same length to be added.")
#         return Vector([x + y for x, y in zip(self.components, other.components)])
    
#     def subtract(self, other):
#         if len(self.components) != len(other.components):
#             raise ValueError("Vectors must be of the same length to be subtracted.")
#         return Vector([x - y for x, y in zip(self.components, other.components)])
    
#     def dot(self, other):
#         if len(self.components) != len(other.components):
#             raise ValueError("Vectors must be of the same length to dot product.")
#         return sum([self.components[i] * other.components[i] for i in range(len(self.components))])
    
#     def norm(self):
#         return math.sqrt(sum([x ** 2 for x in self.components]))
    
#     def __str__(self):
#         return "(" + ",".join(str(x) for x in self.components) + ")"
    
#     def equals(self, other):
#         if isinstance(other, Vector):
#             return self.components == other.components
#         return False

# # 第五题
# # TODO: create the User class
# # it must support rank, progress, and the inc_progress(rank) method
# class User ():    
#     def __init__ (self):
#         self.RANKS = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]
#         self.rank = -8
#         self.rank_index = 0
#         self.progress = 0
        
#     def inc_progress (self, rank):
#         rank_index = self.RANKS.index(rank)
        
#         # 计算rank的差，得出可以获得多少进度
#         if(self.rank!=8):
#         # 完成的是同等级的题目
#             if rank_index == self.rank_index:
#                 self.progress += 3

#             # 完成的是比当前等级低一级的题目
#             elif rank_index == self.rank_index - 1:
#                 self.progress += 1

#             # 完成的是比当前等级高的题目
#             elif rank_index > self.rank_index:
#                 difference = rank_index - self.rank_index
#                 self.progress += 10 * difference * difference

#             # 如果进度大于100，升级，每减去100进度，升一级    
#             while self.progress >= 100:
#                 self.rank_index += 1
#                 self.rank = self.RANKS[self.rank_index]
#                 self.progress -= 100    

#                 # 如果升到8级（最高级），进度被置为0
#                 if self.rank == 8:
#                     self.progress = 0
#                     return