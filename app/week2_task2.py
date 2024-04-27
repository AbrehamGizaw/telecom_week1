# from sqlalchemy import create_engine

# postgress_url= 'postgresql://postgres:1127@localhost:5432/telecom'

# engine = create_engine(postgress_url)



import pandas as pd

# query = "select * from xdr_data"
# df = pd.read_sql(query, engine)

# df.to_csv("sql/csv.csv", index=False)

# Read the data from the SQL dump
data = pd.read_csv("sql/telecom.sql", delimiter='\t')

# Selecting relevant columns for aggregation
relevant_columns = ["MSISDN/Number", "Dur. (ms)", "Total UL (Bytes)", "Total DL (Bytes)", 
                    "Social Media DL (Bytes)", "Social Media UL (Bytes)", 
                    "Google DL (Bytes)", "Google UL (Bytes)", 
                    "Email DL (Bytes)", "Email UL (Bytes)", 
                    "Youtube DL (Bytes)", "Youtube UL (Bytes)", 
                    "Netflix DL (Bytes)", "Netflix UL (Bytes)", 
                    "Gaming DL (Bytes)", "Gaming UL (Bytes)", 
                    "Other DL (Bytes)", "Other UL (Bytes)"]

# Rename columns for easier access
data.columns = [column.strip().replace(' ', '_').lower() for column in data.columns]

# Aggregate per user
aggregated_data = data.groupby("msisdn/number")[relevant_columns].agg(
    num_sessions=("msisdn/number", "size"),
    session_duration=("dur._(ms)", "sum"),
    total_ul=("total_ul_(bytes)", "sum"),
    total_dl=("total_dl_(bytes)", "sum"),
    social_media_dl=("social_media_dl_(bytes)", "sum"),
    social_media_ul=("social_media_ul_(bytes)", "sum"),
    google_dl=("google_dl_(bytes)", "sum"),
    google_ul=("google_ul_(bytes)", "sum"),
    email_dl=("email_dl_(bytes)", "sum"),
    email_ul=("email_ul_(bytes)", "sum"),
    youtube_dl=("youtube_dl_(bytes)", "sum"),
    youtube_ul=("youtube_ul_(bytes)", "sum"),
    netflix_dl=("netflix_dl_(bytes)", "sum"),
    netflix_ul=("netflix_ul_(bytes)", "sum"),
    gaming_dl=("gaming_dl_(bytes)", "sum"),
    gaming_ul=("gaming_ul_(bytes)", "sum"),
    other_dl=("other_dl_(bytes)", "sum"),
    other_ul=("other_ul_(bytes)", "sum")
)

# Print the aggregated data
print(aggregated_data)
