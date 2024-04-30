from flask import Flask, render_template, request
import requests
import cohere  

app = Flask(__name__)
cohere_api_key = '---'
cohere_api_url = 'https://api.cohere.ai/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_content():
    prompt = request.form['prompt']
    co = cohere.Client(cohere_api_key)
    response = co.generate(  
    model='command-nightly',  
        prompt = prompt,  
    max_tokens=100,  
    temperature=0.750)

    generated_content = response.generations[0].text
    return render_template('index.html', generated_content=generated_content)




if __name__ == '__main__':
    app.run(debug=True)
