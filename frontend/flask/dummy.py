from flask import Flask,render_template, request, jsonify

app = Flask(__name__,template_folder="../")

@app.route("/")
def hello():
    return render_template('html/index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json() # retrieve the data sent from JavaScript

    # process the data using Python code
    result = data['value'] + " hello world"
    return jsonify(result=result) # return the result to JavaScript

if __name__ == '__main__':
    app.run(debug=True)
