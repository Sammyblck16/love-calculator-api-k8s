from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to the Love Calculator API!"

@app.route('/calculate', methods=['POST'])
def calculate_love():
    data = request.get_json()
    name1 = data.get("name1", "")
    name2 = data.get("name2", "")

    names_combined = (name1 + name2).lower()

    true_count = sum(names_combined.count(c) for c in "true")
    love_count = sum(names_combined.count(c) for c in "love")

    score = int(f"{true_count}{love_count}")

    if score < 10 or score > 90:
        message = f"Your score is {score}, you go together like coke and mentos."
    elif 40 <= score <= 50:
        message = f"Your score is {score}, you are alright together."
    else:
        message = f"Your score is {score}."

    return jsonify({"score": score, "message": message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
