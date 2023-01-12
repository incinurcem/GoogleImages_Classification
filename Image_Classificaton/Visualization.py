from Exploratory_Data_Analysis import train_images,train_labels,test_images,test_labels,class_names
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



#Plot bar representation of data

_, train_counts = np.unique(train_labels, return_counts=True)
_, test_counts = np.unique(test_labels, return_counts=True)
pd.DataFrame({'train': train_counts,
              'test': test_counts},
             index=class_names
             ).plot.bar()
plt.show()



train_images = train_images / 255.0
test_images = test_images / 255.0





#Random display of a photo

def display_random_image(class_names, images, labels):
  
    index = np.random.randint(images.shape[0])
    plt.figure()
    plt.imshow(images[index])
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.title('Image #{} : '.format(index) + class_names[labels[index]])
    plt.show()

display_random_image(class_names, train_images, train_labels)





#Random display of photos corresponding labels

def display_examples(class_names, images, labels):
    fig = plt.figure(figsize=(10,10))
    fig.suptitle("Some examples of images of the dataset", fontsize=16)
    for i in range(25):
        index = np.random.randint(images.shape[0])
        plt.subplot(5,5,i+1)
        plt.xticks([])
        plt.yticks([])
        plt.grid(False)
        plt.imshow(images[index], cmap=plt.cm.binary)
        plt.xlabel(class_names[labels[index]])
    plt.show()

display_examples(class_names, train_images, train_labels)