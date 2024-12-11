**Project Update:**

1. Have you already collected, or do you have access to, all of the data that you will need in order to complete your project? If not, please estimate the percentage of the data that you have, describe any issues that you are having, and what your plan is for getting the rest of the data.

We have the below dataset of top songs, and we can match the songs to their corresponding spotify info from the Spotify API with their spotify ID. We match them to the lyrics with the same spotify ID (https://github.com/akashrchandran/spotify-lyrics-api). We do have all the data in a sense although it still needs to be cleaned in the way we outline below. 

This data set has the top songs from 73 countries updated daily ([https://www.kaggle.com/datasets/asaniczka/top-spotify-songs-in-73-countries-daily-updated](https://www.kaggle.com/datasets/asaniczka/top-spotify-songs-in-73-countries-daily-updated)). From the data set we are going to focus on the top 50 songs each day from November 11th, 2023 to November 11th, 2024 in the 73 countries included in the dataset.  Additionally, the dataset contains the Spotify ID of each top song, so we can use that to 

2. What is the single biggest unresolved issue you are having? Please describe it briefly, and what your plan is for resolving this issue.

We were struggling to find a way to get the lyrics from the top songs we are looking at.  Thankfully, we found an API that uses musixmatch which corresponds with the lyrics that are already on Spotify, so we should be able to use the same Spotify IDs from the original kaggle data set to get the lyric information we need.  Now, we just have to put it all together and synthesize all of the different aspects into one data set.

3. What are the elements from outside of the course, if any, that you plan to incorporate into your project?

We’re going to use tidytext ([https://www.tidytextmining.com/](https://www.tidytextmining.com/)), an R package for doing NLP. However, we will mainly be relying on the basic functionalities, and use the outputs from the simple analyses as datasets to perform analytics on with techniques covered in the course.