import pandas as pd

def export_to_csv(data, path="data/output.csv"):
    df = pd.DataFrame(data)
    df.to_csv(path, index=False)