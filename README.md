# soramitsu test task code

Simple python (flask) app to check current Moscow time via GET request
provided with Dockerfile to build image for this app

to run app locally:
```shell
pip install -r requirements.txt
python app.py
```

to build and run as docker container:
```shell
docker build -t time_app:latest .
docker run -d -p 80:80 --name time_app_1 time_app
```
(assuming you are in project root and port 80 is not allocated)

check time:
```
curl -X GET localhost
```
or
http://localhost
