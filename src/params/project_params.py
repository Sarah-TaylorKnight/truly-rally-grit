# == Project Variables == #

RANDOM_STATE = 42

# == Paths == #

# Note - all paths are based on github codespaces paths,
# ordinarily data would be saved externally to the repo,
# this is only done as data is not sensitive
DATA_PATHS: dict[str, str] = {
    "mh_raw": "/workspaces/truly-rally-grit/data/mental_health/01_raw_data/depression_data.csv",
    "mh_raw_train": "/workspaces/truly-rally-grit/data/mental_health/01_raw_data/depression_data_train.csv",
    "mh_raw_test": "/workspaces/truly-rally-grit/data/mental_health/01_raw_data/depression_data_test.csv",
}
