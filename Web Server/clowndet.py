import subprocess
from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
app = ClarifaiApp("INUyp_yCjazrOaEHiOYUuj2z9IMn8NI02QLMtYpQ","o6lCyQZYokg84eRY-JzsdP3UK6MhOOyzXaUz2E-T")

ronald = '/home/pi/hackumass-knockknock/Web Server/static/image.jpg'
model = app.models.get('general-v1.3')
image = ClImage(file_obj=open(ronald,'rb'))
print model.predict([image])

