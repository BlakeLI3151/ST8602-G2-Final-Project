# The Information Cocoon Detector

## Project Proposal Analysis Worksheet
### Innovative Solutions Using AI and Cloud Technology
 
Group Members: Wenxuan LI, Yihan GENG

 
### Topics – The “What”:

Information cocoon detector. Information cocoon is a phenomenon in which people tend to receive the same group of information due to the recommendation algorithms. Sometimes the users are locked inside their own bubbles, making it difficult to receive messages from outside the boundary.
The application is intended to help analyze users' reading history to help them find out if they are trapped inside a specific cocoon without being aware of it and provide them with advice and recommendation on other materials and information in other areas.
By approval of collecting data, the app can also be used as a statistical tool to create an analysis chart to illustrate the main focus of the current society and the trend of the reading chosen by the public.

### Design Considerations:
 
Based on the user-provided series of articles, we will analyze if there are any potential algorithmic effects, and return the categorization result and potential bias within each article to the user.

### Overall Solution:

Our solution uses Machine Learning Model to categorize the user into different groups based on their daily reading materials, and construct a web interface to allow users to find out the result themselves. Consideration is mainly from the articles’ perspective and the users’ perspective. 
For articles, our service has two functions:
Categorize texts into different groups like commercials, sports, etc., to detect if there is a recommendation algorithm behind it.
Detect the political leaning of each text and inform users. It can judge the bias inside the texts to keep users informed when reading the texts, like right-wing, republican, neutral, etc.
For users, our service has two functions:
After analyzing the texts given by users, we could detect if the user has been labeled, and return a possible user portrait in the current platform if it exists.
Mark the potential bias of each text for users’ reference.
*Future evolvability: 
Integrate with the search engine for the related news of each text. With this search engine, our service could return a list of opinions from different groups corresponding to the text. Also, it could be used for fake news detection to an extent.
It also has the potential to be evolved in TV and radio broadcasts. Integrating speech-to-text services such as Azure Speech Recognition with our solution, users could watch TV or listen to the radio while getting real-time feedback on the current news.
Our service could be implemented as an add-on service in browsers to achieve convenience. 


### Topics – The “Why”:

The recommendation algorithms have trapped people to repeatedly receive and devour the same group of resources every day, hard to jump out of the cocoon and discover the things they may be interested in but never got the chance to do so. The divided online world is making it harder for people to understand and accept different opinions, increasing aggression and undermining community unity. As such, we regard our solution in the following aspects:
1. Raising concerns about propaganda, fake news, calling for rational thinking, refusal to labeling. Social media misinformation and adversarial propaganda have caused more anxiety and depression than ever before, especially during the current epidemic.
2. People seem to be curious to know what labels they belong to, and what labels the current reading article belongs to, e.g., Spotify year review, … Even if they don’t mind being labeled, many of them may have the interest to discover what they look like in others’ opinion.
3. Provide the user with a border view of their thoughts and provide suggestions on other fields. People may be interested in areas they have never mentioned or viewed before.



### Implementation Considerations:

The main procedures are similar to recommendations, but our goal by implementing such algorithms is reversed. We are going to use Python and relevant packages to perform machine learning, categorizing the text dataset we extracted from reliable sources. Our main goal is to build the categorization model and challenge the series of documents given by the user, thus finding out the potential labels of each set of texts.

Reuse of Existing Github Project: 
A previous completed public repo illustrated the use of a python program for extracting data from articles by Feryandi. Part of the code could be used to help gather data from the target user’s history of reading (https://github.com/feryandi/CRF-Article-Extractor).


### Source
[1] https://www.kaggle.com/code/vijju6/politicians-social-media-posts/data
[2] https://academic.oup.com/poq/article/80/S1/250/2223443
[3] [2109.00024] Machine-Learning media bias
    https://arxiv.org/abs/2109.00024
[4] Data Set | Quantifying News Media Bias through Crowdsourcing and Machine Learning Dataset | ID: 8w32r569d | Deep Blue 
    https://deepblue.lib.umich.edu/data/concern/data_sets/8w32r569d
[5] https://www.kaggle.com/datasets/patthoo/data-analysis-challenge-classifying-news-articles
[6] [2105.11910] MBIC -- A Media Bias Annotation Dataset Including Annotator Characteristics pandemic of social media panic travels faster    	  than the COVID-19 outbreak | Journal of Travel Medicine | Oxford Academic
    https://arxiv.org/abs/2105.11910
[7] https://github.com/feryandi/CRF-Article-Extractor



### Link to Proposal Document 
https://docs.google.com/document/d/1Uql-GE4_SSQBIQyAumLwCo7JmcJWAhMgr1QTAVl2GRE/edit
### Link to Final Report 
https://docs.google.com/document/d/1NETsxAI2OlrDNVQ1IXFpR98O9jcIppn45x7msjO896I/edit#
###Link to Github Page
https://github.com/BlakeLI3151/ST8602-G2-Final-Project


### Steps and Assignment /Responsibilities
1)       Put all doc and links about the project into github
2)       Include proposal in readme
3)       Create skeleton of paper ready in google docs and link in github
a.       Abstract
b.       Introduction
c.        Related Work
d.       Solution Design
e.       Solution Implementation
f.         Lessons Learned and Beyond
g.       Conclusion
h.       References
4)       Daily Basis
a.       Update the paper
b.       Communication about the project in slack
c.        Check code in GitHub

### Discussion about Minimum Viable Prototype(MVP)
1)       Brainstorm on steps to follow to implement a prototype
a.       Design review (as compared to original suggestions)
   i.      Digital solution technology
1.       Cloud or laptops
2.       MQTT
3.       Big Data analytics
4.       DL
5.       Web App
6.       Block Chain
b.       Questions: W6 and more?
                       i.      What the project is about
                       ii.      Why we are doing it
                       iii.      How to do part it
                         iv.      Who is the solution intended for
                         v.      When should the solution be used
                         vi.      Where should the solution be used
c.        Gather reusable technology components(e.g. Lot ML)
d.       TODO: Review and install various components
e.       TODO: Adapt and assemble the various components
2)       Documentation:
a.       Update the readme and GitHub
b.       Fill in sections of the short paper




### Team:
1)       Review areas in red above and finalize
2)       Work on implementation details

### TA/Prof:
1)       Send updated Project – high level plan
2)       Put the code for reusable projects
3)       Share some business/tech posters
4)       Divide the work
5)       Help the team with tech details
6)       Relocate the code for reusable project
