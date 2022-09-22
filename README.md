# Flask Application

[![Build Status](https://api.travis-ci.org/tomoncle/flaskapp.svg?branch=master)][travis]

* Python Version: 3.7
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

## Others

* 数据库更新迁移

```bash
$ flask db init
$ flask db migrate
```

* Dockerfile 构建

```bash
$ ./docker-build.sh
```

* celery异步处理
* swagger配置

## Authors

* [tomoncle](https://github.com/tomoncle)
* 源码地址：https://github.com/tomoncle/flaskapp

[travis]: https://travis-ci.org/tomoncle/flaskapp
