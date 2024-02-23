# era_v2_S5

This repository contains Python code for ERAv2 course session 5: PyTorch assignment. The code is organized into three files:

1. `model.py`: This file contains the model definition , as well as functions for training and testing the model.

2. `utils.py`: This file contains utility functions for loading and preprocessing the dataset, etc.

3. `S5.ipynb`: This Jupyter Notebook file serves as the main entry point for the project. Its where the functions defined in `model.py` and `utils.py` to train and evaluate the model on a specific dataset are called.

## Files Overview

- `model.py`:
  - Defines the architecture of the model (`Net` class).
  - Contains functions for training and testing the model (`train` and `test`).
  - Contains function to do define, train, test and share loss and accuracy plots of the model (`start_model_train_and_test`).

- `utils.py`:
  - Defines utility functions for loading and preprocessing the dataset (`get_test_train_data` and `test_train_data_loader`).

- `S5.ipynb`:
  - The functions defined in `model.py` and `utils.py` to train and evaluate the CNN are called here.
  - The notebook starts with necessary imports followed by reading/downloading and loading the test and train data using `utils.py` functions.
  - Next the data is verified by plotting it.
  - Afterwards the functions from `model.py` is called to start the model training and test the model and give out the test and train data loss and accuracy plots.
