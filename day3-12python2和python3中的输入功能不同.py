#coding=utf-8

a = input("请输入你的名字：")

print(a)
#python3可以支持正常的input功能，input里输入的任何内容都作为字符窜
#而python2当中input则会当作代码执行，容易出现漏洞，不安全

b = raw_input("请输入你的名字：")
print(b)
#python2中需要使用input输入字符窜，则需要使用raw_input才能正常不出现异常
#raw_input则不适合python3,会出现异常
