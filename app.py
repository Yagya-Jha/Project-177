from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

templates = [
    {
        "inputs": 5,
        "category": "Board Game",
        "word": "Chess"
    },
    {
        "inputs": 6,
        "category": "European Country Name",
        "word": "France"
    },
    {
        "inputs": 5,
        "category": "What You Say When You Pick Up Call",
        "word": "Hello"
    },
    {
        "inputs": 8,
        "category": "World's Oldest Language",
        "word": "Sanskrit"
    },
    {
        "inputs": 5,
        "category": "Country which never Becane a colony",
        "word": "Nepal"
    },
    {
        "inputs": 4,
        "category": "Song which every child knows",
        "word": "ABCD"
    },
    {
        "inputs": 5,
        "category": "What fell on newton's head",
        "word": "Apple"
    }
    
    

]

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/get-template")
def get_template():
  return jsonify({
        "status": "success",
        "word": random.choice(templates)
  })

if __name__ == '__main__':
  app.run()
