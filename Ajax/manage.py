#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Ajax.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)



######### =============== Ajax实现流程 =============== #########
# 基于JS 实现Ajax
# Step1 : var xmlHttp = XMLHttpRequest()
# Step2 : xmlHttp.open('')
# Step3 : xmlHttp.send('name = alex')   #请求体内容 get无请求体(url后就是‘请求体’)【send(null) 无请求体发送null】  post(有请求体)
# Step4 : var context = xmlHttp.responseText #监听函数监听responseText属性：

# JSON 与 JSONP



# 基于jquery 的ajax 实现 最底层的封装 $.ajax()
