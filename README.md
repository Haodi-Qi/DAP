# Talk-Like-TED
This project started in Jan 2019, as part of the Data Associate Programme in SMU Business Intelligence Analytics. 
The main contributors are Fabian Toh, Qi Haodi, and Tan Kin Meng. 

The project involves analysis on Ted Talk data (more than 2400 rows of data/TED talks). The data is available in Kaggle: https://www.kaggle.com/rounakbanik/ted-talks

There are two main types of analysis we carried out: Statistical Analysis on the metadata and Text Analysis on the transcript

<h2> Statistical Analysis </h2>

For the statistical analysis, we mainly focused on the rating of the TED Talks with other attributes, such as duration, number of comments and views. We discovered some interesting correlations among the attributes and suggested possible explanations, such as negative correlation between Courageous and Inspiring. 

Moreover, we attempted to predict the popularity of a talk, which is quantified by the number of comments and views, with the ratings and other attributes. The results are not as promising but we believe it was a good attempt. 

We further analyzed the talks by their tags. Distribution graph and boxplots of the viwership and comments were plotted and analyzed. It is intereseting to see the distribution graph of the number of talks by tag follows the Power Law (or 80:20 rule), and Culture tag stands out as the tag with the most views and comments based on the median value.

<h2> Text Analysis </h2>

Before cleaning the transcript, we eyeballed some of the scripts and found out that TED holds a variety of talks, including musical performances and live events. Those talks may have transcripts as lyrics, or just a few lines from the performers. We decided to remove those talks as they may affect our analysis later. After the filtering, we implemented a preprocessing with the Spacy module and contractions module. Considering the various topics of TED Talks, we also leveraged the Named Entity Recognition technique built in the Spacy module to isolate out entities. 

First we analyzed the correlation between the average and median sentence length of talks and the percentage of Longwinded and Confusing rating received, as we hypothesized that when the speaker speaks more long sentences, the eaiser for the audience to become lost and confused. The hypothesis was invalidated.

Then we analyzed the audience reactions captured in the transcript, such as "Laughters" and "Appaulse", with the ratings, as we hypothesized that the more laughters a talk generates, the funnier the audience would find the talk to be. The correlation is indeed positive, and we discovered some other interesting correlations as well. 

Lastly, we attempted to use Term Frequency - Inverse Document Frequecy (TF-IDF) metric to extract the keywords. We used simple Python dictionaries to compute the metric, and evaluated the results by inputing the keyword in the search bar of ted.com and checking where the corresponding talk would appear in the search results. The results are generally promising, as the keyword would help return the corresponding talk in the first page of the search results, if not the top 3 results.
