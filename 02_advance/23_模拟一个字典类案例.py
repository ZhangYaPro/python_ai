class MyDict:
    def __init__(self):
        #初始化一个字典
        self.data = {}

    def __str__(self):
        return f"MyDict内容：{self.data}"

    def __repr__(self):
        return f"MyDict({self.data!r})"

    def __len__(self):
        return len(self.data)

    def __getitem__(self, key):
        print(f"正在读取 key：{key}")
        return self.data[key]

    def __setitem__(self, key, value):
        print(f"正在设置 {key} = {value}")
        self.data[key] = value

    def __delitem__(self, key):
        print(f"正在删除 key：{key}")
        del self.data[key]

    def __contains__(self, key):
        return key in self.data

    def __call__(self):
        print("当前数据：", self.data)

    def __iter__(self):
        return iter(self.data)


d = MyDict()

d["name"] = "Tom"
d["age"] = 18

print(d["name"])
print(len(d))
print("age" in d)

for key in d:
    print(key)

d()

del d["age"]

print(d)
print(repr(d))