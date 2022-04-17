# Cryptweets
**Integrating Twitter API with transformers to predict future movement of cryptocurrencies and stocks**
![](https://images6.alphacoders.com/114/thumb-1920-1141549.png)
It is known that social media platforms like twitter plays an imortant role in determining the price of financial asset platforms like stock market and crytpocurrencies. It is expected to increase the price of Doge after a tweet from Elon musk. Here the sentiment of public about a cryptocoin or stock (or any current issue going on!) could be calculated with the help of **twitter api** and **huggingface transformers** and a little mathematics
## Libraries used
tweepy - 4.8.0

emoji - 1.7.0

transformers - 4.18.0

streamlit - 1.8.0

torch - 

## How to configure
Tweets related to specific keyword is extracted with the api and then it's sentiment is analysed to predict the movement of curresponding asset. The project is deployed in streamlit platfrom. It could be find **[here](https://share.streamlit.io/haleelsada/cryptweets/main/app.py)**. 

 The project colab page could be found **[here](https://github.com/haleelsada/Cryptweets/blob/main/Cryptweet.ipynb)**
