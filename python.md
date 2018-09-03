#Python pip升级及安装

### 查看pip 版本号 
```
python 2.7.0 版本  pip --version
python 3.6.0 版本  pip3 --version
```

###  pip版本升级 
```
window                 pip install --upgrade pip
mac    ,lunix               sudo pip install -U pip
```

###  查看Python版本
```
python 2.7.0 版本            ipython
python 3.6.0 版本            ipython3
```

### pip安装
```
列出所有的安装包   pip list
pip检测更新            pip list –outdated
pip升级包            pip install --upgrade packagename
pip卸载包             pip uninstall packagename
```
### PyQt5 安装
```
sudo pip3 install pyqt5
```
### 将Python文件打包成exe   window
```
1、使用pyinstaller

step1：安装pyinstaller，在cmd窗口使用pip install pyinstaller安装

step2：cd 到你的文件目录cd D:\py\python testcases\Slice

step3：运行pyinstaller -F SliceFile.py，注意-F是大写

step4：看结果，结果在新生成的文件夹dist下就有SliceFile.exe

补充一下后来发现的问题，运行pyinstaller -F SliceFile.py后的exe打开时总是先有一个cmd窗口出现，要去掉的话应该用运行pyinstaller -F -w SliceFile.py

缺点：不具备可移植性，只能在该
```

### Pycharm 不联想
```
File  - > Power Save Model(不勾选) -> 省电模式 
```
### Python gbk 与 utf-8 的区别
```
gbk:是在国家标准GB2312基础上扩容后兼容GB2312的标准（好像还不是国家标准）。GBK编码专门用来解决中文编码的，是双字节的。不论中英文都是双字节的。
UTF－8 编码是用以解决国际上字符的一种多字节编码，它对英文使用8位（即一个字节），中文使用24位（三个字节）来编码.英文字符较多的论坛则用UTF－8 节省空间
UTF8是国际编码，它的通用性比较好，外国人也可以浏览论坛，GBK是国家编码，通用性比UTF8差，不过UTF8占用的数据库比GBK大
```

### Python  Mac 快捷键
```
Tab / Shift + Tab   缩进、不缩进当前行
cmd+d               在下一行复制本行的内容
```

### Python 函数用法 
```
默认参数 
def func(name,age = 10):
    print(name,age)
    
不定长参数           
///TOOD  *以元祖的形式导入，存放所有未命名的参数变量
def func(name,*args):
    print(name,args)
    
///TOOD **以字典的形式导入，存放所有的未命名字典
def func(*args,**kwargs):
    print(args,kwargs)

匿名函数
lambda 由三部分组成 ，lambda 关键字， 变量 ，返回值

///TOOD  split()  ///对字符串切片 获取单个字符长度
string = "im a  fine "
string.split()
```
### Python 装饰器 （拓展原来函数功能的一种函数）
```

```
### Python 迭代器  （本质就是通过调用Nex()函数实现）
```
```

### __block修饰   __block Bool  IsTrue = Yes;  Static Bool  IsTrue = Yes; 
```
当在block内部使用block外部定义的局部变量时,如果变量没有被__block修饰,则在block内部是readonly(只读的),

不能对他修改,如果想修改,变量前必须要有__block修饰

__block的作用告诉编译器,编译时在block内部不要把外部变量当做常量使用,还是要当做变量使用.

如果再block中访问全局变量,就不需要__block修饰.
```



