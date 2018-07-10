#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time           : 18-7-5 下午5:57
# @Author         : Tom.Lee
# @File           : swagger_for_api.py
# @Product        : PyCharm
# @Docs           : 
# @Source         : 

from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """
    This is the summary defined in yaml file
    First line is the summary
    All following lines until the hyphens is added to description
    the format of the first lines until 3 hyphens will be not yaml compliant
    but everything below the 3 hyphens should be.
    ---
    tags:
      - users
    parameters:
      - in: query
        default: tom
        name: username
        type: string
        required: true
      - in: header
        default: 123abc
        name: token
        type: string
        required: true
    responses:
      200:
        description: A json format data
        schema:
          id: response_info
          properties:
            code:
              type: integer
              description: http response code
              default: 200
            path:
              type: string
              description: request url path
              default: 'http://localhost:5000/'
            args:
              type: string
              description: request parameters
              default: '{}'
            headers:
              type: string
              description: request headers
              default: '{}'
    """
    return jsonify({
        'code': 200,
        'path': request.url_root,
        'args': dict(request.args),
        'headers': dict(request.headers),
    })


if __name__ == '__main__':
    """
    curl http://localhost:5001/apidocs/
    """
    from flasgger import Swagger

    swag = Swagger(app)
    app.run(debug=True, port=5001)
