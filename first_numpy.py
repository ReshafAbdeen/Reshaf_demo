import numpy as np

class SmartNeuralNetwork:
    def __init__(self):
        self.inputs = np.array([
            [10, 3],  
            [-50, -5], 
            [25, 4]    
        ])
        
        self.weights = np.array([[2], [5]])
        self.bias = 10 

    def forward_pass_with_relu(self):
        raw_output = (self.inputs @ self.weights) + self.bias
        print("=== 📉 Raw Output (Before ReLU) ===")
        print(raw_output)
     
        activated_output = np.maximum(0,raw_output )
        
        print("\n=== Final Output (After ReLU Security Guard) ===")
        print(activated_output)

if __name__ == "__main__":
    nn = SmartNeuralNetwork()
    nn.forward_pass_with_relu()