from flask import Flask
app = Flask(__name__)
# Creation of basic Routes
@app.route("/")
def home():
    return "Hello World"

@app.route("/about")
def about():
    return "Welcome to about my Page"

@app.route("/contact")
def contact():
    return "Welcome to contact Page"
#Dyanmic routes
@app.route("/user/<name>")
def user(name):
    return f" Hello {name}"
#multiple Dyanmic Parameters
@app.route("/student/<name>/<course>")
def student(name,course):
    return f"  {name} is learning {course}"
if __name__ == "__main__":
    app.run(debug=True)