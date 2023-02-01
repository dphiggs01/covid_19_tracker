import celery
from data_prep.covid_19_ny_times_data_prep.data_check import check_nytimes_data

@celery.task()
def check_nyt_data():
    logger = check_nyt_data.get_logger()
    logger.info("Git Hub Check")
    check_nytimes_data()
