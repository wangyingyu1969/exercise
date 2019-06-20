# 常规FOR循环

myValve = []
for valve in range(1, 10):
    myValve.append(valve ** 2)

print(myValve)

# 用一行代码实现
myData = [i ** 2 for i in range(1, 10)]
print('我是一行代码的结果', myData)

# 用 函数map(function,interable),这函数生成的结果是一个迭代器，故要用list转换。其中lambda是匿名函数
iDate = list(map(lambda x: x ** 2, range(1, 10)))
print('map function for loop', iDate)


# 用函数filter(function,interable),这函数生成的结果是一个迭代器，故要用list转换。
def is_odd(n):
    return n % 2 == 1


toomy = list(filter(is_odd, range(1, 10)))
print('list formed by filter', toomy)

xx = filter(lambda x: 2 < x < 10, [9, -10, 2, 8, 0, 10])
print(xx)
#
