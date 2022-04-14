import albumentations as A
import cv2
import os

source_folder = 'images_training_raw'
target_folder = 'images_training_generated'

def transformImage(file_image, target):
    transform = A.Compose([
        A.RandomBrightnessContrast(p=0.2),
        A.Blur(p=1.5),
        A.Downscale(p=1.5)
    ])

    image = cv2.imread(file_image)
    result = transform(image=image)["image"]

    cv2.imwrite(os.path.join(target, 'generated_' + file_image.split('/')[-1]), result)

if not os.path.exists(target_folder):
    os.mkdir(target_folder)

if os.path.exists(source_folder):
    for sub_folder in os.listdir(source_folder):
        full_source_folder = os.path.join(source_folder, sub_folder)
        full_target_folder = os.path.join(target_folder, sub_folder)

        if not os.path.exists(full_target_folder):
            os.mkdir(full_target_folder)

        for file in os.listdir(full_source_folder):
            transformImage(os.path.join(full_source_folder, file), full_target_folder)