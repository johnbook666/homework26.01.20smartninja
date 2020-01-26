from flask import Flask, render_template

app = Flask(__name__)

bond_list_craig = ["2006 Casino Royal", "2008 Quantum of solace", "2012 Skyfall", "2015 Spectre", "2020 no time to die"]
bond_list_brosnan = ["1995 Goldeneye", "1997 tomorrow never dies", "1999 the world is not enough", "2002 die another day"]
bond_list_dalton = ["1987 the living daylights", "1989 licence to kill"]


@app.route("/")
def homework_main():
    return render_template("homework_main.html")

@app.route("/craig")
def craig():
    return render_template("craig.html", posts1=bond_list_craig)

@app.route("/brosnan")
def brosnan():
    return render_template("brosnan.html", posts2=bond_list_brosnan)

@app.route("/dalton")
def dalton():
    return render_template("dalton.html", posts3=bond_list_dalton)


if __name__ == '__main__':
    app.run()