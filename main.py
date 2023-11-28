import data_preparation
import feature_extraction
import model_training
import sound_generation
import utils

def main():
    utils.setup_logging()

    # Step 1: Data Preparation
    data_preparation.process()  # Assuming a process function in data_preparation.py

    # Step 2: Feature Extraction
    feature_extraction.process_folder('tagged_sounds')

    # Step 3: Model Training
    features_df = feature_extraction.load_features('extracted_features.csv')
    model = model_training.train_model(features_df)

    # Step 4: Sound Generation
    # Example: Generating a sound based on random features
    input_features = model_training.generate_random_features(model)
    sound_generation.generate_and_save_sound(model, input_features, 'generated_sound.wav')

if __name__ == "__main__":
    main()
