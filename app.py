from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/details')
def details():
    src = request.args.get("src")
    description = request.args.get("description")
    additionalDescription = request.args.get("additionalDescription")

    return render_template('details.html', src=src, description=description, additionalDescription=additionalDescription)

if __name__ == '__main__':
    app.run(debug=True)
