# ST8602-G2-Final-Project
The Final Project of ST8602 Group 2

Project Proposal Analysis Worksheet
 
Innovative Solutions Using AI and Cloud Technology
 
 
 
##Topics – The “What”:

Information cocoon detector. Information cocoon is a phenomenon which people tend to receive the same group of information due to the recommendation algorithms. 

locked in their own bubbles which makes them difficult to receive messages outside the boundary.
 
Information cocoon detector. Information cocoon is a phenomenon in which people tend to receive the same group of information due to the recommendation algorithms. Sometimes the users are locked inside their own bubbles which makes them difficult to receive messages from outside the boundary.
The application is intended to help analyze users' reading history to help them find out if they are trapped inside a specific cocoon without being aware of it and provide them with advice and recommendation on other materials and information in other areas.
By approval of collecting data, the app can also be used as a statistical tool to create an analysis chart to illustrate the main focus of the current society and the trend of the reading chosen by the public.

##Design Considerations:
 
 It has two main aspects: users and texts. 
For texts, our service has two functions:
Categorize texts into different groups like commercial, sports, …, to detect if there is a recommendation algorithm behind.
Detect the political leaning of each text and inform users. It can judge the bias inside the texts to keep users informed when reading the texts, like right-wings, republican, neutral…
For users, our service has two functions:
	After analyzing the texts given by users, we could detect if the user has been labelled, and return a possible user portrait in the current platform if exists 
	Mark the potential bias of each text for users’ reference.
*Future evolvability: Integrate with search engine for the related news of each text. With this search engine, our service could return a list of opinions from different groups corresponding to the text. Also, it could be used for fake news detection to an extent.
1. Detect if the users are trapped inside the cocoon and provide analysis and suggestions
2. Completely software solutions
3. Need to acquire the reading and surfing history under users' approval
4. Extract the  main idea of the articles inside the reading history and store the data into the could services
5. Categorize the texts into different groups based on their focus and record which group belongs to the users
6. Generate a web interface to help the user operate the search themself
7. The function can also be used to combine with the search engine
8. The function can also be used to combine with statistical count




##Overall Solution:

Users could use our solution as an add-on service. By extracting the texts on the page, our solution will analyze and categorize them in order to detect .If most files are detected to be categorized into the same group, then there is a high possibility that the user has been trapped in the information cocoon. We will then try to compare the groups and return a list of news from the corresponding opposite and neutral groups.

1.       Use Machine Learning Model to categorize the user into different groups based on their daily reading materials.
2.       Construct a web interface to allow user find out the result them self.


##Topics – The “Why”:

The recommendation algorithms has trapped people to repeatedly received and devour the same group of resources everyday, hard to jump out of the cocoon and discover the things they may be interested in but never got the chance to do so.

1.
Raising concerns about propaganda, fake news, calling for rational thinking, refusal to labeling
  2.
People seem to be curious to know what labels they belong to, e.g., Spotify year review, …
Even if they don’t mind being labeled, many of them may have the interest to discover what they look like in others’ opinion.
3. Provide the user with a border view of their thoughts and provide suggestions on other fields. People may be interested in the fields which they have never mentioned or viewed before.

##Implementation Considerations:

The main procedures are similar to recommendation, but the spirit inside is reversed.

First, we are going to extract a series of news to perform machine learning, in order to construct the database and a pre-built model for the bias judgment. They will be categorized into neutral and partisan news groups, respectively. With the trained model, we can then use it to analyze users’ input and determine the political leanings. We can collect users’ responses and marks after the service, thus further improving our model.

What’s more, algorithms often tag people with different labels to recommend the potential information. We could train the model to reversely identify the labels which users belong to in the platform. It could help them 

It also has the potential to be evolved in TV and radio broadcasts.




##Source
https://www.kaggle.com/code/vijju6/politicians-social-media-posts/data
https://deepblue.lib.umich.edu/data/concern/file_sets/3r074t98m
https://academic.oup.com/poq/article/80/S1/250/2223443?login=false
https://arxiv.org/abs/2109.00024
https://www.kaggle.com/datasets/patthoo/data-analysis-challenge-classifying-news-articles
https://arxiv.org/abs/2105.11910
 
