# Talk-Like-Ted
This project started in Jan 2019, as part of the Data Associate Programme in SMU Business Intelligence Analytics. 
The main contributors are Fabian Toh and me. 

The project involves analysis on Ted Talk data (more than 2400 rows of data). The data is available in Kaggle: 

We first carried out some data cleaning, such as removal of na values in columns, splitting the rating and tags for each talk and create new dataframes for them. We did not manage to clean the occupation field as we did not really know how. We may re-visit this field in the future, as we believe it is worth analysing.

Then we moved on to carry out a text analysis on the transcripts. In the process, we realised the transcripts actually include song transcripts with music symbols, so we need to deal with those first. Next, we tried information retrieval using term frequency-inverse document frequency, sentiment analysis, and Latent Dirichlet allocation for topic modelling. We are still in the midst of improving our LDA models. 

In the future, we may attempt more models, such as topic classification with tags using logistics regression or support vector machines.
