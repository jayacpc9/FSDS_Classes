from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<H1> Hello, Harsha..!!</H1>"


if __name__ == "__main__":
    # host_ip='127.0.0.1' # localhost
    # host_ip='192.168.1.65' # or provide 0.0.0.0 so that it uses both local host and ip address
    host_ip='0.0.0.0'
    host_port =8085
    app.run(host=host_ip, port=host_port, debug=True)