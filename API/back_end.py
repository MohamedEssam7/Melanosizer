from tensorflow import keras
from PIL import Image
from numpy import asarray
import numpy as np

model = keras.models.load_model('model_D9v13.h5')
# Image type must be numpy array
def predict(image):
    def standardize(img, mean):
        std = 55.30462222768374
        img = (img - mean) / std
        return img

    mean = [143.33956166346746, 148.21742939479066, 190.40706684440573]
    r_channel = standardize(asarray(image.resize((224, 224)))[:, :, 0], mean[0])
    g_channel = standardize(asarray(image.resize((224, 224)))[:, :, 1], mean[1])
    b_channel = standardize(asarray(image.resize((224, 224)))[:, :, 2], mean[2])
    prediction = model.predict(np.expand_dims(np.array(np.stack([r_channel, g_channel, b_channel], axis=-1)), 0),
                               verbose=0)
    return prediction

def classify(img):
    result = predict(img)
    return result[0][0]