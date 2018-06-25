#Question 1 :   What is an access token? Generate your access token for any API.(for example Twitter,Spotify etc).


The Access Token is a credential that can be used by an application to access an API.

It can be any type of token (such as an opaque string or a JWT) and is meant for an API. Its purpose is to inform the API that the bearer of this token has been authorized to access the API and perform specific actions (as specified by the scope that has been granted).

The Access Token should be used as a Bearer credential and transmitted in an HTTP Authorization header to the API.




*to generate access token


1. Create a twitter account
2. Go to apps.twitter.com
3. Click on create new application
4. Fill the form
5. Click on create new application
6. Note the consumer_key,consumer_secret,access_token,access_token_secret



#Question 2 :-   Get the IP address of some common sites like Google, Facebook by using DNS lookup.

# Google
C:\Users\HP>nslookup google.com
Server:  UnKnown
Address:  2405:200:800::1

Non-authoritative answer:
Name:    google.com
Addresses:  2404:6800:4002:802::200e
          172.217.31.14
		  
		 
# Facebook		 
C:\Users\HP>nslookup facebook.com
Server:  UnKnown
Address:  2405:200:800::1

Non-authoritative answer:
Name:    facebook.com
Addresses:  2a03:2880:f10c:283:face:b00c:0:25de
          157.240.13.35



#Question3:- Using Tweepy library try to extract tweets from Twitter.



import tweepy

consumer_key_017='******************'
consumer_secret_017='***************'


access_token_017='******************'
access_token_secret_017='****************'


auth=tweepy.OAuthHandler(consumer_key_017,consumer_secret_017)
auth.set_access_token(access_token_017, access_token_secret_017)
api = tweepy.API(auth)

tweets=api.search('#MumbaiRains', lang="en",count=08,tweet_mode="extended")


#print(tweets)

for tweet in tweets :
    print("------------------------------")
    print(tweet.full_text)
    print("------------------------------")
	

#Question 4:  What is a difference between library and API . Figure it out with examples.


A library is a collection of functions / objects that serves one particular purpose.
you could use a library in a variety of projects. (Various specialized services in our case)

ex: JQuery library, is a library of prewritten,
cross-browser Javascript animations and functions 
which you will need while making a website.


An API is an interface for other programs to interact with your program or library without having direct access.
( giving specifications for our need to various vendors in our case)

ex: with Google Map APIs you can show maps for different places without 
writing/hosting the whole code on your server, and just use it,
usually this data transfer is in form of JSON i.e JavaScript Object Notation.
