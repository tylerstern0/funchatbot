import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
import keras.optimizers
import random

import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle

intents_file = open('intents.json').read()
intents = json.loads(intents_file)


print("train_chatbot complete")
