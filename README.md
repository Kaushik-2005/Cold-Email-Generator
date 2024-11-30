# Cold Mail Generator
Cold Mail Generator is a tool developed using the services of Groq, and Langchain. It can used to generate personalized emails for applying for a job. Users can input the URL of a company's job requirement page. The tool will extract all the skills, and requirements of that job. The email consists of links related to work done by the user stored in the Vector database based on the job requirement.

## Getting Started
1. **Clone the repo:**
Run this command in your bash to clone the repo.
```bash
    git clone https://github.com/Kaushik-2005/Cold-Email-Generator.git
    cd Cold-Email-Generator
```

2. **Install all dependencies:**
Install all the dependencies by running this code in bash.
```bash
    pip install -r requirements.txx
```

3. **Set up Environmental Variable:**
Create a `.env` file to store the Groq API key. You can get the API key from [here](https://console.groq.com/keys)
```bash
    GROQ_API_KEY = your-groq-api-key
```

4. **Run the application:**
Run this command in your bash.
```bash
    streamlit run app/main.py
```

## Usage
- The project is located in `App` folder. 
- The main application is located in `app/main.py`. All the UI is built in this Python script.
- The LLM is built in `chains.py`. Here is where the details from the job URL are extracted and the personalized email is generated.
- `portfolio.py` helps in storing the user's personnel work in a vector database and it will provide related URL of previous work based on the job requirement.
- `utils.py` cleans the text extracted from the job webpage.

- All the previous work of the user should be in a CSV file and should be named `portfolio.csv`. It should be located in `App/resource/portfolio.csv`.
- For reference, you can look at `my_reference.csv` to know how the portfolio should be.
