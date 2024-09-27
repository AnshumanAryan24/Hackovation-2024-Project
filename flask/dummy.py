import wikipedia
from flask import Flask,render_template, request, jsonify


app = Flask(__name__,template_folder="./frontend/html/")

@app.route("/")
def init_app():
    return render_template('index.html')

# ------------------------------------------------------
# WIKIPEDIA

@app.route("/relateddesc", method=["POST"])
def relateddesc(search_term: str, n_words: int = 100):
    if (n_words < 0):
        n_words = 100
    search_term = "_".join(search_term.split())    
    res_dict = {term: wikipedia.summary()[0:n_words] for term in wikipedia.search(search_term)}
    return jsonify(res_dict)


if __name__ == '__main__':
    app.run(debug=True)
