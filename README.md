# Quotes Recommendation Chatbot using RASA

## Project Overview

This project is an AI chatbot that recommends motivational quotes to users based on their input.
The chatbot is built using **RASA NLU** and **Python** and can understand user messages and respond with relevant quotes.

The chatbot can be integrated with a simple web interface for interaction.

---

## Features

* Natural Language Understanding using RASA
* Quote recommendation system
* CSV dataset of quotes
* Custom actions using Python
* Web interface for chatbot interaction

---

## Technologies Used

* Python
* RASA
* HTML / JavaScript
* Pandas
* Machine Learning

---

## Project Structure

quotes_chatbot/
│
├── actions/            # Custom Python actions
├── data/               # NLU training data and stories
├── dataset/            # Quotes dataset
├── tests/              # Test stories
├── config.yml          # RASA pipeline configuration
├── domain.yml          # Chatbot domain
├── credentials.yml     # Credentials configuration
├── endpoints.yml       # Action server endpoint
└── index.html          # Web interface

---

## Installation

### Clone the repository

git clone https://github.com/SukhveerSinghYadav/A-Quotes-Recommendation-Bot-built-using-RASA-NLU-understands.git

### Navigate to project folder

cd quotes_chatbot

### Create virtual environment

python -m venv rasa_env

### Activate environment

Windows:
rasa_env\Scripts\activate

### Install dependencies

pip install rasa pandas

---

## Train the Model

rasa train

---

## Run Action Server

rasa run actions

---

## Run Chatbot

rasa shell

---

## Web Interface

You can also connect the chatbot with the provided **index.html** for a simple web interface.

---

## Future Improvements

* Deploy chatbot on cloud
* Improve NLU accuracy
* Add voice input
* Integrate with messaging platforms

---

## Author

Sukhveer Singh Yadav
