from tqdm import tqdm
import cv2
import numpy as np
import os


#Preparing for class

class_names = ['foggy', 'rainy', 'snowy', 'sunny']
class_names_label = {class_name: i for i, class_name in enumerate(class_names)}

nb_classes = len(class_names)

IMAGE_SIZE = (150, 150)



# Settings of labels and photos

def load_data():

    datasets = ['/Desktop/dataset/train', '/Desktop/dataset/test']
    output = []

    for dataset in datasets:
        images = []
        labels = []

        print("Loading {}".format(dataset))
        
        for folder in os.listdir(dataset):
            label = class_names_label[folder]
            
            for file in tqdm(os.listdir(os.path.join(dataset, folder))):
                img_path = os.path.join(os.path.join(dataset, folder), file)

                image = cv2.imread(img_path)
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
                image = cv2.resize(image, IMAGE_SIZE)

                images.append(image)
                labels.append(label)

        images = np.array(images, dtype='float32')
        labels = np.array(labels, dtype='int32')

        output.append((images, labels))

    return output


#Assigning datas to variables with the help of function

(train_images, train_labels), (test_images, test_labels) = load_data()



#Checking size and shape of datas 

n_train = train_labels.shape[0]
n_test = test_labels.shape[0]

print("Number of training labels: {}".format(n_train))
print("Number of testing labels: {}".format(n_test))
print("Each image is of size: {}".format(IMAGE_SIZE))
print("train image size:", train_images.shape)
print("test image size:", test_images.shape)



#Shaping of photos

train_images = train_images.reshape(1600, 3*150*150)
test_images = test_images.reshape(400, 3*150*150)
