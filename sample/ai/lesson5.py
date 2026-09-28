import tensorflow as tf
from  tensorflow.keras import layers, models
import matplotlib.pyplot as plt

(x_train, y_train),(x_test, y_text)= tf.keras.datasets.mnist.load_data()

x_train, x_test = x_train / 255.0, x_test / 255.0

model= models.Sequential ([layers.Flattern(imput_shape=(28,28)),layers.Dense(128, activation='relu'), layers.Dense(10, activation='softmax')])

model.compile( optimizer='adam',loss='sparse_categorical_corssentropy', metrics=['accuracy'])

model,fit(x_train,y_train, epochs=5)

test_loss, test_acc= model.evaluate(x_test, y_test)
print("Test Accuracy:",test_acc)
plt.imshow(x_text[0], cmap=plt.cm.binary)
plt.title(f"predicted: {predictions[0].argmax()} | Actual: {y_test[0]}")
plt.show()

