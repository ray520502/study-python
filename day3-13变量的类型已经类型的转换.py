#coding=utf-8
#if 用来完成半段

#if 条件：
#   条件成立的时候，做的事情

age = input("请输入你的年龄：")#input会默认把所有的输入内容都归类为字符窜
ageNum = int(age)              #所以需要用int()把age转化为int数字类型

#定义的类型有一下常见几种str/int/float/list等等，可用type(定义)来查询类型



#if如果年龄大于18岁则可以进网吧happy

if ageNum>=18:
    print("恭喜～你的年龄大于18岁，可以进网吧happy！")

else:
    print("你年龄太小赶紧回家做作业")
