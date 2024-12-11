#after not being allowed to use musixmatch API, not having spotify IDs on genius API, getting rate limited on genius API, finally found a way that took 20 hours to run to get the lyrics for most of the 17,102 unique songs.
import lyricsgenius
import pandas as pd
import time

access_token = #Redacted for github push
genius = lyricsgenius.Genius(access_token)
#init
genius.verbose = False 
genius.remove_section_headers = True  
genius.skip_non_songs = False 
genius.excluded_terms = ["(Remix)", "(Live)"]
#method to continuously update and resume from checkpoints if computer turned off
output_csv = "/Users/yotamtwersky/Desktop/spotify_data_with_lyrics_matched.csv" 

df = pd.read_csv(output_csv)

def normalize_text(text):
    if pd.isna(text):
        return ""
    return text.lower().strip()

# normalization for track and artist names
df["track_name_norm"] = df["track_name"].apply(normalize_text)
df["artist_name_norm"] = df["artist_names"].apply(normalize_text)

# removena
unmatched_df = df[df["lyrics"].isna()]

# lyrics fetcher
def fetch_lyrics(track_name, artist_name):
    try:
        song = genius.search_song(track_name, artist_name)
        if song:
            return song.lyrics
        return None
    except Exception as e:
        if "429" in str(e):
            raise Exception("Rate limit hit (429 Too Many Requests)")
        print(f"Error fetching lyrics for '{track_name}' by '{artist_name}': {e}")
        return None

# counter for stashing progress
matches_found = 0

batch_counter = 0  # counter to track songs processed in the current batch
for index, row in unmatched_df.iterrows():
    track_name = row["track_name"]
    artist_name = row["artist_names"]
    print(f"Fetching lyrics for row {index} - '{track_name}' by '{artist_name}'...")
    try:
        lyrics = fetch_lyrics(track_name, artist_name)
        if lyrics:
            df.at[index, "lyrics"] = lyrics
            matches_found += 1
            batch_counter += 1
            print(f"Match found! Total matches so far: {matches_found}")

        # save progress
        if batch_counter == 50:
            df.to_csv(output_csv, index=False)
            print("Progress saved after 50 songs.")
            batch_counter = 0 
    except Exception as e:
        if "Rate limit hit" in str(e):
            print(f"Rate limit hit. Stopping at row {index}.")
            break

    # delay to avoid rate limits
    time.sleep(1)

# save final
df.to_csv(output_csv, index=False)
print(f"Total matches found: {matches_found}")
print(f"Final progress saved to {output_csv}.")
