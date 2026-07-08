#Python Loop vs NumPy Vectorization

import numpy as np
import time

print("\033[1m"+"==Welcome to Numpy Vs Python Loops=="+"\033[0m")

size = 1000000
python_loop = list(range(size))
numpy = np.arange(size)
print(f"Loading {size} records in memory")

print("\n======Python Loop Test=====")
start_time_py = time.time()
python_result = [x * 5 for x in python_loop]
end_time_py = time.time()
py_duration = end_time_py - start_time_py
print(f"Numpy Time Duration {py_duration:.4f} second")

print("\n======Numpy Test======")
start_time_np = time.time()
numpy_result = numpy * 5
end_time_np = time.time()
numpy_duration = end_time_np - start_time_np
print(f"Numpy Time Duration {numpy_duration:.4f} second")

speed_duration = py_duration / numpy_duration
print(f"\n\033[1m Result :Numpy is {speed_duration}x Faster!\033[0m")