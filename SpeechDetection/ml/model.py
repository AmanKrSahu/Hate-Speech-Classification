# Creating Model Architecture
from SpeechDetection.entity.config_entity import ModelTrainerConfig
from keras import Sequential
from keras.layers import Embedding, LSTM, Dense, SpatialDropout1D
from tensorflow.keras.optimizers import RMSprop
from SpeechDetection.constants import *

class ModelArchitecture:
    def __init__(self):
        pass

    def get_model(self):
        model = Sequential()
        model.add(Embedding(MAX_WORDS, 100, input_shape=(MAX_LEN,)))
        model.add(SpatialDropout1D(0.2))
        model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
        model.add(Dense(1, activation=ACTIVATION))
        model.summary()
        model.compile(loss=LOSS, optimizer=RMSprop(), metrics=METRICS)

        return model
    