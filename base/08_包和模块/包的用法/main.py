#从datatools这个包中导出processor，reader模块
from datatools import  processor,reader,writer

def main():
    writer_len = writer.write_file('data.txt','hello world！')
    #写入失败直接返回
    if not writer_len:
        return
    #写入成功
    print('写入成功!')
#读取文件
    data = reader.read_file('data.txt')
    if not data:
        print('读取文件失败!')
        return

    print('读取成功，读取的数据为:',data)

if __name__ == '__main__':
    main()