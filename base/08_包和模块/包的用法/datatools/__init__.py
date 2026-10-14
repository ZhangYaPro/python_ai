__version__ = "0.1.0"
#从同级目录core目录下导入processor模块
from .core import processor
#从同级目录io目录下导入模块
from .io import reader,writer
#暴露模块名--表示datatools这个包导出了那些函数
__all__ = ['processor','reader','writer']