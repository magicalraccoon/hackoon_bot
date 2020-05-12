FROM python:3
ADD logic.py /
ADD .env /
RUN pip install pytz git+https://github.com/IAmTomahawkx/TwitchIO.git@master python-dotenv
CMD [ "python", "./logic.py" ]