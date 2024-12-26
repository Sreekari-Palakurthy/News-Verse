from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Route for login page

@app.route('/login')
def login():
    return render_template('login.html')  # Correct path

# Route for Get News page
@app.route('/get-news')
def get_news():
    return render_template('get_news.html')  # Correct path

# Route for Upload page
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    return render_template('upload.html')  # Correct path

if __name__ == '__main__':
    app.run(debug=True)
