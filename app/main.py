import sujmarkov, requests, random
m = sujmarkov.Markov(n=2)



clarifaiHeaders = {'Authorization': 'Bearer MJaTQDJBZdYZQwuIg12A9bNuWCEo2L'}
clarifaiData = requests.get('https://api.clarifai.com/v1/tag/?url=http://www.clarifai.com/img/metro-north.jpg',  headers=clarifaiHeaders)
clarifaiParse_data = clarifaiData.json()
clarifaiClasses = clarifaiParse_data['results'][0]['result']['tag']['classes']


with open('corpus.txt') as f:
    for line in f:
        m.add(line.split())

generatedTitle = m.generate()


number = random.randint(1, len(generatedTitle)-1)
generatedTitle[number] = clarifaiClasses[0]
if len(generatedTitle) >= 5:
	number = random.randint(1, len(generatedTitle)-1)
	generatedTitle[number] = clarifaiClasses[1]
if len(generatedTitle) >= 10:
	number = random.randint(1, len(generatedTitle)-1)
	generatedTitle[number] = clarifaiClasses[2]



print(" ".join(generatedTitle))