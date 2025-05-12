import streamlit as st
from pathlib import Path

# --- CONFIGURATION ---
st.set_page_config(page_title="Thai Learning Community", layout="wide")
st.image("assets/banner.jpg", use_column_width=True)

# --- GOOGLE FORM EMBED LINK ---
GOOGLE_FORM_EMBED_URL = "https://forms.gle/QoXLDN8dbepnWZRv6"

# --- EVENTS MAPPING ---
events = {
    "Bangkok Event": "bangkok_event",
    "Metal Craft": "metal_craft",
    "Singapore Event": "singapore_event"
}

# --- Custom CSS ---
st.markdown("""
    <style>
        body {
            background-color: #eaf4fc;
        }
        .custom-header {
            background-color: #d0e8ff;
            padding: 2rem;
            border-radius: 20px;
            text-align: center;
            box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
        }
        .card {
            background-color: white;
            padding: 1rem;
            border-radius: 15px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            margin-bottom: 1rem;
            text-align: center;
        }
        .card img {
            border-radius: 10px;
            max-width: 100%;
            height: auto;
        }
        .card-title {
            font-weight: 600;
            margin-top: 0.5rem;
            color: #333;
        }
        .card-text {
            color: #555;
            font-size: 0.9rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar Navigation ---
st.sidebar.title("Menu")
view = st.sidebar.radio("Navigate to:", ["Home", "Photo Gallery", "Video Gallery", "Register"])

# --- Homepage ---
if view == "Home":
    st.markdown('<div class="custom-header"><h1>Welcome to the Thai Learning Community</h1></div>', unsafe_allow_html=True)
    st.write(" ")

    # --- Upcoming Event ---
    st.subheader("🎉 Upcoming Event")
    upcoming_event_title = "Metal Craft"
    upcoming_event_folder = "metal_craft"
    upcoming_event_desc = "Discover traditional Thai craftsmanship through metalworking."

    img_dir = Path(f"events/{upcoming_event_folder}/images")
    image_files = list(img_dir.glob("*.[jp][pn]g"))
    upcoming_image = str(image_files[0]) if image_files else "https://via.placeholder.com/600x300.png?text=Upcoming+Event"

    st.markdown(f"""
        <div class="card" style="max-width: 600px; margin: auto;">
            <img src="{upcoming_image}" />
            <div class="card-title" style="font-size: 1.5rem;">{upcoming_event_title}</div>
            <div class="card-text">{upcoming_event_desc}</div>
        </div>
    """, unsafe_allow_html=True)

    st.write("---")

    # --- Past Events Section ---
    st.subheader("Past Events")

    event_display_data = {
        "Bangkok Event": {
            "desc": "Explore Thai culture and urban life in Bangkok.",
            "folder": "bangkok_event"
        },
        "Singapore Event": {
            "desc": "A vibrant showcase of multicultural learning in Singapore.",
            "folder": "singapore_event"
        }
    }

    card_data = []
    for title, data in event_display_data.items():
        img_dir = Path(f"events/{data['folder']}/images")
        image_files = list(img_dir.glob("*.[jp][pn]g"))
        image_path = str(image_files[0]) if image_files else "https://via.placeholder.com/300x180.png?text=No+Image"

        card_data.append({
            "title": title,
            "desc": data["desc"],
            "img": image_path
        })

    cols = st.columns(len(card_data))
    for i, (col, card) in enumerate(zip(cols, card_data)):
        with col:
            if st.button(card["title"]):
                st.session_state["selected_event"] = card["title"]
                st.session_state["jump_to"] = "Photo Gallery"
                st.experimental_rerun()

            st.markdown(f"""
            <div class="card">
                <img src="{card['img']}" />
                <div class="card-title">{card['title']}</div>
                <div class="card-text">{card['desc']}</div>
            </div>
            """, unsafe_allow_html=True)

# --- Event Media Gallery ---
elif view in ["Photo Gallery", "Video Gallery"]:
    selected_event = st.session_state.get("selected_event", None)
    if not selected_event:
        selected_event = st.selectbox("Select an event:", list(events.keys()))
    else:
        st.markdown(f"**Selected event:** {selected_event}")

    event_key = events[selected_event]
    image_dir = Path(f"events/{event_key}/images")
    video_dir = Path(f"events/{event_key}/videos")

    if view == "Photo Gallery":
        st.subheader(f"Photos from: {selected_event}")
        image_files = list(image_dir.glob("*.[jp][pn]g"))
        if image_files:
            cols = st.columns(3)
            for i, image_file in enumerate(image_files):
                with cols[i % 3]:
                    st.image(str(image_file), caption=image_file.stem, use_column_width=True)
        else:
            st.info("No images found for this event.")

    elif view == "Video Gallery":
        st.subheader(f"Videos from: {selected_event}")
        video_files = list(video_dir.glob("*.mp4"))
        if video_files:
            for video_file in video_files:
                st.video(str(video_file))
                st.caption(video_file.stem)
        else:
            st.info("No videos found for this event.")

# --- Registration Form ---
elif view == "Register":
    st.header("Register Your Interest")
    st.markdown("Please fill in the form below to sign up for our future events:")

    st.markdown(
        f"""
        <iframe src="{GOOGLE_FORM_EMBED_URL}"
        width="100%" height="800" frameborder="0" marginheight="0" marginwidth="0">Loading…</iframe>
        """,
        unsafe_allow_html=True,
    )