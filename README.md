## Setup

1.Clone the repository:

    git clone -b master https://github.com/SJ-1407/Lambda.git  
    cd Lambda
   
2.Create and activate a virtual environment:  

     python -m venv any_name     
     .\any_name\Scripts\activate   
  
3. Install dependencies:   
      First go to the directory Lambda
      cd path to Project_1
     then  install the requirements using the command

       pip install -r requirements.txt

4. Provide the openai api key
      Create a .env file in the folder  and then add the key like below
          openai_api_key="your key"
      
     
6.  Run the app:    

        streamlit run app.py



#Chatbot  will be available at http://localhost:8501/.   
