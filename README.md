# simpleChatGPTBot
This is a simple, experimental bot used to play with ChatGPT based models

# Create an OpenAPI account and create your key
Once you sign up and create a free tier OpenAPI account [create a key](https://platform.openai.com/account/api-keys).

# Add your key to the **.env** file
It should look something like
```
OPENAI_API_KEY=YOURKEYHERE
```

# Put some test data in the data directory and ingest data into OpenAPI
This code is built to read in text files from the **data** directory. 
- Drop some documents into the data directory
- Run ```python generate_index.py```

NOTE: You will need to install a set of libraries using 'pip'. I may not have them all covered here. If any are missed, look at the error generated from python and 'install' the missing library.

Here are a set of examples for this code.
```
pip install gpt-index
pip install Markdown
pip install display
pip install IPython
pip install docx2txt
pip install dotenv
```

# Ask the model your questions
The generate step will take some time. Once completed you should notice some usage from [the usage page](https://platform.openai.com/account/usage). Once completed, you can execute ```python interviews.py``` and it "should" ask "What would you like to ask...".

Type in your question.

Hit 'Enter'.

Have fun.


