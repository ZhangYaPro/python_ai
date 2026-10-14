def safe_read_file(filename):
    """完整的安全文件读取函数"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except FileNotFoundError:
        print(f"错误：文件 '{filename}' 不存在")
        return None
    except PermissionError:
        print(f"错误：没有权限读取文件 '{filename}'")
        return None
    except UnicodeDecodeError:
        print(f"错误：文件编码错误，尝试使用 GBK 编码")
        try:
            with open(filename, 'r', encoding='gbk') as f:
                content = f.read()
            return content
        except:
            return None
    except IOError as e:
        print(f"错误：I/O 错误 - {e}")
        return None

def safe_write_file(filename, content):
    """完整的安全文件写入函数"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"成功写入文件 '{filename}'")
        return True
    except PermissionError:
        print(f"错误：没有权限写入文件 '{filename}'")
        return False
    except IOError as e:
        print(f"错误：写入失败 - {e}")
        return False