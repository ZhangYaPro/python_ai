from setuptools import setup, find_packages

setup(
    name='datatools',
    version='1.0.0',
    description='数据处理工具包',
    author='yabo',
    author_email='18567678872@163.com',
    url='https://github.com/yourusername/datatools',
    license='MIT',
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[
        'numpy>=1.19.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)