def save_to_csv(data, filename):
    import pandas as pd
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

def load_from_csv(filename):
    import pandas as pd
    return pd.read_csv(filename)

def generate_summary_statistics(data):
    import pandas as pd
    df = pd.DataFrame(data)
    return df.describe()