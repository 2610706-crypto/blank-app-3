import streamlit as st

# 1. 웹 페이지 제목 설정
st.title("🎢 놀이기구 탑승 가능 여부 확인기")
st.write("본인의 키를 입력하면 탑승 가능 여부를 알려드립니다.")

st.divider() # 구분선

# 2. 사용자 입력 받기 (기본값 150, 최소 50, 최대 250)
height = st.number_input('키를 입력하세요 (cm):', min_value=50, max_value=250, value=150, step=1)

# 슬라이더로도 조절할 수 있게 만들고 싶다면 아래 주석을 해제하세요.
# height = st.slider('키를 선택하세요 (cm):', min_value=50, max_value=250, value=150)

st.subheader("결과")

# 3. 작성하신 조건문 로직 적용 (st.success, st.warning, st.error로 시각 효과 주기)
if height < 100:
    st.error('❌ 탑승 불가 (100cm 미만)')
elif height < 130:
    st.warning('👨‍👦 보호자 동행 시 탑승 가능')
elif height < 195:
    st.success('🟢 탑승 가능')
else:
    st.error('❌ 탑승 불가 (195cm 이상)')