from config_system import config_manager

"""主函数"""
config_file = 'config.json'

# 加载配置
config = config_manager.load_config(config_file)

if not config:
    # 创建默认配置
    config = {
        'app_name': 'MyApp',
        'version': '1.0.0',
        'debug': True,
        'port': 8000
    }
    config_manager.save_config(config_file, config)

# 获取配置值
app_name = config_manager.get_config_value(config, 'app_name')
print(f"应用名称：{app_name}")

# 修改配置
config = config_manager.set_config_value(config, 'debug', False)
config_manager.save_config(config_file, config)
