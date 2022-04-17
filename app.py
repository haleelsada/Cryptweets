import streamlit as st
import cryptweet
st.set_page_config(page_title="Cryptweets",page_icon='https://preview.pixlr.com/images/800wm/100/1/1001457242.jpg')

st.title('Cryptweets')
st.header("Using Twitter API to predict future movement of cryptocurrencies and stocks")
test='It is known that social media platforms like twitter plays an imortant role in determining the movement of financial asset platforms like stock market and crytpocurrencies. It is expected to increase the price of Doge after a tweet from Elon musk. Here the sentiment of public about a cryptocoin or stock (or any current issue going on!) could be calculated with the help of twitter api and huggingface transformers and a little mathematics'

st.subheader(test)
key = st.text_input(label="Enter the keyword eg:#bitcoin ",)

while key!='':
    st.subheader(cryptweet.sentimentanalyser(key))
    break
