import cv2
import numpy as np
import os
import pandas as pd
import skimage.feature as skft
import pickle   

def feature_extraction(filename):
    # path to the directory containing the grayscale images
    grayscale_images_dir = 'uploads'
    # path to the directory where the CSV file will be saved
    csv_file_path = 'extracted.csv'

    # create an empty list to store the features
    features = []

    # load the image
    image = cv2.imread(os.path.join(grayscale_images_dir, filename), 0)

    # extract 10 different features from the image
    feature1 = skft.corner_harris(image).mean()
    feature2 = skft.blob_doh(image).mean()
    if np.isnan(feature2):
        feature2 = 0.0
    feature3 = skft.blob_log(image).mean()
    if np.isnan(feature3):
        feature3 = 0.0
    feature4 = skft.blob_dog(image).mean()
    if np.isnan(feature4):
        feature4 = 0.0
    feature5 = skft.peak_local_max(image).mean()
    feature6 = skft.hog(image).mean()
    feature7 = cv2.mean(image)[0]
    feature8 = skft.canny(image).mean()
    feature9 = cv2.minMaxLoc(image)[0]
    feature10 = cv2.minMaxLoc(image)[1]

    # append the features to the list
    features.append([feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8, feature9, feature10])

    # create a Pandas DataFrame from the list of features
    df = pd.DataFrame(features, columns=['HOG', 'LBP1', 'LBP2', 'Contrast', 'Dissimilarity', 'Homogeneity', 'Energy', 'Correlation', 'ASM', 'f10'])

    # save the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False)

    return df

