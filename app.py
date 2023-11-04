from flask import Flask

app = Flask(__name__)
app.secret_key = "mys3cr3tk3y"

@app.route('/')
def index():
    return "hello world from Gonzalo Rodriguez"

if __name__ == '__main__':
    app.run(port=7000, host="0.0.0.0",debug=True)
