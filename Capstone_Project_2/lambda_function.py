import tensorflow.lite as tflite # se supone que se comenta este
# import tflite_runtime.interpreter as tflite # PARA EL DOCKERFILE DESCOMENTAR ESTE!! Y COMENTAR EL DE ARRIBA
from keras_image_helper import create_preprocessor

interpreter = tflite.Interpreter(model_path='mask-model.tflite')
interpreter.allocate_tensors()

preprocessor = create_preprocessor('xception', target_size=(224, 224))

input_index = interpreter.get_input_details()[0]['index']
output_index = interpreter.get_output_details()[0]['index']

classes =['WithMask', 'WithoutMask']

# url = 'https://raw.githubusercontent.com/16danielvm/MLZoomCamp/master/Capstone_Project_2/final_model/45.png'

def predict(url):
    
    X = preprocessor.from_url(url)
    
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    float_predictions = preds[0].tolist()
    
    return dict(zip(classes, float_predictions))

def lambda_handler(event, context):
    url = event['url']
    result = predict(url)
    return result