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


#### Activating the NLP Service and obtaining permission key in GCP

To use the Cloud Natural Language API in our application, we must activate said API within the project and obtain an access key in JSON format, this procedure is detailed in the following images:

When activating the API, it asks to be linked to the billing account.

Now, we obtain the credentials in json format that will allow us to connect to the NLP service of our project:

We now need to create a service account, which can have any name:

We continue configuring it as indicated and we get the json file


### Twitter Developers account

Since the interest of the application is not only sentiment analysis, but that these come from Twitter, we must have an account on [Twitter Developers](https://developer.twitter.com/en).

This step is perhaps the one that takes the most time, since accessing the Twitter API requires creating an App within the Twitter Developers account, and for this we must fill out a record where we expose the use that we will give to said application.

Once the creation of the App is authorized, we can navigate to its  [details](https://developer.twitter.com/en/apps). There we look at the Keys and Tokens tab, if necessary, click on the “Create” button in “Access token & access token secret”.


Create a json file with the following structure:

Keys.json:

```
{
    "Access_token":"Twitter-Access-Token",
    "Access_token secret":"Twitter-Access-Token-Secret",
    "API_key":"Twitter-API-Key",
    "API_secret key":"Twitter-API-Secret Key"
}
```

Once you have this file, you have everything you need to test the application.
## Testing the application

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

### Run test file

```
python3 application.py -q NLP
```

You can replace "NLP" with any other search query of interest, if it is more than one word it should be used in double quotes: "Machine Learning".
