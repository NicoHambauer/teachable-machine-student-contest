# Nico Hambauer <nico.hambauer@fau.de> 2024
import csv
# export PIPENV_PYTHON=$(conda run which python)
import os
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def teachable_model_predict_sample(model_path, labels_path, img_path="testset/Head-samples/58.jpg"):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)
    # Load the model
    model = load_model(model_path, compile=False)

    # Load the labels
    class_names = open(labels_path, "r").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(img_path).convert("RGB")

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # plot and show the image first

    plt.imshow(image_array)
    plt.show()

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", confidence_score)


def evaluate_model_on_testset(model_path, labels_path, testset_directory):
    # Load the model and labels
    model = load_model(model_path, compile=False)

    # Read the class names and create a mapping from class names to integer labels
    with open(labels_path, "r") as f:
        label_mappings = {line.split()[1]: int(line.split()[0]) for line in f.readlines()}

    image_paths = []  # This will hold the paths of all images
    true_labels = []  # This will hold the true labels for all images

    # Collect all image paths and their corresponding true labels
    for category_folder in os.listdir(testset_directory):
        category_path = os.path.join(testset_directory, category_folder)
        if os.path.isdir(category_path):  # Check if it is a directory
            true_label = category_folder.split('-')[0]  # Extract the true label from the folder name
            true_label_int = label_mappings[true_label]  # Convert true label to int
            for image_name in os.listdir(category_path):
                if image_name.lower().endswith(".jpg"):  # Check if the file is an image
                    image_paths.append(os.path.join(category_path, image_name))
                    true_labels.append(true_label_int)

    # Initialize the data array with the right shape
    n_images = len(image_paths)
    data = np.ndarray(shape=(n_images, 224, 224, 3), dtype=np.float32)

    # Process each image and load into the data array
    for i, image_path in enumerate(image_paths):
        # Preprocess the image
        image = Image.open(image_path).convert("RGB")
        image = ImageOps.fit(image, (224, 224), Image.Resampling.LANCZOS)
        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
        data[i] = normalized_image_array  # Load the image into the data array

    # Predict the classes for all images
    predictions = model.predict(data)
    predicted_indices = np.argmax(predictions, axis=1)

    # Calculate the test accuracy
    accuracy = accuracy_score(true_labels, predicted_indices)
    return accuracy

# Add this function to update the CSV with the student's score
def update_student_score_in_csv(email, score, csv_file_path):
    updated = False
    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    for row in data:
        if email in row:
            row[-1] = f"{score:.4f}"
            updated = True
            break

    if updated:
        with open(csv_file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    evaluate_challenge = True
    # Adjust these paths to match your directory structure
    model_path = "converted_keras/keras_model.h5"
    labels_path = "converted_keras/labels.txt"

    sample_path = "testset/Head-samples/58.jpg"
    testset_directory = "testset/"

    if evaluate_challenge:
        test_accuracy = evaluate_model_on_testset(model_path, labels_path, testset_directory)
        print("Test accuracy:", f"{test_accuracy:.4f}")
    else:
        teachable_model_predict_sample(model_path, labels_path, sample_path)
