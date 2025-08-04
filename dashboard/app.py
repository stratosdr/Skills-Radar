import streamlit as st
import requests

st.set_page_config(page_title="Skills Radar", layout="centered")

st.title("Skills Radar")
st.write("Analyze a job description to extract the predicted job category and top technical skills.")

# Input field
job_text = st.text_area("Enter job description", height=200)

# Number of top skills to extract
top_n = st.slider("Number of top skills to extract", min_value=3, max_value=15, value=5)

if st.button("Analyze"):
    if not job_text.strip():
        st.warning("Please enter a job description.")
    else:
        with st.spinner("Calling API..."):
            try:
                # Send request to /predict endpoint
                pred_res = requests.post(
                    "http://127.0.0.1:8000/predict",
                    json={"text": job_text}
                )
                pred_res.raise_for_status()
                category = pred_res.json().get("category", "N/A")

                # Send request to /skills endpoint
                skill_res = requests.post(
                    f"http://127.0.0.1:8000/skills?top_n={top_n}",
                    json={"text": job_text}
                )
                skill_res.raise_for_status()
                skills = skill_res.json().get("skills", [])

                st.success("Analysis complete!")
                st.markdown(f"**Predicted Category:** {category}")
                st.markdown("**Top Skills:**")
                for i, skill in enumerate(skills, 1):
                    st.markdown(f"- {i}. `{skill}`")

            except requests.exceptions.RequestException as e:
                st.error(f"API request failed: {e}")
