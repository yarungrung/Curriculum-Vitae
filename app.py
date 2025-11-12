import streamlit as st
from datetime import date

st.set_page_config(layout="wide", page_title="蔡亞蓉的履歷！")

st.title("蔡亞蓉的履歷！")

st.markdown(
    """
    以下為我的自我介紹，其餘分頁為大學期間所舉辦過的活動、做過的報告及成品展示
    """,
    unsafe_allow_html=True
)

st.markdown("### 基本資料與自我介紹")
st.markdown(
    """
     <p>
    基本資料<br>
    1. 連絡電話：0939988593 <br>
    2. email：s1243032@gm.ncue.edu.tw <br>
    3. 學歷：彰化師範大學地理學系🌏三年級🗺️<br>
    4. 工作經歷：2024年暑期，於台北市立兒童新樂園擔任工讀生 <br>
                2025年暑期，於社區游泳池擔任救生員
    5. 專業技能：<br>
       (1)駕照種類：機車駕照 <br>
       (2)語文能力：中文、英文、台語、西班牙文(A1) <br>
       (3)電腦能力：excel、word、canva、QGIS、Arcgis<br>

    自我介紹<br>
    您好，我是目前就讀彰化師範大學地理系三年級的蔡亞蓉， 縱
    </p>
    """,
    unsafe_allow_html=True
)

st.markdown("### 南科發展史📒")
st.image("南科史2.jpg")