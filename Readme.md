# Pension Advisor Chatbot

Welcome to the **Pension Advisor Chatbot** – a conversational AI built with PyTorch and Flask. This project showcases a neural network for intent classification combined with a clean web interface, designed to impress in technical interviews.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Training the Model](#training-the-model)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Chatbot Assistant leverages a neural network built with PyTorch to classify user intents and provide relevant responses. It includes a function mapping mechanism (e.g., retrieving stock data) and is served via a Flask-based web interface.

<img src="Pension Plan Advisor.png" alt="Screenshot of the Chatbot Interface" width="400">

## Features

- **Neural Network-Based NLP:** Uses a fully connected network to classify intents.
- **Dynamic Function Mappings:** Integrate functionalities like stock lookup.
- **Web Interface:** A sleek and responsive chat interface built with HTML, CSS, and JavaScript.
- **Modular Design:** Easy to extend and maintain.

## Tech Stack

- **Python 3**
- **PyTorch**
- **Flask**
- **HTML/CSS/JavaScript**
- **nltk & numpy**

## Project Structure
```
├── app.py                     
├── main.py                    
├── fin_intents.json           
├── model_dimensions.json      
├── chatbot_model.pth          
├── requirements.txt           
├── README.md                  
├── .gitignore                 
├── static/
│   └── style.css              
└── templates/
    └── index.html             
```


## Installation

1. **Clone the Repository:**

```
   git clone https://github.com/yourusername/chatbot_project.git
   cd chatbot_project
```
2. **Set Up a Virtual Environment:**
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. **Install Dependencies:**
```
pip install -r requirements.txt
```

## Usage
Start the Flask application by running:

```
python app.py
```
Open your browser and navigate to http://127.0.0.1:5000 to begin chatting with the bot.

## Model Re-training
If you need to retrain the model:

1. Uncomment the training section in main.py.

2. Create a .json file with the same structure as the fin_intents.json file and add the desired data

3. Run main.py to generate a new chatbot_model.pth and model_dimensions.json.

4. Re-comment the training code once the model has been trained for normal usage.


## Contributing
Contributions, improvements, and suggestions are welcome! Please feel free to fork the repository, make your changes, and submit a pull request.