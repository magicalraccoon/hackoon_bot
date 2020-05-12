FROM python:3
ADD logic.py /
ADD .env /
RUN pip install twitchio python-dotenv
CMD [ "python", "./logic.py" ]
