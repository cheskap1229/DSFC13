import streamlit as st
./.streamlit/config.toml
[theme]

# Primary accent for interactive elements
primaryColor = '#7792E3'

# Background color for the main content area
backgroundColor = '#273346'

# Background color for sidebar and most interactive widgets
secondaryBackgroundColor = '#B9F1C0'

# Color used for almost all text
textColor = '#FFFFFF'

# Font family for all text in the app, except code blocks
# Accepted values (serif | sans serif | monospace) 
# Default: "sans serif"
font = "sans serif"

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
st.caption("Spending frequency (how often is this customer making a transaction?), Seasonal spending trends (are there any abrupt changes in spending habits across the year?), Categorical budget allocation (what are the customers spending on?), Payment mode preferences (does this client prefer to transact online or purchase in-store?)")
st.markdown("Customer Demographic:")
st.caption("Customer age groups, Geographical location, Gender, Industry of work, Profession")
st.markdown("---")

st.image('methodology.png')
st.caption("These are the five components of the methodology. Problem Scoping was done to create quantifiable goals and objectives, such as ensuring .")
st.markdown("---")

st.image('adobo_clients.png')
st.caption("Who are the Adobo clients? Based on 100,000 transaction data points obtained from January 2020 to December 2021, ACC was observed to have 94 unique clients. The majority of these customers are male, making up 93.6%, and range from 51-95 years old. They live in 60 cities across the Philippines, with the greatest percentage in Luzon, followed by Mindanao then Visayas.")
st.markdown("---")

st.image('limitations.png')
st.caption("Limitations")
st.markdown("---")

st.image('demographic.png')
st.caption("Demographic")
st.markdown("---")


