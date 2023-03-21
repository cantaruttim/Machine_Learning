from tensorflow.keras.layers import TextVectorization
import numpy as np

# Example training data, of dtype `string`.
training_data = np.array([["This is the 1st sample."], ["And here's the 2nd sample."]])