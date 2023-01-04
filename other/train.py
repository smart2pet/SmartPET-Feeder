import os
import sys
import time
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

config = tf.compat.v1.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.3  # type: ignore
tf.compat.v1.keras.backend.set_session(tf.compat.v1.Session(config=config))

train_x = [
    [50],
    [100],
    [150],
    [175],
    [200],
    [250],
    [300],
    [75],
    [125],
    [225],
    [275],
    [25],
    [35],
    [15],
    [5],
]
# Bring your data here. train_y is the amount of food dropped when turn the laps in train_x, a data in train_y matches a data in train_x. Don't change train_x, 
# you need to do these test and bring the amount of food dropped in train_y (the unit is gram).

# You may train in multiple times to get the best result.
train_y = [
    [30],
    [50],
    [65],
    [75],
    [90],
    [105],
    [125],
    [45],
    [60],
    [90],
    [110],
    [15],
    [25],
    [11],
    [5],
]
train_x = np.array(train_x)
print(train_x)
train_y = np.array(train_y)



def build_model() -> tf.keras.Sequential:
    """Builds a model.

    Args:
      None

    Returns:
      A compiled Keras model.
    """
    model = keras.Sequential(
        [
            layers.Dense(54, activation="relu"),
            layers.Dense(32, activation="relu"),
            layers.Dense(1),
        ]
    )
    optimizer = tf.keras.optimizers.RMSprop(0.001)
    model.compile(loss="mse", optimizer="adam", metrics=["mae", "mse"])
    return model  # type: ignore


model = build_model()

class PrintDot(keras.callbacks.Callback):
    def on_epoch_end(self: object, epoch: int, logs: dict) -> None:
        """
        This is a multi-line Google style docstring.

        Args:
          self: The object.
          epoch: The epoch.
          logs: The logs.

        Returns:
          None.
        """
        if epoch % 100 == 0:
            print("")
        print(".", end="")


EPOCHS = 1000000
early_stop = keras.callbacks.EarlyStopping(
    monitor="val_loss", patience=100, restore_best_weights=True
)
history = model.fit(
    train_y,
    train_x,
    epochs=EPOCHS,
    validation_split=0.3,
    verbose=0,  # type: ignore
    callbacks=[early_stop, PrintDot()],
)
model.save("./model.h5")
# Do the test.
test_predictions = model.predict([[60]])
print(test_predictions)
# After the test, please do the test on your motor and see the amount of food dropped.
# If there was a big error(more than ±4 gram), please train again.
# If it's always like that, please check the data.
