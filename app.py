from flask import Flask, render_template

# Initialization
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/run-script')
def run_script():
    # Your Python script execution logic goes here
    # For demonstration purposes, I'll just print a message
    print("Python script executed!")
    return "Script executed"


if __name__ == "__main__":
    app.run(debug=True)

# app we are running for flask
# considering these changes for existing 
# winow we are creating 