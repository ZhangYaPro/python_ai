'''
读写Json
'''
'''
import json
#从文件中读取json字符串加载成json对象，  叫做反序列化
json对象 = json.load(json文件) 
#将json对象写入文件中，叫做序列化
json.dump(json对象，文件)
  json对象  就是一个字典
'''
import json

# 读取 JSON
def read_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

# 写入 JSON
def write_json(filename, data):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)