# encoding=utf-8
# Date: 2018-09-28
# Author: MJUZY


from keras.preprocessing.image import ImageDataGenerator
from Prepare import train_dir
from Prepare import validation_dir

train_datagen = ImageDataGenerator(rescale=1./255)
test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(150, 150),
    batch_size=20,
    class_mode='binary')

validation_generator = test_datagen.flow_from_directory(
    validation_dir,
    target_size=(150, 150),
    batch_size=20,
    class_mode='binary')

for data_batch, labels_batch in train_generator:
    print('data batch shape : ', data_batch.shape)
    print('labels batch shape :', labels_batch.shape)
    break