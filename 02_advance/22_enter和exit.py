'''
演示enter和exit操作
'''
class MyContext:
    def __enter__(self):
        print("进入 with")
        return "资源对象"

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("退出 with")
        print("异常类型：", exc_type)
        print("异常值：", exc_val)

#MyContext()先调用__enter__方法，返回的值给到resource这个参数中，然后再调用__exit__这个函数进行回收
with MyContext() as resource:
    print(resource)