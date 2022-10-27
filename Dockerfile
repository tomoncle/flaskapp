FROM tomoncle/python3.10
MAINTAINER tomoncle <tomoncle@sina.com>

WORKDIR /workspace
ADD ./ /workspace/flaskapp
RUN apk update
RUN pip install -r /workspace/flaskapp/requirements.txt

EXPOSE 5000
CMD ["python", "/workspace/flaskapp/bootstrap_app.py"]
