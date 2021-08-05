from flask import Flask,render_template,request,redirect
import csv
app=Flask(__name__)



@app.route('/')
def my_home():
    return render_template("index.html")
@app.route('/<string:page>')
def pages(page):
    return render_template(page)

@app.route('/submit_form',methods=["POST","GET"])
def login():
    if request.method=="POST":
        data=request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
    else:
        return "Something went wrong"

def write_to_csv(data):
    with open("database.csv",mode="a",newline='') as database:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer=csv.writer(database,delimiter=",",quotechar='"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])
#@app.route('/works.html')
#def my_works():
#    return render_template("works.html")

#@app.route('/contact.html')
#def my_contact():
#    return render_template("contact.html")
#@app.route('/about.html')
#def my_about():
#    return render_template("about.html")

