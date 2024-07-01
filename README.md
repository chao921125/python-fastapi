```shell
uvicorn main:app --reload

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