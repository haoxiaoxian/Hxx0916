#获取移动平均值
#
# def average():
#     sum = 0   #总和
#     count = 0 #项
#     avg = 0
#     while True:
#         num = yield avg
#         sum += num
#         count +=1
#         avg = sum/count
#
# g = average()
# g.__next__() #到第一个yield
# while 1:
#     num = int(input('input a number:'))
#     average = g.send(num) #到第二个yield
#     print(average)
#
#

#带装饰器的
def wrapper(func):
    def inner(*args,**kwargs):
        ret = func(*args,**kwargs)
        ret.__next__()
        return ret
    return inner

@wrapper
def average():
    sum = 0
    count = 0
    avg = 0
    while True:
        num = yield avg
        sum += num
        count += 1
        avg = sum/count

avg_g = average()
while 1:
    number = int(input('input a number:'))
    ret = avg_g.send(number)
    print(ret)