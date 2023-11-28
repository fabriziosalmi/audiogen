import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)


def load_features(features_file):
    """
    Load extracted features from a CSV file.
    :param features_file: Path to the CSV file containing extracted features.
    :return: DataFrame with features.
    """
    return pd.read_csv(features_file)

def train_model(features_df):
    """
    Train a classification model on the provided features.
    :param features_df: DataFrame containing features and sound type labels.
    :return: Trained model.
    """
    if 'sound_type' not in features_df.columns:
        raise ValueError("The 'sound_type' column is missing from the features DataFrame.")

    X = features_df.drop(columns=['file', 'sound_type'])
    y = features_df['sound_type']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print(f"Model Training Accuracy: {model.score(X_test, y_test)}")

    return model

if __name__ == "__main__":
    features_file = 'extracted_features.csv'
    features_df = load_features(features_file)

    model = train_model(features_df)
    joblib.dump(model, 'sound_type_classifier.pkl')

