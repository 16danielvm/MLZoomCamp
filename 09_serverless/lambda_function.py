
import tensorflow.lite as tflite # se supone que se comenta este
# import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor

interpreter = tflite.Interpreter(model_path='clothing-model.tflite')
interpreter.allocate_tensors()

preprocessor = create_preprocessor('xception', target_size=(299, 299))

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

classes = ['dress',
 'hat',
 'longsleeve',
 'outwear',
 'pants',
 'shirt',
 'shoes',
 'shorts',
 'skirt',
 't-shirt']

# url = 'http://bit.ly/mlbookcamp-pants'

def predict(url):
    
    X = preprocessor.from_url(url)
    
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)
    
    return dict(zip(classes, preds[0]))

def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result





