from flask import Flask,render_template

app=Flask(__name__)



@app.route('/home')
def pk():
    return render_template("pk.html")


if(__name__=='__main__'):
    app.run(debug=True)
