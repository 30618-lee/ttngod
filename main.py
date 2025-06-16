import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="고등학생 SNS 사용 분석", layout="wide")
st.title("📱 고등학생 SNS 사용 시간 분석")

# 데이터 불러오기 (예시용 CSV 경로)
@st.cache_data
def load_data():
    df_sns = pd.read_csv("data/sns_usage_by_service.csv")
    df_time = pd.read_csv("data/media_usage_by_school_level.csv")
    # 필터링: 고등학생 + SNS 관련
    df_sns = df_sns[df_sns["학교급"] == "고등학교"]
    df_time = df_time[df_time["매체"] == "SNS"]
    return df_sns, df_time

df_sns, df_time = load_data()

# 1. 서비스별 이용률 시각화
st.subheader("1️⃣ SNS 서비스별 고등학생 이용률 (Matplotlib)")
fig1, ax1 = plt.subplots(figsize=(10, 5))
df_plot = df_sns.groupby("서비스명")["이용률"].mean().sort_values(ascending=False)
ax1.bar(df_plot.index, df_plot.values, color='skyblue')
ax1.set_ylabel("이용률 (%)")
ax1.set_xlabel("SNS 서비스")
ax1.set_title("고등학생의 SNS 서비스별 평균 이용률")
st.pyplot(fig1)

# 2. SNS 이용시간 분포 (히스토그램)
st.subheader("2️⃣ SNS 이용 시간 분포")
fig2, ax2 = plt.subplots()
ax2.hist(df_time["이용시간(분)"], bins=10, color='lightcoral', edgecolor='black')
ax2.set_xlabel("이용 시간(분)")
ax2.set_ylabel("학생 수")
ax2.set_title("고등학생의 SNS 일일 이용 시간 분포")
st.pyplot(fig2)

# 원본 데이터 보기
if st.checkbox("📄 원본 데이터 보기"):
    st.write("SNS 서비스별 이용률 데이터")
    st.write(df_sns.head())
    st.write("이용 시간 데이터 요약")
    st.write(df_time.describe())
