import json

from flask import Flask, request
app = Flask(__name__)

import banco_brasil

@app.route("/")
def hello():
    return "nonono"

@app.route('/banco-brasil/pagamentos', methods=['GET', 'POST'])
def banco_brasil_pagamentos():
    if request.method == 'POST':
        try: 
            data = request.get_json()
            if not data:
                data = json.loads(request.data)
            return banco_brasil.processa_pagamentos(data)
        except:
            return 'error'

    else:
        return 'heyheyhey' 
