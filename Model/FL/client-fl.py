import os
import flwr as fl
import tensorflow as tf
import numpy as np

# Make TensorFlow log less verbose
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

# Load and preprocess the MNIST dataset
def load_data():
    # Load MNIST dataset
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()
    
    # Normalize pixel values
    x_train = x_train.astype('float32') / 255.0
    x_test = x_test.astype('float32') / 255.0
    
    return (x_train, y_train), (x_test, y_test)

# Create and compile Keras model
def create_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    
    model.compile(
        optimizer='adam',
        loss='sparse_categorical_crossentropy',
        metrics=['accuracy']
    )
    return model

# Define Flower client
class MnistClient(fl.client.NumPyClient):
    def __init__(self):
        self.model = create_model()
        (self.x_train, self.y_train), (self.x_test, self.y_test) = load_data()

    def get_parameters(self, config):
        """Get parameters of the local model."""
        return [param.numpy() for param in self.model.trainable_weights]

    def fit(self, parameters, config):
        """Train parameters on the locally held training set."""
        # Update local model parameters
        self.model.set_weights(parameters)

        # Get hyperparameters for this round
        batch_size = config["batch_size"]
        epochs = config["local_epochs"]

        # Train the model using hyperparameters from config
        history = self.model.fit(
            self.x_train,
            self.y_train,
            batch_size=batch_size,
            epochs=epochs,
            validation_split=0.1,
        )

        # Return updated model parameters and results
        parameters_updated = [param.numpy() for param in self.model.trainable_weights]
        num_examples_train = len(self.x_train)
        results = {
            "loss": history.history["loss"][0],
            "accuracy": history.history["accuracy"][0],
            "val_loss": history.history["val_loss"][0],
            "val_accuracy": history.history["val_accuracy"][0],
        }
        
        return parameters_updated, num_examples_train, results

    def evaluate(self, parameters, config):
        """Evaluate parameters on the locally held test set."""
        # Update local model with global parameters
        self.model.set_weights(parameters)

        # Evaluate global model parameters on the local test data
        loss, accuracy = self.model.evaluate(self.x_test, self.y_test)
        
        return loss, len(self.x_test), {"accuracy": accuracy}

# Start Flower client
if __name__ == "__main__":
    fl.client.start_numpy_client(
        server_address="localhost:8080",
        client=MnistClient(),
    )