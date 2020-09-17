from flask import Flask, render_template


app = Flask(__name__)
app.config["SECRET_KEY"] = 'theXyz'

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/dna', methods=['POST'])
def dna():
      dna_seq = request.form['dna_seq'])
        #<your code for dna seq generation>
       #return render_template(<page.html>)

    
if __name__ == "__main__":
    app.config["DEBUG"] = True
    app.run()
