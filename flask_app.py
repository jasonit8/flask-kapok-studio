from flask import Flask,render_template

app = Flask(__name__)

items = [['information','monalisa.png'],['games','cards.png'],['contact','textbox.png']]

@app.route('/')
def home(items=items):
    render = render_template(template_name_or_list='index.html',items=items)
    return render

@app.route('/page')
def page():
    return '<a href="/">return</a>'

app.run()