file_read=open("README.txt","r")
file_write=open("README[附件]","w")

text=file_read.read()
file_write.write(text)

file_write.close()
file_read.close()