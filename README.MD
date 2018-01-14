# 基础教程

### 配置 Python 环境
<div align="lefg">

由于抢课脚本是用 Python 编写，所以，要跑起来需要有 Python 环境，首先，从官网下载安装包进行安装
[Windows 安装包下载](httpshttps://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic//www.python.orhttps://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/fthttps://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/pythohttps://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/2.7.1https://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/python-2.7.14.msi)
下载完成后双击该文件进行安装，安装过程请记住下图箭头所指的路径，后面会用到
![](https://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/1.png)

安装完成后，打开文件管理器（即“我的电脑”），在文件管理器上面地址栏输入刚刚安装过程中记下来的路径，打开里面的 Scripts 文件夹，复制整个路径，然后鼠标放到“此电脑”上，右击，选择属性
![](https://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/15.png)



随后点击高级系统设置，在新窗口中打开环境变量



![](https://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/2.png)

![](https://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/3.png)

然后双击path，在”编辑环境变量“页新建两次环境变量，其值如下图所示，其中 C:\Python27 即是安装过程中记下来的路径

![](https://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/5.png)

![](https://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/4.png)



完成后所有窗口都点击确定将其关闭，同时按 windows 键和 r 键，在弹出来的窗口中输入 cmd 并点击确定



![](https://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/6.png)

在打开的命令行窗口内输入 python 并回车，如果看到 Python 2.7 等内容，说明 Python 运行环境正常，输入 exit() 退出后，输入 pip --version，如下图所示什么 pip 也是正常的，待会可以用 pip 安装我们需要的 requests库

![](https://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/7.png)

如果 pip 正常，可以继续输入 pip install requests 安装 requests 库，装好这个库脚本才可以正常运行

![](https://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/8.png)

如果 pip 不正常或者上面的安装过程不顺利，可以下载[ reqeusts 库源文件](httpshttps://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic//pypi.python.orhttps://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/packagehttps://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/bhttps://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/ehttps://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/eab4fc3752e3d240468a8c0b284607899d2fbfb236a56b7377a329aa8d0https://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/requests-2.18.4.tar.gz#md5=081412b2ef79bdc48229891af13f4d82)进行安装。下载完成后，将压缩文件解压出来，打开文件夹，将路径复制出来，在命令行里将该路径放到 cd 后面（注意 cd 后面有空格），切换到该目录下，输入

> python setup.py install 

即可安装 requests 库

![](https://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/14.png)

requests 库安装完成后可以如下图进行检验，没有报错即安装成功

![](https://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/9.png)



### 读取用户 Cookie 和课程代号
*在此仅以火狐和谷歌两种浏览器为例演示如何读取用户 Cookie 和课程代号*
Cookie 是用来识别用户身份的，在脚本运行时加入 Cookie 的目的是告诉系统是你要选课，而不是其他人，而课程代号则是用来告诉系统你要选哪一门课
##### 火狐浏览器
登录教务处后，在浏览器中点击地址栏最左边的小图标，然后点击弹出页上的小箭头查看细节，紧接着点击更多信息

![](https://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/cookie3.png)
![](https://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/cookie4.png)

可以看到下面的窗口，再点击查看 Cookie 即可看到浏览器保存的 Cookie 信息，其中，站点为 jwms.bit.edu.cn 的就是我们要的 Cookie，把它的内容全部复制出来

![](https://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/10.png)

![](https://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/11.png)

在选课页面把鼠标放到选课按钮上，浏览器左下角就会出现一段文字，括号内的数字即是课程代号，每一门课程都对应一个唯一的代号



![](https://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/id.png)

有了 Cookie 和课程代号之后，就可以开始运行脚本了，在命令行里输入

> python 脚本路径 选课类型 Cookie 课程代号 

然后回车脚本就开始工作了，其中脚本路径因人而异，可以输入到此处直接用鼠标将脚本文件拉到命令行窗口内，选课类型那个位置可以是1或者2，但所选为体育课时请输入2，其它课都是1，Cookie 填入自己的 Cookie 值， 代号可以有多个，用空格分开

![](https://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/12.png)

![选体育课](https://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/13.png)

##### 谷歌浏览器
读取 Cookie 的过程和火狐浏览器类似，下图有完整演示
![](https://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/cookie1.png)
![](https://raw.githubusercontent.com/JustianPupil/BIT-something/master/pic/cookie2.png)

获取课程代号的方法和火狐浏览器完全相同

</div>

*本教程主要针对用户较多的 Windows 平台编写，如果 Mac 用户需要帮助可以通过我的 email 联系我*

*考虑到我只是一名无知的小学生，此教程如果有错误的地方还请各位大佬指出来， email: Justian@protonmail*

*惟愿北理没有卖课换课这些交易*

[获取getclass.py](https://raw.githubusercontent.com/JustianPupil/BIT-something/master/getclass.py)
