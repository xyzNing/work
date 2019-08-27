# def test(number):
#     def test_in(number2):
#         return number+number2
#     return test_in
# a=test(10)
# print(a(100))

def magic(func):
    print("正在调用magic")
    def magic_in(*args,**kwargs):
        print("正在调用magic_in")
        rest=func(*args,**kwargs)
        print("magic_in方法调用完成")
        return rest
    return magic_in

@magic    #test=magic_in(test)
def test():
    print("正在调用test")
@magic
def test1(a,b):
    print("正在调用test1")
    return a+b
# test()
s=test1(1,2)
print(s)