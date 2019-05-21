# youtubedl

# This program will help you to convert video to mp3-format and when your file is ready, you will get an email of link, where is your ready file. 

# In setting some slots are gitignored:
SECRET_KEY : This is the secret key of the project, for each project it is individual.
EMAIL_HOST_USER : Here you need to enter your email address
EMAIL_HOST_PASSWORD : Here is the generated password that is available to you after two-step validation
DEBUG : your browser will show you an ERROR if there True, change to False and will show you standart 404 ERROR. 
# To run project
First write in your Terminal :
celery -A youtubedl worker -l info ; 
Second open another Terminal and write ;
python3 manage.py runserver.
