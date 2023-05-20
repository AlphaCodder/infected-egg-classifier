# Infected Egg Classifier

![SciKitLearn](https://scikit-learn.org/stable/_static/scikit-learn-logo-small.png)
![Python](https://www.python.org/static/community_logos/python-logo-master-v3-TM.png)
![Flask](https://flask.palletsprojects.com/en/2.0.x/_images/flask-logo.png)
![KNN](https://www.newtechdojo.com/wp-content/uploads/2020/06/KNN-Head.png)

The **Infected Egg Classifier** is a powerful machine learning project that utilizes the **K-Nearest Neighbors (KNN)** algorithm to classify infected eggs. This project aims to provide an accurate and efficient solution for identifying eggs that are contaminated or infected with pathogens.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Evaluation](#evaluation)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Egg contamination is a significant concern in the food industry, as it can lead to various health risks. The Infected Egg Classifier aims to tackle this problem by leveraging the power of machine learning. The KNN algorithm is used to classify eggs based on features extracted from images, helping to identify infected eggs more efficiently.

## Installation

To use the Infected Egg Classifier, follow these steps:

1. Clone the repository:

```
git clone https://github.com/AlphaCodder/infected-egg-classifier.git
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

## Usage

After installing the required dependencies, you can run the Infected Egg Classifier using the following command:

```
python classify.py --image <path_to_image>
```

Replace `<path_to_image>` with the path to the image you want to classify.

## Dataset

The Infected Egg Classifier relies on a carefully curated dataset of infected and non-infected egg images. The dataset consists of thousands of labeled images, ensuring a robust and accurate training process.

## Model Training

To train the model from scratch, follow these steps:

1. Prepare your dataset by organizing infected and non-infected egg images into separate folders.

2. Run the following command to start the training process:

```
python train.py --data <path_to_dataset> --k <value_of_k>
```

Replace `<path_to_dataset>` with the path to your prepared dataset and `<value_of_k>` with the desired number of neighbors for the KNN algorithm.

3. The training process will begin, and the model will be saved upon completion.

## Evaluation

We have conducted extensive evaluations to assess the performance of the Infected Egg Classifier. The results indicate high accuracy and precision in detecting infected eggs. For detailed evaluation metrics, refer to the [Evaluation.md](https://github.com/AlphaCodder/infected-egg-classifier/blob/main/Evaluation.md) file.

## Contributing

Contributions to the Infected Egg Classifier are welcome! If you have any ideas, improvements, or bug fixes, please submit a pull request. Ensure that you adhere to the coding standards and provide clear documentation.

## License

The Infected Egg Classifier is licensed under the [MIT License](https://github.com/AlphaCodder/infected-egg-classifier/blob/main/LICENSE). Feel free to use, modify, and distribute this project as per the license terms.

---

Thank you for using the Infected Egg Classifier! If you have any questions or need assistance, please reach out to us at [kumars23279@gmail.com](mailto:kumars23279@gmail.com).
