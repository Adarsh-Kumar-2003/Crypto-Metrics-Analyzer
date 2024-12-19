from sklearn.model_selection import train_test_split
import numpy as np

# Step 1: Split into training+validation set and test set (80%-20%)
X_train_val, X_test, Y_train_val, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Step 2: Split training+validation set into training set and validation set (75%-25% of train_val)
X_train, X_val, Y_train, Y_val = train_test_split(X_train_val, Y_train_val, test_size=0.25, random_state=42)

# Checking of the datasets
#print("Training set shape:", X_train.shape)
#print("Validation set shape:", X_val.shape)
#print("Test set shape:", X_test.shape)
n_outputs = 2  # Number of outputs
num_features = 4  # Number of input features

model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=n_outputs, activation='linear')
])

# Compile the model
model.compile(optimizer='adam', loss='mse', metrics=['mae'])
model.fit(X_train, Y_train, epochs=100, batch_size=10, verbose=1)
