# Import the model and other libraries

import tensorflow as tf
import keras
from keras.preprocessing import image
import numpy as np

def get_classes(file_path):
    # Create an instance of 'myModel' imported above
    modelleaf = tf.keras.models.load_model('leafmodel.h5')
    # Load image and preprocess it
    img = image.load_img(file_path, target_size=(244, 244))
    x = image.img_to_array(img)
    x = tf.image.rgb_to_grayscale(x)
    #x= np.array([x])
    x = np.expand_dims(x, axis=0)
    x = x/255.0
    categories = ['Alpinia Galanga (Rasna)','Ficus Religiosa (Peepal Tree)','Moringa Oleifera (Drumstick)','Punica Granatum (Pomegranate)']


    # This is the inference time. Given an instance, it produces the predictions.
    predy = (modelleaf.predict(x)>0.5).astype("int32")
    y_classes = np.argmax(predy)
    preds = categories[y_classes]
    return preds