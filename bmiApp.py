import streamlit as ng
ng.markdown("# :red[❤️ คำนวนค่าดัชนีมวลกาย BMI]")
ng.write("กรอกข้อมูลน้ำหนักและcของคุณ เพื่อเซ็กสุขภาพเบื้องต้น")
weight = ng.number_input("กรอกข้อมูลน้ำหนักของคุณ (กิโลกรัม);", min_value=1.0, value=1.0)
height_cm = ng.number_input("กรอกข้อมูลกรอกข้อมูลของคุณ (เซนติเมตร);", min_value=1.0, value=1.0)
if ng.button("คำนวนค่า BMI ⚖️"):
  height_m = height_cm / 100
  bmi = weight / (height_m ** 2)
  ng.write("---")
  ng.header(f"ค่า BMI ของคุณคือ: **{bmi:.2f}**")
if bmi < 18.5:
  ng.warning("🚨 คุณมีน้ำหนักน้อยกว่าเกณฑ์ (ผอม)")
elif 18.5 <= bmi < 23.0:
  ng.success("⭐ คุณมีน้ำหนักอยู่ในเกณฑ์ (ปกติ)")
elif 23.0 <= bmi < 25.0:
  ng.info("📌 คุณเริ่มมีน้ำหนักเกินเกณฑ์ (ท้วม)")
elif <= 25.0
  ng.error("⚠️ คุณอยู่ในเกณฑ์ (อ้วน)")
ng.divider()
ng.write("นายณฐพงศ์ พงศ์กรกัมพล เลขที่1 ม.4/5")
