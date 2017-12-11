#coding=utf-8
#定义一个变量，获取用户输入的一个信息
#input是输入
hight = int(input('请输入你的身高:'))
#print是输出
print(hight)

print('hight变量里的值是%d'%hight)

name = '老马' #双引号内的内容都是字符串

print('你的名字叫%s'%name)#字符串只能用%s

num = 15

print('数字是%d'%num) #整数都是用%d

########################################

#打印名片
newName = input("请输入你的名字：")
phoneNum = input("请输入你的手机号码：")
qqNum = input("请输入你的QQ号码：")
age = input("请输入你的年龄：")
male = input("请输入你的性别：")


print("============================")
print("你的名字叫：%s"%newName)
print("你的性别是：%s"%male)
print("你的手机号是：%s"%phoneNum)
print("你的QQ号是：%s"%qqNum)
print("你的年龄是：%s"%age)
print("============================")
