from flask import Flask, request
from flask_talisman import Talisman

app = Flask(__name__)
Talisman(app)

@app.route('/')
def index():
    return "Hello Https"

@app.route('/record')
def record():
    return "true"


# @app.before_request
# def before_request():
#     if not request.is_secure:
#         print('http重定向')
#         url = request.url.replace('http://', 'https://', 1)
#         return redirect(url, code=301)
#     else:
#         print('https流量')

if __name__ == '__main__':
    # app.run(ssl_context='adhoc')
    app.run(debug=True,
     host='0.0.0.0',
     ssl_context=(
        "./server.crt",
        "./server.key")
    )