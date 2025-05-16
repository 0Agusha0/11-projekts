from flask import Flask, render_template
 
app = Flask('app')
 
@app.route('/')
def index():
    return render_template('index.html')
 
@app.route('/spele')
def spele():
    return render_template('spele.html')
 
@app.route('/top')
def top():
    return render_template('top.html')
 
@app.route('/par')
def par():
    return render_template('par.html')
 
if __name__ == '__main__':
    app.run(debug=True)
