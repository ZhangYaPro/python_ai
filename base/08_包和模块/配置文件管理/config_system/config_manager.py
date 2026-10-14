import json
import os
def load_config(filename):
    '''
    """加载配置文件"""
    :param filename: 加载的文件路径
    :return:  json对象，就是字典
    '''
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            config = json.load(f)
        print(f"配置已加载：{filename}")
        return config
    except FileNotFoundError:
        print(f"错误：配置文件不存在 - {filename}")
        return {}
    except json.JSONDecodeError:
        print(f"错误：配置文件格式错误 - {filename}")
        return {}

def save_config(filename, config):
    '''
     """保存配置文件"""
    :param filename:加载的json文件路径
    :param config: json对象，字典
    :return:
    '''
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        print(f"配置已保存：{filename}")
        return True
    except IOError as e:
        print(f"错误：保存配置失败 - {e}")
        return False

def get_config_value(config, key, default=None):
    '''
    """获取配置值"""
    :param config: 字典
    :param key: 字典某想要获取的一个key
    :param default: 默认
    :return:
    '''
    #获取config字典中key为
    return config.get(key, default)

def set_config_value(config, key, value):
    '''
    """设置配置值"""
    :param config: 字典
    :param key:要设置的关键字
    :param value:要设置关键字对应的值
    :return:返回字典
    '''
    config[key] = value
    return config


