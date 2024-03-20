## Setup

1.Clone the repository:

    git clone -b master https://github.com/SJ-1407/Lambda.git  
    cd "path to Lambda"
   
2.Create and activate a virtual environment:  

     python -m venv any_name     
     .\any_name\Scripts\activate   
  
3. Install dependencies:   
      First go to the directory Lambda

           cd "path to Lambda"
    then  install the requirements using the command

       pip install -r requirements.txt

5. Provide the openai api key
      Create a .env file in the Lambda folder  and then add your openai key like below:

        openai_api_key="your key"
      
     
7.  Run the app:    

        streamlit run app.py



#  Chatbot will be available at: http://localhost:8501/.   
