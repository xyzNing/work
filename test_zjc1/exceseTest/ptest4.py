def test():
    i=0
    while i<5:
        ret=yield i
        return ret
        i+=1

a=test()
next(a)
print(a.__next__())
# print("-"*30)
# for i in a:
#     print(i)