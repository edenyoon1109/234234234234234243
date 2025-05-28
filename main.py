import streamlit as st
import pandas as pd
import plotly.express as px

# 구글 드라이브에서 데이터 불러오기
data_url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
df = pd.read_csv(data_url)

st.title("Plotly 시각화 예제")

# 데이터 보여주기
st.write("데이터 미리보기:", df.head())

# 데이터 컬럼 리스트 확인
cols = df.columns.tolist()
st.write("데이터 컬럼:", cols)

# 예: 첫번째와 두번째 컬럼으로 산점도 그리기
if len(cols) >= 2:
    fig = px.scatter(df, x=cols[0], y=cols[1], title=f"{cols[0]} vs {cols[1]} 산점도")
    st.plotly_chart(fig)
else:
    st.write("데이터 컬럼이 충분하지 않습니다.")
