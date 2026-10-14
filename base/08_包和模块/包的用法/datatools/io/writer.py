def write_file(filename,data):
    try:
        with open(filename,'a',encoding='utf-8') as f:
            return f.write(data)
    except Exception as e:
        print('写文件异常，e is ',e)
        return None