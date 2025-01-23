import pandas as pd
import numpy as np
import pytest

from src.functions.helper_functions import split_data


class TestSplitData:
    @pytest.mark.parametrize("split_fraction", [0, 0.2, 0.7, 1, None])
    def test_returned_rowcount_correct(self, split_fraction):
        df_to_split = pd.DataFrame(
            np.random.randint(0, 100, size=(100, 4)), columns=list("ABCD")
        )

        train, test = split_data(df_to_split)

        msg = f"Row count is not as required after splitting.\nBefore: {len(df_to_split)}\nAfter: {len(train) + len(test)}"

        assert len(df_to_split) == len(train) + len(test), msg
