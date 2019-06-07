from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html",times=4)

@app.route('/<x>') 
def mult(x):
    num=int(x)
    return render_template("index.html",times=num)

if __name__=="__main__":
    app.run(debug=True)
