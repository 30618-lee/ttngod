import streamlit as st
import pandas as pd

st.set_page_config(page_title="고등학생 SNS 분석", layout="wide")
st.title("📱 고등학생 SNS 사용 시간 분석")

# 예시용 데이터 생성 (실제 데이터 파일 대신 간이 데이터 사용 가능)
data = {
    "서비스명": ["인스타그램", "유튜브", "페이스북", "카카오스토리", "틱톡"],
    "이용률_남학생": [70, 85, 30, 25, 60],
    "이용률_여학생": [80, 90, 20, 30, 65]
}
df = pd.DataFrame(data)

time_data = {
    "이용시간구간": ["0~1시간", "1~2시간", "2~3시간", "3시간 이상"],
    "학생 수": [120, 230, 150, 100]
}
df_time = pd.DataFrame(time_data)

# 1. 서비스별 이용률 시각화 (Streamlit 내장 바차트)
st.subheader("1️⃣ SNS 서비스별 이용률 (남학생)")
st.bar_chart(df.set_index("서비스명")[["이용률_남학생"]])

st.subheader("2️⃣ SNS 서비스별 이용률 (여학생)")
st.bar_chart(df.set_index("서비스명")[["이용률_여학생"]])

# 2. 이용 시간 분포
st.subheader("3️⃣ SNS 이용 시간 분포")
st.bar_chart(df_time.set_index("이용시간구간"))

# 3. 데이터 보기
if st.checkbox("📄 원본 데이터 보기"):
    st.write("서비스별 이용률")
    st.dataframe(df)
    st.write("이용 시간 분포")
    st.dataframe(df_time)
