import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from tensorflow import keras


mnist = keras.datasets.mnist

# Split train and test data
(x_train, y_train), (x_test, y_test) = mnist.load_data()
print("Train Data Shape: ",x_train.shape, y_train.shape)
print("Test Data Shape: ",x_test.shape, y_test.shape)
print("--------------------------------------------------------------------------")

# normalize: 0,255 -> 0,1
x_train, x_test = x_train / 255.0, x_test / 255.0

# sequential model
model = keras.models.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10),
])


# loss and optimizer
loss = keras.losses.SparseCategoricalCrossentropy(from_logits=True)
optim = keras.optimizers.Adam(learning_rate=0.001)
metrics = ["accuracy"]

model.compile(loss=loss, optimizer=optim, metrics=metrics)

# training
batch_size = 64
epochs = 7

model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, shuffle=True)
print("Model Training Complete! Now evaluating...")
print("--------------------------------------------------------------------------")
model.evaluate(x_test, y_test, batch_size=batch_size)

# save model
print("--------------------------------------------------------------------------")
model.save("nn.keras") 
print("Model Saved!")



