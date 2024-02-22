# read 默认一次把所有内容读入内存
# readline 方法可以一次读取一行

file = open("hello.txt")
while True:
    text=file.readline()
    if not text:# 如果没有读取到内容就break
        break
    print(text)
file.close()