from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_heroku():
  return "Hello flask APP!"

if __name__ == '__main__':
  app.run(debug=True)