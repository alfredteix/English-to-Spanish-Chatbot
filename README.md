# English-to-Spanish-Chatbot
Chatbot that uses Together AI API to translate text from english to spanish
Overview
This is a simple Python-based English to Spanish translator that uses the Together.ai API to generate translations. The program allows users to enter text in English, and it returns the Spanish translation in real-time. It runs in a continuous loop until the user types "exit".

Features
AI-powered translations using the Llama-3.3-70B-Instruct-Turbo model
Interactive command-line interface for real-time translation
Minimal setup required—just install dependencies and run the script
Uses Together.ai API for generating accurate translations
Technologies Used
Python for scripting
Requests library for API communication
Together.ai API for AI-based translations
Setup and Installation
Prerequisites
Python 3 installed on your system
A free API key from Together.ai
Installation Steps
Clone this repository:
bash
Copy
Edit
git clone https://github.com/yourusername/english-to-spanish-translator.git
Navigate to the project folder:
bash
Copy
Edit
cd english-to-spanish-translator
Install the required dependency:
bash
Copy
Edit
pip install requests
Open translator.py and replace "your_api_key_here" with your actual Together.ai API key.
Usage
Run the script:
bash
Copy
Edit
python translator.py
Enter any English phrase to translate it into Spanish.
Type "exit" to close the program.
Example Interaction
pgsql
Copy
Edit
Need to translate English to Spanish? Type 'exit' to quit.

Please type your message here: How are you?
AI Response: ¿Cómo estás?

Please type your message here: I love learning new languages.
AI Response: Me encanta aprender nuevos idiomas.

Please type your message here: exit
Goodbye!
Customization
Change "English" and "Spanish" in translate_text() to support other language pairs.
Adjust the "temperature" value in the API call to make translations more creative or precise.
Future Enhancements
Add support for more languages (French, German, etc.)
Develop a web-based or GUI version using Streamlit
Integrate speech-to-text functionality for spoken translations
Contributing
If you'd like to improve this project, feel free to fork this repository and submit a pull request!

License
This project is licensed under the MIT License.
