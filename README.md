# SIH2K22

- Problem statement: [Extraction of Data including voice and images from various social Media platforms from Disaster struck areas](https://vikas-066f8f.webflow.io/)

    <img src = "https://education21.in/wp-content/uploads/2022/02/sih.png">

- Team – <b>gitinitrepo</b>
- Ministry : National Disaster Response Force (NDRF)

<b>Team Members:</b>

Gautham Prabhu (<b>Team Lead</b>), Anurag Chowdhury, Soumya A R, Anshita Palorkar, Tanay Gupta, MV Srujan;

We represented our college Manipal Institute of Technology in the hackathon

# ABSTRACT

<b>VIKAS</b>, A real-time, multimodal solution linking disaster victims and first responders from NDRF: streamlining support to the most vulnerable.

In the event of a disaster, many people turn to social media to seek support, both material and mental. The data from these posts aids in increasing situational awareness as soon as possible. Text, images, videos, and audio extracted in real-time from these social media posts play a crucial role in identifying appropriate emergency responses to a particular disaster. Once irrelevant information is filtered out, deep-learning-based classification, object identification and natural language processing methods are used to expedite emergency response decision-making
processes. Easy-to-interpret visualizations provide details further facilitate the distribution of resources and dispatch required personnel to affected areas.

<img src="https://i.imgur.com/78tP0Gk.png"> 

Our solution involves the following components:

1) Data extraction- Realtime extraction of raw data 
2) Analysis of extracted data
   
# Data Extraction

Our project mainly deals with data that is available from tweets. This generally comprises <b>texts</b> and <b>images</b> extracted from the respective tweets.

## Text extraction
Our solution uses the Twitter API to access tweets in realtime during the occurence of a disaster. The Twitter API can be used to programmatically retrieve and analyze Twitter data, as well as build for the conversation on Twitter.

Tweepy is an easy to use Python library for accessing the Twitter API. 

The easiest way to install the latest version from PyPI is by using pip:

```bash
pip install tweepy
```

Using the API, A keyword and stream time are entered, and data is streamed real-time in a database framework. This data may include the text content and geolocations of the tweets along with links to images and videos.

For cleaning of data and preprocessing our model does the following:

- Remove non alphanumeric characters (ex. punctuation)
- Remove emoticons, URLs, emails, ‘RT’ using regular expression.
- Duplicated tweets are placed in a different pandas dataframe.
- Irrelevant tweets are filtered out using Natural Language Processing.

We also developed a Word Cloud which generates a collection of words which are associated with the disaster. These words are generated according to the frequency of their usage and their relevance with respect to the disaster.

<img src="https://i.imgur.com/wEtRtGh.png"> 


<img src="https://i.imgur.com/oLqYSNT.png"> 

An illustration of the word cloud for the tweets relevant to Japan bombings 


For determining the relevancy of a tweet, we used the [Crisis NLP dataset](https://crisisnlp.qcri.org/). We use a BERT based model to analyze this text which is described in the next section.

## Image extraction

Images are extracted from image links present after the relevant tweets are filtered. These images are then analysed later using Computer Vision models.


# Analysis of extracted data


## Analysing text







