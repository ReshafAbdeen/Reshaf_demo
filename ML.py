import numpy as np 

class Dataset:
    def __init__(self, X, y):
        self.X = np.array(X, dtype=float)
        self.y = np.array(y, dtype=float)
        self.mean = None
        self.std = None

    def normalize(self):
        self.mean = self.X.mean(axis=0)
        self.std = self.X.std(axis=0)
        self.X = (self.X - self.mean) / self.std
        return self

    def train_test_split(self, test_ratio=0.2):
        # Adding this method so the Trainer can actually split the data
        indices = np.arange(len(self.X))
        np.random.shuffle(indices)
        
        split_idx = int(len(self.X) * (1 - test_ratio))
        train_idx, test_idx = indices[:split_idx], indices[split_idx:]
        
        X_train, X_test = self.X[train_idx], self.X[test_idx]
        y_train, y_test = self.y[train_idx], self.y[test_idx]
        return X_train, X_test, y_train, y_test

class NeuralLayer:
    def __init__(self, input_dim, output_dim, activation='relu'):
        self.weight = np.random.randn(input_dim, output_dim) * 0.1
        self.bias = np.zeros(output_dim)
        self.activation = activation
        self.output = None
        self.input = None

    def forward(self, X):
        self.input = X 
        z = X @ self.weight + self.bias
        self.output = self._activate(z)
        return self.output

    def _activate(self, z):
        if self.activation == 'relu':
            return np.maximum(0, z)
        elif self.activation == 'sigmoid':
            return 1 / (1 + np.exp(-z))
        return z

    def backward(self, grad_output, lr):
        if self.activation == 'relu':
            grad_output = grad_output * (self.output > 0)
        elif self.activation == 'sigmoid':
            grad_output = grad_output * self.output * (1 - self.output)

        grad_weights = self.input.T @ grad_output
        grad_bias = grad_output.sum(axis=0)
        grad_input = grad_output @ self.weight.T

        self.weight -=  lr * grad_weights / len(self.input)
        self.bias -= lr *  grad_bias / len(self.input)
        return grad_input

# Moved this class outside of NeuralLayer
class NeuralNetwork:
    def __init__(self):
        self.layers = []
        self.loss_history = []

    def add_layer(self, layer):
        self.layers.append(layer)
        return self

    def forward(self, X):
        out = X
        for layer in self.layers:
            out = layer.forward(out)
        return out  # Fixed empty return

    def backward(self, grad, lr):
        for layer in reversed(self.layers):
            grad = layer.backward(grad, lr)

    def train(self, X, y, epochs=100, lr=0.01):
        y = y.reshape(-1, 1)
        for epoch in range(epochs):
            preds = self.forward(X)
            loss = np.mean((preds - y) ** 2)
            self.loss_history.append(loss)

            grad = 2 * (preds - y) / len(X)
            self.backward(grad, lr)

            if epoch % 20 == 0:
                print(f"Epoch {epoch:<4} | Loss: {loss:.4f}")

    def predict(self, X):
        return self.forward(X) # Fixed missing function call ()


class Trainer:
    def __init__(self, model, dataset):
        self.model = model
        self.dataset = dataset

    def run(self, epochs=100, lr=0.01, test_ratio=0.2):
        X_train, X_test, y_train, y_test = self.dataset.train_test_split(test_ratio)
        print("Training Start")
        self.model.train(X_train, y_train, epochs, lr)

        preds = self.model.predict(X_test)
        test_loss = np.mean((preds.flatten() - y_test) ** 2)
        print(f"Training complete! Test Loss: {test_loss:.4f}")


if __name__ == "__main__":
    np.random.seed(42)

    X = np.random.rand(200, 1) * 10
    y = 3 * X.flatten() + 5 + np.random.randn(200) * 0.5

    dataset = Dataset(X, y).normalize()

    model = (NeuralNetwork()
             .add_layer(NeuralLayer(1, 8, activation='relu'))
             .add_layer(NeuralLayer(8, 1, activation="linear")))

    trainer = Trainer(model, dataset)
    trainer.run(epochs=200, lr=0.1)