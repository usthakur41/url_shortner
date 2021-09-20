# url_shortner

**Build Instructions:**
```
a) Clone this repo
b) cd ./src
c) docker build -t url_shortner:latest ./
```

**Run instructions:**

a) Run the url_shortner app in the container
`docker run -d -p 5000:5000  --name url_shortner_container url_shortner`
b) Access the API using curl command:
`curl -i -X POST "http://localhost:5000/url/test"`
```
[root@system src]# curl -i -X POST "http://localhost:5000/url/test"
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 69
Server: Werkzeug/1.0.1 Python/2.7.17
Date: Mon, 20 Sep 2021 08:25:33 GMT

{"body": "http://localhost:5000/g9wP", "msg": "Success", "error": ""}

[root@system src]# curl -i -X POST "http://localhost:5000/url/test"
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 69
Server: Werkzeug/1.0.1 Python/2.7.17
Date: Mon, 20 Sep 2021 08:25:39 GMT

{"body": "http://localhost:5000/g9wP", "msg": "Success", "error": ""}
```
