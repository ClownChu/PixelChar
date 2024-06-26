import random
from PIL import Image
import re

def generate_detailed_character_base():
    """
    Randomly selects and generates a detailed base for a character from a set of variations.
    Each base variation has a unique layout or theme.
    """

    base_variation = [
        [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # Hair 1
        [0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0,   0],  # Hair 2
        [0,   0,   0,   0,   1,   1,   1,   1,   1,   1,   0,   0,   0,   0],  # Hair 3
        [0,   0,   0,   1,   1,   1,   1,   1,   1,   1,   1,   0,   0,   0],  # Hairline
        [0,   0,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   0,   0],  # Top-Forehead
        [0,   0,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   0,   0],  # Bottom-Forehead
        [0,   0,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   0,   0],  # Eyes
        [0,   0,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   0,   0],  # Nose
        [0,   0,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   0,   0],  # Nose bridge
        [0,   0,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   0,   0],  # Top-Mouth
        [0,   0,   0,   1,   1,   1,   1,   1,   1,   1,   1,   0,   0,   0],  # Face with patch
        [0,   0,   0,   0,   1,   1,   1,   1,   1,   1,   0,   0,   0,   0],  # Chin
        [0,   0,   0,   0,   0,   0,   1,   1,   0,   0,   0,   0,   0,   0],  # Neck
        [0,   0,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   0,   0],  # Shirt Colar
        [0,   0,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   0,   0],  # Shirt Top-Middle
        [0,   0,   1,   1,   1,   1,   1,   1,   1,   1,   1,   1,   0,   0],  # Shirt Middle
        [0,   0,   1,   0,   1,   1,   1,   1,   1,   1,   0,   1,   0,   0],  # Shirt Bottom-Middle
        [0,   0,   1,   0,   1,   1,   1,   1,   1,   1,   0,   1,   0,   0],  # Belt
        [0,   0,   1,   0,   1,   1,   1,   1,   1,   1,   0,   1,   0,   0],  # Upper Leg
        [0,   0,   0,   0,   1,   1,   0,   0,   1,   1,   0,   0,   0,   0],  # Knees
        [0,   0,   0,   0,   1,   1,   0,   0,   1,   1,   0,   0,   0,   0],  # Calf
        [0,   0,   1,   1,   1,   1,   0,   0,   1,   1,   1,   1,   0,   0],  # Shoes
    ]

    eye_styles = {
        'normal': {
            1: [
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 1
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 2
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 3
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hairline
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Top-Forehead
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Bottom-Forehead
                [  -1,  -1,  -1,  -1,   5,  -1,  -1,  -1,  -1,   5,  -1,  -1,  -1,  -1],  # Eyes
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Nose
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Nose bridge
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Top-Mouth
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Face with patch
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Chin
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Neck
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Colar
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Top-Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Bottom-Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Belt
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Upper Leg
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Knees
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Calf
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shoes
            ],
        },
    }

    nose_styles = {
        'normal': {
            1: [
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 1
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 2
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 3
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hairline
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Top-Forehead
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Bottom-Forehead
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Eyes
                [  -1,  -1,  -1,  -1,  -1,  -1,   9,   9,  -1,  -1,  -1,  -1,  -1,  -1],  # Nose
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Nose bridge
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Top-Mouth
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Face with patch
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Chin
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Neck
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Colar
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Top-Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Bottom-Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Belt
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Upper Leg
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Knees
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Calf
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shoes
            ],
        },
    }

    ears_styles = {
        'normal': {
            1: [
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 1
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 2
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 3
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hairline
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Top-Forehead
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Bottom-Forehead
                [  -1,   9,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,   9,  -1],  # Eyes
                [  -1,   9,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,   9,  -1],  # Nose
                [  -1,   9,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,   9,  -1],  # Nose bridge
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Top-Mouth
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Face with patch
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Chin
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Neck
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Colar
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Top-Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Bottom-Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Belt
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Upper Leg
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Knees
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Calf
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shoes
            ],
        },
    }

    mouth_styles = {
        'smiling': {
            1: [
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 1
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 2
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 3
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hairline
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Top-Forehead
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Bottom-Forehead
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Eyes
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Nose
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Nose bridge
                [  -1,  -1,  -1,  -1,   6,  -1,  -1,  -1,  -1,   6,  -1,  -1,  -1,  -1],  # Top-Mouth
                [  -1,  -1,  -1,  -1,  -1,   6,   6,   6,   6,  -1,  -1,  -1,  -1,  -1],  # Face with patch
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Chin
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Neck
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Colar
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Top-Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Bottom-Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Belt
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Upper Leg
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Knees
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Calf
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shoes
            ],
        },
    }

    hair_styles = {
        'short': {
            1: [
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 1
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 2
                [  -1,  -1,  -1,  -1,  11,  11,  11,  11,  11,  11,  -1,  -1,  -1,  -1],  # Hair 3
                [  -1,  -1,  -1,  11,  11,  11,  -1,  11,  -1,  11,  11,  -1,  -1,  -1],  # Hairline
                [  -1,  -1,  11,  11,  -1,  11,  -1,  -1,  11,  -1,  11,  11,  -1,  -1],  # Top-Forehead
                [  -1,  -1,  11,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  11,  -1,  -1],  # Bottom-Forehead
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Eyes
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Nose
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Nose bridge
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Top-Mouth
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Face with patch
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Chin
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Neck
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Colar
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Top-Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Bottom-Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Belt
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Upper Leg
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Knees
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Calf
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shoes
            ]
        },
        'long': {
            1: [
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 1
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 2
                [  -1,  -1,  -1,  -1,  11,  11,  11,  11,  11,  11,  -1,  -1,  -1,  -1],  # Hair 3
                [  -1,  -1,  -1,  11,  11,  11,  -1,  11,  -1,  11,  11,  -1,  -1,  -1],  # Hairline
                [  -1,  -1,  11,  11,  -1,  11,  -1,  -1,  11,  -1,  11,  11,  -1,  -1],  # Top-Forehead
                [  -1,  -1,  11,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  11,  -1,  -1],  # Bottom-Forehead
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Eyes
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Nose
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Nose bridge
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Top-Mouth
                [  -1,  -1,  11,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  11,  -1,  -1],  # Face with patch
                [  -1,  -1,  11,  11,  -1,  -1,  -1,  -1,  -1,  -1,  11,  11,  -1,  -1],  # Chin
                [  -1,  -1,  11,  11,  11,  -1,  -1,  -1,  -1,  11,  11,  11,  -1,  -1],  # Neck
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Colar
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Top-Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Bottom-Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Belt
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Upper Leg
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Knees
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Calf
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shoes
            ]
        },
    }

    shirt_styles = {
        'short': {
            1: [
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 1
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 2
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 3
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hairline
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Top-Forehead
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Bottom-Forehead
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Eyes
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Nose
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Nose bridge
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Top-Mouth
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Face with patch
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Chin
                [  -1,  -1,  -1,  -1,  -1,   2,  -1,  -1,   2,  -1,  -1,  -1,  -1,  -1],  # Neck
                [  -1,  -1,   2,   2,   2,   2,   2,   2,   2,   2,   2,   2,  -1,  -1],  # Shirt Colar
                [  -1,  -1,   2,   2,   2,   2,   2,   2,   2,   2,   2,   2,  -1,  -1],  # Shirt Top-Middle
                [  -1,  -1,   2,   2,   2,   2,   2,   2,   2,   2,   2,   2,  -1,  -1],  # Shirt Middle
                [  -1,  -1,  -1,  -1,   2,   2,   2,   2,   2,   2,  -1,  -1,  -1,  -1],  # Shirt Bottom-Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Belt
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Upper Leg
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Knees
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Calf
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shoes
            ],
        },
    }

    waist_styles = {
        'belt': {
            1: [
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 1
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 2
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 3
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hairline
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Top-Forehead
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Bottom-Forehead
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Eyes
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Nose
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Nose bridge
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Top-Mouth
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Face with patch
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Chin
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Neck
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Colar
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Top-Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Bottom-Middle
                [  -1,  -1,  -1,  -1,   7,   7,  10,  10,   7,   7,  -1,  -1,  -1,  -1],  # Belt
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Upper Leg
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Knees
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Calf
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shoes
            ],
        },
    }

    pants_styles = {
        'normal': {
            1: [
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 1
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 2
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 3
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hairline
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Top-Forehead
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Bottom-Forehead
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Eyes
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Nose
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Nose bridge
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Top-Mouth
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Face with patch
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Chin
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Neck
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Colar
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Top-Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Bottom-Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Belt
                [  -1,  -1,  -1,  -1,   3,   3,   3,   3,   3,   3,  -1,  -1,  -1,  -1],  # Upper Leg
                [  -1,  -1,  -1,  -1,   3,   3,  -1,  -1,   3,   3,  -1,  -1,  -1,  -1],  # Knees
                [  -1,  -1,  -1,  -1,   3,   3,  -1,  -1,   3,   3,  -1,  -1,  -1,  -1],  # Calf
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shoes
            ],
        },
    }

    feet_styles = {
        'shoes': {
            1: [
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 1
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 2
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 3
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hairline
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Top-Forehead
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Bottom-Forehead
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Eyes
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Nose
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Nose bridge
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Top-Mouth
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Face with patch
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Chin
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Neck
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Colar
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Top-Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Bottom-Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Belt
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Upper Leg
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Knees
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Calf
                [  -1,  -1,   4,   4,   4,   4,  -1,  -1,   4,   4,   4,   4,  -1,  -1],  # Shoes
            ],
        },
    }

    hands_styles = {
        'normal': {
            1: [
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 1
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 2
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hair 3
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Hairline
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Top-Forehead
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Bottom-Forehead
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Eyes
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Nose
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Nose bridge
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Top-Mouth
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Face with patch
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Chin
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Neck
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Colar
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Top-Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shirt Bottom-Middle
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Belt
                [  -1,  -1,   8,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,   8,  -1,  -1],  # Upper Leg
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Knees
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Calf
                [  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1,  -1],  # Shoes
            ],
        },
    }

    styles = [
        get_random_style(hair_styles),
        get_random_style(eye_styles),
        get_random_style(nose_styles),
        get_random_style(mouth_styles),
        get_random_style(ears_styles),
        get_random_style(shirt_styles),
        get_random_style(pants_styles),
        get_random_style(hands_styles),
        get_random_style(waist_styles),
        get_random_style(feet_styles),
    ]
    
    for i in range(len(base_variation)):
        for j in range(len(base_variation[i])):
            for style in styles:
                if style[i][j] !=  -1:
                    base_variation[i][j] = style[i][j]

    if random.choice([True, False]):
        base_variation = base_variation + [
            [   0,   0,   4,   4,   0,   4,   0,   0,   4,   0,   4,   4,   0,   0],  # Heils
        ]

    variations = [base_variation]
    selected_base = random.choice(variations)

    final_character_base = selected_base
    return final_character_base

def get_random_style(styles):
    style_type = random.choice(list(styles.keys()))
    num_of_variations = len(styles[style_type])
    style_variation = random.randint(1, num_of_variations)
    style = styles[style_type][style_variation]
    return style

def adjust_color(base_color, min_difference=25, contrast=False):
    """Adjust a color to ensure it has a minimum difference from the base_color and optionally contrast."""
    adjusted_color = []
    for base_channel in base_color:
        if contrast:
            channel = base_channel - min_difference if base_channel >  128 else base_channel + min_difference
        else:
            channel = random.randint(0,  255)
            while abs(channel - base_channel) < min_difference:
                channel = random.randint(0,  255)
        adjusted_color.append(max(0, min(channel,  255)))
    return tuple(adjusted_color)

def generate_character_colors():
    """Generate a set of colors for the character's skin, hair, clothes, etc."""
    skin_colors = [
        (255,  224,  189),  # Light skin
        (240,  184,  160),  # Light medium
        (224,  172,  105),  # Medium
        (198,  134,  66),   # Medium dark
        (141,  85,  36),    # Dark
        (91,  60,  17),     # Very dark
        (70,  40,  10),     # Lighter black
        (40,  20,   0),      # Light black
        (0,   0,   0),        # Black
    ]
    skin_color = random.choice(skin_colors)

    shirt_color = adjust_color(skin_color,  80) 

    pants_color = adjust_color(shirt_color,  80)
    shoes_color = adjust_color(pants_color,  80)

    belt_color = adjust_color(pants_color,  25, contrast=True)
    belt_knocle_color = adjust_color(belt_color,  25, contrast=True)

    eye_colors = [
        (119,  78,  59),  # Brown
        (72,  105,  148), # Blue
        (79,  114,  70),  # Green
        (37,  79,  72),   # Hazel
        (167,  85,  44),  # Amber
        (105,  82,  92),  # Gray
    ]
    eye_color = random.choice(eye_colors)

    mouth_color = adjust_color(skin_color,  50, True)
    head_parts_color = adjust_color(skin_color,  25, True)
    hands_color = adjust_color(shirt_color, contrast=True)
    hair_color = (random.randint(0,  255), random.randint(0,  255), random.randint(0,  255))

    colors = {
        -1: (0, 0, 0, 0),
        0: (0, 0, 0, 0),
        1: skin_color,
        2: shirt_color,
        3: pants_color,
        4: shoes_color,
        5: eye_color,
        6: mouth_color,
        7: belt_color,
        8: hands_color,
        9: head_parts_color,
        10: belt_knocle_color,
        11: hair_color,
    }
    return colors


def create_and_save_detailed_character(filename="character.png"):
    """Create a detailed character and save it to a file."""
    base_pixels = generate_detailed_character_base()
    colors = generate_character_colors()

    img_size = (len(base_pixels[0]), len(base_pixels))
    img = Image.new("RGBA", img_size)
    pixels = img.load()

    for y, row in enumerate(base_pixels):
        for x, pixel in enumerate(row):
            pixels[x, y] = colors.get(pixel, (0,   0,   0))

    img = img.resize((img_size[0] *  64, img_size[1] *  64), Image.NEAREST)
    img.save(filename)

if __name__ == "__main__":
    create_and_save_detailed_character()