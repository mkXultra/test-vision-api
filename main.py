import io
from google.cloud import vision

client = vision.ImageAnnotatorClient()
with io.open('img/img.png', 'rb') as image_file:
    content = image_file.read()
image = vision.Image(content=content)

response = client.text_detection(image=image)
print(response)

texts = response.text_annotations

for text in texts:
    print(text.description)