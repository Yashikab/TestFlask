from flask import Flask, request, jsonify, abort
import os
app = Flask(__name__)


@app.route("/")
def show_page():
    name = os.environ['TEST']
    return name


@app.route('/testget')
def testget():
    # prid = prudct id
    name = request.args.get('prid')
    if name.isdecimal():
        return_msg = jsonify(
            {
                'prid': int(name),
                'data': 'test'
            }
        )

    else:
        abort(400, 'Key Error (key must be integer)')

    return return_msg


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
