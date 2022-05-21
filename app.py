from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/flutterProjects")
def flutter():
    return render_template("FlutterProjects.html")

@app.route("/pythonProjects")
def python():
    return render_template("pyprojects.html")

if __name__ == "__main__":
    app.run(debug=True)