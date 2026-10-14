def read_file(filename):
    try:
        with open(filename,'r',encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print('读取文件异常，e is ',e)
        return None