def func2():
    x = 1 / 0  # 这里会抛出异常

def func1():
    func2()  # 异常会从这里传播出去

def main():
    try:
        func1()
    except ZeroDivisionError:
        print("捕获到异常：除以零")

main()