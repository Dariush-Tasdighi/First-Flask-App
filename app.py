"""First App"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """First (Default) Action"""

    # return "Hello, World!"
    return "<h1>Hello, World!</h1>"

def main():
    """Main Function"""

    # app.run(host="192.168.2.3")
    # app.run(host="127.0.0.1") # Local Host
    # app.run(host="0.0.0.0") # Both
    # app.run(host="0.0.0.0", debug=True) # Default Port: 5000
    app.run(host="0.0.0.0", port=5555, debug=False)

if __name__ == '__main__':
    main()
