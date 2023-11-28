import os
import json
from pydub import AudioSegment

def load_tags(tags_file):
    """
    Load tags from a JSON file.
    :param tags_file: Path to the JSON file containing tags.
    :return: Dictionary of tags.
    """
    with open(tags_file, 'r') as file:
        tags = json.load(file)
    return tags

def tag_sounds(input_folder, output_folder, tags):
    """
    Organize and tag sound files.
    :param input_folder: Folder containing input sound files.
    :param output_folder: Folder where tagged sound files will be saved.
    :param tags: Dictionary of tags for categorizing sounds.
    """
    for sound_file in os.listdir(input_folder):
        sound_path = os.path.join(input_folder, sound_file)
        sound = AudioSegment.from_file(sound_path)
        
        for tag, criteria in tags.items():
            if criteria in sound_file:
                tagged_folder = os.path.join(output_folder, tag)
                if not os.path.exists(tagged_folder):
                    os.makedirs(tagged_folder)
                sound.export(os.path.join(tagged_folder, sound_file), format='wav')

if __name__ == "__main__":
    input_folder = 'input_sounds'
    output_folder = 'tagged_sounds'
    tags_file = 'sound_tags.json'

    tags = load_tags(tags_file)
    tag_sounds(input_folder, output_folder, tags)
