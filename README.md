# 🎵 AudioGen: AI-Powered Sound Generation & Classification 🎶

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen)](CONTRIBUTING.md)

## 🌟 Overview

**AudioGen** is a powerful and versatile tool that leverages AI and machine learning to generate, classify, and analyze audio.  Whether you're a musician looking for unique soundscapes, a sound engineer needing efficient audio classification, or a developer wanting to integrate audio intelligence into your applications, AudioGen provides an intuitive and customizable platform to bring your sonic visions to life.  Imagine creating custom sound effects for a video game, automatically tagging audio files in a large library, or even generating entirely new musical compositions – AudioGen makes it possible.

## ✨ Key Features

*   🎤 **Sound Generation:**  Generate diverse and original sounds using pre-trained models or your own custom-trained models. Create everything from realistic ambient noises to synthesized instrument sounds, all from Python or a command-line interface.
*   🎚️ **Audio Classification:** Automatically categorize audio files into predefined sound types (e.g., "speech," "music," "nature sounds").  Leverage pre-trained models for immediate use or train your own classifiers for specialized sound recognition tasks.
*   🧠 **Custom Model Training:**  Train your own sound classification models using extracted audio features and your own datasets.  Fine-tune models to achieve optimal accuracy for your specific audio needs.
*   📊 **Advanced Feature Extraction:**  Extract a wide range of audio features (e.g., Chroma STFT, Root Mean Square Energy (RMSE), Spectral Centroid, MFCCs) to gain deeper insights into your audio data.
*   📂 **Data Preparation Tools:**  Organize, tag, and prepare audio datasets for efficient model training and evaluation.  Utilities for splitting audio files, converting formats, and creating balanced datasets.
*   🔧 **Customizable Pipelines:** Tailor every step of the audio processing workflow, from feature extraction parameters to model architectures. Experiment with different configurations to optimize performance and create truly unique audio experiences.
*   🔌 **Seamless Integration:**  Easily integrate AudioGen's capabilities into your existing Python applications, web services, or audio processing pipelines.

## 🛠️ Installation

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/fabriziosalmi/audiogen.git
    cd audiogen
    ```

2.  **Create a Virtual Environment (Recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate on Windows
    ```

3.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

### 🔊 Generate Sounds

#### Command Line Interface (CLI)

Generate a "synth" sound using the CLI:

```bash
python generate_sound_cli.py --sound_type synth --output synth_sound.wav
```

This will generate a sound and save it as `synth_sound.wav`. Check the documentation for supported sound types and other options.

#### Python Script

Integrate sound generation directly into your Python code:

```python
from audiogen.sound_generation import generate_sound  # Adjust import based on your project structure

# Example usage (replace with your actual model and features)
model = load_your_trained_model()  # Replace with your model loading code
input_features = {'frequency': 440, 'duration': 2} # Sample features (adjust as needed)
sound = generate_sound(model, input_features)

# Save the generated sound (example using a library like soundfile)
import soundfile as sf
sf.write('generated_sound.wav', sound, samplerate=44100)
print("Sound generated and saved as generated_sound.wav")
```

**Important:**  The `sound_generation` module and its related functions are placeholders. You'll need to adapt the code based on your specific implementation.

### 🏋️‍♂️ Train a Model

1.  **Prepare Your Audio Data:** Organize your audio files into folders representing different classes (e.g., `dogs`, `cats`, `birds`).

2.  **Extract Features:**

    ```python
    from audiogen.feature_extraction import extract_features  # Adjust import based on your project structure

    features = extract_features('path/to/audio/dog_bark.wav')
    print(features)  # Print the extracted features (e.g., as a dictionary)
    ```

    This will output a dictionary containing the extracted audio features for the provided audio file.

3.  **Train the Model:**

    ```python
    from audiogen.model_training import train_model, load_features  # Adjust import based on your project structure
    import pandas as pd

    # Assuming you have extracted features and saved them in a CSV file
    features_df = pd.read_csv('extracted_features.csv') # Use pandas for loading

    # Assuming your CSV has a 'label' column for audio class
    model = train_model(features_df, label_column='label')

    # Save the trained model
    import joblib
    joblib.dump(model, 'trained_sound_classifier.pkl')
    print("Model trained and saved as trained_sound_classifier.pkl")
    ```

    **Important:** The `model_training` module and its related functions are placeholders.  Implement your training logic using libraries like scikit-learn, TensorFlow, or PyTorch.  The example uses Pandas to load a CSV.  Adjust this based on how you manage your extracted features.

### 📊 Extract Features

```python
from audiogen.feature_extraction import extract_features  # Adjust import based on your project structure

features = extract_features('path/to/audio/sample.wav')
print(features)
```

This will print a dictionary or other data structure containing the extracted features.  Refer to the documentation for a list of available features and their meanings.

### 📂 Data Preparation

```python
from audiogen.data_preparation import tag_sounds  # Adjust import based on your project structure

tag_sounds('input/audio_folder', 'output/labeled_audio', 'audio_tags.json')
```

This function (and the module itself) needs to be implemented based on your desired data preparation strategy. Consider using libraries like `pydub` for audio manipulation.

## 📚 Documentation

Comprehensive documentation is available in the `docs/` directory.  This includes:

*   API reference
*   Tutorials
*   Examples
*   Troubleshooting guide

## 🤝 Contributing

We welcome contributions of all kinds! Please see our [contributing guidelines](CONTRIBUTING.md) for details on how to get involved.  Areas for contribution include:

*   Adding new sound generation models
*   Improving existing audio classifiers
*   Developing new audio features
*   Writing documentation
*   Creating example scripts
*   Fixing bugs

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
