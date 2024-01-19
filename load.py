import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image
import io


model = keras.models.load_model("nn.keras")

# load the image
with open('5.jpg', 'rb') as file:
    image_bytes = file.read()
    pillow_img = Image.open(io.BytesIO(image_bytes)).convert('L')


# transform image, same as for training!
data = np.asarray(pillow_img)
print(data.shape)
data = data / 255.0
data = data[np.newaxis, ..., np.newaxis]
print(data.shape)
# --> [1, x, y, 1]
data = tf.image.resize(data, [28, 28])
print(data.shape)


# predict
predictions = model(data)
predictions = tf.nn.softmax(predictions)
pred0 = predictions[0]
label0 = np.argmax(pred0)
print(label0)