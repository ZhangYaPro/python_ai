from nacl import encoding


def read_file(filename,mode,encoding="utf-8"):
    try:
        # 可能出错的代码
        with open(filename, mode, encoding=encoding) as f:
            content = f.read()
    except FileNotFoundError:
        print("错误：文件不存在")
    except Exception as e:
        print(f"发生错误: {e}")
    else:
        # 只有在 try 块成功执行时才运行
        print(f"文件读取成功，内容长度: {len(content)} 字符")
    finally:
        #无论正确还是错误
        # 无论如何都会执行
        print("文件操作完成")

