import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder


def build_preprocessing_pipeline() -> ColumnTransformer:
    """
    Builds the scikit-learn preprocessing pipeline for the California Housing dataset.
    This handles missing values, scaling for numerical features,
    and one-hot encoding for the 'ocean_proximity' categorical feature.
    """

    # Numerical features
    num_features = [
        "longitude",
        "latitude",
        "housing_median_age",
        "total_rooms",
        "total_bedrooms",
        "population",
        "households",
        "median_income",
    ]

    # Categorical features
    cat_features = ["ocean_proximity"]

    # 1. Pipeline for numeric features: Impute missing -> Scale
    num_pipeline = Pipeline(
        [("imputer", SimpleImputer(strategy="median")), ("scaler", StandardScaler())]
    )

    # 2. Pipeline for categorical features: Impute missing -> One-Hot Encode
    cat_pipeline = Pipeline(
        [
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("one_hot", OneHotEncoder(sparse_output=False, handle_unknown="ignore")),
        ]
    )

    # Combine both pipelines using ColumnTransformer
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", num_pipeline, num_features),
            ("cat", cat_pipeline, cat_features),
        ],
        remainder="drop",  # Drops any column not specified above (like target if passed)
    )

    return preprocessor


if __name__ == "__main__":
    # Test execution
    print("Building Data Preprocessing Pipeline...")
    pipeline = build_preprocessing_pipeline()
    print("Pipeline built successfully!")
