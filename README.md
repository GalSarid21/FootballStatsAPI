# FootballStats API
A rest api which provides football related data.

# FootballerFinancialData API QuickStart
    In order to run this project successfully, please follow the next steps:
        1. Clone the repository to your local machine
        2. Run pip install -r requirements.txt
        3. Run python manage.py migrate

        NOTE: a json file with initial DB values is attached in -  
              footballer_financial_data --> examples --> add_all.json

        4. make footballer/add/ call with the add_all.json data
        5. Run python manage.py migrate one more time
        6. make footballer/all/ to make sure all the data is in the DB