import streamlit as st
import datetime

# --- UI 구성 ---
st.set_page_config(page_title="Easy Work Log", page_icon="📝", layout="centered")
st.title("📝 Easy Work Log - 업무 일지 작성")

# 오늘 날짜 자동 표기
today = datetime.date.today().strftime("%Y-%m-%d")
st.markdown(f"**날짜:** {today}")

# 업무 유형 선택 (확장 가능)
work_types = ["일반 업무", "회의", "개발", "기획", "연구", "기타"]
selected_types = st.multiselect("업무 유형을 선택하세요 (복수 선택 가능)", work_types, default=[work_types[0]])

# 업무 내용 입력
content = st.text_area("업무 내용", height=200, placeholder="오늘의 업무 내용을 입력하세요...")

# 업무 시간 기록 (옵션)
col1, col2 = st.columns(2)
with col1:
    start_time = st.time_input("업무 시작 시간", value=datetime.time(9, 0))
with col2:
    end_time = st.time_input("업무 종료 시간", value=datetime.time(18, 0))

# 제출 버튼
submit = st.button("작성 및 저장")

# 결과 메시지 영역
if submit:
    if not content.strip():
        st.warning("업무 내용을 입력해 주세요.")
    else:
        # 실제 LLM/Google Drive 연동 로직은 추후 구현
        st.success("업무 일지가 성공적으로 작성되었습니다! (예시)")
        st.markdown(f"**[작성 결과 미리보기]**\n- 날짜: {today}\n- 유형: {', '.join(selected_types)}\n- 시작: {start_time}\n- 종료: {end_time}\n- 내용: {content}")

# (확장) 업무 시간 시각화/그래프 영역 (예시)
st.markdown("---")
st.subheader("📊 업무 시간 기록 및 통계 (예시)")
# 추후 실제 데이터와 연동
st.info("업무 시간 그래프 및 월별 리포트 기능은 추후 제공 예정입니다.")
