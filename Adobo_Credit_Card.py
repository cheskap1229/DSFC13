import streamlit as st

st.image('images/adobo.png', width=100)
st.title ('HELLO, :red[RISKS], GOODBYE.') 
st.header('Profiling Churn Risk of Customers for Cost Optimization', divider='red')

st.subheader("The Challenge:")
st.markdown("Adobo Credit Card (ACC) strives to optimize sales, boost business performance, and drive customer satisfaction.")
st.subheader("The Goal:")
st.markdown("Develop sales and marketing strategies that will further increase customers' card usage.")
st.markdown("---")

st.subheader("Risk-Profiling Objectives:")
st.markdown("In classifying the clients of Adobo Credit Card according to their churn risk, valuable insights on the clients can be obtained based on the following areas.")

st.markdown("Spending Behavior:")
st.caption("Spending frequency - how often is this customer making a transaction?, Seasonal spending trends - are there any abrupt changes in spending habits across the year?, Categorical budget allocation - what are the customers spending on?, Payment mode preferences - does this client prefer to transact online or purchase in-store?")
st.markdown("Customer Demographic:")
st.caption("Customer age groups - is this customer a Boomer? a Gen X?, Geographical location - what regions are these customers from?, Gender, Industry of work, Profession")
st.markdown("---")

st.image('methodology.png')
st.caption("The scope of the problem is that there is a category of customers who are at high risk of churning. The goal is to propose strategies to encourage these users to be more active credit card users, while ensuring the continued customer satisfaction Problem Scoping initiated by the discovery that the customers could be clustered into risk levels. this is the main issue we want to solve. high-risk customers must be contacted personally during specifc periods of inactivity. we want to encourage mid risk to lower their being risk by increasing their rfm scores. we want to further engage low risk customers and ensure the ACC product continues to be satisfactory (meaning they use their card frequently) was done to create quantifiable goals and objectives, such as ensuring .")
st.markdown("---")

st.image('adobo_clients.png')
st.caption("Who are the Adobo clients? Based on 100,000 transaction data points obtained from January 2020 to December 2021, ACC was observed to have 94 unique clients. The majority of these customers are male, making up 93.6%, and range from 51-95 years old. They live in 60 cities across the Philippines, with the greatest percentage in Luzon, followed by Mindanao then Visayas.")
st.markdown("---")

st.image('limitations.png')
st.markdown("-Customer satisfaction is defined by")
st.markdown("-Churn is defined as soft churn")
st.markdown("---")

st.image('demographic.png')
st.caption("Demographic")
st.markdown("---")


