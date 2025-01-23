"""Script including all preprocessing functions"""

from src.functions.helper_functions import split_data
from src.params.project_params import DATA_PATHS
from src.params.mh_params import BINARY_MAPPINGS, ORDINAL_MAPPINGS

import pandas as pd
from sklearn.pipeline import Pipeline
from tubular.mapping import MappingTransformer


def load_data() -> tuple[pd.DataFrame]:
    # Load raw data
    raw_mh_data = pd.read_csv(DATA_PATHS["mh_raw"])

    train, test = split_data(raw_mh_data)

    # Save split data for later reference if required
    train.to_csv(DATA_PATHS["mh_raw_train"])
    test.to_csv(DATA_PATHS["mh_raw_test"])

    return train, test


def create_preprocessing_pipeline() -> Pipeline:
    processing_pipeline = Pipeline(
        [
            ("map ordinal columns", MappingTransformer(mappings=ORDINAL_MAPPINGS)),
            ("map binary columns", MappingTransformer(mappings=BINARY_MAPPINGS)),
        ]
    )
