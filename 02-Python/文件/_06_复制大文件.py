file_read=open("README.txt","r")
file_write=open("README[附件]","w")
# 2.读写
while True:
    text = file_read.readline()

    #判断是否读取到内容:
    if not text:
        break

    file_write.write(text)

file_write.close()
file_read.close()