from flask import Flask, render_template, url_for
import re
from string import digits

app = Flask(__name__)

def process_name(name):
    processed_name = re.sub(r'\d+', '', name).strip()

    if re.search(r'\d', name):
        table = str.maketrans('', '', digits)
        new_name = name.translate(table)
        return new_name.upper()
    else:
        
        if processed_name.isupper():
            return processed_name.lower()
       
        elif processed_name.islower():
            return processed_name.upper()
        
        else:
            return processed_name.capitalize()
        

@app.route('/<name>')
def greet(name):
    greeting_name = process_name(name)
    return f'Welcome, {greeting_name}, to my CSCB20 website!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)



