# Flask Application

## Code Structure

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


## Authors
* [tomoncle](https://gitlab.com/tomoncle)