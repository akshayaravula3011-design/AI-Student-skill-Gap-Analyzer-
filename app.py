import streamlit as st

st.set_page_config(
    page_title="AI Student Skill Gap Analyzer",
    page_icon="🎓"
)

st.title("🎓 AI Student Skill Gap Analyzer")
st.write("Analyze your skills and identify the skills you need to improve.")

name = st.text_input("Enter your name")

skills = st.text_area(
    "Enter your current skills",
    placeholder="Example: Python, SQL, Excel, Machine Learning"
)

career = st.selectbox(
    "Select your target career",
    [
        "Data Scientist",
        "Data Analyst",
        "Machine Learning Engineer",
        "Software Developer"
    ]
)

if st.button("Analyze Skill Gap"):
    if not name or not skills:
        st.warning("Please enter your name and current skills.")
    else:
        user_skills = {
            skill.strip().lower()
            for skill in skills.split(",")
            if skill.strip()
        }

        required_skills = {
            "Data Scientist": {"python", "sql", "machine learning", "statistics"},
            "Data Analyst": {"python", "sql", "excel", "statistics"},
            "Machine Learning Engineer": {"python", "machine learning", "deep learning", "tensorflow"},
            "Software Developer": {"python", "git", "sql", "data structures"}
        }

        target_skills = required_skills[career]

        matched = user_skills.intersection(target_skills)
        missing = target_skills.difference(user_skills)

        st.success(f"Hello {name}! Here is your skill gap analysis.")

        st.subheader("✅ Skills You Have")
        for skill in matched:
            st.write(f"• {skill.title()}")

        st.subheader("📚 Skills You Need To Improve")
        for skill in missing:
            st.write(f"• {skill.title()}")

        if target_skills:
            score = len(matched) / len(target_skills) * 100
            st.subheader("📊 Skill Match Score")
            st.progress(int(score))
            st.write(f"Your current skill match is **{score:.1f}%**.")