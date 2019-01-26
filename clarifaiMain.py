from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as C1Image
from os import listdir
from os.path import isfile, join
from twilio.rest import Client
import os

from flask import Flask, render_template, request
from werkzeug import secure_filename
app = Flask(__name__)

clarifai_app = ClarifaiApp(api_key='e30c5080088c4c998632632e5aa7b267')
model = clarifai_app.models.get('general-v1.3')

@app.route('/upload')
def upload_file():
    return render_template('index.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        gunactive = False
        f = request.files['file']
        image = C1Image(file_obj=open(f, 'rb'))
        results = model.predict([image])
        for concept in results['outputs'][0]['data']['concepts']:
            value = concept['value']
            name = concept['name']
            if value > 0.8:
                if name in gun_concepts:
                    print(concept['name'], value )
                    gunactive = True

        if gunactive == True:
            import twilio_code

        return 'file uploaded succesfully'

if __name__ == '__main__':
    app.run(debug = True)
