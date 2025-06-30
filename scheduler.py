import pandas as pd
from datetime import datetime
from collections import Counter

def parse_csv(file):
    df = pd.read_csv(file)
    return df

def suggest_meeting_time(df):
    all_slots = df.values.flatten()
    counts = Counter(all_slots)
    best_time, _ = counts.most_common(1)[0]
    return best_time
