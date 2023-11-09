from flask import Flask, render_template, send_file, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/uk_cities.json')
def get_uk_cities():
    # Load and serve the 'uk_cities.json' file
    return send_file('static/uk_cities.json', as_attachment=True)


@app.route('/favicon.ico')
def favicon():
    return '', 204


if __name__ == '__main__':
    app.run(debug=True)
