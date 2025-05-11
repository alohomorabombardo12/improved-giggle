import streamlit as st
from pathlib import Path

# --- CONFIGURATION ---
st.set_page_config(page_title="ชุมชนการเรียนรู้ภาษาไทย - Thai Learning Community", layout="wide")

# --- Replace with your actual Google Form EMBED URL ---
GOOGLE_FORM_EMBED_URL = "https://docs.google.com/forms/d/e/your-embed-form-link/viewform?embedded=true"

# --- Title and Welcome ---
st.title("ยินดีต้อนรับสู่ชุมชนการเรียนรู้ภาษาไทย!")
st.subheader("Welcome to the Thai Learning Community")
st.write("Discover past moments from our events and register to join our growing family of Thai learners.")

# --- Sidebar Navigation ---
st.sidebar.title("เมนู | Menu")
view = st.sidebar.radio("เลือกหมวดหมู่ | Choose a section", ["ภาพกิจกรรม | Event Photos", "วิดีโอ | Videos", "ลงทะเบียน | Register"])

# --- Image Section ---
if view.startswith("ภาพกิจกรรม"):
    st.header("ภาพกิจกรรมที่ผ่านมา")
    image_dir = Path("images")
    image_files = list(image_dir.glob("*.[jp][pn]g"))

    if image_files:
        cols = st.columns(3)
        for i, image_file in enumerate(image_files):
            with cols[i % 3]:
                st.image(str(image_file), caption=image_file.stem, use_column_width=True)
    else:
        st.info("ยังไม่มีภาพกิจกรรม กรุณาเพิ่มรูปภาพในโฟลเดอร์ 'images/'")

# --- Video Section ---
elif view.startswith("วิดีโอ"):
    st.header("วิดีโอกิจกรรม")
    video_dir = Path("videos")
    video_files = list(video_dir.glob("*.mp4"))

    if video_files:
        for video_file in video_files:
            st.video(str(video_file))
            st.caption(video_file.stem)
    else:
        st.info("ยังไม่มีวิดีโอ กรุณาเพิ่มไฟล์ในโฟลเดอร์ 'videos/'")

# --- Registration Section ---
elif view.startswith("ลงทะเบียน"):
    st.header("ลงทะเบียนเข้าร่วมชุมชน")
    st.markdown("กรุณากรอกแบบฟอร์มด้านล่างเพื่อลงทะเบียนเข้าร่วมกิจกรรมและชุมชนของเรา:")

    st.markdown(
        f"""
        <iframe src="{GOOGLE_FORM_EMBED_URL}"
        width="100%" height="800" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
        """,
        unsafe_allow_html=True,
    )
