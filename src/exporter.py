import pandas as pd
import os

def export_to_csv(data, path="data/output.csv"):
    os.makedirs(os.path.dirname(path), exist_ok=True)  # <-- FIX
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)
