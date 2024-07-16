from setuptools import setup, find_packages
with open("./README.md",mode='r',encoding='utf-8') as f:
    des = f.read()

setup(
    name="thznumpy",      # 包名，用于安装和调用该包
    version="0.0.1.dev20240716",               # 版本号
    author="Sen",
    description="a math lib developed by Sen",
    long_description=des,
    long_description_content_type='text/markdown',
    author_email="tianhuzong@qq.com",
    url="https://github.com/tianhuzong/thztnumpy",
    license="MIT",
    packages=find_packages(),     
    install_requires=[
        'sympy',
        'numpy',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
