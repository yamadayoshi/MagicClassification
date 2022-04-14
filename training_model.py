from keras_preprocessing.image import load_img, img_to_array
from numpy import asarray
import utils

symbols_dir = 'symbols'

training_dir = 'symbols/training'
training_dir = 'symbols/validation'
validation_dir = 'symbols/validation'

HEIGHT = 150
WIDTH = 150

EDITIONS = ['GRN','NEO', 'ZNR']

# model = utils.training_model(HEIGHT, WIDTH, training_dir, validation_dir)
model = utils.load_model()

#predict
image_path = 'symbols/validation/GRN/grn_r_c.jpg'
# image_path = 'symbols/validation/NEO/neo_u_4.jpg'
# image_path = 'symbols/validation/ZNR/znr_b_1.jpg'

img = asarray(load_img(image_path, target_size=(HEIGHT, WIDTH))).astype('float32')
img /= 255

i = img_to_array(img)
i = i.reshape((1,) + i.shape)

print(i.shape)

prob = model.predict(i)

print(prob)