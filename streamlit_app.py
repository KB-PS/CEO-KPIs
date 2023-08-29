import datetime
import pandas as pd
import numpy as np
import os
import streamlit as st
from src.stobjects import KpiComponent
#from src.settings import keboola_client

st.set_page_config(layout="wide")
#st.title('💰 KPI Dashboard')

@st.experimental_memo(ttl=7200)
def read_df(table_id, index_col=None, date_col=None):
    return pd.read_csv('/data/in/table/your_data.csv',  index_col=index_col, parse_dates=date_col)
    #keboola_client.tables.export_to_file(table_id, '.')
    #table_name = table_id.split(".")[-1]
    #return pd.read_csv(table_name, index_col=index_col, parse_dates=date_col)

# 1 mock a dataframe
message = "from inside2 false"
rec = [{'channel':'tmp_streamlit_slack', 'text':message}]

# LINK TO THE CUSTOM CSS FILE
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + "/style.css")as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

date_from_c, date_to_c = st.columns(2)

df = read_df("in.c-empower_kpis.kpi_data", date_col=["date"])
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
