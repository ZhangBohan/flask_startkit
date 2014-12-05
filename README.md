#Flask StartKit


## How to start？
    # 复制代码到本地
    git clone https://github.com/ZhangBohan/flask_startkit.git
    # 安装virtualenv，用于创建Python虚拟环境，如果安装则跳过
    sudo pip install virtualenv 
    # 建立虚拟环境
    virtualenv env --no-site-packages
    # 启动虚拟环境
    source env/bin/activate
    # 以开发模式启动该项目
    python dev_server.py
    
在游戏器打开：[http://127.0.0.1:9000/hello_world](http://127.0.0.1:9000/hello_world)
或者新打开命令行输入`curl http://127.0.0.1:9000/hello_world`


如果看到了`Hello World!`，就是安装成功了！
    
## Web Server
 
 [dev server](dev_server.py): 开发用web服务器，代码有变化自动reload
 ```
 python dev_server.py
 ```

 [prod server](prod_server.py): 生产用web服务器，高性能

 ```
  usage: prod_server.py [-h] command

  positional arguments:
    command     action [start, stop, restart, status]

  optional arguments:
    -h, --help  show this help message and exit
 ```
