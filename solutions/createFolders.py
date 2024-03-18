# Script for creating all folders in each directory
import os


folders = [
    folder
    for folder in os.listdir("./solutions")
    if os.path.isdir(os.path.join("./solutions", folder))
]

for folder in folders:
    path = f"./solutions/{folder}"
    
    os.makedirs(f"{path}/bonus", exist_ok=True)
    os.makedirs(f"{path}/problem1", exist_ok=True)
    os.makedirs(f"{path}/problem2", exist_ok=True)
    os.makedirs(f"{path}/problem3", exist_ok=True)

    for problem in ["bonus", "problem1", "problem2", "problem3"]:
        with open(f"{path}/{problem}/main.py", "w") as f:
            pass