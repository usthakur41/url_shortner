# url_shortner

**Build Instructions:**
```
a) Clone this repo
b) cd ./src
c) python3 init_db.py
d) docker build -t url_shortner:latest ./
```

**Run instructions:**

a) Run the url_shortner app in the container
`docker run -d -p 5000:5000  --name url_shortner_container url_shortner`

b) Access the API using curl command:
```
[root@thakur1 src]# curl -i -X POST "http://localhost:5000/url" -H 'Content-Type: application/json' -d '{"url":"https://github.com/usthakur41/url_shortner/blob/main/README.md"}'
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 74
Server: Werkzeug/2.0.1 Python/3.6.8
Date: Mon, 20 Sep 2021 10:04:02 GMT

{"short_url": "http://localhost:5000/z9jO", "error": "", "msg": "Success"}[root@thakur1 src]#
[root@thakur1 src]#
[root@thakur1 src]#
[root@thakur1 src]# curl -i -X POST "http://localhost:5000/url" -H 'Content-Type: application/json' -d '{"url":"https://github.com/usthakur41/url_shortner/blob/main/README.md"}'
HTTP/1.0 200 OK
Content-Type: text/html; charset=utf-8
Content-Length: 74
Server: Werkzeug/2.0.1 Python/3.6.8
Date: Mon, 20 Sep 2021 10:04:07 GMT

{"short_url": "http://localhost:5000/z9jO", "error": "", "msg": "Success"}[root@thakur1 src]#
[root@thakur1 src]#
[root@thakur1 src]#

```
