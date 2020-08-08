import os, sys
# sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

INPUT_DATASET_BASE_PATH_AIRBNB = str(os.path.join(os.path.dirname(__file__), "airbnb_seattle/dataset/data" ))
INPUT_DATASET_AIRBNB_LISTINGS = str(os.path.join(INPUT_DATASET_BASE_PATH_AIRBNB, "listings.csv" ))
INPUT_DATASET_AIRBNB_REVIEWS = str(os.path.join(INPUT_DATASET_BASE_PATH_AIRBNB, "reviews.csv" ))
INPUT_DATASET_AIRBNB_CALENDAR = str(os.path.join(INPUT_DATASET_BASE_PATH_AIRBNB, "calendar.csv" ))

print(f"INPUT_DATASET_AIRBNB_LISTINGS {INPUT_DATASET_AIRBNB_LISTINGS}")
print(f"INPUT_DATASET_AIRBNB_REVIEWS {INPUT_DATASET_AIRBNB_REVIEWS}")
print(f"INPUT_DATASET_AIRBNB_CALENDAR {INPUT_DATASET_AIRBNB_CALENDAR}")
