import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="고등학생 SNS 사용 분석", layout="wide")
st.title("📊 고등학생 SNS 사용 시간 분석")

@st.cache_data
def load_data():
    df_sns = pd.read_csv("data/sns_usage_by_service.csv")
    df_school = pd.read_csv("data/media_usage_by_school_level.csv")
    # 예: 고등학생 필터
    df_sns_hs = df_sns[df_sns["학교급"]=="고등학교"]
    df_time = df_school[df_school["매체"]=="SNS"]["이용시간(분)"]
    return df_sns_hs, df_time

df_sns, df_time = load_data()

st.subheader("1️⃣ 플랫폼별 고등학생 SNS 서비스 이용률")
fig1 = px.bar(df_sns, x="서비스명", y="이용률", color="성별", barmode="group",
              labels={"이용률":"이용률(%)"})
st.plotly_chart(fig1, use_container_width=True)

st.subheader("2️⃣ 전체 청소년의 SNS 이용 시간 분포")
fig2 = px.histogram(df_time, nbins=20, labels={"value":"이용시간(분)"})
st.plotly_chart(fig2, use_container_width=True)

if st.checkbox("원본 데이터 보기"):
    st.write(df_sns.head())
    st.write(df_time.describe())
