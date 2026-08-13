AI Resume Screening Agent

An AI-powered resume screening system that automatically evaluates candidates against a job description, calculates a match score, ranks candidates, and generates detailed AI-based reasoning using Groq LLM.

 Features

- Resume parsing from text files
-  Job description-based candidate screening
-  Deterministic skill matching and scoring
-  Groq LLM-powered candidate reasoning
- Automatic candidate ranking
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
 Architecture

The system follows a two-layer screening approach:

Layer 1 — Deterministic Screening

The resume text is parsed and compared with the job description. Required skills are identified and matched against each candidate's resume.

The scoring component calculates a weighted candidate-match score and identifies:

- Matched skills
- Missing skills
- Final candidate score

Layer 2 — LLM Reasoning

After deterministic scoring, the candidate information is sent to a Groq-powered LLM.

The LLM generates an explanation covering:

- Overall candidate assessment
- Why the candidate matches
- Important strengths
- Missing or weaker requirements
- Final recommendation

This separation makes the system more explainable because the numerical score is calculated independently before the LLM provides the reasoning.

 Workflow


Job Description
       │
       ▼
Resume Parser
       │
       ▼
Skill Extraction & Matching
       │
       ▼
Deterministic Scoring
       │
       ▼
Candidate Ranking
       │
       ▼
Groq LLM Reasoning
       │
       ▼
Final Candidate Assessment
       │
       ├── CSV Results
       └── JSON Results
Scoring Methodology

The candidate score is calculated deterministically before the LLM reasoning stage.

The system compares the skills identified in the job description with the skills found in each resume.

The scoring process considers:

- Required technical skills
- Matched skills
- Missing skills
- Relative importance of the matched requirements

The resulting score is used to rank candidates from highest to lowest match.

For example, during testing, the system produced results such as:

| Rank | Resume | Score |
|---|---|---:|
| 1 | resume_01.txt | 71.46% |
| 2 | resume_09.txt | 59.42% |
| 3 | resume_03.txt | 57.85% |
| 4 | resume_07.txt | 53.34% |

The LLM does not determine the numerical score. It receives the calculated score, matched skills, and missing skills and generates an explanation based on those results.
 Technologies Used

- Python — application logic and processing
- Pandas — data handling and result generation
- Scikit-learn — TF-IDF-based text processing and scoring
- PyMuPDF — PDF resume parsing
- python-docx — DOCX resume parsing
- Groq API — LLM-powered candidate reasoning
- python-dotenv — secure environment variable loading
- Streamlit — web-based user interface
- Git & GitHub — version control and project hosting
 Project Structure


AI-Resume-Screening-Agent/
│
├── app.py                   Main command-line screening application
├── streamlit_app.py         Streamlit web interface
├── resume_parser.py         Resume file parsing
├── scorer.py                Candidate scoring and ranking
├── llm_reasoning.py         Groq LLM reasoning
├── sample_resumes.py        Sample resume generation/data
├── requirements.txt         Python dependencies
├── .gitignore               Files excluded from Git
├── README.md                Project documentation
│
└── data/
    ├── job_description.txt
    └── resumes/
        ├── resume_01.txt
        ├── resume_02.txt
        ├── ...
        └── resume_10.txt
Installation and Setup
1. Clone the repository
git clone git@github.com:varsha015s/AI-Resume-Screening-Agent.git
cd AI-Resume-Screening-Agent
2. Create a virtual environment
python -m venv .venv
3. Activate the virtual environment on Windows
.venv\Scripts\activate
4. Install dependencies
pip install -r requirements.txt
5. Configure the Groq API key

Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key_here

The .env file is intentionally excluded from GitHub through .gitignore.
Running the Application
Command-Line Version

Run:

python app.py

The application will:

Load the job description.
Load the resumes.
Calculate deterministic candidate scores.
Rank the candidates.
Generate LLM-based explanations.
Display the final ranking.
Streamlit Web Interface

Run:

streamlit run streamlit_app.py

Then open:

http://localhost:8501

The Streamlit interface provides a browser-based way to screen candidates.

 Input

The system uses:

A job description containing the requirements for the role
Candidate resumes containing education, skills, and experience

The current sample project includes a job description and 10 sample resumes under the data/ directory.

 Output

The screening system produces:

Candidate ranking
Match percentage
Matched skills
Missing skills
AI-generated candidate reasoning

The command-line application saves results as:

output/ranked_candidates.csv
output/ranked_candidates.json

Generated output files are excluded from GitHub through .gitignore.

 Design Decisions
Deterministic scoring before LLM reasoning

The numerical candidate score is calculated before calling the LLM. This separates measurable screening logic from natural-language explanation.

LLM used for explanation

The LLM is not responsible for inventing the score. It explains the structured screening result and provides a human-readable recommendation.

Environment variable for API security

The Groq API key is stored in .env rather than source code and is excluded from version control.

Trade-offs
Rule-based scoring

Advantages

Easy to understand
Deterministic
Fast
Reproducible

Limitations

Keyword-based matching can miss semantic similarities
Related terms may sometimes be treated as different skills
LLM reasoning

Advantages

Provides natural-language explanations
Helps summarize candidate strengths and weaknesses
Makes results easier for humans to interpret

Limitations

Requires an API connection
Adds API cost and latency
Generated explanations should be treated as decision support rather than the sole hiring decision

 Limitations
Skill matching is primarily based on textual matching.
Similar terms such as abbreviations and expanded forms may require normalization.
The current sample application uses text-based sample resumes for demonstration.
LLM output depends on the quality of the supplied resume and job description.
Automated screening should support, not replace, human recruitment decisions.

 Future Improvements

Semantic skill matching using embeddings
Skill normalization such as NLP → Natural Language Processing
Improved weighting of required versus optional skills
Candidate comparison dashboard
PDF and DOCX upload through the Streamlit interface
Database integration
Authentication and role-based access
Automated report generation
More advanced explainability and evaluation metrics

 Sample Result

During testing, the system successfully processed 10 resumes and generated a ranked candidate list.

Example:

1. resume_01.txt - 71.46%
2. resume_09.txt - 59.42%
3. resume_03.txt - 57.85%
4. resume_07.txt - 53.34%
5. resume_10.txt - 33.96%

Each candidate was also evaluated for matched skills, missing skills, and AI-generated reasoning.

 Use Cases

This project can be used as a foundation for:

Automated recruitment screening
Candidate ranking
Skill-gap analysis
HR screening assistance
Explainable AI recruitment workflows
 Author

Varsha S

GitHub: https://github.com/varsha015s

