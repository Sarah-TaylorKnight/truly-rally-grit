from src.mental_health_investigation.preprocess_data import load_data


if __name__ == "__main__":
    train, test = load_data()
    # Process each sample based on findings in 01_initial_data_prep.ipynb
