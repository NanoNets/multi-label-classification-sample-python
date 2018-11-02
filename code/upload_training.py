import requests 
import json
import os
import random

BASE_URL = 'http://app.nanonets.com/api/v2/MultiLabelClassification/'
AUTH_KEY = os.environ.get('NANONETS_API_KEY')
MODEL_ID = os.environ.get('NANONETS_MODEL_ID')

image_folder_path = "./multilabel_data/ImageSets/"
annotations_folder = "./multilabel_data/Annotations/"

def create_image_dictionary():
    image_label_dictionary = {}
    for image in os.listdir(image_folder_path):
        annotatios_file_name  = os.path.join(annotations_folder, "%s.txt"%(image.rsplit('.', 1)[0]))
        if not os.path.isfile(annotatios_file_name):
            continue
        all_labels = [x for x in open(annotatios_file_name, 'r').read().split('\n') if x]
        image_label_dictionary[os.path.join(image_folder_path, image)] = all_labels
    return image_label_dictionary

def upload_images(model_id):
    url = BASE_URL + 'Model/%s/UploadFiles/'%(model_id)
    image_label_dictionary = create_image_dictionary()
    all_images = image_label_dictionary.keys()
    random.shuffle(all_images)
    n = len(all_images)
    for i, image in enumerate(all_images):
        if i%100==0:
            print ("%d of %d images has been uploaded"%(i, n))
        labels = image_label_dictionary[image]
        _, image_name = os.path.split(image)
        files = open(image, 'rb')
        data = {'files' : files,
                'data' :('', '[{"filename":"%s", "categories": %s}]'%(image_name, json.dumps(labels)))}
        response = requests.post(url, auth= requests.auth.HTTPBasicAuth(AUTH_KEY, ''), files=data)
    print ("%d of %d images has been uploaded"%(i, n))
    return json.loads(response.text)

if __name__=="__main__":
    upload_images(MODEL_ID)
    print("\n\n\nNEXT RUN: python ./code/train_model.py")