import numpy as np

class NeuralMath:
    def __init__(self):
        # 🏢 3 Gharo ka data (Row 1 = Ghar 1, Row 2 = Ghar 2...)
        # Har ghar ke paas 2 features hain: [Age, Rooms]
        # Matrix Size: 3 Rows, 2 Columns (3x2)
        self.inputs = np.array([
            [10, 3],  # Ghar 1: Age=10, Rooms=3
            [40, 5],  # Ghar 2: Age=40, Rooms=5
            [25, 4]   # Ghar 3: Age=25, Rooms=4
        ])
        
        # 🧠 Neural Network ke Weights (Har feature ke liye ek weight)
        # Matrix Size: 2 Rows, 1 Column (2x1)
        self.weights = np.array([
            [2],  # Age ka weight
            [5]   # Rooms ka weight
        ])

    def forward_pass(self):
        print("=== 📥 Inputs Matrix (3x2) ===")
        print(self.inputs)
        
        print("\n=== 🧠 Weights Matrix (2x1) ===")
        print(self.weights)
        
        # ------------------------------------------------------------------
        # 🧠 YAHAN APNA JADU DIKHAO!
        # Task: 'self.inputs' aur 'self.weights' ka Matrix Multiplication karo (@ operator use karke)
        
        nn_output = self.inputs @ self.weights
        
        # ------------------------------------------------------------------
        
        print("\n=== 🚀 Neural Network Output (3x1) ===")
        print(nn_output)

if __name__ == "__main__":
    bot = NeuralMath()
    bot.forward_pass()