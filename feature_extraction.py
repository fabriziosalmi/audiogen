import os
import numpy as np
import librosa
import pandas as pd

def extract_features(file_path):
    """
    Extract audio features from a file.
    :param file_path: Path to the audio file.
    :return: Array of extracted features.
    """
    y, sr = librosa.load(file_path, sr=None)
    features = {
        'chroma_stft': np.mean(librosa.feature.chroma_stft(y=y, sr=sr)),
        'rmse': np.mean(librosa.feature.rms(y=y)),
        'spectral_centroid': np.mean(librosa.feature.spectral_centroid(y=y, sr=sr)),
        'spectral_bandwidth': np.mean(librosa.feature.spectral_bandwidth(y=y, sr=sr)),
        'rolloff': np.mean(librosa.feature.spectral_rolloff(y=y, sr=sr)),
        'zero_crossing_rate': np.mean(librosa.feature.zero_crossing_rate(y)),
        'harmony': np.mean(librosa.effects.harmonic(y)),
        'perceptr_mean': np.mean(librosa.effects.percussive(y))
    }
    return features

def process_folder(folder_path):
    features_list = []
    for subdir, dirs, files in os.walk(folder_path):
        sound_type = os.path.basename(subdir)
        for file in files:
            if file.endswith('.wav'):
                file_path = os.path.join(subdir, file)
                features = extract_features(file_path)
                features['file'] = file
                features['sound_type'] = sound_type  # Add sound type label
                features_list.append(features)
    return pd.DataFrame(features_list)



if __name__ == "__main__":
    input_folder = 'tagged_sounds'
    features_df = process_folder(input_folder)
    features_df.to_csv('extracted_features.csv', index=False)

