from flask import Flask, render_template, request



app = Flask(__name__)

@app.route('/')
def home():

    return render_template('index.html')
    return ("This is homepage.")

@app.route('/check', methods = ['POST'])

def check():

    inp = request.form.get("user_input")

    return render_template("process.html", inp = inp)

@app.route('/IntByParts', methods = ['POST'])
def intbyparts():
    u = request.form.get("u")
    dv = request.form.get("dv")


    return u + "  " + dv


@app.route('/IntByTrig' , methods = ["POST"])
def intbytrig():

    inh = request.form.get("input_int_by_trig")
    # print(inh)
    return  inh


if __name__ == "__main__":
    app.run(debug = True)