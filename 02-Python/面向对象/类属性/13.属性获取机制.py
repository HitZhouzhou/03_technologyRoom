#类也是一种重要的对象,类是一个模板,在程序中只有一个

class Tool:
    count=0
    def __init__(self,name):
        self.name=name # 实例属性
        Tool.count+=1  # 类属性

tool1=Tool("斧头")
tool2=Tool("榔头")
tool3=Tool("水桶")
tool4=Tool("monkey")
tool3.count=99
# 输出工具对象的总数
print(Tool.count)
print("工具对象总数: %d"% tool4.count)
# python向上查找

print(tool4.name)

