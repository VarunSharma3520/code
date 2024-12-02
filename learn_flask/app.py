from flask import Flask, request,render_template

app = Flask(__name__)

@app.route("/",methods=["GET","POST","DELETE"])
def hello_world():
    if request.method=="POST":
        return "ha bhai sab maje ma"
    elif request.method == "DELETE":
        return "delete method called on delete route(/)"
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5000,debug=True)
