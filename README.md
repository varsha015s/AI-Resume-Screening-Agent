AI Resume Screening Agent

An AI-powered resume screening system that automatically evaluates candidates against a job description, calculates a match score, ranks candidates, and generates detailed AI-based reasoning using Groq LLM.

 Features

-  Resume parsing from text files
-  Job description-based candidate screening
-  Deterministic skill matching and scoring
-  Groq LLM-powered candidate reasoning
-  Automatic candidate ranking
-  Matched and missing skill identification
-  Streamlit web interface
-  CSV and JSON result generation

Technologies Used

- Python
- Streamlit
- Groq API
- Large Language Models (LLMs)
- Pandas
- Python pathlib
- Git & GitHub

Project Structure


AI-Resume-Screening-Agent/
│
├── app.py
├── streamlit_app.py
├── llm_reasoning.py
├── resume_parser.py
├── scorer.py
├── sample_resumes.py
├── requirements.txt
├── .gitignore
│
└── data/
    ├── job_description.txt
    └── resumes/
        ├── resume_01.txt
        ├── resume_02.txt
        ├── ...
        └── resume_10.txt
