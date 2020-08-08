import pandas as pd

from model_dev.settings import INPUT_DATASET_AIRBNB_LISTINGS, INPUT_DATASET_AIRBNB_REVIEWS, \
    INPUT_DATASET_AIRBNB_CALENDAR


def create_input_df():
    print(f"INPUT_DATASET_AIRBNB_LISTINGS {INPUT_DATASET_AIRBNB_LISTINGS}")
    listings_df = pd.read_csv(INPUT_DATASET_AIRBNB_LISTINGS)

    print(f"INPUT_DATASET_AIRBNB_REVIEWS {INPUT_DATASET_AIRBNB_REVIEWS}")
    reviews_df = pd.read_csv(INPUT_DATASET_AIRBNB_REVIEWS)

    print(f"INPUT_DATASET_AIRBNB_CALENDAR {INPUT_DATASET_AIRBNB_CALENDAR}")
    calendar_df = pd.read_csv(INPUT_DATASET_AIRBNB_CALENDAR)

    return [listings_df, reviews_df, calendar_df]