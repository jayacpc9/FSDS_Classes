from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<H1>Hello world example</H1>"


# to use the below method using the url as follows
# http://192.168.1.65:8086/hello
@app.route("/hello")
def hello():
    return "<H1>Using Route for Hello World</H1>"

# to use the below method using the url as follows
# http://192.168.1.65:8086/greet/jaya
# out put will be Hello! Jaya
@app.route("/greet/<name>")
def greet(name):
    return f"<H1>Hello! {name}</H1>"

# method to return multiplication tables
# accepts integers num1 and num2 and prints the multiplication tales
# if <int: num1> data type is not specified, it will consider it as string.
@app.route("/multiply/<int:num1>/<int:num2>")
def multiplication(num1, num2):
    print("num1,num2 : ",num1,",",num2)
    multiplication_tables=f"<H1>Multiplication Tables of number {num1} upto times {num2}</H1><P><P>"
    for i in range(1, num2 + 1):      
       multiplication_tables+= f"<H1>{num1} * {i} = {i*num1}</H1><P>"
    #    print(multiplication_tables)
    return multiplication_tables

# to return an error code use curl command in terminal
# curl -I http://127.0.0.1:8086/geterror
@app.route("/geterror")
def showerror():
    return "<H1>Showing Error</H1>", 404

if __name__ =="__main__":
    app.run(host = '0.0.0.0', port=8086)

