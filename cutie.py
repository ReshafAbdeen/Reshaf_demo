class AImodel:
    def __init__(self, model_name, accuracy):
        self.name = model_name
        self.accuracy = accuracy

    def show_detail(self):
        print(f"Model ka Name {self.name}")
        print(f"Model ki accuracy {self.accuracy}")

    def predict(self, data):
        print(f"{self.name} is predicting result for {data}")


model1 = AImodel("Zomato_Rzter", 93.4)
model2 = AImodel("Desi_chatgpt", 94.3)

print("\n---Model1 Testing---")
model1.show_detail()
model1.predict("Zomato resturant ka data")


print("\n---Model2 Testing---")
model2.show_detail()
model2.predict("Bhai python oops kiya hota hai")