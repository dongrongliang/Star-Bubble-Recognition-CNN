from __future__ import print_function
import keras
from keras import backend as K
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Conv2D, MaxPooling2D


keras.preprocessing.image.ImageDataGenerator(featurewise_center=False,
    samplewise_center=False,
    featurewise_std_normalization=False,
    samplewise_std_normalization=False,
    zca_whitening=False,
    zca_epsilon=1e-6,
    rotation_range=40,
    width_shift_range=0.,
    height_shift_range=0.,
    shear_range=0.,
    zoom_range=0.,
    channel_shift_range=0.,
    fill_mode='nearest',
    cval=0.,
    horizontal_flip=False,
    vertical_flip=False,
    rescale=1. / 255,
    preprocessing_function=None,
    data_format=K.image_data_format())

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        './train',
        target_size=(200,200),
        batch_size=2,
        class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
        './validation',
        target_size=(200,200),
        batch_size=3,
        class_mode='binary')

kernel_size=10
pool_size_1=4
pool_size_2=2
model = Sequential()
model.add(Conv2D(32, (kernel_size, kernel_size), padding='same',
                 input_shape=(200, 200,3)))
model.add(Activation('relu'))
model.add(Conv2D(32, (kernel_size, kernel_size)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(pool_size_1, pool_size_1)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (kernel_size, kernel_size), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64, (kernel_size, kernel_size)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(pool_size_2, pool_size_2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(1,activation="sigmoid"))



model.compile(loss=keras.losses.binary_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])


history = model.fit_generator(
        train_generator,
        steps_per_epoch=20,
        epochs=10,
        validation_data=validation_generator,
        validation_steps=10)

score =model.evaluate_generator(validation_generator, 10, max_queue_size=4, workers=1, use_multiprocessing=False)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

predict_datagen = ImageDataGenerator(rescale=1./255)

pre_generator = predict_datagen.flow_from_directory(
        './predict',
        target_size=(200,200),
        batch_size=1,
        shuffle=False,
        class_mode=None)

score_predict=model.predict_generator(pre_generator, 8, max_queue_size=8, workers=1, use_multiprocessing=False, verbose=0)
print('Probability of no bubble:\n', score_predict)


