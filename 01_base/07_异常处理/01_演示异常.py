
try:
    file_r = open("./example.txt","r",encoding="utf-8")
    data = file_r.read()
    print(data)
    file_r.close()
except FileNotFoundError:
    print('文件不存在！')
except Exception as e:
    print('兜底捕获异常')


def safe_divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("错误：不能除以零")
        #异常时返回的值
        return None
    #正常情况下返回的值
    return result

print(safe_divide(10, 2))   # 5.0
print(safe_divide(10, 0))   # 错误：不能除以零

def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("错误：文件不存在")
    except PermissionError:
        print("错误：没有权限")
    except UnicodeDecodeError:
        print("错误：编码错误")

read_file("a.txt")

#一个 except 块捕获多个异常
def read_file2(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except (FileNotFoundError, PermissionError):
        print("错误：文件访问失败")

def read_file3(filename):
    try:
        with open('nonexistent.txt', 'r') as f:
            content = f.read()
    except FileNotFoundError as e:
            #获取异常类型
        print(f"异常类型: {type(e)}")
        print(f"异常信息: {e}")