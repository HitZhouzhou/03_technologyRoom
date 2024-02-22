def input_password():
    # 1.提示用户输入密码
    pwd=input("请输入密码: ")

    # 2.判读密码长度
    if len(pwd)>=8:
        return pwd
    print("主动抛出异常")
    ex=Exception("密码长度不够")
    raise ex

print(input_password())