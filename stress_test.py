# ==========================================
# OS-Lab 01: CPU Stress Test
# Student ID:  [67128389]
# ==========================================
import math
import time

# TODO: Write the intensive computation loop here
# Follow the instructions in the Lab manual.
print("Starting CPU Stress Test... Press Ctrl+C to stop.")
while True:
    math.factorial(50000)  # Intensive calculation