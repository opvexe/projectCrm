## Django
```
pip install Django

创建 mysite

django-admin.py startproject blog 

Mac： 删除非空文件夹 rm -r -f filename
Mac: 回到上一页文件 cd - 
Mac: 回到用户目录 cd ~
Mac: 快捷键保存 control + s

python manage.py runserver 8080
python manage.py runserver 0.0.0.0:8000
python manage.py runserver

```
### 管理数据库
```


# python manage.py makemigrations   ##生成数据库表
# python manage.py migrate
# python manage.py createsuperuser
# username  admin
# password admin1234
# python manage.py runserver 8001
# 127.0.0.1:8001/admin

django-admin.py startproject mysite #创建mysite 文件

python manage.py makemigrations   ##生成数据库表
python manage.py migrate
python manage.py createsuperuser               # 创建超级管理员
python manage.py flush　　　　　　　　　　　　　　  # 清空数据库


#此命令会询问是 yes 还是 no, 选择 yes 会把数据全部清空掉，只留下空表

python manage.py dbshell            　　　　     # 数据库命令行
[Django 会自动进入在settings.py中设置的数据库，如果是 MySQL 或postgreSQL,会要求输入数据库用户密码。在这个终端可以执行数据库的SQL语句。如果您对SQL比较熟悉，可能喜欢这种方式。]

python manage.py dumpdata appname > appname.json    # 导出数据
python manage.py loaddata appname.json  　　　　　　  # 导入数据

　　
```

## 报错解决
```
You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

解决方法： python manage.py migrate
```
### html 文件放在templates
```
cur_time.html 放在 templates 文件夹内 （django 内层搜索文件目录封装templates）

TEMPLATES = [
{
'BACKEND': 'django.template.backends.django.DjangoTemplates',
'DIRS': [os.path.join(BASE_DIR, 'templates')]
}
```

###  注释 django.middleware.csrf.CsrfViewMiddleware
```
理由： form 提交订单的时候会检测csrf的随机字符串
django.middleware.csrf.CsrfViewMiddleware
```

### html 标签
```
标签网站： http://www.w3school.com.cn/tags/tag_hr.asp
<hr> 水平线,段落 

```
###  Satic 静态文件
```
Pycharm : New - Python Package 创建 Satic 文件
```


