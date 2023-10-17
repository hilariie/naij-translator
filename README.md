# About Naij-translator
This is a simple system that transcribes audio in english and translates it to Nigerian languages such as pidgin, igbo, hausa, yoruba, etc. The more popular the language, the better the accuracy.
___
## How to run and Dependacies
1. To run create and activate a virtual environment with python >= 3.8
`conda create -n venv python=3.9` | `conda activate venv`
2. Install pytorch. Refer to their [website](https://pytorch.org/get-started/locally/).
3. clone this repository: `git clone <repo>`
4. Enter into the directory: `cd naij-translator`
5. Install remaining requirements: `pip install -r requirements.txt`
6. Run program: `python3 main.py`
___
*Note*: You'd need an [openai api key](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key). Copy your key and modify the [config.yaml](config.yaml) file accordingly.
___