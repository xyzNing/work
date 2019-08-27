class Test():
    def __init__(self):
        __num=100

    def get_num(self):
        return self.__num

    def set_num(self,num):
        self.__num=num

    num=property(get_num,set_num)

t=Test()
t.num=50
print(t.num)


