from flask import Flask
from flask import request
from flask import render_template
import sujmarkov, requests, random 
import secrets

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("my-form.html")

@app.route('/', methods=['POST'])
def my_form_post():
	# import pdb; pdb.set_trace()
	m = sujmarkov.Markov(n=2)
	link = request.form['text']
	clarifaiHeaders = {'Authorization': secrets.CLARIFAI_AUTH }
	clarifaiData = requests.get('https://api.clarifai.com/v1/tag/?url='+link, headers=clarifaiHeaders)
	clarifaiParse_data = clarifaiData.json()
	clarifaiClasses = clarifaiParse_data['results'][0]['result']['tag']['classes']

	print("passed clarifai")

	with open('corpus.txt') as f:
	    for line in f:
	        m.add(line.split())

	generatedTitle = []

	while len(generatedTitle)<8:
		generatedTitle = m.generate()

	number = random.randint(1, len(generatedTitle)-1)
	generatedTitle[number] = clarifaiClasses[0]	
	number = random.randint(1, len(generatedTitle)-1)
	generatedTitle[number] = clarifaiClasses[1]
	if len(generatedTitle) >= 10:
		number = random.randint(1, len(generatedTitle)-1)
		generatedTitle[number] = clarifaiClasses[2]

	return " ".join(generatedTitle)+"   "+link
    

if __name__ == '__main__':
	app.run()