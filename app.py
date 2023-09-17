from flask import Flask, render_template, jsonify

app=Flask(__name__)

PEOPLE=[
    {'id': 1,
     'name': 'Bela',
     'age': 27,
     'nationality': 'brazilian'
     },
     {'id': 2,
     'name': 'Maria',
     'age': 26,
     'nationality': 'russian'
     },
     {'id': 3,
     'name': 'Carlos',
     'age': 32,
     'nationality': 'mexican'
     },
     {'id': 4,
     'name': 'Anne',
     'age': 31,
     'nationality': 'swedish'
     },
]

@app.route("/")
def index():
    return render_template('home.html',
                            people=PEOPLE)

@app.route("/api/people")
def list_people():
    return jsonify(PEOPLE)

if __name__ == "__main__":
    app.run(debug=True)