import streamlit as st

st.title("RFM Segmentation and K-Means Clustering")
st.header("Inputting RFM Scores in K-means Outputs 3 customer clusters. Let's take a look at these clusters.", divider = 'red')

st.subheader("RFM Segmentation")
st.image('RFM_table.png')
st.markdown("To quantify the spending habits of ACC clients, the following features were extracted from the data: recency score, frequency score, and monetary score. Recency Score is set from 1-5, with 1 indicating that the customer's last transaction was more than a year ago and 5 indicating that the customer's last transaction was within a month ago. A Frequency Score of 1 means that the customer has made less than 600 transactions in total while an FS of 4 means that the customer made at least 1800 transactions. Lastly, a customer spending less than \$10,000 will obtain a Monetary Score of 1 while spending more than \$100,000 will give them a score of 4.")
st.markdown("---")

st.image('kmeans2.png')
st.caption("K-means")
st.markdown("---")

st.image('kmeans.png')
st.caption("K-means")
st.markdown("Three clusters were generated from K-means: From this data it can be seen that high-risk customers are defined The data science team defines high-risk customers as those with low RFM scores, since these ho have not made  with low recency To successfully cluster")
st.markdown("---")
