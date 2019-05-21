# youtubedl

SECRET_KEY : This is the secret key of the project, for each project it is individual.
EMAIL_HOST_USER : Here you need to enter your email address
EMAIL_HOST_PASSWORD : Here is the generated password that is available to you after two-step validation
# To run project
First write in your Terminal 
celery -A youtubedl worker -l info
Second open another Terminal and write
python3 manage.py runserver
