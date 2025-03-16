import turtle
#第一个圆
# turtle.penup()
# turtle.goto(-100,0)
# turtle.pendown()
# turtle.color("blue")
# turtle.width(10)
# turtle.pensize(3)
# turtle.circle(100)
# #第二个圆
# turtle.penup()
# turtle.goto(50,0)
# turtle.pendown()
# turtle.color("black")
# turtle.circle(100)
# #第三个圆
# turtle.penup()
# turtle.goto(200,0)
# turtle.pendown()
# turtle.color("red")
# turtle.circle(100)
# #第四个圆
# turtle.penup()
# turtle.goto(-40,-130)
# turtle.pendown()
# turtle.color("yellow")
# turtle.circle(100)
# #第五个圆
# turtle.penup()
# turtle.goto(120,-130)
# turtle.pendown()
# turtle.color("green")
# turtle.circle(100)
#turtle.done()
import math
import turtle
x1,y1=100,100
x2,y2=100,-100
x3,y3=-100,-100
x4,y4=-100,100
turtle.penup()
turtle.goto(x1,y1)
turtle.pendown()
turtle.goto(x2,y2)
turtle.goto(x3,y3)
turtle.goto(x4,y4)

#计算起始点与终点的距离
distance=math.sqrt((x1-x2)**2+(y1-y2)**2)
turtle.write(int(distance))
turtle.done()