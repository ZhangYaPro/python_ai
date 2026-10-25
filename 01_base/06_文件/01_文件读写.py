'''
演示文件读写
'''

'''
1. file = open(文件路径，模式，编码)
file是文件对象，里面包含了文件描述符
2.file.read() 读取  file.write(内容)
3.file。close()
'''
'''
1.‘r’  读取   文件不存在时报错
2.‘w’  写入   文件不存在时创建  并且写入时时删除覆盖
3.‘a’  追加   文件不存在时创建 
'''
#写入文件
#创造文件对象
file_w = open("./example.txt","w",encoding="utf-8")
#write返回实际写入文件的字符数
data = file_w.write("我叫小张不嚣张！")
print(data)
file_w.close()

#读文件
#创造文件对象
file_r = open("./example.txt","r",encoding="utf-8")
data = file_r.read()
print(data)
file_r.close()

#追加文件
#创造文件对象
file_a = open("./example.txt","a",encoding="utf-8")
data = file_a.write("hello")
print(data)
file_a.close()