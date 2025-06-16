import streamlit as st
import pandas as pd

st.set_page_config(page_title="고등학생 SNS 이용률", layout="wide")

st.title("📱 고등학생 SNS 서비스 이용률 분석")
st.caption("출처: 한국언론진흥재단 『10대 미디어 이용 실태조사』 (2022.12.31)")

# 고등학생 SNS 이용률 데이터 (직접 입력)
data = {
    "SNS": ["인스타그램", "유튜브", "페이스북", "트위터", "카카오스토리", "틱톡", "핀터레스트", "밴드"],
    "이용률 (%)": [90.7, 89.6, 33.1, 24.0, 17.2, 16.6, 11.8, 5.0]
}
df = pd.DataFrame(data)
df.set_index("SNS", inplace=True)

# 바 차트 출력
st.subheader("✅ SNS별 이용률 (고등학생 기준)")
st.bar_chart(df)

# 데이터 테이블 확인용
if st.checkbox("📄 데이터 표로 보기"):
    st.dataframe(df)
