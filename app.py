from flask import Flask, request, jsonify, session
from flask_session import Session
import config

app = Flask(__name__)
app.config.from_object(config)
Session(app)

@app.route('/start_game', methods=['POST'])
def start_game():
    username = request.json.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    
    if 'username' in session and session['username'] == username:
        return jsonify({
            "message": "Session already exists",
            "credits": session['credits']
        }), 200
    
    session['username'] = username
    session['credits'] = config.STARTING_CREDITS
    return jsonify({
        "message": "New session created",
        "credits": session['credits']
    }), 201

@app.route('/cash_out', methods=['POST'])
def cash_out():
    if 'username' not in session:
        return jsonify({"error": "No active session found"}), 404
    
    credits = session['credits']
    session.clear()
    
    return jsonify({
        "message": "Successfully cashed out",
        "credits": credits
    })

if __name__ == '__main__':
    app.run(debug=True)