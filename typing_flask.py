from flask import Flask,render_template,request
import random as rd
import paragraphs as pg
from model import main_class
from time import *

mc = main_class()
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])

def typetest():
    random_paragraph = rd.choice(pg.list_of_paragraph)
    user_test = request.form.get('fronttest')
    mistake_total = mc.mistake_count(random_paragraph,user_test)

    return render_template('main.html',mistake_total=mistake_total,random_paragraph=random_paragraph,len_of_original=len(random_paragraph))

if __name__ == '__main__':
    app.run(debug=True)