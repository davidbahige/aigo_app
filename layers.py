# Custom L1 Distance layer module


# Import Dependencies
import tensorflow as tf
from tensorflow.keras.layers import Layer

# Custom L1 Distance from Jupyter
class L1Dist(Layer):
    def __init__(self,**kwargs):
        super().__init__()
     
    # Similarity calculation
    def call(self, input_embedding, validation_embedding):
        return tf.math.abs(input_embedding - validation_embedding)