import pandas as pd

from model_dev.settings import INPUT_DATASET_AIRBNB_LISTINGS, INPUT_DATASET_AIRBNB_REVIEWS, \
    INPUT_DATASET_AIRBNB_CALENDAR


def create_input_df():

    listings_df = pd.read_csv(INPUT_DATASET_AIRBNB_LISTINGS)
    reviews_df = pd.read_csv(INPUT_DATASET_AIRBNB_REVIEWS)
    calendar_df = pd.read_csv(INPUT_DATASET_AIRBNB_CALENDAR)

    return [listings_df, reviews_df, calendar_df]
