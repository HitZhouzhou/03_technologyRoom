class Dog(object):
    @staticmethod
    def run():
        print("static-小狗要跑...")
    @classmethod
    def run(cls):
        print("cls--小狗要跑")
Dog.run()
dog1 = Dog
dog1.run()