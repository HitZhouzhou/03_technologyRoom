import _1_测试模块1
import _2_测试模块2
_1_测试模块1.hello()
_2_测试模块2.hello()

import _2_测试模块2 as h2
h2.hello()
# 如果直接执行模块,都输出__main__
if __name__=="__main__":

    print(__name__)
