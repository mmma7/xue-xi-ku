# import io
# a="asnjdcmkashnchjk"
# sio=io.StringIO(a)
# print(sio)
# print(sio.getvalue())
# sio.seek(5)
# sio.write("1234")
# print(sio.getvalue())
# sio.seek(1)
# sio.write("11")
# print(sio.getvalue())

# print(int('12',16))
# a=[10,10.0,'mingzi']
# print(a)

# a=list(range(0,10,2))
# print(a)
# a=[x*2 for x in range(0,3)]
# b=[y for y in range(30,100,2) if y%3==0]
# print(b)

# a=[10,20]
# a.append(30) #尾部插入
# b=[30,40]
# a.extend(b) #将第一个列表在尾部接上另一个
# a.insert(0,100) #在一个位置上插入一个，其他的往后靠
# print(a)

# a=[10,20,30,10,40,50]
# del a[2]#输入的是位置
# b=a.pop()#没输入默认是最后一个
# a.remove(10)#删除第一个出现的目标
# print(a,b)

# a=[10,20,30,40,50,60,70,80,90,100]
# print(a.index(50,2,7))
# print(a.count(50))
# print(len(a))

# a=[30,60,30,10,50]
# # a.sort()
# # print(a)
# # a.sort(reverse=True)
# # print(a)
# # import random
# # random.shuffle(a)
# # print(a)
# b=sorted(a)
# c=sorted(a,reverse=True)
# print(b)
# print(c)
# print(max(a))
# print(min(a))
# print(sum(a))

# a=[
#     ["搞笑吧",18,30000,"北京"],      #二维列表
#     ["逆天弟",19,40000,"广州"]
# ]
# print(a[1][3])  #先行后列
# for m in range(2):
#     for n in range(4):
#         print(a[m][n],end="\t")
#     print()

# a=(10,)     #元组 tuple
# print(type(a))
# b=tuple(range(6))
# c=tuple()
# d=tuple('ni hao',)
# e=tuple([10,20,30,40,50])
# print(b)
# print(c)
# print(d)
# print(e)































