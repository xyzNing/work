import types
class Test(object):
    __slots__ = ("name","age" )
    def __init__(self,name,age):

        self.name=name
        self.age=age

def run(self):
    print("---1---")

@staticmethod
def eat():
    print("---eat---")

@classmethod
def sleep(cls):
    print("---sleep---")
test=Test("ss",10)
print(test.name,test.age)

test1=Test("s",10)
Test.eat=eat
test.eat()

Test.sleep=sleep
Test.sleep()

p1=Test('SS',12)
p1.run=types.MethodType(run,p1)
p1.run()
