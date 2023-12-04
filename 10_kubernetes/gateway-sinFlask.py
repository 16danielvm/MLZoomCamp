# Importaciones de bibliotecas necesarias
import grpc
import tensorflow as tf
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc
from keras_image_helper import create_preprocessor

# Dirección del servidor TensorFlow Serving
host = 'localhost:8500'

# Configuración del canal gRPC y creación del stub
channel = grpc.insecure_channel(host)
stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)

# Creación de un preprocesador de imágenes usando Xception
preprocessor = create_preprocessor('xception', target_size=(299, 299))

# Función para convertir un array NumPy a un protocolo TensorFlow
def np_to_proto(data):
    return tf.make_tensor_proto(data, shape=data.shape)

# Función para preparar una solicitud de predicción
def prepare_request(X):
    pb_request = predict_pb2.PredictRequest()
    pb_request.model_spec.name = 'clothing-model'
    pb_request.model_spec.signature_name = 'serving_default'
    pb_request.inputs['input_16'].CopyFrom(np_to_proto(X))
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

# Bloque principal
if __name__ == '__main__':
    # Ejemplo de URL de imagen a predecir
    url = 'http://bit.ly/mlbookcamp-pants'
    
    # Realización de la predicción y muestra del resultado
    response = predict(url)
    print(response)
