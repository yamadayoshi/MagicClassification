from tensorflow.keras import layers, models, optimizers
from tensorflow import keras
from keras_preprocessing.image import ImageDataGenerator

def training_model(height, width, training_dir, validation_dir):

    #build model
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(height, width, 3)))
    model.add(layers.MaxPool2D(2, 2))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPool2D(2, 2))
    model.add(layers.Conv2D(128, (3, 3), activation='relu'))
    model.add(layers.MaxPool2D(2, 2))
    model.add(layers.Flatten())
    model.add(layers.Dropout(0.2))
    model.add(layers.Dense(512, activation='relu'))
    model.add(layers.Dense(3, activation='softmax'))

    # model.summary()

    #compile model
    model.compile(loss='categorical_crossentropy', optimizer=optimizers.RMSprop(1e-4), metrics='acc')

    train_data = ImageDataGenerator(rescale=1./255, rotation_range=40, width_shift_range=0.2, height_shift_range=0.2, 
                                    shear_range=0.2, zoom_range=0.2, horizontal_flip=True, fill_mode='nearest')

    # train_data = ImageDataGenerator(rescale=1./255)

    validation_data = ImageDataGenerator(rescale=1./255)

    train_gen = train_data.flow_from_directory(training_dir, target_size=(height, width), batch_size=32, class_mode='categorical')
    validation_gen = validation_data.flow_from_directory(validation_dir, target_size=(height, width), batch_size=32, class_mode='categorical')

    # for data_batch, labels_batch in train_gen:
    #     print('data batch shape:', data_batch.shape)
    #     print('labels batch shape:', labels_batch.shape)
    #     break

    history = model.fit(train_gen, steps_per_epoch=2, epochs=1000, validation_data=validation_gen, validation_steps=3)

    print('Saving h5 file')
    model.save('symbols.h5')

    return model

def load_model():
    return keras.models.load_model('symbols.h5')