# 🎵 Audiogen: AI-Powered Sound Generation & Classification 🎶

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![License: MIT](https://img.shields.io/badge/License-MIT-green) ![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen)

## 🌟 Overview

**Audiogen** is an advanced sound generation and classification tool powered by AI and machine learning! 🎧 Whether you're a musician, sound engineer, or developer, Audiogen provides an intuitive way to create unique sounds, classify audio, and build custom sound models with ease.

## ✨ Features

- 🎤 **Sound Generation**: Create unique sounds using pre-trained models through Python scripts or a command-line interface (CLI).
- 🎚️ **Audio Classification**: Automatically classify audio files into different sound types using machine learning models.
- ⚙️ **Machine Learning Model Training**: Train your own sound classification models using extracted audio features.
- 📊 **Audio Feature Extraction**: Extract and analyze a wide range of audio features (e.g., chroma_stft, rmse, spectral centroid).
- 🗂️ **Data Preparation**: Organize and tag sound files for training and testing.
- 🔧 **Customizable Pipelines**: Fine-tune models, adjust feature extraction parameters, and customize the sound generation pipeline.
- 🛠️ **Integration Ready**: Seamlessly integrate sound generation and classification capabilities into your own applications.

## 🛠️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/fabriziosalmi/audiogen.git
   cd audiogen
   ```

2. **Install the Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

### 🔊 Generate Sounds

#### Command Line Interface
Generate specific types of sounds using the CLI:

```bash
python generate_sound_cli.py --sound_type <your_sound_type>
```

#### Python Script
Integrate sound generation into your Python projects:

```python
from sound_generation import generate_sound

generate_sound(model, input_features)
```

### 🏋️‍♂️ Train a Model

1. **Prepare Your Data**: Extract features from your audio files:
   ```python
   from feature_extraction import extract_features

   features = extract_features('path/to/audio/file.wav')
   ```

2. **Train the Model**:
   ```python
   from model_training import train_model, load_features

   features_df = load_features('extracted_features.csv')
   model = train_model(features_df)
   ```

### 📊 Extract Features

Extract features from audio files using:

```python
from feature_extraction import extract_features

features = extract_features('path/to/audio/file.wav')
```

### 🗂️ Prepare Your Data

Organize and tag your sound files:

```python
from data_preparation import tag_sounds

tag_sounds('input/folder', 'output/folder', 'tags.json')
```

## 🤝 Contributing

We welcome contributions! Please check out our [contributing guidelines](CONTRIBUTING.md) to get started.

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
