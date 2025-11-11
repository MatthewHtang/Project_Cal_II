from flask import Flask, render_template, request

from Om import main as func1

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

    inp = request.form.get("input_int_by_trig")
    i = 0
    sin_power = "1"
    cos_power = "1"

    # print(inp)
    if "^" in inp:
        
        while i < len(inp):

            if inp[i] == "s" and "^" in inp[i:]:
                if inp[i+3] == " ":
                    i+=1 
                if inp[i+3] ==  "^" :
                    if inp[i+4] == " ":
                            i+=1
                    sin_power = inp[i+4]
                    i += 5
                    while i < len(inp) and ((inp[i] != "(") and (inp[i] != " ") and (inp[i]!="x")) :
                        sin_power += inp[i]
                        i += 1
                    continue


            if inp[i] == "c" and "^" in inp[i:] :
                if inp[i+3] == " ":
                    i+=1 
                if inp[i+3] ==  "^" :
                    if inp[i+4] == " ":
                            i+=1
                    cos_power = inp[i+4]
                    i += 5
                    while i < len(inp) and ((inp[i] != "(") and (inp[i] != " ") and (inp[i]!="x")) :
                        cos_power += inp[i]
                        i += 1
                    continue

            

            i+=1

    # print(sin_power, cos_power)

    res = func1.trig_ratios(int(sin_power), int(cos_power))
    # print(inh)
    return render_template("result.html", inp=inp, result=res)




if __name__ == "__main__":
    app.run(debug = True)

# run the program for sin ^301 x and 