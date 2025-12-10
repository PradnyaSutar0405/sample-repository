import arithmetic
import geometry

print("Hello World!!")

num1=int(input("enter num1:"))
num2=int(input("enter num2:"))

arithmetic.add(num1,num2)

arithmetic.substract(num1,num2)

len=int(input("enter length:"))
br=int(input("enter breadth:"))

geometry.cal_rect_area(len,br)
geometry.cal_rect_peri(len,br)