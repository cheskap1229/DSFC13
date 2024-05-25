import streamlit as st

st.title("RFM Segmentation and :red[K-Means Clustering]")
st.header("Inputting RFM Scores in K-means outputs 3 customer clusters. Let's take a look at these clusters.", divider = 'red')

st.subheader("RFM Segmentation")
st.image('RFM_table.png')
st.markdown("To quantify the spending habits of ACC clients, the following features were extracted from the data: Recency Score, Frequency Score, and Monetary Score. Recency Score is set from 1-5, with 1 indicating that the customer's last transaction was more than a year ago and 5 indicating that the customer's last transaction was within a month ago. A Frequency Score of 1 means that the customer has made less than 600 transactions in total while an FS of 4 means that the customer made at least 1800 transactions. Lastly, a customer spending less than \$10,000 will obtain a Monetary Score of 1 while spending more than \$100,000 will give them a score of 4.")
st.markdown("---")

st.subheader("K-Means Clustering")
st.markdown("From RFM Segmentation, the Recency, Frequency, and Monetary values were then plugged into the K-means clustering algorithm, which first computes k number of clusters using one of 2 methods.")
st.markdown("Before the data can be clustered, the number of clusters k must first be evaluated by either the Elbow Method or the Silhouette Score Method. The Silhouette Score Method is favorable when data is skewed or there are duplicates in the data since this method identifies them [1]. However, the team selected the k given by the Elbow Method since the graph shows the typical elbow graph. The sharp decreasing slope in intertia, (which is related to the distance between the points and centroids*) indicates that there is a clear pattern or good clustering in the dataset, which is ideal when choosing the Elbow Method [1].")
st.image('kmeans2.png')
st.caption("Sources:")
st.caption("[1] https://adria708.medium.com/elbow-method-vs-silhouette-co-efficient-in-determining-the-number-of-clusters")
#st.caption("[2] https://www.codecademy.com/learn/dspath-unsupervised/modules/dspath-clustering/cheatsheet")
st.markdown("---")

st.image('kmeans.png')
st.caption("K-means")
st.markdown("Three clusters were generated from K-means: From this data it can be seen that high-risk customers are defined The data science team defines high-risk customers as those with low RFM scores, since these ho have not made  with low recency To successfully cluster")
st.markdown("---")
