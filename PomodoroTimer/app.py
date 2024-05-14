from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_timer', methods=['POST'])
def start_timer():
    # Implement the logic for starting the timer
    return jsonify({"status": "started"})

@app.route('/pause_timer', methods=['POST'])
def pause_timer():
    # Implement the logic for pausing the timer
    return jsonify({"status": "paused"})

@app.route('/reset_timer', methods=['POST'])
def reset_timer():
    # Implement the logic for resetting the timer
    return jsonify({"status": "reset", "time": "25:00"})

if __name__ == '__main__':
    app.run(debug=True)
