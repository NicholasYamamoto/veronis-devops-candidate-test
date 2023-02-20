from flask import Flask, Response

app = Flask(__name__)

# Creating 2 endpoints for /test1 and /test2 that return different status codes
@app.route("/test1")
def test_1():
    status_code = Response(status=200)
    return status_code

@app.route("/test2")
def test_2():
    status_code = Response(status=201)
    return status_code

if __name__ == '__main__':
    app.run(port=8080)