import streamlit as st
import pandas as pd

# df = pd.read_csv('./data/tatedama_utf.csv')
df = pd.read_csv('./data/tatedama.csv')
# st.dataframe(df)
# st.table(df)
st.line_chart(df)
st.bar_chart(df['購入額'])

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot(df.index, df['購入額'])
ax.set_title('FX graf')
st.pyplot(fig)

