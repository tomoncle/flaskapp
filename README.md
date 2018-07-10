# Flask Application

* 拓展flask支持banner， 支持config.properties配置文件导入
* 模块化设计，支持数据库迁移
* 封装sqlalchemy数据库操作
* 自动转json
* 配置拦截器，异常自动解析(web请求返回错误页面，curl请求返回错误json)
* 拓展flask内置函数，支持环境变量
* 集成celery框架异步处理
* 支持docker构建
* flask jinja2模板示例
* swagger api文档配置
* 等等

# 模块结构图
        .

        .
        ├── banner.txt
        ├── bootstrap_app.py
        ├── bootstrap_celery.py
        ├── config.properties
        ├── config.py
        ├── Dockerfile
        ├── examples
        │   ├── extensions_flask_form.py
        │   ├── extensions_flask_SQLAlchemy.py
        │   ├── hello_world.py
        │   ├── index.py
        │   ├── __init__.py
        │   └── rest_api.py
        ├── flaskapp
        │   ├── common
        │   │   ├── error_view.py
        │   │   ├── exceptions.py
        │   │   ├── __init__.py
        │   │   ├── logger.py
        │   │   ├── response.py
        │   │   ├── tools.py
        │   │   └── utils.py
        │   ├── core
        │   │   ├── database.py
        │   │   ├── http_handler.py
        │   │   ├── http_interceptor.py
        │   │   └── __init__.py
        │   ├── extends
        │   │   ├── banner.py
        │   │   ├── functions.py
        │   │   └── __init__.py
        │   ├── __init__.py
        │   ├── models
        │   │   ├── base.py
        │   │   ├── clazz.py
        │   │   ├── __init__.py
        │   │   ├── school.py
        │   │   └── user.py
        │   ├── plugins
        │   │   ├── flask_celery.py
        │   │   └── __init__.py
        │   ├── services
        │   │   ├── base.py
        │   │   ├── __init__.py
        │   │   └── statement.py
        │   └── views
        │       ├── async_handler.py
        │       ├── error_handler.py
        │       ├── index_hander.py
        │       ├── __init__.py
        │       ├── rest_clazz_handler.py
        │       ├── rest_login_handler.py
        │       ├── rest_school_handler.py
        │       └── rest_user_handler.py
        ├── git-user-config.sh
        ├── README.md
        ├── requirements.txt
        ├── static
        │   ├── css
        │   │   └── layout.css
        │   ├── favicon.ico
        │   ├── images
        │   │   └── 0.jpg
        │   └── js
        │       └── app.js
        ├── stop-app.sh
        ├── templates
        │   ├── 404.html
        │   ├── examples
        │   │   ├── extensions_flask_form.html
        │   │   └── extensions_flask_sqlAlchemy.html
        │   ├── index.html
        │   └── layout.html
        └── test
            ├── config.properties
            ├── __init__.py
            ├── plugins
            │   ├── __init__.py
            │   └── test_celery_task.py
            ├── test_banner.py
            ├── test_celery.py
            ├── test_db.py
            ├── test_extend_func.py
            ├── test_lru.py
            ├── test_platform.py
            └── views
                └── test_school.py


# 数据库封装
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/5 20:52
# @Author  : TOM.LEE
# @File    : database.py
# @Software: PyCharm
from flaskapp import db
from ..common import ConsoleLogger, relative_path, MySQLDataError

__all__ = ['Persistence', 'Modify', 'Modify2', 'Remove', 'Query', 'Query2']

logger = ConsoleLogger(name=relative_path(__file__))


class Database(object):
    """
    database interface
    """


class Transactional(Database):
    def __init__(self, **kwargs):
        """
        事务层
        :param auto_commit: 是否自动提交
        """
        self._auto_commit = kwargs.get('auto_commit', True)
        self.model = kwargs.get('model_class')
        if not self.model:
            raise AssertionError('<class {}>: Required parameter model_class is not present.'
                                 .format(self.__class__.__name__))
        self.session = db.session
        # logger.info('init Transactional')

    def auto_commit(self):
        """
        是否自动提交事务
        :return:
        """
        if self._auto_commit:
            self.session.commit()

    def _check_type(self, obj):
        if not isinstance(obj, self.model):
            raise AssertionError('obj must be <class {}> type.'
                                 .format(self.model.__class__.__name__))


class Persistence(Transactional):
    def __init__(self, **kwargs):
        super(Persistence, self).__init__(**kwargs)
        # logger.info('init Persistence')
        

class Modify(Transactional):
    def __init__(self, **kwargs):
        super(Modify, self).__init__(**kwargs)
        # logger.info('init Modify')


class Remove(Transactional):
    def __init__(self, **kwargs):
        super(Remove, self).__init__(**kwargs)
        # logger.info('init Remove')


class Query(Database):
    def __init__(self, **kwargs):
        # logger.info('init Query')
        self.model = kwargs.get('model_class', None)
        if not self.model:
            raise AssertionError('<class {}>: model_class is not found.'
                                 .format(self.__class__.__name__))


class Modify2(Database):
    @classmethod
    def _auto_commit(cls):
        db.session.commit()


class Query2(Database):
    def __init__(self):
        """需要传入实体类型来使用该类"""
        # logger.info('init Query2')

```

# banner 配置
![图片描述][1]

# 接口浏览
![图片描述][2]

# 错误处理
* 页面请求：
![图片描述][3]
* curl请求：
![图片描述][4]

# 级联查询转json
![图片描述][5]

# 拓展flask启动方法start
```python
from flaskapp import app

if __name__ == "__main__":
    app.start()
    # app.start(port=5258, debug=False)
```
# 数据库更新迁移
```bash
$ python manager.py db init
$ python manager.py db migrate
```

# Dockerfile 构建
```bash
$ ./docker-build.sh
```
# celery异步处理
* 见项目test目录test_celery.py

# swagger配置
* 见项目examples目录swagger_for_api.py

# 更多信息见项目源码，希望对你有所帮助

## Authors
* [tomoncle](https://gitlab.com/tomoncle)
* 源码地址：https://gitlab.com/tomoncle/flaskapp


  [1]: https://img.mukewang.com/5b44c9d800017d6710510320.png
  [2]: https://img.mukewang.com/5b44c9fd0001c04c05120485.png
  [3]: https://img.mukewang.com/5b44ca6700010b0208470229.png
  [4]: https://img.mukewang.com/5b44cabb0001cf0909330121.png
  [5]: https://img.mukewang.com/5b44cb570001d28307850472.png
