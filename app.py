from flask import Flask,render_template,request



app= Flask(__name__)
WORDS=[]
with open('large','r') as file:
    for line in file:
        WORDS.append(line.rstrip())


@app.route('/')
def index():
    x=request.args.get("x")
    return render_template("index.html",x=x)

@app.route('/search')
def search():
    q= request.args.get('q')
    words=[]
    for word in WORDS:
        if word.startswith(q):
            words.append(word)
    return render_template("search.html",q=words)
    #a=['aspect', 'alphas', 'alfanso', 'bravo','charlie']
