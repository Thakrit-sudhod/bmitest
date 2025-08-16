import streamlit as st
import os

st.set_page_config(page_title='welcome to my web', page_icon='😅')

def show_image(filename):
    if os.path.exists(filename):
        st.image(filename)
    else:
        st.warning(f"ไม่พบไฟล์รูปภาพ: {filename}")

kg = st.number_input('น้ำหนัก (kg) :')
cm = st.number_input('ส่วนสูง (cm) :')

if st.button('คำนวณ'):
    if kg <= 0 or cm <= 0:
        st.error('ไอเอ๋อ')
        show_image('X.png')
    else:
        bmi = kg / (cm / 100) ** 2
        st.write(f'BMI = {bmi:.2f}')
        
        if bmi < 18.5:
            st.info('กินหน่อย')
            show_image('A.png')
        elif bmi < 23:
            st.success('ปกติดีน้อง')
            show_image('B.png')
        elif bmi < 30:
            st.warning('เริ่มจำ้มั่ม')
            show_image('C.png')
        else:
            st.error('กินเยอะไปแล้วน่ะ')
            show_image('D.png')

