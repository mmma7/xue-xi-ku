# score=int(input("请输入分数："))
# grade=''
# if(score<60):
#     grade="不及格"
# elif(score<90):
#     grade="良好"
# elif(score<=100):
#     grade="优秀"
#
# print("分数是：{0}，等级是：{1}".format(score,grade))
from PyQt5.QtXml import QDomCDATASection

# x=int(input("请输入x的坐标："))
# y=int(input("请输入y的坐标："))
#
# if(x==0 and y==0):print("原点")
# elif(x==0):print("y轴")
# elif(y==0):print("x轴")
# elif(x>0 and y>0):
#     print("第一象限")
# elif(x<0 and y>0):
#     print("第二象限")
# elif(x<0 and y<0):
#     print("第三象限")
# elif(x<0 and y>0):
#     print("第四象限")

# score=int(input("请输入一个在0~100的数字："))
# degree=("ABCD")
#
# if(score>100 or score<0):
#     score=int(input("输入错误，请再输入一个在0~100的数字"))
# else:
#     num=score//10
#     if(num<6):num=5
#
# print("分数是：{0}，等级是：{1}".format(score,degree[9-num]))

# num=0
# sum_num=0
#
# while num<=100: #条件判断
#     sum_num=sum_num+num
#     num=num+1
#
# print(sum_num)
#
# num=0
#
# while num<10:
#     print(num)
#     num=num+1
# print("end")

sum_all=0
sum_even=0
sum_odd=0

#for num in range(101):
 #   sum_all=sum_all+num
    #if(num%2==0):
   #     sun_even=sum_even+num
  #  else:
 #       sum_odd=sum_odd+num

#print("0到100的和为:{0}，偶数和为:{1}，奇数和为:{2}".format(sum_all,sum_even,sum_odd))

# for x in range(6):
#     print(0,end="\t")

# for x in range(4):
#     for y in range(4):
#         print(y,end="\t")
#     print()
# print()
# for x in range(4):
#     for y in range(4):
#         print(x,end="\t")
#     print()

#九九乘法表
# for m in range(1,10):
#     for n in range(1,m+1):
#         print("{0}*{1}={2}".format(n,m,m*n),end="\t")
#     print()

#筛选多个字典，可以把字典放进列表进行
# r1=dict(name="高小一",age=18,city="北京")
# r2=dict(name="高小二",age=19,city="深圳")
# r3=dict(name="高小三",age=20,city="广州")
# tb=[r1,r2,r3]
#
# for x in tb:
#     if x.get("age")>=19:
#         print(x)
#     else:
#         print("你还太年轻了")

# while True:
# #while True: 构建了一个条件永远为真的循环，也被叫做无限循环。
# #只要程序不遇到跳出循环的语句，循环体中的代码就会一直不断地执行。
#     a = input("请输入一个字符（输入Q或q时结束）:")
#     #if a.upper()=="Q":
#     if a=="Q" or a=="q":
#         print("结束循环，退出")
#         break
#     else:
#         print(a)

# #要求输入员工的薪资，若薪资小于0则重新输入，最后打印出录入员工的数量和薪资明细，以及平均薪资

# empNum=0
# salarySum=0
# salary={}
# while True:
#     t=input("请输入你的名字（输入Q或q结束循环）：")
#     s=input("请输入你的薪资")
#     if t.upper()=="Q":
#         print("循环结束")
#         break        #使无限循环能够退出
#     elif t=="" or s=="":
#         print("输入无效，请重新输入")
#         continue
#     elif float(s)<=0 :
#         print("输入无效，请重新输入")
#         continue
#     else:print("输入成功")      #else可以省略
#     empNum+=1
#     salarySum+=float(s)
#     salary[t]=s
#
# print("员工数量为：",empNum)
# for key,value in salary.items():
#      print(f"{key}的薪资是{value}")
# print("总薪资为：{0}".format(salarySum))
# print("平均薪资为：{0}".format(salarySum/empNum))

# employees = {}
# total_salary = 0

# while True:
#     name = input("请输入员工名字（输入 '结束' 停止录入）：")
#     if name == '结束':
#         break
#     while True:
#         try:
#             salary = input("请输入该员工的薪资：")
#             if salary == '':
#                 print("薪资不能为空，请重新输入。")
#                 continue
#             salary = float(salary)
#             if salary < 0:
#                 print("薪资不能小于 0，请重新输入。")
#             else:
#                 employees[name] = salary
#                 total_salary += salary
#                 break
#         except ValueError:
#             print("输入的薪资不是有效的数字，请重新输入。")
#
# employee_count = len(employees)
# if employee_count > 0:
#     average_salary = total_salary / employee_count
# else:
#     average_salary = 0
#
# print(f"录入员工的数量为：{employee_count}")
# print(f"员工与其对应薪资明细如下：")
# for name, salary in employees.items():
#     print(f"{name}: {salary}")
# print(f"平均薪资为：{average_salary}")

t=0
x=[]
for i in range(4):
    s = input("请输入你的工资(输入Q或q结束循环)：")
    if s.upper()=="Q":
        print("循环结束")
        break
    elif float(t)<0:
        print("请重新输入一个数")
        continue
    t+=float(s)
    x.append(float(s))
else:
    print("录入成功")

print("录入薪资为：",s)
print(f"录入平均薪资为{t/4}")












































