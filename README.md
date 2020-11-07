<p>
  <a href="https://www.linkedin.com/in/bhargav-sonvane" target="_blank">
   <img src="https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white">
 </a>
  <a href="https://opensource.org/licenses/MIT" target="_blank">
   <img src="https://img.shields.io/badge/License-MIT-yellow.svg?&style=for-the-badge&logoColor=white">
 </a>
</p>

# Tweets Sentiment Analysis

This project comprises of performing Sentiment Analysis on tweets without having prior knowledge of NLP techinques.
I have used GCP Free trial is used for using Cloud Natural Lanuguage API. So follow my steps carefully to avoid costs of that service. 


## Requirements

- Python version >= 3.4
- GCP Account.
- Twitter Developer account.


### GCP Account Setup

The Google Cloud Free Program comprises the following: 90-day, $300 Free Trial: New Google Cloud and Google Maps Platform users can take advantage of a 90-day trial period that includes $300 in free Cloud Billing credits to explore and evaluate Google Cloud and Google Maps Platform products and services.

#### GCP Project Creation

Dashboards are one way for you to view and analyze metric data. The Cloud Console provides predefined dashboards that require no setup or configuration.  
GCP project is a way for managing the services that we want to include among your organization and to hold control expenses, access authorizations to services that are configured within GCP.


#### NLP API Activation
Cloud Natural Lanuguage API must be activated within the project and for that GCP creates a service access key in the JSON file.
Steps are as follows:
1. Link your billing account for activating the API.
2. Create credentials is JSON format for connecting to the NLP API.
3. Create a service account.
4. Get the JSON file.


### Twitter Developers account

The tweets source is Twitter, so Twitter Developer Account is essential.
For accessing Twitter API, requires creating an APP within the Twitter Developers Account. After that, twiiter api keys & tokens need to be created. [details](https://developer.twitter.com/en/apps)

JSON file:
Keys.json:
```
{
    "Access_token":"Twitter-Access-Token",
    "Access_token secret":"Twitter-Access-Token-Secret",
    "API_key":"Twitter-API-Key",
    "API_secret key":"Twitter-API-Secret Key"
}
```
Now we have everything to need to sentiment the tweets using NLP API.

## Test Your Effort!

To verify that everything works correctly, a file is included that can be run on the command line and observe the results.

The steps to follow are those:

### Clone this repository

```
git clone https://github.com/bhargavsonvane/twittersentiment-nlpai.git
cd twittersentiment-nlpai
```

### Create Python Virtual Environment and Install Dependencies

```
python3 -m venv <virtualenvname>
```

In my case, <any name> is "virtualenvname".

```
source virtualenvname/bin/activate
pip3 install -r requirements.txt
```

### Set Google environment variable

Run at the command line:

```
export GOOGLE_APPLICATION_CREDENTIALS=<path-to-gcp-credential-file.json>
```

<path-to-gcp-credential-file.json> is the file that we downloaded with the Google credentials.

**Note:** This may be different for Windows Operating Systems, in my case I am on Ubuntu but it should work in the same way for Mac environments.

### Here You GO!! Run test file

```
python3 application.py -q GCP
```
Note here, GCP is the search term, use double quotes for more words in search terms like "India GDP".
