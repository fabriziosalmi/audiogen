import numpy as np
import joblib
from scipy.signal import chirp, spectrogram
import matplotlib.pyplot as plt
import soundfile as sf

def load_model(model_file):
    """
    Load the trained model from a file.
    :param model_file: Path to the model file.
    :return: Loaded model.
    """
    return joblib.load(model_file)

def generate_sound_features(model, input_features):
    """
    Generate new sound features using the model.
    :param model: Trained model.
    :param input_features: Input features to base the generation on.
    :return: Generated sound features.
    """
    return model.predict([input_features])[0]

def synthesize_sound(features):
    """
    Synthesize a sound from given features.
    :param features: Features of the sound to generate.
    :return: Synthesized sound as a numpy array.
    """
    t = np.linspace(0, 1, int(44100))
    synthesized_sound = chirp(t, f0=features[0], f1=features[-1], t1=1, method='linear')
    return synthesized_sound

if __name__ == "__main__":
    model_file = 'audio_model.pkl'
    model = load_model(model_file)

    # Example: Generating a sound based on random features
    input_features = np.random.rand(model.n_features_)
    generated_features = generate_sound_features(model, input_features)
    sound = synthesize_sound(generated_features)

    # Save the generated sound to a file
    sf.write('generated_sound.wav', sound, 44100)

    # Optional: Display a spectrogram of the generated sound
    f, t, Sxx = spectrogram(sound, 44100)
    plt.pcolormesh(t, f, Sxx, shading='gouraud')
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.show()
