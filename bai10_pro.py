import streamlit as st
from datetime import date
 
st.set_page_config(page_title="🎂 Đặt Tiệc Sinh Nhật", page_icon="🎉", layout="wide")
 
st.markdown(
    """
    <div style="text-align:center; background:linear-gradient(90deg,#ff9a9e,#fad0c4);
                padding:25px; border-radius:20px; color:white;">
        <h1>🎈 Happy Party Planner 🎈</h1>
        <h4>Hãy chọn món ngon và để chúng tôi chuẩn bị cho buổi tiệc hoàn hảo của bạn!</h4>
    </div>
    """,
    unsafe_allow_html=True
)
 
appetizer = {
    "Gỏi củ hủ dừa": 80000,
    "Súp gà": 60000,
    "Mực chiên xù": 90000
}
 
main = {
    "Lẩu hải sản": 250000,
    "Tôm lăn bột sốt chanh dây": 180000,
    "Bít tết": 220000,
    "Heo sữa quay": 260000
}
 
dessert = {
    "Rau câu phô mai": 50000,
    "Hoa quả dầm": 60000,
    "Cheesecake": 70000
}
 
st.markdown("### 💌 Thông tin đặt tiệc")
 
with st.form("party_form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("👤 Họ và tên")
        phone = st.text_input("📞 Số điện thoại")
        guest_count = st.number_input("👥 Số lượng khách", min_value=1, value=10)
    with col2:
        date_party = st.date_input("📅 Ngày tổ chức", value=date.today())
        location = st.text_input("🏠 Địa điểm tổ chức")
        note = st.text_area("📝 Ghi chú thêm (nếu có)")
 
    st.markdown("### 🍽️ Chọn thực đơn của bạn")
    opt1 = st.multiselect("🥗 Món khai vị", list(appetizer.keys()))
    opt2 = st.multiselect("🍛 Món chính", list(main.keys()))
    opt3 = st.multiselect("🍰 Món tráng miệng", list(dessert.keys()))
    submitted = st.form_submit_button("✨ Xác nhận đặt tiệc ✨")
 
if submitted:
    if not name or not phone or not location:
        st.error("⚠️ Vui lòng nhập đầy đủ thông tin cá nhân và địa điểm!")
    else:
        st.success("🎉 Cảm ơn bạn! Dưới đây là hóa đơn đặt tiệc của bạn:")
        st.markdown("---")
        st.markdown(f"""
        <div style="background:#fff8f0; padding:20px; border-radius:15px;">
            <h2 style="text-align:center;">🧾 HÓA ĐƠN ĐẶT TIỆC</h2>
            <p><b>Khách hàng:</b> {name}</p>
            <p><b>Số điện thoại:</b> {phone}</p>
            <p><b>Ngày tổ chức:</b> {date_party.strftime('%d/%m/%Y')}</p>
            <p><b>Địa điểm:</b> {location}</p>
            <p><b>Số lượng khách:</b> {guest_count}</p>
        </div>
        """, unsafe_allow_html=True)
 
        total = 0
 
        def show_menu_section(title, items, menu):
            global total
            st.markdown(f"#### {title}")
            if not items:
                st.write("_(Không chọn món nào)_")
            else:
                for item in items:
                    price = menu[item]
                    total += price
                    st.write(f"- {item}: **{price:,.0f} VNĐ**")
 
        show_menu_section("🥗 Món khai vị", opt1, appetizer)
        show_menu_section("🍛 Món chính", opt2, main)
        show_menu_section("🍰 Món tráng miệng", opt3, dessert)
 
        st.markdown("---")
        st.markdown(
            f"""
            <div style="text-align:center; background:#ffe5b4; padding:20px;
                        border-radius:20px; margin-top:10px;">
                <h2>💰 Tổng cộng: <span style="color:#d90429;">{total:,.0f} VNĐ</span></h2>
                <p style="font-size:18px;">🎂 Chúc buổi tiệc của bạn thật vui vẻ và trọn vẹn 🎉</p>
            </div>
            """,
            unsafe_allow_html=True
        )
 
        st.balloons()
 
st.markdown("""
<style>
    .stApp {
        background-color: #fffdf9;
    }
    .stForm {
        background: #fffaf5;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0px 3px 10px rgba(0,0,0,0.1);
    }
    .stButton>button {
        background: linear-gradient(90deg,#ff758c,#ff7eb3);
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 16px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)