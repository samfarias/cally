import io
import os
import json

#Imports the Google Cloud Client Library
from google.cloud import vision

#set the os GCP APP variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'cloudvisionkey.json'

#name of image path to send
file_name = os.path.abspath('/Users/sam/Documents/cally/mockschedule.jpeg')

#image = types.Image(content=content)
def detect_text(file_name):
    """Detects text in the file."""
    
    #instantiates a new client
    client = vision.ImageAnnotatorClient()
    #ah yeah. this loads image onto memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
 

    for text in texts:
        print(text)
        print('\n"{}"'.format(text.description))
        

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


#run our program
detect_text(file_name)



