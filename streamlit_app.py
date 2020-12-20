import streamlit as st
import pandas as pd
from apriori import runApriori, dataFromFile, to_str_results

st.markdown("# Grant test app on Streamlit")

support = st.slider("Enter the Minimum Support Value", min_value=0.1, max_value=0.9, value=0.15)
confidence = st.slider(
    "Enter the Minimum Confidence Value", min_value=0.1, max_value=0.9, value=0.6
)

inFile = dataFromFile("store_data.csv")

items, rules = runApriori(inFile, support, confidence)

i, r = to_str_results(items, rules)

st.markdown("## Results")

st.markdown("### Frequent Itemsets")
st.write(i)

st.markdown("### Frequent Rules")
st.write(r)
