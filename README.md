```shell
# conda

# 全环境 生成
pip3 freeze > requirements.txt
# 根据项目 生成
pip3 install pipreqs
pipreqs ./ --encoding=utf-8 --force
# 安装
pip3 install -r requirements.txt

# 运行
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
uvicorn main:app --host 0.0.0.0 --port 80

# 后台运行
nohup uvicorn main:app --host 0.0.0.0 --port 8000 &
ps aux | grep uvicorn
kill <PID>

# API DOCpi
/docs

# dev
pip install "fastapi[all]"
pip3 install "fastapi[all]"

# prod
pip install fastapi
pip3 install fastapi

pip install "uvicorn[standard]"
pip3 install "uvicorn[standard]"

uvicorn main:app --reload
```
```text
# 请求类型
@app.get()
@app.post()
@app.put()
@app.delete()
@app.options()
@app.head()
@app.patch()
@app.trace()
# 路由，同路由命名下，动态参数路由应当在最后
@app.post("/")
@app.post("/url")
@app.post("/url/{id}")
# None 可选参数下的默认值，不写默认值则必传
@app.post("/url/")
```

|                                                                         |
|-------------------------------------------------------------------------|
| [三方库](https://github.com/vinta/awesome-python)                          |
| [算法](https://github.com/TheAlgorithms/Python)                           |
| [算法](https://github.com/tensorflow/tensorflow)                          |
| [系统设计](https://github.com/donnemartin/system-design-primer/tree/master) |

###### book
FastAPI Web开发入门、进阶与实战
Python FastAPI Web开发从入门到项目实战
利用FastAPI构建Python微服务

https://gitee.com/xiaozhong1988/fastapi_tutorial

| https://github.com/mjhea0/awesome-fastapi                                             |
|---------------------------------------------------------------------------------------|
| [full-stack-fastapi-template](https://github.com/fastapi/full-stack-fastapi-template) |
| [ai jina](https://github.com/jina-ai/jina)                                            |
| []()                                                                                  |
