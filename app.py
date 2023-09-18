from flask import Flask, render_template, jsonify

app=Flask(__name__)

BUNNIES=[
    {'id': 1,
     'species': 'Holland Lop',
     'origin': 'Netherlands',
     'weight': '1.4 to 2'
    },
     {'id': 2,
     'species': 'Lionhead',
     'origin': 'USA',
     'weight': '1.1 to 1.7'
     },
     {'id': 3,
     'species': 'Dwarf Papillon',
     'origin': 'France',
     'weight': '1 to 1.9'
     },{'id': 4,
     'species': 'Pigmy rabbit',
     'origin': 'USA',
     'weight': '0.3 to 0.5'
     },
]

@app.route("/")
def index():
    return render_template('home.html',
                            bunnies=BUNNIES)

@app.route("/api/bunnies")
def list_people():
    return jsonify(BUNNIES)

if __name__ == "__main__":
    app.run(debug=True)