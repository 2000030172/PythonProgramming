from flask import *
import sqlite3
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/add")
def add():
    return render_template("add.html")
@app.route("/view")
def view():
    conn=sqlite3.connect("feedback.db")
    conn.row_factory=sqlite3.Row
    cur=conn.cursor()
    cur.execute("select * from Feedback")
    rows=cur.fetchall()
    return render_template("view.html",rows=rows)
@app.route("/savedetails",methods=["POST","GET"])
def saveDetails():
    msg="msg"
    if request.method=="POST":
        try:
            email=request.form["email"]
            feedback=request.form["feedback"]
            with sqlite3.connect("feedback.db") as conn:
                cur=conn.cursor()
                cur.execute("INSERT into Feedback(email,feedback) values(?,?)",(email,feedback))
                conn.commit()
            msg="Employee successfully added"
        except:
            email=request.form["email"]
            if email=='admin@gmail.com':
                return render_template("view.html",msg=msg)
        else:
            conn.rollback()
            msg="We cannot add the employee to the list"
        finally:
            return render_template("success.html",msg=msg)
            conn.close()
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
