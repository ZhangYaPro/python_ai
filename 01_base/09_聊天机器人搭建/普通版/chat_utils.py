'''
这是一个聊天的工具类，用来调用ollama大模型
'''
#1.导包

import ollama
#2.定义函数，给打模型发送请求，并获取处理结果
def get_response(prompt):
    #2.1 发送请求，获取响应
    response = ollama.chat(model='deepseek-r1:1.5b',messages=[
        {'role':'user',
         'content':prompt,}
    ])
    #2.2 获取模型处理的结果(文本信息)
    print(response['message']['content'])

def get_response_list(prompt_list):
    '''
    根据历史提示词记录列表，选出最近的20条，作为消息发送给大模型，从而形成记忆功能。
    :param prompt_list: 提示词列表，[{'role':'user','content':'AI怎么学?'},
    {'role':'assistant','content':'去kaggle学习'},
    {'role':'user','content':'还有什么方法？'}]
    :return:大模型的回答文本
    '''
    # 2.1 获取列表中最近的20条记录，作为参考发送给大模型
    response = ollama.chat(model='deepseek-r1:1.5b',messages=prompt_list[-20:])
    #2.2 获取模型处理的结果(文本信息)
    print(response['message']['content'])

def get_response_list2(prompt_list):
    stream = ollama.chat(
        model='deepseek-r1:1.5b',
        messages=prompt_list[-20:],
        stream=True,   # 流式输出
    )
    for chunk in stream:
        print(chunk['message']['content'], end='', flush=True)

def get_response_list3(prompt_list):
    stream = ollama.chat(
        model='deepseek-r1:1.5b',
        messages=prompt_list[-20:],
        stream=True,
    )
    for chunk in stream:
        # 打印思考过程（如果有）
        print(chunk['message'].get('reasoning_content', ''), end='', flush=True)
        # 打印正式回答
        print(chunk['message']['content'], end='', flush=True)

if __name__ == '__main__':
    # get_response('您好，学习AI的方式有哪些?')
    messages_list = [{'role':'user','content':'您好，学习AI的方式有哪些?'}]
    # get_response_list(messages_list)
    # get_response_list2(messages_list)
    get_response_list3(messages_list)

