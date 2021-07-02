# app.py
from flask import Flask, jsonify, request, render_template
import os
app = Flask(__name__)

######## HOME ############
@app.route('/')
def test_page():
    return render_template('index.html')

# run app
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)