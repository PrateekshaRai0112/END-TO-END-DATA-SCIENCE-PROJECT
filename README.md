# END-TO-END-DATA-SCIENCE-PROJECT

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: PRATEEKSHA RAI

*INTERN ID*: CT04DN723

*DOMAIN*: DATA SCIENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

## Iris Flower Classifier Web App

## Overview

The Iris Flower Classifier is a simple yet powerful machine learning web application that predicts the species of an iris flower based on four input features: sepal length, sepal width, petal length, and petal width. This project leverages the classic Iris dataset, a well-known dataset in the machine learning community, to train a Logistic Regression model. The model is then deployed via a Flask web application, allowing users to input measurements and get real-time predictions of the flower species.

The primary goal of this project is to demonstrate the end-to-end workflow of a data science project — from data collection and preprocessing, model training, evaluation, to deployment and visualization — in a user-friendly web interface. It is an excellent starting point for beginners interested in machine learning and web deployment.

## Project Structure

iris-flower-classifier/

├── app.py               # Flask web application script

├── model1.pkl            # Serialized trained model

├── train_model.ipynb    # Jupyter notebook for training and saving the model

├── templates/

    └── index.html       # HTML template for the input form and prediction display

## Dataset

The project uses the famous Iris dataset, originally introduced by Ronald Fisher in 1936. It contains 150 samples of iris flowers collected from three species:

* Iris Setosa

* Iris Versicolor

* Iris Virginica

Each sample has four features measured in centimeters:

* Sepal Length

* Sepal Width

* Petal Length

* Petal Width

These features serve as input variables for classification.

## Model Training

The model training is performed in the Jupyter notebook train_model.py. The workflow includes:

`Loading the dataset`: Using scikit-learn’s built-in Iris dataset loader.

`Data splitting`: Splitting data into training and testing subsets to evaluate performance.

`Model selection`: Logistic Regression was chosen due to its simplicity and effectiveness on this dataset.

`Training`: The model learns to classify iris species based on the features.

`Evaluation`: The model’s accuracy is calculated on the test set to ensure good performance.

`Serialization`: The trained model is saved as model.pkl using Python’s pickle module.

## Web Application

The Flask application (app.py) serves a user interface through which users can:

Input the four numerical features.

Submit the data for prediction.

View the predicted iris species on the same page.

The app loads the trained model on startup and uses it to predict species based on user input in real-time. The interface is implemented using a simple HTML form (templates/index.html) styled with embedded CSS to ensure clean and user-friendly interactions.

## Installation and Setup

To run this project locally, follow these steps:

Create a virtual environment (recommended):

`python -m venv venv
venv\Scripts\activate`

 Install Required Python Libraries

`pip install flask
pip install scikit-learn
pip install numpy`

Train the model (optional if model.pkl is already provided):

`Run the train_model.py in vscode to generate model1.pkl`.

Run the Flask app:

`python app.py`

Access the app:

`Open your browser and go to http://127.0.0.1:5000`

## Usage

Enter values for sepal length, sepal width, petal length, and petal width in centimeters.

Click Predict.

`The predicted iris species will be displayed below the form.`

## Technologies Used

`Python 3.8+`

`Flask`: Micro web framework for serving the application.

`scikit-learn`: Machine learning library used for model training.

`HTML/CSS`: For frontend form and styling.

## Future Work

Add support for batch predictions by uploading CSV files.

Improve frontend design with frameworks like Bootstrap or React.

Deploy the app to cloud platforms such as Heroku or Render for public access.

Experiment with more complex models like Random Forests or Neural Networks.

## Acknowledgments

The original Iris dataset, freely available via scikit-learn.

The many open-source projects that made this project possible.

# Output
![Image](https://github.com/user-attachments/assets/4160b554-81a2-4b25-96aa-bf12429b118d)








