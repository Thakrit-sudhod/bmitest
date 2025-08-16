import streamlit as st
from gtts import gTTS
import io
import base64

st.set_page_config(page_title='welcome to my web', page_icon='😅')

kg = st.number_input('น้ำหนัก (kg) :')
cm = st.number_input('ส่วนสูง (cm) :')

if st.button('คำนวณ'):
    if kg <= 0 or cm <= 0:
        st.error('ไอเอ๋อ')
        st.image('X.png')
        word = 'อย่าหลอน'
    else:
        bmi = kg / (cm / 100) ** 2
        st.write(f'BMI = {bmi:.2f}')
        
       
        if bmi < 18.5:
            st.info('กินหน่อย')
            st.image('A.png')
            word = 'มึงเป็นสเกลริตั้นหรอ'
        elif bmi < 23:
            st.success('ปกติดีน้อง')
            st.image('B.png')
            word = 'แฮนส้ำโบร๋'
        elif bmi < 30:
            st.warning('เริ่มจำ้มั่ม')
            st.image('C.png')
            word = 'เบาหน่อยช่วงนี้'
        else:
            st.error('กินเยอะไปแล้วน่ะ')
            st.image('D.png')
            word = 'แดกเยอะไปแล้ว'

                   
        tts = gTTS(text=word, lang='th')
        mp3_fp = io.BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)



        b64 = base64.b64encode(mp3_fp.read()).decode()
        audio_html = f"""
        <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(audio_html, unsafe_allow_html=True)


