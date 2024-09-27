from PyPDF2 import PdfReader
from flask import Flask, jsonify, request 
app = Flask(__name__)
@app.route('/pdfparsingtool', methods=['GET'])
def parse():
  PATH = request.args.get('number', default=1, type=str)
  reader = PdfReader(PATH)
  return jsonify({'pages': [page.extract_text() for page in reader.pages()]})
# meta = reader.metadata
# print("Total Pages: ", len(reader.pages))
# # All of the following could be None!
# print("Author: ", meta.author)
# print("Creator: ", meta.creator)
# print("Producer: ", meta.producer)
# print("Subject: ", meta.subject)
# print("Title: ", meta.title)

if __name__ == '__main__':
    app.run(debug=False)