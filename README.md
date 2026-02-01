# Teachable Machine Student Contest Environment Setup

This guide provides instructions on how to set up the Python environment required for running the Teachable Machine project on macOS, specifically optimized for Apple Silicon (M1/M2 chips).

## Leaderboard & AI-Challenge Webpage

- [Teachable Machine Student Contest Leaderboard](https://nicohambauer.github.io/teachable-machine-student-contest/)

## Tool for AI Model Training

- [Teachable Machine by Google](https://teachablemachine.withgoogle.com)

## Requirements

- Conda (Miniconda or Anaconda)
- macOS with Apple Silicon (M1/M2)


## Conda Environment Installation with YAML File

To use this YAML file, save it as `teachable-ml.yml` and then run the following command to create the Conda environment:

```bash
conda env create -f teachable-ml.yml
```

After creating the environment, activate it with:

```bash
conda activate teachable-ml
```

This setup ensures that users can quickly get started with the Teachable Machine project by following clear, step-by-step instructions, and using a YAML file reduces the potential for errors during the installation of dependencies.

## Manual Environment Setup

1. **Create a Conda Environment**

   Open your terminal and run the following command to create a new Conda environment named `teachable-ml` with Python 3.9:

   ```bash
   conda create --name teachable-ml python=3.9
   ```

2. **Activate the Environment**

   Activate the newly created environment:

   ```bash
   conda activate teachable-ml
   ```

3. **Install Required Packages**

   Install `tensorflow-macos`, `tensorflow-metal` for GPU support, `keras` version 2.13.1, and `numpy` version 1.24.3 using pip:

   ```bash
   pip install tensorflow-macos tensorflow-metal pillow matplotlib scikit-learn keras==2.13.1 numpy==1.24.3
   ```

## Setup Verification

After installation, verify the setup by running the following commands in your terminal:

```bash
python -c "import tensorflow as tf; print(tf.__version__)"
python -c "import keras; print(keras.__version__)"
python -c "import numpy; print(numpy.__version__)"
python -c "import sklearn; print(sklearn.__version__)"
python -c "import matplotlib; print(matplotlib.__version__)"
python -c "import PIL; print(PIL.__version__)"
```

If the installations were successful, you should see the versions of TensorFlow, Keras, and NumPy printed without errors.
