try:
    num=int(input("输入一个整数: "))

    result=8/num

    print(result)
# except ZeroDivisionError:
#     print("除0错误")




except Exception as result:
    print("[未知错误] %s" % result)