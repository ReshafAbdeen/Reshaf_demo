class AIModel:
    def __init__(self, model_name, accuracy):
        self.name = model_name
        self.accuracy = accuracy

    def show_detail(self):
        print(f"Model name {self.name }\nAccuracy {self.accuracy}")


class MachineLearning(AIModel):
    def train(self):
        print(f"{self.name} train ho rha hai data or formla  use karke.")


class DeepLearningModel(AIModel):
    def train(self):
        print(f"{self.name} train ho rha hai . Neural network or GPUs use karke.")


ml_model = MachineLearning("Zomato_Linear_agression", 87.0)
dl_model = DeepLearningModel("Zomato_barin_Neural_net", 90.9)


print("\n---Testing Polymorphism---")
ml_model.show_detail()
dl_model.show_detail()


