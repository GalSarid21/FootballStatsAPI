# FootballStats API
A rest api which provides football related data.
Built with Django framework.

# FootballerFinancialData API QuickStart
    In order to run this project successfully, please follow the next steps:
        1. Clone the repository to your local machine
        2. Run pip install -r requirements.txt
        3. Run python manage.py migrate

        NOTE: a json file with initial DB values is attached in -  
              footballer_financial_data --> examples --> add_all.json

        4. Run python manage.py runserver and click on the auto message development server endpoint

        NOTE: development server endpoint most likely to be - http://127.0.0.1:9000/ where it configured to port 9000

        5. Make a footballer/add/ call with the add_all.json data
        6. Run python manage.py migrate one more time
        7. Make a footballer/all/ to make sure all the data is in the DB
