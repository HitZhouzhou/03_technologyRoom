# 1.打开文件
file_read = open("README.txt")
file_write =open("README[附件]","w")
# 2. 读取文件内容
text = file_read()
file_write.write(text)
print(text)

# 3.关闭文件
file.close()
# 如果不关闭文件会造成系统消耗
