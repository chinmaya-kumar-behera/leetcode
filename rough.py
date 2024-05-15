# x = dict([[10,20]])

# class CustomError(Exception):
#     def __init__(self,value):
#         self.value = value

#     def __str__(self):
#         return self.value

# def customDict(it):
#     d = {}
#     for kv in it:
#         if len(kv) != 2:
#             raise CustomError('Subsequence length is not 2')
#         k,v = kv
#         d[k] = v
#     return d

# try:
#     cIter = customDict([[10,20],'b8','cd',('prime',5)])
#     print(cIter)
# except:
#     print("length error is handled")
# else:
#     print("else block")
# finally:
#     print("finally block called")
# a



class Sample:
    pass

x = Sample()

print(x)
print(x.__new__(Sample))
print(x.__str__())
print(x.__init__())



print(x.__str__())


# def single_ton(cls):
#     instance = None
#     def inner(*args,**kwargs):
#         nonlocal instance
#         if instance is None:
#             # instance = cls.__new__(cls, *args, **kwargs)
#             # instance = instance.__init__(*args, **kwargs)
#             instance = cls()
#         return instance
#     return inner

# @single_ton
# class sample:
#     def __init__(self):
#         print("Object created")

# s1 = sample()
# s2 = sample()
# print(s1 is s2)



