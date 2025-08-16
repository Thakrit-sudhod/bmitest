import streamlit as st

st.set_page_config(page_title='welcome to my web', page_icon='😅')

kg = st.number_input('น้ำหนัก (kg) :')
cm = st.number_input('ส่วนสูง (cm) :')

if st.button('คำนวณ'):
    if kg <= 0 or cm <= 0:
        st.error('ไอเอ๋อ')
        st.image('X.png')
    else:
        bmi = kg / (cm / 100) ** 2
        st.write(f'BMI = {bmi:.2f}')
        
        if bmi < 18.5:
            st.info('กินหน่อย')
            st.image('A.png')
        elif bmi < 23:
            st.success('ปกติดีน้อง')
            st.image('B.png')
        elif bmi < 30:
            st.warning('เริ่มจำ้มั่ม')
            st.image('C.png')
        else:
            st.error('กินเยอะไปแล้วน่ะ')
            st.image('D.png')
