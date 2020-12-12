from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

render_template

app = Flask(__name__)

poll = MongoClient('localhost', 27017)
db = poll.dbsparta


@app.route('/')
def home():
    return render_template('project.html')


@app.route('/poll', methods=['POST'])
def test_post():
    title_receive = request.form['title_give']
    print(title_receive)
    poll = {'title': title_receive}
    db.polls.insert_one(poll)
    return jsonify({'result': 'success', 'msg': '이 요청은 POST!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
