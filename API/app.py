from PIL import Image
from flask import Flask, request
import numpy as np
from status import *
from back_end import classify
from matplotlib import pyplot as plt
from flask_cors import CORS
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from views import *
from apispec_webframeworks.flask import FlaskPlugin
from flask_swagger_ui import get_swaggerui_blueprint
import json

# Swagger API Docs Auto generation
spec = APISpec(
    title="Melanosizer API",
    version="1.0.0",
    openapi_version="2.0.0",
    info=dict(
        description="This is a swagger api documentation for Melanosizer project",
        version="1.0.0",
        contact=dict(
            email="shimaa.mostafaa.07@gmail.com"
            ),
        license=dict(
            name="Apache 2.0",
            url='http://www.apache.org/licenses/LICENSE-2.0.html'
            )
        ),
    servers=[
        dict(
            description="Melanosizer server",
            url="http://127.0.0.1:5000"
            )
        ],
    plugins=[FlaskPlugin(), MarshmallowPlugin()],
)

app = Flask(__name__)
app.secret_key = 'THIS A SUPER SECRT KEY0'
app.config['SESSION_TYPE'] = 'filesystem'
CORS(app)

### swagger specific ###
SWAGGER_URL = ''
API_URL = 'static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Melanosizer project"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

@app.route('/api/predict', methods=['POST'])
def predict():
    ''' Predict the image.
    ---
    post:
      consumes:
      - multipart/form-data
      produces:
      - application/json
      parameters:
      - in: formData
        name: image
        type: file
        required: true
        description: the image file to be processing
      responses:
        200:
          description: Return prediction results
          schema: ResultSchema
        400:
          description: Return error message
          schema: ErrorSchema
    '''
    # Input
    img = request.files['image']

    if not img.mimetype.startswith('image'):
        #Output
        return {'message': 'Error: Allow only image files'}, HTTP_400_BAD_REQUEST

    img = Image.open(img)
    img = img.convert('RGB')

    # plt.imshow(img, interpolation='nearest')
    # plt.show()
    result = classify(img)

    # Ouput
    return {
        'result': str(result)
           }, HTTP_200_OK

#if __name__ == "_main_":
app.run(host='127.0.0.1', port=5000)
# Since path inspects the view and its route,
# we need to be in a Flask request context
with app.test_request_context():
    spec.path(view=predict)
    pass

# We're good to go! Save this to a file for now.
with open('static/swagger.json', 'w') as f:
    json.dump(spec.to_dict(), f)