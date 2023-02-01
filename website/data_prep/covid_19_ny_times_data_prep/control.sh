#!/bin/bash

if [ "$(uname)" == "Darwin" ]; then
  PRJ_BASE="/Users/danhiggins/Code/GATech/CSE6242_Data_Visual_Analytics"
else
  PRJ_BASE="/home/ubuntu/Applications"
fi

if [ -d "/home/ubuntu/Applications/python_envs" ]; then
    source /home/ubuntu/Applications/python_envs/bin/activate
fi

WEBSITE_HOME=${PRJ_BASE}/covid_19_analysis
DATA_HOME=${PRJ_BASE}/covid-19-data

## See if we have new data from NYTimes
cd ${DATA_HOME} || exit # exit if cd fails
git pull

## Run the data update scripts
cd ${WEBSITE_HOME}/data_prep/covid_19_ny_times_data_prep || exit
python covid_19_cases_by_county.py
python covid_19_cases_by_state.py

## Touch the files so that the web server will refresh
touch ${WEBSITE_HOME}/website/templates/*


