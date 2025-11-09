import os
import io
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
from PIL import Image

# --- 준비 ---
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 모델 설정
TEXT_MODEL  = "models/gemini-2.5-flash"         # 텍스트 분석용

text_model  = genai.GenerativeModel(TEXT_MODEL)

# --- UI ---
st.title("🌤 감정 요약 ")
st.write("당신의 하루를 표현하면, Gemini가 감정을 요약해 드립니다.")

user_input = st.text_area("오늘의 기분을 적어주세요:", "")

if st.button("분석하고 요약 생성"):
    if not user_input.strip():
        st.warning("문장을 입력해주세요!")
        st.stop()

    # 1️⃣ 감정 요약
    
    summary_prompt = f"""
    다음 문장을 읽고 감정을 요약해줘.
    감정 이름(기쁨, 슬픔, 분노, 불안 등)과 이유를 간단히 한 문장으로 표현해줘.
    입력: "{user_input}"
    """
    response = text_model.generate_content(summary_prompt)
    summary = response.text.strip()
    st.subheader("🧠 감정 요약 결과")
    st.write(summary)
