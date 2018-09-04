### HTML标签

###  <h1 标签
```
<h1 id="xiaoming">  ///id 是标签的身份证 方便以后获取该标签的属性
```
### 
### 换行
```
<br>
例如：<a href="">订单</a><br>
```
### <div> 标签
```
<div class="page-header"></div>
快捷使用方法: div>page*3>a +Tab
```
### a标签
```
 <a href="/order">订单</a><br>
 点击事件： href 文件路径 /order
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
