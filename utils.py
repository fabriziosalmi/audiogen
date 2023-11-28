import json
import logging

def setup_logging():
    """
    Setup logging configuration.
    """
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def save_json(data, filename):
    """
    Save data to a JSON file.
    :param data: Data to be saved.
    :param filename: Name of the file to save the data in.
    """
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

def load_json(filename):
    """
    Load data from a JSON file.
    :param filename: Name of the file to load the data from.
    :return: Loaded data.
    """
    with open(filename, 'r') as file:
        return json.load(file)

def normalize_data(data):
    """
    Normalize data.
    :param data: Data to be normalized.
    :return: Normalized data.
    """
    return (data - data.min()) / (data.max() - data.min())
