from hello import *
import tensorflow as tf
import numpy as np

def shuffle_in_unison(a, b):
        assert len(a) == len(b)
        shuffled_a = np.empty(a.shape, dtype=a.dtype)
        shuffled_b = np.empty(b.shape, dtype=b.dtype)
        permutation = np.random.permutation(len(a))
        for old_index, new_index in enumerate(permutation):
            shuffled_a[new_index] = a[old_index]
            shuffled_b[new_index] = b[old_index]
        return shuffled_a, shuffled_b

def build_model():
    
    neurons = 24
 

    # Initialize weights and biases for the neural network
    initializer = tf.initializers.GlorotUniform()
    w1 = tf.Variable(initializer(shape=(m, neurons)), dtype=tf.float32)
    b1 = tf.Variable(tf.zeros(shape=(neurons)), dtype=tf.float32)
    w2 = tf.Variable(initializer(shape=(neurons, neurons*2)), dtype=tf.float32)
    b2 = tf.Variable(tf.zeros(shape=(neurons*2)), dtype=tf.float32)
    w3 = tf.Variable(initializer(shape=(neurons*2, neurons*2)), dtype=tf.float32)
    b3 = tf.Variable(tf.zeros(shape=(neurons*2)), dtype=tf.float32)
    w4 = tf.Variable(initializer(shape=(neurons*2, 1)), dtype=tf.float32)
    b4 = tf.Variable(tf.zeros(shape=(1)), dtype=tf.float32)

    # Define model architecture
    model = tf.keras.models.Sequential([
        tf.keras.layers.InputLayer(input_shape=m),
        tf.keras.layers.Dense(units=neurons, activation='relu'),
        tf.keras.layers.Dense(units=neurons*2, activation='relu'),
        tf.keras.layers.Dense(units=neurons*2, activation='relu'),
        tf.keras.layers.Dense(units=1, activation='sigmoid'),
    ])
    
  
    
    model.layers[0].set_weights([w1, b1])
    model.layers[1].set_weights([w2, b2])
    model.layers[2].set_weights([w3, b3])
    model.layers[3].set_weights([w4, b4])

    return model


n, m = np.shape(vec)


x = vec
x , outcome = shuffle_in_unison(x, outcome)
        
print(np.shape(x))


model = build_model()
model.compile(optimizer='adam', loss='binary_crossentropy')
model.fit(vec,outcome,epochs = 10)



y_hat = model.predict(x)


ct = 0
ctdum = 0
totct = 0
for i in vec:
    outputprob = y_hat[totct]
    if outputprob > 0.6:
        if outcome[totct] == 0 and vec[totct][0] > 60 :
            ct += 1
        ctdum += 1
    elif outputprob < 0.4 and vec[totct][0] > 60:
        if outcome[totct] == 1:
            ct += 1
        ctdum += 1
    totct += 1
    
    
print(100 - (ct / ctdum) * 100)

