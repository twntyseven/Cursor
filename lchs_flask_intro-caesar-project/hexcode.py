from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

def valid_hex_code(hex_code):
    for char in range(hex_code):
        if char.isdigit() or char.upper() in 'ABCDEF':
            return True

        else:
            return False;

# Code the 'valid_hex_chars' function here:

@app.route('/hex_form', methods=["GET", "POST"])
def hex_form():    
    if request.method == 'POST':
        hex = request.form['hex']
        hex_length = len(hex)
        if(valid_hex_code(hex)):
            feedback = "Successful submission!"

        else:
            hex = '00FF00'
            feedback = "Incorrect Hexcode!"
    else:
        hex = '00FF00'
        feedback = 'hi'

    return render_template('hex_form.html', hex = hex, feedback = feedback)

if __name__ == '__main__':
    app.run()

# Find the exercise instructions here:
# https://education.launchcode.org/lchs/chapters/flask-intro/exercises.html
