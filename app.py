import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# 1. Page Config
st.set_page_config(page_title="Executive Analytics", layout="wide")

# 2. Enhanced Professional CSS (Glassmorphism & Midnight Theme)
st.markdown("""
    <style>
    /* Global Styles */
    .stApp { background-color: #0f172a; color: #f1f5f9; }
    
    /* Home Page Container */
    .home-container { text-align: center; padding-top: 150px; }
    
    /* Dashboard Cards */
    div[data-testid="stVerticalBlock"] div[data-testid="stVerticalBlock"] {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3);
    }
    
    /* Headers & Metrics */
    h1 { color: #38bdf8 !important; }
    .stMetricValue { color: #ffffff !important; }
    
    /* Buttons */
    div.stButton > button { 
        background: linear-gradient(90deg, #38bdf8, #818cf8); 
        color: white; border: none; padding: 12px 40px; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. State & Data
if "page" not in st.session_state: st.session_state.page = "home"
df = pd.DataFrame({'Date': pd.date_range(start='2026-01-01', periods=100), 
                   'Sales': np.random.randint(1000, 5000, 100), 
                   'Category': np.random.choice(['Marketing', 'Operations'], 100)})

# 4. Routing Logic
if st.session_state.page == "home":
    st.markdown("<div class='home-container'><h1>Executive Analytics Suite</h1><p>Data-Driven Decision Making</p></div>", unsafe_allow_html=True)
    if st.columns([1, 1, 1])[1].button("Enter Analytics Dashboard"):
        st.session_state.page = "dashboard"
        st.rerun()

elif st.session_state.page == "dashboard":
    st.title("📈 Performance Analytics")
    
    # KPIs in stylized cards
    col1, col2, col3 = st.columns(3)
    col1.metric("Revenue", "$452,000", "12%")
    col2.metric("Orders", "1,204", "5%")
    col3.metric("Satisfaction", "100%")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Chart Area
    c1, c2 = st.columns([2, 1])
    with c1:
        st.subheader("Revenue Trends")
        fig = px.line(df, x='Date', y='Sales', color='Category', color_discrete_sequence=['#38bdf8', '#fb7185'])
        fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color="white")
        st.plotly_chart(fig, use_container_width=True)
        
    with c2:
        st.subheader("Data Audit")
        st.dataframe(df.head(10), use_container_width=True)
        if st.button("Back to Home"):
            st.session_state.page = "home"
            st.rerun()