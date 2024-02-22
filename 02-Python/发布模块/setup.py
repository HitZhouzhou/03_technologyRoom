from distutils.core import setup

setup(name="pig",
      version="1.0",
      description="测试发布模块",
      long_description="测试发布模块",
      author="pig",
      author_email="hitzhoujy@163.com",
      url="pig.com",
      py_modules=["_message.send_message",
                  "_message.receive_message"])
