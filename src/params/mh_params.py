# == Column groupings == #

TARGET = "History of Mental Illness"

# Column groups come from investigation in
# analysis/mental_health_investigation/01_initial_data_prep.ipynb

BINARY_COLUMNS = [
    "History of Mental Illness",
    "History of Substance Abuse",
    "Family History of Depression",
    "Chronic Medical Conditions",
]

# == Mappings == #

# Mappings come from investigation in
# analysis/mental_health_investigation/01_initial_data_prep.ipynb

BINARY_MAP = {"Yes": 1, "No": 0}
BINARY_MAPPINGS = {col: BINARY_MAP for col in BINARY_COLUMNS}

ORDINAL_MAPPINGS = {
    "Education Level": {
        "High School": 0,
        "Associate Degree": 1,
        "Bachelor's Degree": 2,
        "Master's Degree": 3,
        "PhD": 4,
    },
    "Physical Activity Level": {
        "Sedentary": 0, 
        "Moderate": 1,
        "Active": 2, 
    },
    "Alcohol Consumption": {
        "Low": 0,
        "Moderate": 1, 
        "High": 2, 
    },
    "Dietary Habits": {
        "Unhealthy": 0, 
        "Moderate": 1, 
        "Healthy": 2,
    },
    "Sleep Patterns": {
        "Poor": 0,
        "Fair": 1, 
        "Good": 2, 
    },
}
