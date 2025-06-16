import streamlit as st
import pandas as pd

# CSV 파일 불러오기
df = pd.read_csv("한국언론진흥재단_10대미디어이용통계_SNS 서비스별 이용률_20221231 (1).csv", encoding="cp949")

st.title("📱 고등학생 SNS 서비스 이용률 분석")
st.markdown("출처: 한국언론진흥재단 (2022)")

# 고등학생 컬럼만 추출
df_sns = df[["내 용", "고등학생"]].rename(columns={"내 용": "SNS", "고등학생": "이용률 (%)"})
df_sns.set_index("SNS", inplace=True)

# 시각화
st.subheader("✅ SNS별 이용률 (고등학생 기준)")
st.bar_chart(df_sns)

# 데이터 확인
if st.checkbox("📄 원본 데이터 보기"):
    st.dataframe(df)
