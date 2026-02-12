# Nico Hambauer <nico.hambauer@ur.de> 2026
import os
import pandas as pd
import zipfile
from tensorflow.keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score

np.set_printoptions(suppress=True)

def predict_single(model_dir, img_path):

    model_path = f"{model_dir}/keras_model.h5"
    labels_path = f"{model_dir}/labels.txt"

    model = load_model(model_path, compile=False)
    class_names = open(labels_path, "r").readlines()

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    image = Image.open(img_path).convert("RGB")

    # resizing to 224x224 and crop from center
    image_size = (224, 224)
    image = ImageOps.fit(image, image_size, Image.Resampling.LANCZOS)

    image_array = np.asarray(image)

    plt.imshow(image_array)
    plt.show()

    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    data[0] = normalized_image_array

    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    print("Class:", class_name[2:], end="")
    print("Confidence Score:", confidence_score)


def evaluate_model_on_testset(model_dir, testset_directory):

    model_path = f"{model_dir}/keras_model.h5"
    labels_path = f"{model_dir}/labels.txt"

    model = load_model(model_path, compile=False)

    # Read the class names and create a mapping from class names to integer labels
    with open(labels_path, "r") as f:
        label_mappings = {line.split()[1]: int(line.split()[0]) for line in f.readlines()}

    image_paths = []
    true_labels = []

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

    data = np.ndarray(shape=(len(image_paths), 224, 224, 3), dtype=np.float32)

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
    return accuracy_score(true_labels, predicted_indices)


def record_students_score(pseudonym, score, csv_file_path):

    if not os.path.exists(csv_file_path):
        # Create a DataFrame with just the headers, and save it
        pd.DataFrame(columns=["pseudonym", "accuracy"]).to_csv(csv_file_path, index=False)

    df = pd.read_csv(csv_file_path)

    if pseudonym in df["pseudonym"].values:
        print(f"Pseudonym '{pseudonym}' already exists in the leaderboard. Not updating.")
        exit(1)

    new_row_df = pd.DataFrame([{"pseudonym": pseudonym, "accuracy": f"{score:.4f}"}])
    df = pd.concat([df, new_row_df], ignore_index=True)

    df.to_csv(csv_file_path, index=False)
    print(f"New entry for pseudonym '{pseudonym}' recorded with score {score:.4f}.")


if __name__ == '__main__':

    pseudonym = input("Enter an imaginary name for the contest: ")
    student_dir = f"models/{pseudonym}"

    if not os.path.exists(student_dir):
        os.makedirs(student_dir)
    else:
        print(f"Directory {student_dir} already exists. Please delete it or choose a different name.")
        exit(1)

    # Define the path to the downloaded zip file
    zip_path = os.path.expanduser("~/Downloads/converted_keras.zip")

    # Check if the zip file exists
    if os.path.exists(zip_path):
        target_dir = os.path.join(student_dir, "converted_keras")
        # Create the target directory if it doesn't exist
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
        # Unzip the file into the target directory
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(target_dir)
        # Check if the files were extracted successfully
        if os.path.exists(f"{target_dir}/keras_model.h5") and os.path.exists(f"{target_dir}/labels.txt"):
            # Delete the zip file
            os.remove(zip_path)
        else:
            print("Model files were not extracted successfully. Please check the zip file.")
            exit(1)
    else:
        print(f"Zip file '{zip_path}' does not exist. Please download it and place it in the Downloads folder.")
        exit(1)


    model_dir = f"{student_dir}/converted_keras/"
    testset_directory = "final_testset/"

    test_accuracy = evaluate_model_on_testset(model_dir, testset_directory)
    print("Test accuracy:", f"{test_accuracy:.4f}")

    record_students_score(pseudonym, test_accuracy, "_data/leaderboard.csv")
