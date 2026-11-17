# vision.py
import io
import os
from dotenv import load_dotenv
from google.cloud import vision

load_dotenv()


def extract_text(file_path):
    """Runs OCR on an image and returns the full detected text block."""
    client = vision.ImageAnnotatorClient()
    with io.open(file_path, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    response = client.text_detection(image=image)

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

    texts = response.text_annotations
    return texts[0].description if texts else ""
    # texts[0] for full block; texts[1:] for single words w box bounds


if __name__ == '__main__':
    print(extract_text(os.path.abspath('WorkDates.jpg')))