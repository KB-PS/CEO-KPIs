#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 12:05:14 2023

@author: ondrejsvoboda
"""
import streamlit as st
from src.notifications import init_jira_client
from kbcstorage.client import Client

DECIMALS = 1

# jira
SERVER = st.secrets["jira_credentials"]["server"]
USER_EMAIL = st.secrets["jira_credentials"]["email"]
JIRA_API_TOKEN = st.secrets["jira_credentials"]["jira_api_token"]
jira_cli = init_jira_client(SERVER, USER_EMAIL, JIRA_API_TOKEN)

# credentials
KEBOOLA_STACK = st.secrets["keboola_credentials"]["stack"]
KEBOOLA_TOKEN = st.secrets["keboola_credentials"]["token"]
keboola_client = Client(KEBOOLA_STACK, KEBOOLA_TOKEN)
