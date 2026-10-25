from log_system import logger

"""主函数"""
# 写入日志
logger.write_log("程序启动", level='INFO')
logger.write_log("开始处理数据", level='INFO')

try:
    # 模拟处理
    result = 10 / 0
except ZeroDivisionError:
    logger.write_log("发生错误：除以零", level='ERROR')

logger.write_log("程序结束", level='INFO')

# 读取日志
logs = logger.read_logs()
print("\n今日日志：")
for log in logs:
    print(log.strip())
