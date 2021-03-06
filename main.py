import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


import tensorflow as tf
physical_devices = tf.config.experimental.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)


from keras import models
from keras import layers
from keras.datasets import mnist
from keras.utils import to_categorical


def build_model():
	model = models.Sequential()
	model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
	model.add(layers.MaxPooling2D((2, 2)))
	model.add(layers.Conv2D(64, (3,3), activation='relu'))
	model.add(layers.MaxPooling2D((2, 2)))
	model.add(layers.Conv2D(64, (3,3), activation='relu'))
	model.add(layers.Flatten())
	model.add(layers.Dense(64, activation='relu'))
	model.add(layers.Dense(10, activation='softmax'))	# output layer
	model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])
	return model


def main():

	# data
	(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
	train_images = train_images.reshape((60000, 28, 28, 1))
	train_images = train_images.astype('float32') / 255
	test_images = test_images.reshape((10000, 28, 28, 1))
	test_images = test_images.astype('float32') / 255
	train_labels = to_categorical(train_labels)
	test_labels = to_categorical(test_labels)

	# model
	model = build_model()
	model.fit(train_images, train_labels, epochs=5, batch_size=64)
	test_loss, test_acc = model.evaluate(test_images, test_labels)
	print('Test accuracy: ', round(test_acc, 3) * 100, '%')


if __name__ == '__main__':
	main()