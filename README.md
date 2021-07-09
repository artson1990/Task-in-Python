# Overview

This is the code for Stock Price's task using python for interview.
The code uses dependencies like Streamlit to make an interactive dashboard for visual charts and yfinance to help us download stock price data from Yahoo Finance for free. Then we will run the app in docker container using Linux.

I uploaded 2 directories to this repository every one of them have a text file with the commands that I used to run the app using Streamlit and also commands for creating image and run the app using Docker container.

## Dependencies

* Streamlit(https://streamlit.io/)

* yfinance(https://pypi.org/project/yfinance/)

* pip(https://pip.pypa.io/en/stable/cli/pip_install/)

* Docker(https://www.docker.com/)

* Install Docker Engine on Debian(https://docs.docker.com/engine/install/debian/)

### Install missing dependencies using pip

````
sudo pip install streamlit yfinance
````

#### Demo Usage Streamlit

````
streamlit run program.py
````

#### Demo Usage Docker

````
docker run -p 8501:8501 app:latest
````
























