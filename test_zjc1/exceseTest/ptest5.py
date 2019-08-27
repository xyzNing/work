L=['Hello', 'World', 18, 'Apple', None]
L1=[s.lower() for s in L if isinstance(s,str)]
print(L1)
import hashlib
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
def login(user,password):
    md5=hashlib.md5()
    md5.update((password).encode("utf-8"))
    if db[user]==md5.hexdigest():
        print("success")
    else:
        print("Fail")
s=login('bob','abc999')
import random
L2=[]
print(random.randrange(1,100))
for i in range(10):
    L2.append(random.randint(1,100))
print(L2)
# print(L2.sort())
# print(L2)
# print(L2[:3])
for i in range(len(L2)-1):
    for j in range(i,len(L2)-1):
        if L2[i]>L2[j+1]:
            L2[i],L2[j+1]=L2[j+1],L2[i]

print(L2)

# def sum(L):
#     s=0
#     for i in L:
#         s+=i+1
#     return s
# s=sum([1,2,3,4])
# print(s)                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
LL=map(lambda x:x+1,[1,2,3,4])
print(list(LL))
print(sum([1,2,3,4]))
from functools import reduce
print(reduce((lambda x,y:x+y),[1,2,3,4]))

