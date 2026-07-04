from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<H1>Hello, World..!!</H1>"


if __name__ == "__main__":
    # host_ip='127.0.0.1'
    host_ip='192.168.1.65'
    host_port =8085
    app.run(host=host_ip, port=host_port)