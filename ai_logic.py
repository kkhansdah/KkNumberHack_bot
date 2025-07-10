
import json
from collections import Counter

# Load memory from file
def load_memory():
    try:
        with open("memory.json", "r") as f:
            return json.load(f)
    except:
        return {}

# Basic AI Prediction Logic
def predict_numbers(last10, memory):
    # Frequency count
    freq = Counter(last10)
    top = freq.most_common(3)

    # Pattern 1: Most Frequent
    p1 = [x[0] for x in top]

    # Pattern 2: From memory file (trained on last 5 numbers)
    key = "-".join(map(str, last10[-5:]))
    p2 = memory.get(key, [])

    # Merge both predictions with priority
    result = list(dict.fromkeys(p2 + p1))[:3]

    logic = "Pattern Memory + Frequency"
    return result, logic

# Accuracy checker
def update_accuracy(predicted, actual):
    return actual in predicted
