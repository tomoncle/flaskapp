FROM tomoncle/python27:alpine.latest
MAINTAINER Tom.Lee <1123431949@qq.com>

WORKDIR /workspace
ADD ./ /workspace/flaskapp

RUN pip install -r /workspace/flaskapp/requirements.txt

EXPOSE 5000
CMD ["python", "/workspace/flaskapp/bootstrap_app.py"]