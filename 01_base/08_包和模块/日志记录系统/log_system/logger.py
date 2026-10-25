import os
from datetime import datetime

def create_log_file(log_dir='logs'):
    '''创建日志目录'''
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    #返回log文件夹的相对位置
    return log_dir

def write_log(message, log_dir='logs',level='INFO'):
    '''
    将日志信息写入log文件中
    :param message: message是日志信息，
    :param log_dir:log_dir要存储日志的文件位置，
    :param level:level是日志级别参数，INFO表示默认普通运行信息
    :return:None
    '''
    try:
        #创建日志目录  -- 调用create_log_file()函数
        create_log_file(log_dir)

        #生成日志文件名
        #datetime.now()获取今天的日期时间
        #strftime 表示格式化为**年月日字符串**
        today = datetime.now().strftime('%Y-%m-%d')
        #log_file 日志名称
        #`os.path.join()`：把文件夹路径和文件名拼在一起
        log_file = os.path.join(log_dir,f'{today}.log')

        # 生成日志内容
        '''
        - `[{timestamp}]` 把时间用方括号包起来
        - `[{level}]` 日志级别（INFO / ERROR / WARNING）方括号包裹
        - `{message}` 你传入的日志文本内容
        '''
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_content = f"[{timestamp}] [{level}] {message}\n"

        # 写入日志
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(log_content)
        print(f"日志已记录：{log_content.strip()}")

    except Exception as e:
        print(f'错误:写入日志失败{e}')

def read_logs(log_dir='logs', date=None):
    '''
    读取日志中的内容
    :param log_dir:日志目录
    :param date:  要读取的日志时间
    :return:
    '''
    try:
        if date is None:
            date = datetime.now().strftime('%Y-%m-%d')
        log_file = os.path.join(log_dir, f'{date}.log')
        if not os.path.exists(log_file):
            print(f"日志文件不存在：{log_file}")
            return []
        with open(log_file, 'r', encoding='utf-8') as f:
            logs = f.readlines()
        return logs

    except Exception as e:
        print(f"错误：读取日志失败 - {e}")
        return []