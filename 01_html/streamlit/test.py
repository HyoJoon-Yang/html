#pip install streamlit
# streamlit 라이브러리 호출
import streamlit as st

# 마크다운을 기반으로 한 꾸미기 기능 작동
st.write(
    """
    # 웹 앱 스터디 및 테스트 용 페이지
    ### 열심히 배우는 중...
    * 1$ = 1300원
    """
)

# https://unsplash.com
# https://pixabay.com/ko
st.image(
    "https://cdn.pixabay.com/photo/2022/01/13/07/06/house-6934544_960_720.jpg"
    )