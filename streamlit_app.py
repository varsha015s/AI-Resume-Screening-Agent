import streamlit as st
from pathlib import Path

from resume_parser import load_all_resumes
from scorer import rank_resumes
from llm_reasoning import generate_candidate_reasoning


st.set_page_config(
    page_title="AI Resume Screening Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Screening Agent")

st.write(
    "Automatically screen all resumes from the "
    "data/resumes folder using AI."
)

st.divider()

# File locations
job_description_path = Path("data/job_description.txt")
resume_folder = Path("data/resumes")

# Check job description
if not job_description_path.exists():

    st.error(
        "Job description not found at "
        "data/job_description.txt"
    )

    st.stop()

# Check resume folder
if not resume_folder.exists():

    st.error(
        "Resume folder not found at "
        "data/resumes"
    )

    st.stop()

# Load job description
job_description = job_description_path.read_text(
    encoding="utf-8"
)

# Find resumes
resume_files = list(resume_folder.glob("*.txt"))

st.subheader("📂 Available Resumes")

st.write(
    f"Found **{len(resume_files)} resumes**."
)

for file in resume_files:
    st.write(f"• {file.name}")

st.divider()

if st.button(
    "🔍 Screen All Candidates",
    type="primary"
):

    with st.spinner("Loading resumes..."):

        resumes = load_all_resumes(
            str(resume_folder)
        )

    if not resumes:

        st.error("No resumes found.")

        st.stop()

    st.success(
        f"Loaded {len(resumes)} resumes successfully."
    )

    # Calculate candidate scores
    with st.spinner(
        "Calculating candidate scores..."
    ):

        results = rank_resumes(
            job_description,
            resumes
        )

    st.success(
        "Candidate scoring completed."
    )

    # Create resume lookup
    resume_lookup = {
        resume["filename"]: resume["text"]
        for resume in resumes
    }

    # Generate AI reasoning
    with st.spinner(
        "Generating AI explanations..."
    ):

        for result in results:

            resume_text = resume_lookup[
                result["filename"]
            ]

            try:

                explanation = (
                    generate_candidate_reasoning(
                        job_description=job_description,
                        resume_text=resume_text,
                        score=result["final_score"],
                        matched_skills=result[
                            "matched_skills"
                        ],
                        missing_skills=result[
                            "missing_skills"
                        ]
                    )
                )

                result[
                    "ai_reasoning"
                ] = explanation

            except Exception as error:

                result[
                    "ai_reasoning"
                ] = (
                    f"AI reasoning unavailable: "
                    f"{error}"
                )

    st.success(
        "AI reasoning completed."
    )

    st.divider()

    st.header("🏆 Final Candidate Ranking")

    # Display all candidates
    for result in results:

        with st.expander(
            f"#{result['rank']} — "
            f"{result['filename']} — "
            f"{result['final_score']}%"
        ):

            st.write(
                "**Matched Skills:**"
            )

            if result["matched_skills"]:

                st.write(
                    ", ".join(
                        result["matched_skills"]
                    )
                )

            else:

                st.write("None")

            st.write(
                "**Missing Skills:**"
            )

            if result["missing_skills"]:

                st.write(
                    ", ".join(
                        result["missing_skills"]
                    )
                )

            else:

                st.write("None")

            st.write(
                "**🤖 AI Reasoning:**"
            )

            st.markdown(
                result["ai_reasoning"]
            )