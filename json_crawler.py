import json
import os
import urllib.request as req

sets = ['RNA', 'KHM', 'NEO']
output_folder = 'images_crawler_raw'

# check folders
for s in sets:
    path = os.path.join(output_folder, s)
    if not os.path.exists(path):
        os.mkdir(path)

json_file = json.load(open('json/default-cards-20220313210300.json'))

for line in json_file:
    try:
        if line['set'].upper() in sets:
            if line['layout'] == 'modal_dfc' or line['layout'] == 'transform':
                req.urlretrieve(line['card_faces'][0]['image_uris']['normal'], os.path.join(output_folder, line['set'].upper(), line['card_faces'][0]['name'].replace(' // ', '_') + '.jpg'))
                req.urlretrieve(line['card_faces'][1]['image_uris']['normal'], os.path.join(output_folder, line['set'].upper(), line['card_faces'][1]['name'].replace(' // ', '_') + '.jpg'))
            else:
                req.urlretrieve(line['image_uris']['normal'], os.path.join(output_folder, line['set'].upper(), line['name'].replace(' // ', '_') + '.jpg'))
                
    except NameError:
        print(line['name'])