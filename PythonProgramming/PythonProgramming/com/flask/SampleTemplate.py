from flask import Flask ,render_template
app = Flask(__name__,template_folder ="templates")

@app.route("/welcome")
def welcome():
    return "<H1>Welcome page</H1>"


@app.route("/")
def index():
    my_value = "my value param is printed"
    my_result = 10 + 20
    # return render_template('index.html')
    return render_template("index.html", myvalue=my_value, myresult=my_result)

if __name__ =="__main__":
    app.run(host = '0.0.0.0', port=8086)

