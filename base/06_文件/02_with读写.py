#创建文件对象
with open('./example2.txt','w',encoding='utf-8') as f:
    f.write('我是张亚博\n我的地球号是18567678872,欢迎加我一起学习!')

#读取文件内容
with open('./example2.txt','r',encoding='utf-8') as f:
    #读取所有行，每一行数据是列表的一个元素
    data = f.readlines()
    print(data)

#按照行来读取文件
with open('./example2.txt','r',encoding='utf-8') as f:
    while True:
        #按照行读取
        line = f.readline()
        if line:
            print(line)
            continue
        break

#读取文件，使用for循环
with open('./example2.txt','r',encoding='utf-8') as f:
    #通过for循环从文件中依次读取一行
    for line in f:
        print(line)


#按照列表多行写入
#准备数据
datas = ['张','亚','博1']
with open('./example3.txt','w',encoding='utf-8') as f:
    #将列表写入到文件
    f.writelines(datas)


