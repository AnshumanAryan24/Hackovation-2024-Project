import wikipedia
import PyPDF2
from flask import Flask,render_template, request, jsonify
from summarizer import Summarizer, TransformerSummarizer


app = Flask(__name__,template_folder="../frontend/html")

# -------------------------------- ROUTING --------------------------------
@app.route("/")
def init_app():
    global GPT2_model
    GPT2_model = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2-medium")
    return render_template('index.html')

@app.route("/flashcard.html")
def get_flashcard():
    return render_template('flashcard.html')

@app.route("/mathsolver.html")
def get_mathsolver():
    return render_template('mathsolver.html')

@app.route("/ppt.html")
def get_ppt():
    return render_template('ppt.html')

@app.route("/quiz.html")
def get_quiz():
    return render_template('quiz.html')

@app.route("/cheats.html")
def get_cheats():
    return render_template('cheats.html')

# -------------------------------- WIKIPEDIA --------------------------------
@app.route("/relateddesc")
def relateddesc():
    search_term = request.args.get('searchterm', default=1, type=str).replace(r'%20', r' ')
    return get_wikipedia_results(search_term=search_term, n_words=20)

def get_wikipedia_results(search_term: str, n_words: int = 100):
    if (n_words < 0):
        n_words = 100
    search_term = "_".join(search_term.split()) 
    res_dict = {term: wikipedia.summary(term)[0:n_words] for term in wikipedia.search(search_term) if len(term)!=0}
    return jsonify({'results':str(res_dict)})

# -------------------------------- PDF PARSER --------------------------------
@app.route("/pdfparse")
def get_pdftopics():
    pdf_path = request.args.get('pdfpath', default=1, type=str)
    reader = PyPDF2.PdfReader(pdf_path)

    pages = [page.extract_text() for page in reader.pages]
    full_content = ' '.join(pages).lower()
    full_content = full_content[full_content.index("module:1"):].split()
    content = ''
    for index, word in enumerate(full_content):
        if (word[0:-1] == "module:"):
            continue
        if (word.isnumeric() and ((index+1)<len(full_content) and full_content[index+1]=="hours")):
            continue
        content += word+' '

    content = content[0 : content.index("contemporary issues")]
    content = content.replace(' – ', '\n').replace(' - ', '\n').split('\n')
    content = [item for item in content if "proceedings of the" not in item]
    print('\n'.join(content))

    return jsonify({'content': content})
# def pdfparse():
#     pdf_path = request.args.get('pdfpath', default=1, type=str)
#     output_path = request.args.get('outputpath', default=1, type=str)
#     n_words = request.args.get('nwords', default=1, type=int)

#     topics = get_pdftopics(pdf_path)

#     GPT2_model = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2-medium")

#     flashcards = dict()

#     for topic in topics:
#         try:
#             flashcards[topic] = GPT2_model(' '.join(wikipedia.summary(term).split()), min_length = 10, max_length = 20)
#         except wikipedia.PageError:
#             continue

#     return flashcards


if __name__ == '__main__':
    app.run(debug=True, port=5000)