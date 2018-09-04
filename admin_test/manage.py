#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'admin_test.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


######### =============== 操作流程 =============== #########

# python 版本3.7  端口执行命令:
# python3 manage.py migrate
# python3 manage.py runserver
# django-admin.py startproject mysite

# 生成数据库表命令
# python3 manage.py makemigrations
# python3 manage.py migrate

# 数据库超级管理员
# python3 manage.py createsuperuser
# username admin
# password admin1234
# python3 manage.py runserver

# 关联数据库
# admin.py from crm.models import Topic
# admin.py admin.site.register(Topic)

# 数据库数据操作
# python3 manage.py flush　清空数据库
# python3 manage.py dbshell 数据库命令行  yes||no
# python manage.py dumpdata appname > appname.json    # 导出数据
# python manage.py loaddata appname.json              # 导入数据
# exict() 退出