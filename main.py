# Nico Hambauer <nico.hambauer@fau.de> 2024
import os
import pandas as pd
from tensorflow.keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
import shutil

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
    """
    Records the student's score in a CSV exactly once using pandas.
    If the pseudonym already exists, the function does nothing (no updates).
    If the pseudonym does not exist, a new row is added with the given score.
    """

    # 1. Create an empty CSV with correct columns if it doesn't exist
    if not os.path.exists(csv_file_path):
        # Create a DataFrame with just the headers, and save it
        pd.DataFrame(columns=["pseudonym", "accuracy"]).to_csv(csv_file_path, index=False)

    # 2. Read existing data
    df = pd.read_csv(csv_file_path)

    # 3. Check if pseudonym already exists
    if pseudonym in df["pseudonym"].values:
        print(f"Pseudonym '{pseudonym}' already exists in the leaderboard. Not updating.")
        return  # Do nothing if it exists

    # 4. Append the new row (as a DataFrame) only if pseudonym not found
    new_row_df = pd.DataFrame([{"pseudonym": pseudonym, "accuracy": f"{score:.4f}"}])
    df = pd.concat([df, new_row_df], ignore_index=True)

    # 5. Save back to CSV
    df.to_csv(csv_file_path, index=False)
    print(f"New entry for pseudonym '{pseudonym}' recorded with score {score:.4f}.")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Adjust these paths to match your directory structure
    pseudonym = input("Enter an imaginary name for the contest: ")
    student_dir = f"models/{pseudonym}"
    # crate that subdirectory for name if it does not exist, otherwise promt the user with a failure message
    if not os.path.exists(student_dir):
        os.makedirs(student_dir)
    else:
        print(f"Directory {student_dir} already exists. Please delete it or choose a different name.")
        exit(1)

    # move the folder converted_keras/ with the entire subdirs and files to the new subdirectory, handling the case if it already exists
    # recursively move the subdirectories and files
    if os.path.exists("converted_keras"):
        target_dir = os.path.join(student_dir, "converted_keras")
        # Move the directory, automatically handling subdirectories and files
        shutil.move("converted_keras", target_dir)
    else:
        print("Directory 'converted_keras' does not exist. Please create it and put the converted model there.")
        exit(1)


    model_dir = f"{student_dir}/converted_keras/"
    testset_directory = "final_testset/"

    test_accuracy = evaluate_model_on_testset(model_dir, testset_directory)
    print("Test accuracy:", f"{test_accuracy:.4f}")

    record_students_score(pseudonym, test_accuracy, "leaderboard.csv")
