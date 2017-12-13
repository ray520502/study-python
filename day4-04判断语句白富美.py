#coding=utf-8

#三个条件，皮肤白/有钱/美
color = int(input('请问你的皮肤白吗？1.白 2.不白'))
rich = int(input('请问你的财富总额有多少？'))
beutiful = int(input('请问你漂亮吗？1.是 2.不是'))

if color==1 and rich>100000 and beutiful==1:
    print('你好白富美....')
elif color==1 and rich<100000 and beutiful==1:
    print('你好美女')
elif color==2 and rich>100000 and beutiful==1:
    print('你可能需要去漂白了～')
elif color==1 and rich>100000 and beutiful==2:
    print('你需要去整容了')
elif color==2 and rich<10000 and beutiful==2:
    print('请你努力读书造福社会～')
