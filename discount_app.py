import streamlit as st
st.title("โปรแกรมคำนวณส่วนลดสินค้าและ VAT 7%")
prince = st.number_input("ราคาเต็มของสินค้า (บาท)", min_value=0.0)
coolpong = st.number_input("เปอร์เซ็นต์ส่วนลด (%)", min_value=0.0, max_value=100.0)
if st.button("คำนวณ"):
    discount = prince * coolpong / 100
    vat = (prince - discount) * 0.07
    total = prince - discount + vat
    st.write("ราคาสินค้า:", prince, "บาท")
    st.write("เปอร์เซ็นต์ส่วนลด:", coolpong, "%")
    st.write("ส่วนลดที่ได้รับ:", discount, "บาท")
    st.write("ภาษี VAT 7%:", vat, "บาท")
    st.success(f"ราคาสุทธิที่ต้องจ่าย: {total:.2f} บาท")
