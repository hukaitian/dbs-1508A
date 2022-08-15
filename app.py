from flask import Flask, render_template, request
app = Flask(__name__)
import joblib

# @app.route("/", methods = ["GET","POST"])
# def index():
#     if request.method == "POST":
#         rates = float(request.form.get("rates"))
#         #print(rates)
#         # model1 = joblib.load("regression_DBS")
#         # r1 = model1.predict([[rates]])
#         # model2 = joblib.load('tree_DBS')
#         # r2 = model2.predict([[rates]]) 
#         #return (render_template("index.html",result1 = r1, result2 = r2))
#         return (render_template("index.html",result1 = 'TEMP', result2 = 'TEMP'))
#     else:
#         return (render_template("index.html",result1 = "waiting", result2 = "waiting"))

@app.route("/",methods=['GET','POST'])
def index():
    if request.method=='POST':
        rates=float(request.form.get('rates'))
        model1=joblib.load('regression_DBS')
        r1=model1.predict([[rates]])
        
        model2=joblib.load('regression_Tree')
        r2=model2.predict([[rates]])
        return(render_template("index.html",result1=r1,result2=r2))
    else:
        return(render_template("index.html",result1="waiting",result2="waiting"))

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=int('1111'))
