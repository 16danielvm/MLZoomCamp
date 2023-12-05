# Importaciones de bibliotecas necesarias
import os #### Agregar esta linea despues de crear el docker-compose.yaml
import grpc
import tensorflow as tf
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc
from keras_image_helper import create_preprocessor

from flask import Flask 
from flask import request
from flask import jsonify

from proto import np_to_protobuf #LINEA AGREGADA DESPUES DE CREAR EL ARCHIVO proto.py

host = os.getenv('TF_SERVING_HOST', 'localhost:8500') ####LINEA AGREGADA DESPUES DE CREAR EL ARCHIVO docker-compose.yaml

# Dirección del servidor TensorFlow Serving
# host = 'localhost:8500' ####LINEA COMENTADA DESPUES DE CREAR EL ARCHIVO docker-compose.yaml

# Configuración del canal gRPC y creación del stub
channel = grpc.insecure_channel(host)
stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)

# Creación de un preprocesador de imágenes usando Xception
preprocessor = create_preprocessor('xception', target_size=(299, 299))

#### -------------------->>>FUNCION COMENTADA DESPUES DE CREAR EL ARCHIVO proto.py <<<--------------------
# # Función para convertir un array NumPy a un protocolo TensorFlow
# def np_to_proto(data):
#     return tf.make_tensor_proto(data, shape=data.shape)

# Función para preparar una solicitud de predicción
def prepare_request(X):
    pb_request = predict_pb2.PredictRequest()
    pb_request.model_spec.name = 'clothing-model'
    pb_request.model_spec.signature_name = 'serving_default'
    # pb_request.inputs['input_16'].CopyFrom(np_to_proto(X)) ####LINEA COMENTADA DESPUES DE CREAR EL ARCHIVO proto.py
    pb_request.inputs['input_16'].CopyFrom(np_to_protobuf(X))
    return pb_request

# Lista de clases posibles del modelo
classes = ['dress', 'hat', 'longsleeve', 'outwear', 'pants', 'shirt', 'shoes', 'shorts', 'skirt', 't-shirt']

# Función para procesar la respuesta de la predicción
def prepare_response(pb_response):
    preds = pb_response.outputs['dense_13'].float_val
    return dict(zip(classes, preds))

# Función principal para realizar una predicción
def predict(url):
    # Preprocesamiento de la imagen desde la URL
    X = preprocessor.from_url(url)
    
    # Preparación de la solicitud de predicción
    pb_request = prepare_request(X)
    
    # Envío de la solicitud al servidor TensorFlow Serving a través de gRPC
    pb_response = stub.Predict(pb_request, timeout=20.0)
    
    # Procesamiento de la respuesta y retorno del resultado
    response = prepare_response(pb_response)
    return response

app = Flask('gateway')

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    data = request.get_json()
    url = data['url']
    result = predict(url)
    return jsonify(result)



# Bloque principal
if __name__ == '__main__':
    #### 3 lineas descomentadas despues de crear el archivo proto.py solo para el pipenv
    # Ejemplo de URL de imagen a predecir
    url = 'http://bit.ly/mlbookcamp-pants'
    
    # Realización de la predicción y muestra del resultado
    response = predict(url)
    print(response)
    # app.run(debug=True, host='0.0.0.0', port=9696) ####LINEA COMENTADA DESPUES DE CREAR EL ARCHIVO proto.py solo para el pipenv
