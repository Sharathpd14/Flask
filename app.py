from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)


@app.route("/")
def welcome():
    return "<html><h1>Welcome to this page. This is an amazing page</h1></html>"


@app.route("/index",methods = ['GET'])
def index():
    return render_template("index.html")

@app.route("/form",methods = ['GET','POST'])
def form():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['phone']
        return f"Hello <h1>{name},</h1> your email address is {email} and mobile number is {mobile}"
    return render_template("form.html")

@app.route("/submit1",methods = ['GET','POST'])
def submit1():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['phone']
        return f"Hello <h1>{name},</h1> your email address is {email} and mobile number is {mobile}"
    return render_template("form.html")


@app.route('/success/<int:score>')
def success(score):
    res = " "
    if score > 40:
        res = "Pass" 
    else:
        res = "Fail"   
    return render_template('result.html',result = res)

@app.route('/successres/<int:score>')
def successres(score):
    res = " "
    if score > 40:
        res = "Pass" 
    else:
        res = "Fail" 
        
    exp = {"score":score,"res":res}  
    return render_template('result1.html',result = exp)

@app.route('/submit' ,methods=["GET","POST"])
def submit():
    total_score = 0
    if request.method == "POST":
        sub1 = float(request.form['subject1'])
        sub2 = float(request.form['subject2'])
        sub3 = float(request.form['subject3'])
        sub4 = float(request.form['subject4'])
        
        total_score = (sub1+sub2+sub3+sub4)/4
    else:
        render_template('form1.html')
    
    return redirect(url_for("successres",score = total_score))
    
    


if __name__ == "__main__":
    app.run(debug=True)