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

状态码：

```bash
[28/Feb/2020 19:06:10] "POST /accounts/login/ HTTP/1.1" 302 0
[28/Feb/2020 19:06:27] "GET /readinghub/category/non-fiction/recommend_book/Username HTTP/1.1" 301 0
[28/Feb/2020 19:11:56] "GET /static/images/eee7.jpg HTTP/1.1" 304 0
[28/Feb/2020 19:33:16] "GET /readinghub/profile/XianyuZhang/ HTTP/1.1" 200 12101
```

[`200 OK`](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status/200) 请求成功。成功的含义取决于HTTP方法：

- GET：资源已被提取并在消息正文中传输。
- HEAD：实体标头位于消息正文中。
- POST：描述动作结果的资源在消息体中传输。
- TRACE：消息正文包含服务器收到的请求消息

[`304 Not Modified`](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status/304) 如果客户端发送了一个带条件的 GET 请求且该请求已被允许，而文档的内容（自上次访问以来或者根据请求的条件）并没有改变，则服务器应当返回这个状态码。304 响应禁止包含消息体，因此始终以消息头后的第一个空行结尾。

[`301 Moved Permanently`](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status/301) 被请求的资源已永久移动到新位置，并且将来任何对此资源的引用都应该使用本响应返回的若干个 URI 之一。如果可能，拥有链接编辑功能的客户端应当自动把请求的地址修改为从服务器反馈回来的地址。除非额外指定，否则这个响应也是可缓存的。

[`302 Found`](https://developer.mozilla.org/zh-CN/docs/Web/HTTP/Status/302) 请求的资源现在临时从不同的 URI 响应请求。由于这样的重定向是临时的，客户端应当继续向原有地址发送以后的请求。只有在Cache-Control或Expires中进行了指定的情况下，这个响应才是可缓存的。

# 更新log:

## 2020.2.28 更新log：

将pip requirements更新。Django2 升级为 Django3，带来以下变化：

1. `python manage.py migrate`报错：ImportError: No module named 'django.core.urlresolvers'

> Django 2.0 removes the `django.core.urlresolvers` module, which was moved to `django.urls` in version 1.10. You should change any import to use [django.urls](https://docs.djangoproject.com/en/2.0/ref/urlresolvers/#django.urls.reverse) instead, like this:
>
> ```python
> from django.urls import reverse
> ```

2. `python manage.py runserver`报错：Django TemplateSyntaxError - 'static' is not a registered tag library

> `{% load static %}` and `{% load admin_static %}` were [deprecated in Django 2.1](https://docs.djangoproject.com/en/2.2/releases/2.1/#features-deprecated-in-2-1), and [removed in Django 3.0](https://docs.djangoproject.com/en/dev/releases/3.0/#features-removed-in-3-0).
>
> If you have any of the following in your template:
>
> ```py
> {% load static %}
> {% load static from static %}
> {% load admin_static %}
> ```
>
> You should replace the tag with simply:
>
> ```py
> {% load static %}
> ```

