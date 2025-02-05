# E-Commerce Conversational Chatbot

The E-Commerce Conversational Chatbot is an AI-powered chatbot designed to assist users in finding and recommending products from an e-commerce fashion dataset. The chatbot uses natural language processing and vector search techniques to match user queries with relevant products, enhancing the shopping experience. 

## Features

- **AI-Powered Recommendations**: Utilizes advanced NLP techniques to understand user queries and suggest relevant products.
- **Dynamic Search**: Supports attribute-based searching based on brand, color, category, and more.
- **Vector Database Integration**: Uses Qdrant for efficient and scalable vector-based searches.
- **User-Friendly Interface**: Built with Flask and HTML/CSS for seamless interaction.

## Directory Structure

```bash
E-Commerce_Conversational_Chatbot/
├── flask_chatbot/
│   ├── app.py
│   ├── templates/
│   │   ├── index.html
│   │   ├── chatbot.html
│   ├── static/
│   │   ├── css/
│   │   │   ├── styles.css
│   │   ├── js/
│   │   │   ├── home.js
│   ├── images/
├── requirements.txt
├── LICENSE
├── README.md
```

- `flask_chatbot/app.py`: The main application script that runs the Flask chatbot.
- `templates/`: Contains HTML files for the chatbot interface.
- `static/css/`: Stylesheets for designing the user interface.
- `static/js/`: JavaScript files for interactivity.
- `images/`: Stores images used in the application.
- `requirements.txt`: Lists the Python dependencies required to run the chatbot.
- `LICENSE`: Contains the licensing information for the project.
- `README.md`: Provides an overview and instructions for the project.

## Installation

To set up the chatbot locally, follow these steps:

```bash
# Clone the Repository
git clone https://github.com/priyam-hub/E-Commerce_Conversational_Chatbot.git
cd E-Commerce_Conversational_Chatbot
```

```bash
# Install Dependencies
# Ensure you have Python installed. Then, install the required packages:
pip install -r requirements.txt
```

## Usage

# Run the chatbot application
python flask_chatbot/app.py

This will launch the chatbot on your local server. Open the browser and navigate to the chatbot interface to start interacting.

## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](https://github.com/priyam-hub/E-Commerce_Conversational_Chatbot/blob/main/LICENSE) file for more details.

## Contributors

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.

## Acknowledgements

Special thanks to the developers and contributors who have made this project possible.

---

```md
For more information, visit the [E-Commerce Conversational Chatbot GitHub Repository](https://github.com/priyam-hub/E-Commerce_Conversational_Chatbot).
```

