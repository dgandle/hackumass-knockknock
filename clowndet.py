from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
app = ClarifaiApp("INUyp_yCjazrOaEHiOYUuj2z9IMn8NI02QLMtYpQ","o6lCyQZYokg84eRY-JzsdP3UK6MhOOyzXaUz2E-T")

url = 'https://upload.wikimedia.org/wikipedia/commons/e/e0/Clouds_over_the_Atlantic_Ocean.jpg'
model = app.models.get('general-v1.3')
image = ClImage(url=url) 

app._parse_response(model.predict([image]))


