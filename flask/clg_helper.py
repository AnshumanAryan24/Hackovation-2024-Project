import wikipedia

from flask import Flask,render_template, request, jsonify


app = Flask(__name__,template_folder="../frontend/html")

@app.route("/")
def init_app():
    return render_template('index.html')

# ------------------------------------------------------
# WIKIPEDIA

@app.route("/relateddesc")
def relateddesc():
    search_term = request.args.get('searchterm', default=1, type=str).replace(r'%20', r' ')
    
    print()
    print("--------------------------------")
    print(search_term)
    print("--------------------------------")
    print()

    return get_wikipedia_results(search_term=search_term, n_words=20)

def get_wikipedia_results(search_term: str, n_words: int = 100):
    if (n_words < 0):
        n_words = 100
    search_term = "_".join(search_term.split()) 
    res_dict = {term: wikipedia.summary(term)[0:n_words] for term in wikipedia.search(search_term) if len(term)!=0}
    return jsonify({'results':str(res_dict)})


if __name__ == '__main__':
    app.run(debug=True, port=5000)