import streamlit as st

st.image('images/adobo.png', width=100)
st.title ('HELLO, :red[RISKS] , GOODBYE.') 
st.header('Profiling Churn Risk of Customers for Cost Optimization', divider='red')

st.subheader("The Challenge:")
st.markdown("Adobo Credit Card (ACC) strives to optimize sales, boost business performance, and drive customer satisfaction.")
st.subheader("The Goal:")
st.markdown("Develop sales and marketing strategies that will further increase customers' card usage.")
st.markdown("---")

st.subheader("Risk-Profiling Objectives:")
st.markdown("In classifying the clients of Adobo Credit Card according to their churn risk, valuable insights on the clients can be obtained based on the following areas.")

st.markdown("Spending Behavior:")
st.caption("Spending frequency, Seasonal spending trends and patterns, Categorical budget allocation, Payment mode preferences")
st.markdown("Customer Demographic:")
st.caption("Customer age groups, Geographical location, Gender, Industry of work, profession")
st.markdown("---")

st.image('methodology.png')
st.caption("These are the five components of the methodology. Problem Scoping create quantifiable goals and objectives.")
st.markdown("---")

st.image('adobo_clients.png')
st.caption("Who are the Adobo clients? Based on 100,000 transaction data points obtained from January 2020 to December 2021, ACC was observed to have 94 unique clients. The majority of these customers are male, making up 93.6%, and range from 51-95 years old. They live in 172 cities across the Philippines, with the greatest percentage in Luzon, followed by Mindanao then Visayas.")
st.markdown("---")


