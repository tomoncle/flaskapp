# -*- encoding:utf-8 -*-
"""
default :  * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

"""

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(port=5001, debug=True)
