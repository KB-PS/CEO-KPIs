import datetime
import pandas as pd
import numpy as np
import streamlit as st
from src.stobjects import KpiComponent

st.set_page_config(layout="wide")
#st.title('💰 KPI Dashboard')

# 1 mock a dataframe
message = "from inside2 false"
rec = [{'channel':'tmp_streamlit_slack', 'text':message}]

# LINK TO THE CUSTOM CSS FILE
with open("style.css")as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

date_from_c, date_to_c = st.columns(2)
df = pd.read_csv("data.csv", parse_dates=["date"])
df.sort_values(by="date", inplace=True)

with date_from_c:
    DFROM = st.date_input(
        "From",
        df.date.min()
    )

with date_to_c:
    DTO = st.date_input(
        "To",
        datetime.date.today()
    )

DFROM = DFROM.isoformat()
DTO = DTO.isoformat()

c_sales, c_orders, c_new_customers = st.columns(3)
with c_sales:
    salesc = KpiComponent(df, "sales", np.sum, dto=DTO, dfrom=DFROM)
with c_orders:
    ordersc = KpiComponent(df, "orders", np.mean, dto=DTO, dfrom=DFROM)
with c_new_customers:
    customersc = KpiComponent(df, "new_customers", np.sum, dto=DTO, dfrom=DFROM)

c_margin, c_avg_order, c_conv_rate = st.columns(3)
with c_margin:
    customersc = KpiComponent(df, "on_time_delivery", np.sum, dto=DTO, dfrom=DFROM)
with c_avg_order:
    customersc = KpiComponent(df, "average_order_value", np.sum, dto=DTO, dfrom=DFROM)
with c_conv_rate:
    customersc = KpiComponent(df, "conversion_rate", np.sum, dto=DTO, dfrom=DFROM)
    
