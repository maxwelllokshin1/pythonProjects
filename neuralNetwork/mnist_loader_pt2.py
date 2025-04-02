import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import matplotlib.pyplot as plt
from mnist import MNIST

# Load data
mndata = MNIST('C:/Users/maxwe_kpki328/Downloads/archive')
images, labels = mndata.load_training()
images = np.array(images).reshape(-1, 28, 28, 1) / 255.0
labels = keras.utils.to_categorical(labels, 10)

# Define model
model = keras.Sequential([
    layers.Flatten(input_shape=(28, 28, 1)),
    layers.Dense(20, activation='sigmoid'),
    layers.Dense(10, activation='softmax')
])

# Compile model
model.compile(optimizer=keras.optimizers.Adam(learning_rate=0.01),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# Train model
model.fit(images, labels, epochs=3, batch_size=32, validation_split=0.1)

# Prediction loop
while True:
    index = int(input("Enter a number (0 - 59999): "))
    img = images[index]
    plt.imshow(img.squeeze(), cmap="Greys")
    prediction = model.predict(img.reshape(1, 28, 28, 1))
    plt.title(f"NUMBER: {np.argmax(prediction)}")
    plt.show()
