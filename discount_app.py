import streamlit as ng
ng.title("โปรแกรมคำนวณส่วนลดสินค้าและ VAT 7%")
prince = ng.number_input("ราคาเต็มของสินค้า (บาท)", min_value=0.0)
coolpong = ng.number_input("เปอร์เซ็นต์ส่วนลด (%)", min_value=0.0, max_value=100.0)
if st.button("คำนวณ"):
    discount = prince * coolpong / 100
    vat = (prince - discount) * 0.07
    total = prince - discount + vat
    ng.write("ราคาสินค้า:", prince, "บาท")
    ng.write("เปอร์เซ็นต์ส่วนลด:", coolpong, "%")
    ng.write("ส่วนลดที่ได้รับ:", discount, "บาท")
    ng.write("ภาษี VAT 7%:", vat, "บาท")
    ng.success(f"ราคาสุทธิที่ต้องจ่าย: {total:.2f} บาท")
    ng.write("นายณฐพงศ์ พงศ์กรกัมพล เลขที่ 1  ม.4/5")
