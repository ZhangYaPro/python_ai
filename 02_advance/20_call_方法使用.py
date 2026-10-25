class Add:
    def __call__(self, x, y):
        return x + y
add = Add()
#将对象像函数一样使用，可以触发__call__方法
print(add(3, 5))