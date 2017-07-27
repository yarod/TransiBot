from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras.utils import np_utils
import numpy as np

np.random.seed(123)
data = np.load('database.npy')

data = data.transpose()
print data.shape
np.random.shuffle(data)


X=data[ : , 0:-1 ]
Y=data[ : ,-1 ]
Y=np_utils.to_categorical(Y)
print X[0]
print Y[0]
total_words = 59

print 'Construyendo el modelo'

model = Sequential()

# Input layer has 52 neurons
model.add(Dense(total_words, activation='relu', input_dim=total_words))
# Hidden Layer has 65 neurons
model.add(Dense(65, activation='relu'))
# The output layer has 15 neurons (the same number of classes) using the softmax as activation function
model.add(Dense(15, activation='softmax'))
adam = Adam(lr=0.0001, beta_1=0.9, beta_2=0.999, epsilon=1e-08, decay=0.0)
model.compile(loss = 'categorical_crossentropy', optimizer = adam, metrics = ['accuracy'])
model.summary()
# Training the model
model.fit(X, Y,
          epochs=800,
          batch_size=10,)
model.save("multas.h5")