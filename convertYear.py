import streamlit as st
st.title("แอปพลิเคชั่นแปลง พ.ศ. เป็น ค.ศ.")

bh_year = st.number_input("กรอกปี พ.ศ.")
ce_year = bh_year - 543
st.subheader(f"ตรงกับปี ค.ศ. {ce_year}")
