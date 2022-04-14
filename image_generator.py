from keras_preprocessing.image import ImageDataGenerator
import matplotlib as plt

training_dir = 'symbols/training'

training_data = ImageDataGenerator(rescale=1./255, rotation_range=30, width_shift_range=0.2, height_shift_range=0.2, 
                                    shear_range=0.2, zoom_range=0.2, horizontal_flip=True, fill_mode='nearest')

train_gen = training_data.flow_from_directory(training_dir, target_size=(150, 150), batch_size=1, class_mode='categorical')

fig, ax = plt.subplots(nrows=5, ncols=7, figsize=(150, 150))

for i in range(5):
    image = next(train_gen)[0].astype('uint8')

    ax[i].axis('off')