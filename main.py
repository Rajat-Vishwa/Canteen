from flask import *

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('homepage.html')

if __name__ == '__main__':
    app.run(debug=True)