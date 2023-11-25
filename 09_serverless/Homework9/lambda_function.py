# import tensorflow.lite as tflite # se supone que se comenta este
import tflite_runtime.interpreter as tflite # PARA EL DOCKERFILE DESCOMENTAR ESTE!! Y COMENTAR EL DE ARRIBA
import numpy as np
from io import BytesIO
from urllib import request

from PIL import Image

interpreter = tflite.Interpreter(model_path='bees-wasps-v2.tflite') 
interpreter.allocate_tensors() 

def download_image(url):
    with request.urlopen(url) as resp:
        buffer = resp.read()
    stream = BytesIO(buffer)
    img = Image.open(stream)
    return img


def prepare_image(img, target_size):
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img = img.resize(target_size, Image.NEAREST)
    return img

input_index = interpreter.get_input_details()[0]['index'] 
output_index = interpreter.get_output_details()[0]['index'] 

def preprocessor(url, target_size):

    img = download_image(url)
    img = prepare_image(img, target_size)
    # rescale image and convert to numpy array
    x = np.array(img)/255.
    # create a batch with a single image since this is the expected input to the model:
    X = np.array([x], dtype='float32')

    return X

def predict(url):

    target_size = (150, 150)
    X = preprocessor(url, target_size)

    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    float_predictions = preds[0].tolist()

    # return dict(zip(classes, float_predictions))
    return float_predictions


def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result