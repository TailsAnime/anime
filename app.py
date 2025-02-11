from flask import Flask, render_template

app = Flask(__name__, static_folder='static')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', phone_number="Ashutosh")

@app.route('/logout')
def logout():
    return "You have been logged out!"  # Replace with real logout logic

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

