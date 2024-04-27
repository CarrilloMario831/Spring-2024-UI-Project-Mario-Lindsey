from flask import Flask
from flask import render_template
from flask import Response, request, jsonify, Markup
app = Flask(__name__)

# ROUTES
@app.route('/')
def homepage():
   return render_template('homepage.html')

@app.route('/learn/1')
def learn():
   return render_template('learn.html')

@app.route('/quiz/1')
def quiz():
   return render_template('quiz.html')

@app.route('/map')
def map():
   return render_template('mapTEST.html')

if __name__ == '__main__':
   app.run(debug = True)