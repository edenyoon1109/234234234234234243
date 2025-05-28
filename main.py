import streamlit as st
import pandas as pd
import plotly.express as px

# 구글 드라이브에서 데이터 불러오기
data_url = "https://drive.google.com/uc?export=download&id=1pwfON6doXyH5p7AOBJPfiofYlni0HVVY"
df = pd.read_csv(data_url)

st.title("Plotly 막대그래프 시각화")

st.write("데이터 미리보기:", df.head())

# 데이터 컬럼 리스트 (숫자형 컬럼과 전체 컬럼 분리)
all_columns = df.columns.tolist()
numeric_columns = df.select_dtypes(include='number').columns.tolist()

# x축(범주형 혹은 문자열 컬럼) 선택
x_axis = st.selectbox("X축(범주형) 선택", options=all_columns)

# y축(숫자형 컬럼) 선택
y_axis = st.selectbox("Y축(숫자형) 선택", options=numeric_columns)

if x_axis and y_axis:
    fig = px.bar(df, x=x_axis, y=y_axis, title=f"{x_axis}에 따른 {y_axis} 막대그래프")
    st.plotly_chart(fig)
else:
    st.write("x축과 y축을 올바르게 선택해 주세요.")
