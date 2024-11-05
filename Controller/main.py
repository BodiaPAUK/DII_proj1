import Model.model as model
import Model.inference_mamdani as inference_mamdani
import Model.fuzzy_operators as fuzzy_operators
from flask import Flask, jsonify, abort, request
import dataBase.db_access as db_access

app = Flask(__name__)

inference_mamdani.preprocessing(model.input_lvs, model.output_lv)

'''crisp = [23, 55, 45]

inference_mamdani.preprocessing(model.input_lvs, model.output_lv)
result = inference_mamdani.process(model.input_lvs, model.output_lv, model.rule_base, crisp)
print(result)

for lv in model.input_lvs:
    fuzzy_operators.draw_lv(lv)
fuzzy_operators.draw_lv(model.output_lv)'''

@app.route('/api/calculate-skill-level/<java_skill>/<english_skill>/<soft_skill>', methods=['GET'])
def calculate_skill_level(java_skill, english_skill, soft_skill):
    try:
        java_skill = int(java_skill)
        english_skill = int(english_skill)
        soft_skill = int(soft_skill)
    except ValueError:
        return jsonify({"error": "all parameters must be integers"}), 400

    # Перевіряємо, чи параметри у відповідних діапазонах
    if java_skill < 0 or java_skill > 25:
        return jsonify({"error": "java_skill is out of the range [0;25]"}), 400
    if english_skill < 0 or english_skill > 60:
        return jsonify({"error": "english_skill is out of the range [0;60]"}), 400
    if soft_skill < 0 or soft_skill > 50:
        return jsonify({"error": "soft_skill is out of the range [0;50]"}), 400

    crisp = [java_skill, english_skill, soft_skill]
    result = inference_mamdani.process(model.input_lvs, model.output_lv, model.rule_base, crisp)
    return jsonify(result), 200


# Взаємодія з БД
# TODO
@app.route('/api/save-user', methods=['POST'])
def save_user():
    data = request.get_json()
    username = data.get('username')
    login = data.get('login')
    password = data.get('password')

    if not username or not login or not password:
        abort(400, description="Missing fields")

    db_access.save_user(username, login, password)
    return jsonify("User saved successfully"), 200


@app.route('/api/get-user-by-login/<login>', methods=['GET'])
def get_user_by_login(login):
    user = db_access.get_user_by_login(login)
    if not user:
        abort(404, description="User not found")
    return jsonify({"user_id": user[0], "username": user[1], "password": user[2]}), 200


@app.route('/api/save-user-result', methods=['POST'])
def save_user_result():
    data = request.get_json()
    user_id = data.get('user_id')
    java_skill = data.get('java_skill')
    english_skill = data.get('english_skill')
    soft_skill = data.get('soft_skill')
    result_number = data.get('result_number')
    result_word = data.get('result_word')

    if not all([user_id, java_skill, english_skill, soft_skill, result_number, result_word]):
        abort(400, description="Missing fields")

    db_access.save_user_result(user_id, java_skill, english_skill, soft_skill, result_number, result_word)
    return jsonify("Result saved successfully"), 200


@app.route('/api/get-user-results/<user_id>', methods=['GET'])
def get_user_results(user_id):
    results = db_access.get_user_results(user_id)
    return jsonify(results), 200


if __name__ == '__main__':
    app.run(debug=True)


