import pandas as pd
from sklearn.model_selection import train_test_split
from typing import Optional
from src.params.project_params import RANDOM_STATE


def split_data(
    data: pd.DataFrame,
    stratify_column_name: Optional[str] = None,
    test_fraction: float = 0.2,
) -> tuple[pd.DataFrame]:
    """Subsample based on proportion

    Args:
        data (pd.DataFrame): data to split
        stratify_column_name (Optional[str], optional): column to stratify on if provided. Defaults to None.
        train_fraction (float, optional): proportion to allocate to train. Defaults to 0.8.

    Returns:
        tuple[pd.DataFrame]: tuple of split data, (train, test)
    """

    train_sample, test_sample = trainingSet, testSet = train_test_split(
        data,
        test_size=test_fraction,
        stratify=stratify_column_name,
        random_state=RANDOM_STATE,
    )
    test_sample = data.loc[~data.index.isin(train_sample.index)]

    return train_sample, test_sample
