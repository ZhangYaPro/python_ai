import requests

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "deepseek-r1:1.5b"

# 定义函数，给大模型发送请求，并获取处理结果
def get_response(prompt):
    # 发送请求，获取响应
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
        },
    )
    # 获取模型处理的结果(文本信息)
    return response.json()["message"]["content"]

def get_response_list(prompt_list):
    """
    根据历史提示词记录列表，选出最近的20条，作为消息发送给大模型，从而形成记忆功能。
    :param prompt_list: 提示词列表，[{'role':'user','content':'AI怎么学?'},
         {'role':'assistant','content':'去kaggle学习'},
         {'role':'user','content':'还有什么方法？'}]
    :return:大模型的回答文本
    """
    # 获取列表中最近的20条记录，作为参考发送给大模型
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": prompt_list[-20:],
            "stream": False,
        },
    )
    # 获取模型处理的结果(文本信息)
    return response.json()["message"]["content"]

if __name__ == "__main__":
    # print(get_response("您好，学习AI的方式有哪些?"))
    messages_list = [{'role': 'user', 'content': '您好，学习AI的方式有哪些?'}]
    print(get_response_list(messages_list))
