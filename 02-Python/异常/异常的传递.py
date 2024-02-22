def demo1():
    return int(input("输入一个整数: "))

def demo2():
    return demo1()
# 利用传递性,在主程序中捕获异常
try:
    print(demo1())
except Exception as result:
    print("未知错误 : %s" % result)

