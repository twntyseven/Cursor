from flask import Flask, render_template, request
from encrypt import encrypt

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
@app.route('/user_messages', methods=["GET", "POST"])
def user_message():
    if request.method == "POST":
        message = request.form['message']
        rotation = int(request.form['rotation'])
        encrypted_message = encrypt(message, rotation)
        return render_template('user_message.html', 
                             original_message=message,
                             encrypted_message=encrypted_message,
                             rotation=rotation)
    return render_template('user_message.html')

if __name__ == '__main__':
    app.run()

# Instructions for this project can be found here:
# https://education.launchcode.org/lchs/chapters/flask-intro/project.html
