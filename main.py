import streamlit as st

# Thiết lập tiêu đề trang web
st.set_page_config(page_title="Tra Dung Sai Xà Gồ", page_icon="🏗️")

st.title("🏗️ Tra Dung Sai Xà Gồ AS/NZS 1365")
st.markdown("---")

# 1. Ô nhập Chiều dày thép nền (BMT)
bmt = st.number_input("Nhập chiều dày thép nền BMT (mm) từ bản vẽ:", 
                     value=1.6, min_value=0.1, max_value=4.0, step=0.01)

# 2. Ô chọn Độ mạ (Z)
zinc_options = {
    "Z70": 0.0098, "Z80": 0.0112, "Z100": 0.0140, "Z120": 0.0168,
    "Z180": 0.0252, "Z200": 0.0280, "Z275": 0.0385, "Z350": 0.0490, "Z450": 0.0630
}
zinc_type = st.selectbox("Chọn loại mạ kẽm (Z):", list(zinc_options.keys()), index=6) # Mặc định Z275

# 3. Logic tra bảng 5.1 AS/NZS 1365
def get_tolerance(v):
    if v <= 0.30: return 0.02
    elif v <= 0.50: return 0.03
    elif v <= 0.80: return 0.04
    elif v <= 1.20: return 0.05
    elif v <= 1.60: return 0.06
    elif v <= 2.00: return 0.07
    elif v <= 2.50: return 0.08
    elif v <= 3.00: return 0.09
    elif v <= 4.00: return 0.10
    return None

# 4. Tính toán
tol = get_tolerance(bmt)
t_zinc = zinc_options[zinc_type]

if tol:
    bmt_min = bmt - tol
    bmt_max = bmt + tol
    tct_nominal = bmt + t_zinc
    tct_min = bmt_min + t_zinc

    # 5. Hiển thị kết quả bằng các khung màu
    st.info(f"**Dung sai tiêu chuẩn:** ± {tol} mm")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("BMT tối thiểu", f"{bmt_min:.3f} mm")
    with col2:
        st.metric("BMT tối đa", f"{bmt_max:.3f} mm")

    st.warning(f"**TCT lý thuyết (bao gồm mạ):** {tct_nominal:.3f} mm")
    
    st.error(f"**TCT TỐI THIỂU CẦN ĐO ĐƯỢC:** {tct_min:.3f} mm")
    st.markdown("---")
    st.caption("Ghi chú: Dữ liệu dựa trên AS/NZS 1365:1996 - Table 5.1. TCT = BMT + Thickness of Coating.")
else:
    st.error("Chiều dày nhập vào nằm ngoài phạm vi tiêu chuẩn (0.1 - 4.0mm)")
