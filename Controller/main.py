import Model.model as model
import Model.inference_mamdani as inference_mamdani
import Model.fuzzy_operators as fuzzy_operators
from flask import Flask, jsonify, abort

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
    # TODO
    return jsonify("success"), 200

# повертає пароль для перевірки і зразу (user_id+username) (або якщо є бажання можна (user_id+username) окремим методом)
@app.route('/api/get-user-by-login/<user_id>', methods=['GET'])
def get_user_by_login():
    # TODO
    return jsonify("success"), 200

# user-result - це результат, який отримав користувач від нашої програми
# для зберігання - користувача, 3 вхідні зміннні, 2 вихідні число і слово
# напевно варто всі ці параметри через body оформити
@app.route('/api/save-user-result/<user_id>/<java_skill>/<english_skill>/<soft_skill>/<result_number>/<result_word>/date_time',
           methods=['POST'])
def save_user_result():
    # TODO
    return jsonify("success"), 200

@app.route('/api/get-user-results', methods=['GET'])
def get_user_results():
    # TODO
    return jsonify("success"), 200


if __name__ == '__main__':
    app.run(debug=True)





