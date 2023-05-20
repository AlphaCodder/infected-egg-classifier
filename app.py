import json
import pickle
from flask import Flask, request, render_template
import pandas as pd
import numpy as np
from featureExtraction import feature_extraction

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # process the uploaded file
        file = request.files['image']
        # save the file to ./uploads
        file.save('uploads/' + file.filename)
        # call the feature extraction method
        features = feature_extraction(file.filename)

        model = pickle.load(open('model.pkl', 'rb'))

        # pass the extracted features to the model
        result = json.dumps(model.predict(features).tolist())

        if result == '[0]':
            result = 'Monezia'
        else:
            result = 'Stongstyles'


        return render_template('results.html', prediction=result)
        
    else:
        # Show the upload form
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
