from keras.applications.inception_v3 import InceptionV3
from keras.applications.inception_v3 import preprocess_input
from keras.applications.inception_v3 import decode_predictions
from keras.preprocessing import image
import numpy as np
img = image.load_img('./pen.png',target_size=(299,299))
model = InceptionV3(weights='imagenet',include_top=True)
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)
features = model.predict(x)
print(decode_predictions(features))
