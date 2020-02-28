Pip management:

```bash
# list packages. 列出所有包。
pip list

# list packages that could be upgrated. 列出可升级的包。
pip list --outdate

# latest packages that has been installed. 列出已安装的最新的包。
pip list --uptodate

# upgrade a package. 升级一个包。
pip install --upgrade <package-name>

# pip当前内建命令并不支持升级所有包，但可以使用下面的命令来升级所有包。
pip freeze --local | grep -v '^-e' | cut -d = -f 1 | xargs -n1 pip install -U
```

pip requirement text:

```bash
# 生成requirements.txt文件
pip freeze > requirements.txt

# 安装requirements.txt依赖
pip install -r requirements.txt
```



