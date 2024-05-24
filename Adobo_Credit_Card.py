import streamlit as st

st.image('images/adobo.png', width=100)
st.title ('HELLO, :red[RISKS] , GOODBYE.') 
st.header('Profiling Churn Risk of Customers for Cost Optimization', divider='red')

st.subheader("The Challenge:")
st.markdown("Adobo Credit Card strives to optimize sales, boost business performance, and drive customer satisfaction.")
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

st.image('adobo_clients.png')

