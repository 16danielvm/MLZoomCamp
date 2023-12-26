
# Importing libraries
import warnings
warnings.filterwarnings("ignore")

import tensorflow as tf
tf.get_logger().setLevel('ERROR')
from tensorflow import keras
from tensorflow.keras.applications.mobilenet import MobileNet, preprocess_input
from tensorflow.keras.preprocessing.image import ImageDataGenerator
# Make model
def make_model(learning_rate=0.01, size_inner= 10, input_size=224):

    base_model = MobileNet(weights='imagenet', include_top=False, input_shape=(224,224,3))
    base_model.trainable = False

#############################################################

    inputs = keras.Input(shape=(input_size,input_size,3))
    base = base_model(inputs, training=False)
    vectors= keras.layers.GlobalAveragePooling2D()(base) 

    inner = keras.layers.Dense(size_inner, activation='relu')(vectors) # capa oculta agregada lo que hace es que se agregan mas neuronas a la red para poder tener mas parametros y poder ajustar mejor los datos

    outputs = keras.layers.Dense(2)(inner)
    model = keras.Model(inputs, outputs)

#############################################################

    optimazer = keras.optimizers.Adam(learning_rate=learning_rate)
    loss = keras.losses.BinaryCrossentropy(from_logits=True)
    model.compile(optimizer= optimazer, loss=loss, metrics=['accuracy'])

    return model

input_size = 224

# Preprocessing the images

print('.../Preprocessing images/...')

train_gen = ImageDataGenerator(preprocessing_function=preprocess_input)

train_ds = train_gen.flow_from_directory(
    '../data/data/Train',
    target_size = (input_size,input_size),
    batch_size =16
)

val_gen = ImageDataGenerator(preprocessing_function=preprocess_input)

val_ds = val_gen.flow_from_directory(
    '../data/data/Validation',
    target_size = (input_size,input_size),
    batch_size = 16,
    shuffle = False
)

print('.../Images preprocessed/...')
# checkpoint 

checkpoint = keras.callbacks.ModelCheckpoint(
    'mobileNet_{epoch:02d}_{val_accuracy:.3f}.h5',
    save_best_only=True,
    monitor = 'val_accuracy',
    mode='max'
)

#Parameters

print('.../Charging parameters/...')
learning_rate = 0.01
size = 10

print('.../Parameters charged/...')

# Training the model
model = make_model(
    input_size= 224,
    learning_rate=learning_rate,
    size_inner= size,
)

print('.../Training model/...')

history = model.fit(train_ds, epochs=10, validation_data=val_ds, callbacks= [checkpoint])