from pandas.api.types import is_numeric_dtype
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd

def prepare_data(df: pd.DataFrame, target_column: str):

    X = df.drop(columns=[target_column])
    y = df[target_column]

    X = X.drop(columns=["Applicant_ID"], errors="ignore")

    for col in X.columns:
        if not is_numeric_dtype(X[col]):   # ✅ FIX
            le = LabelEncoder()
            X[col] = le.fit_transform(X[col].astype(str))

    print("=== FINAL DATA TYPES ===")
    print(X.dtypes)

    return train_test_split(X, y, test_size=0.2, random_state=42)

#the import part splits the data into trainig and testing parts
#df is the dataset and target_col is the col we want to predict
#x has all input features and y has all  output features
#test_size is 80% for trainig and 20% for testing
#random_state is for reproducibility-ensures same split each time