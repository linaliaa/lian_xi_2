#第四次实验报告书上习题

# #1
# Lali={'first_name':'Marius','last_name':'ALi','age':'21','city':'weimingshi'}
# print(Lali['first_name'])
# print(Lali['last_name'])
# print(Lali['age'])
# print(Lali['city'])

# #2
# shu={'A':'1','B':'2','C':'3','D':'4','E':'5'}
# for key,value in shu.items():
#     print(key+'最喜欢的数字是：'+value)

# #3
# dics={'list':'列表','var':'变量','int':'整型','boolean':'布尔','str':'字符串'}
# print('dics[\'list\']'+':' + dics['list'])
# print('dics[\'var\']'+':' + dics['var'])
# print('dics[\'int\']'+':' + dics['int'])
# print('dics[\'boolean\']'+':' + dics['boolean'])
# print('dics[\'str\']'+':' + dics['str'])

# #4
# dics={'list':'列表','var':'变量','int':'整型','boolean':'布尔','str':'字符串'}
# for k,v in dics.items():
#     print(k + ':' + v + '\n')

# #5
# heliu={'nile':'egypt','changjiang':'China','xiangjiang':'China'}
# for r,c in heliu.items():
#     print('The '+r+' runs through '+c)
# for r in heliu.keys():
#     print(r)
# for c in heliu.values():
#     print(c)

# #6
# favorite_languages={
#     'jen':'python',
#     'sarah':'c',
#     'edward':'rust',
#     'phil':'python',
#     }
# lists=['jen','sarah','phil','mmm']
# temp=[]
# for k in favorite_languages.keys():
#     temp.append(k)
#     print(temp)
#     for s in lists:
#         if s in temp:
#             print("Thanks")
#         else:
#             print("Please take our poll!")

# #7
# Lali0={'first_name':'Marius0','last_name':'ALi0','age':'20','city':'weimingshi0'}
# Lali1={'first_name':'Marius1','last_name':'ALi1','age':'21','city':'weimingshi1'}
# Lali2={'first_name':'Marius2','last_name':'ALi2','age':'22','city':'weimingshi3'}
# ren=[Lali0,Lali1,Lali2]
# for i in ren[:]:
#     print(i)

# #8
# dog ={'name':'A','age':'1'}
# cat ={'name':'B','age':'2'}
# bird ={'name':'C','age':'3'}
# pets = [dog,cat,bird]
# for p in pets:
#     print(p)

# #9
# favorite_places={'A':'a','B':'b','C':'c'}
# for n in favorite_places.items():
#     print(n)

# #10
# shu={'A':['1','2'],'B':['3','4'],'C':['5','6']}
# for key,value in shu.items():
#     print(key+'最喜欢的数字是：')
#     for value1 in value:
#         print(value1)

# #11
# cities={'beijing':{'country':'China','population':'1000','fact':'超堵'},'changsha':{'country':'China','population':'100','fact':'很堵'},'hangzhou':{'country':'China','population':'500','fact':'很堵2'}}
# for k,v in cities.items():
#     print('城市：'+k+'的信息：')
#     for k1,v1 in v.items():
#         print(k1,v1)

# #第七章练习

# #1
# message=input('请输入您想要租赁的汽车：')
# print('Let me see if I can find you a '+message)

# #2
# message=input('请输入用餐人数：')
# if int(message)>8:
#     print('没有空桌')
# else:
#     print('有空桌')

# #3
# message=input('请输入一个数，将判断这个数是不是10的整数倍：')
# if int(message)%10==0:
#     print(message+'是10的整数倍')
# else:
#     print(message+'不是10的整数倍')

# #4
# message =('请输入一种比萨配料，输入‘quit’后退出程序，请输入：')
# while True:
#     message=input(message)
#     if 'quit' in message:
#         break
#     else:
#         print('我们会在比萨中添加这种配料：'+message)

#5
# message='请输入您的年龄：'
# while True:
#     message=input(message)
#     if 'quit' in message:
#         print('已退出')
#         break
#     elif int (message)<3:
#         print('免费')
#     elif 3<=int(message)<12:
#         print('10r')
#     elif int(message)>=12:
#         print('15r')

#6
# message1=('请输入一种比萨配料，输入‘quit’后退出程序，请输入：')
# active1=True
# while active1:
#     message=input(message1)
#     if 'quit' in message:
#         active1=False
#     else:
#         print('我们会在比萨中添加这种配料：'+message)

#7
# while 1:
#     print('2')

#8
# sandwich_orders=['1','2','3','4']
# finished_sandwiches=[]
# a=True
# while a:
#     if int(len(sandwich_orders))!=0:
#         n=sandwich_orders.pop()
#         finished_sandwiches.insert(0,n)
#     else:
#         a=False
# print(finished_sandwiches)

#9
# print('熟食店的五香烟熏牛肉卖完了')
# sandwich_orders=['1','pastram','2','pastram','3','pastram','4']
# print(sandwich_orders)
# while 'pastram' in sandwich_orders:
#     sandwich_orders.remove('pastram')
# print(sandwich_orders)

#10
# names='请输入你的姓名：'
# places='你想去的地方：'
# n={}
# a=True
# while a:
#     name=input(names)
#     place=input(places)
#     n[name]=place
#     repeat=input('还有吗(答no退出)：')
#     if repeat=='no':
#         a=False
# print(n)

#codewars代码

#第一题
# def naughty_or_nice(data):
#     naughty_count = 0  
#     nice_count = 0  
  
#     for month, days in data.items():  
#         for day, behavior in days.items():  
#             if behavior == 'Naughty':  
#                 naughty_count += 1  
#             elif behavior == 'Nice':  
#                 nice_count += 1  
#             else:  
#                 raise ValueError(f"Unknown behavior: {behavior}")  
      
#     if naughty_count > nice_count:  
#         return "Naughty!"  
#     elif naughty_count < nice_count:  
#         return "Nice!"  
#     else:  
#         return "Nice!"

#第二题
# def get_pins(observed):
#     adjacent_digits = {
#         '0': ['0', '8'],
#         '1': ['1', '2', '4'],
#         '2': ['1', '2', '3', '5'],
#         '3': ['2', '3', '6'],
#         '4': ['1', '4', '5', '7'],
#         '5': ['2', '4', '5', '6', '8'],
#         '6': ['3', '5', '6', '9'],
#         '7': ['4', '7', '8'],
#         '8': ['5', '7', '8', '9', '0'],
#         '9': ['6', '8', '9']
#     }
#     if not observed:
#         return []
#     def generate_pins(observed, current_pin):
#         if len(current_pin) == len(observed):
#             result.append(current_pin)
#             return
#         else:
#             current_digit = observed[len(current_pin)]
#             for neighbor in adjacent_digits[current_digit]:
#                 generate_pins(observed, current_pin + neighbor)
#     result = []
#     generate_pins(observed, "")
#     return result

#第三题
# def protein(rna):  
#     protein_sequence = ""  
#     for i in range(0, len(rna), 3):  
#         codon = rna[i:i+3]  
#         if codon not in PROTEIN_DICT:  
#             continue  
#         if PROTEIN_DICT[codon] == "Stop":  
#             break  
#         protein_sequence += PROTEIN_DICT[codon]  
#     return protein_sequence

#第四题
# def fillable(stock, merch, n):  
#     if merch not in stock:  
#         return False    
#     if stock[merch] < n:  
#         return False  
#     return True

#第五题
# MORSE_CODE['_'] = ' '

# def decodeBits(bits):
#     # 去掉开始的0和结尾的0
#     bits = bits.strip('0')
    
#     # if no zeros in bits
#     if '0' not in bits:
#         return '.'
    
#     # check for multiple bits per dot
#     minOnes = min(len(s) for s in bits.split('0') if s)
#     minZeros = min(len(s) for s in bits.split('1') if s)
#     m = min(minOnes, minZeros)
    
#     # decode bits to morse code
#     return bits.replace('111'*m, '-').replace('0000000'*m, ' _ ').replace('000'*m, ' ').replace('1'*m, '.').replace('0'*m, '')

# def decodeMorse(morseCode):
#     # decode morse code to letters
#     return ''.join(MORSE_CODE[c] for c in morseCode.split())