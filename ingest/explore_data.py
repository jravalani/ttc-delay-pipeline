# %%
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"

# %%
df = pd.read_csv(DATA_DIR / "ttc_subway_delay_data_since_2025.csv")

# %%
df.head(15)
# %%
df.shape

# %%
df.columns

# %%
df.dtypes

# %%
df.isna().sum()

# %%
df["Time"].str.len().value_counts()

# %%
df["_id"].is_unique
# %%
