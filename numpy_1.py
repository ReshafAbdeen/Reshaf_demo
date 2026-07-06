#The AI Matrix Engine

import numpy as np

print("\033[1m" + "=== High-Level NumPy: The AI Matrix Engine ===" + "\033[0m\n")

inputs = np.array([25, 10, 120]) 

weights = np.array([1.5, 0.8, 0.2]) 
final_ai_score = np.dot(inputs, weights)

print("--- Neural Net Calculation ---")
print(f"Player Inputs: {inputs}")
print(f"AI Weights: {weights}")
print(f"\033[1mFinal AI Combat Score: {final_ai_score}\033[0m")


squad_scores = np.array([
    [200, 150, 300],  # 
    [180, 220, 250]   
]) 

bonus = np.array([50, 50, 50])

updated_scores = squad_scores + bonus 

print("\n--- Broadcasting Magic (Bonus Added without Loops!) ---")
print("Original Scores:\n", squad_scores)
print("Updated Scores with Bonus:\n", updated_scores)