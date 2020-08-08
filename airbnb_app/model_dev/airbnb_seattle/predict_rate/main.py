from model_dev.airbnb_seattle.dataset.main import create_input_df


def create_rate_prediction_model():
    listings_df, reviews_df, calendar_df = create_input_df()


if __name__ == '__main__':
    create_rate_prediction_model()
