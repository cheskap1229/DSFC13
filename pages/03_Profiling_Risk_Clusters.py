import streamlit as st

st.title("Profiling Risk Clusters")
st.header("Here you can put each of your key results.", divider = 'red')

st.subheader('Average Inactivity')
st.image('purchasing1.png')
st.caption("Limitations")
st.markdown("---")

st.subheader('Average Spending (PHP) per Transaction')
st.image('purchasing2.png')
st.caption("Limitations")
st.markdown("---")

st.subheader('One-time Purchaser')
st.image('purchasing3.png')
st.caption("Limitations")
st.markdown("---")

st.subheader('Trend of Transaction Volume')
st.image('transaction_volume.png')
st.caption("Limitations")
st.markdown("---")
