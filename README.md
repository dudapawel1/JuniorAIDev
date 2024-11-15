# Article-to-HTML Generator Application

## Description
This application uses the OpenAI API to generate HTML from a given article text. The HTML includes structured headers and placeholders for images, enabling quick formatting of the article.

## Requirements
- Python 3.6 or later
- An OpenAI account and API key

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/dudapawel1/JuniorAIDev.git
   cd JuniorAIDev
2. Install the openai library:
   ```bash
   pip install openai
3. Add your OpenAI API key: Replace ************************* in generate_article.py with your actual OpenAI API key.

## Usage
1. Place the article text in a file named article.txt in the project’s main directory.
2. Run the script:
   ```bash
    python generate_article.py
3. The generated HTML will be displayed in the terminal.

## Project Structure
  generate_article.py – Main script for generating HTML from the article text.
  article.txt – Input file containing the article text.
  article.html – Generated HTML file (optional, if you choose to save it).
  
## Example
When the script is run, the application:
  1. Reads the article content from article.txt.
  2. Sends the text to the OpenAI API to generate structured HTML.
  3. Displays the HTML output in the terminal.
## Notes
  The script generates basic HTML without CSS or JavaScript.
  Only the <body> tag is used in the generated HTML.
