'''
文件偏移量
'''

'''
演示文件便宜量
'''
with open('./example.txt','r',encoding='utf-8') as f:
    #tell()获取当前文件指针的位置，这是按照字节统计的
    print(f'文件开始的偏移量',f.tell())
    #读取10个字符
    content = f.read(10)
    print(f'读取的内容{content}')
    print(f'当前的偏移量:{f.tell()}')
    #回到头部  seek() 是将指针移动到指定的位置上
    f.seek(0)
    content = f.read(10)
    print(f'当前的偏移量:{f.tell()}')

    #从开头移动6个字节   0表示从开头位置移动  1表示从当前位置移动  2表示从末尾位置开始移动
    f.seek(6,0)
    content = f.read(10)
    print(f'读取的内容{content}')
    #从末尾位置向前移动11个字节  -- read不能从末尾向前移动  会报错
    # f.seek(-9,2)
    # content = f.read(10)
    # print(f'读取的内容{content}')

    #将文件指针移动到文件末尾
    f.seek(0,2)
    #因为文件已经移动到文件末尾了,所以f.tell()获取的是文件的大小
    file_size = f.tell()
    print(file_size)



