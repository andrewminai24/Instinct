## Instinct - An automatic text message translator!

To set up for development purposes:

1) Clone repo

2) Create a new virtual environment and install required packages from pip. Also make sure you have Python 3.

3) Replace all Twilio Keys and IDs with your own (preferably using environment variables) in models.py, routes.py, and config.py

4) Set the Google Translate Authentication Path in your terminal, using export GOOGLE_APPLICATION_CREDENTIALS="[PATH]".

5) Set the SmsURL in models.py to whatever your endpoint is for smses.

3) Navigate inside the 'app' directory and run 'flask run' from the command line to start the server. If you navigate to the correct port
on your browser, you can create 'relationships', which are basically pairs of phone numbers that are linked together by an intermediate Twilio number.

Our DevPost can be found at: https://devpost.com/software/e-taw25n

