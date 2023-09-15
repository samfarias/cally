import io
import os
import json

#Imports the Google Cloud Client Library
from google.cloud import vision

#set the os GCP APP variable
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'cloudvisionkey.json'

#name of image path to send
file_name = os.path.abspath('/Users/sam/Documents/cally/Test-OCR-Handwritten.jpg')

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

        # out_file=open("file.json", "a")
        # json.dump((text), out_file)


    # out_file=open("file.json", "w")
    # json.dump((text.description)+("hi"), out_file)
    #

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


#run our program
detect_text(file_name)


# Parse the JSON response
# response_json = json.loads(api_response_text)
# relevant_data = response_json['data']


#         #print incoming json description     ##########O--O############
#         writeFile =open('file_name.json', 'w')
#         writeFile.write(texts)

# # Create a new JSON file and write the relevant data to it
# with open('output.json', 'w') as outfile:
#     json.dump(relevant_data, outfile)
# writeFile.close(output.json)



