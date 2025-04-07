from flask import Flask, render_template, request
import random

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route('/')
@app.route('/hello')
def hello():
   page = """
      <h1>Here's a random number: {0}</h1>
      <form>
         <button>New Number</button>
      </form>
   """
   num = random.randint(1, 25)
   return page.format(num)
@app.route('/goodbye')
def goodbye():
   message = "<h2>This is the second page!</h2>"
   return message
@app.route('/third_page')
def third_page():
   message = "<h2>This is the third page!</h2>"
   return message

@app.route('/form')
def form():
   return render_template("favorite_form.html")

@app.route('/results', methods=["POST"])
def results():
   color_choice = request.form['color']
   number_choice = request.form['luck_num']
   class_choice = request.form['fav_class']
   movie_choice = request.form['best_pix']
   return render_template("form_results.html", color = color_choice, lucky_number = number_choice, fav_class = class_choice, best_pix = movie_choice)

@app.route('/thanks')
def thanks():
   thing = "bomb"
   person = "Bob"
   action = "dancing"
   activity = "person"
   return render_template("tynote.html", name = person, verb = action, gift = thing, noun = activity)

if __name__ == '__main__':
   app.run()