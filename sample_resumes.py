from pathlib import Path

output_folder = Path("data/resumes")
output_folder.mkdir(parents=True, exist_ok=True)

resumes = {
    "resume_01.txt": """
Alex Kumar
B.Tech Computer Science

Skills:
Python, Machine Learning, NLP, Natural Language Processing,
Large Language Models, Generative AI, SQL, Git, GitHub,
Pandas, NumPy, Scikit-learn, APIs

Experience:
Fresher with academic experience in Artificial Intelligence
and Machine Learning.

Projects:
- Built an NLP text classification system using Python and Scikit-learn.
- Developed a Generative AI question-answering application using an LLM API.
- Performed data preprocessing and model evaluation on machine learning datasets.

Education:
B.Tech in Computer Science Engineering
""",

    "resume_02.txt": """
Priya Sharma
B.Tech Information Technology

Skills:
Python, Pandas, NumPy, Data Analysis, SQL, Machine Learning,
Excel, Scikit-learn, Git

Experience:
1 year internship experience in data analysis.

Projects:
- Analysed customer datasets using Python and Pandas.
- Built a machine learning model for customer churn prediction.
- Created SQL queries for data reporting.

Education:
B.Tech in Information Technology
""",

    "resume_03.txt": """
Rohan Mehta
B.Tech Artificial Intelligence

Skills:
Python, LLMs, Generative AI, NLP, Machine Learning,
RAG, Prompt Engineering, APIs, Git, SQL

Experience:
Fresher with strong academic experience in Generative AI.

Projects:
- Built a Retrieval Augmented Generation application.
- Developed an LLM-based document question answering system.
- Created NLP applications using Python.
- Integrated AI APIs into applications.

Education:
B.Tech in Artificial Intelligence
""",

    "resume_04.txt": """
Rahul Sharma
B.Tech Computer Science

Skills:
HTML, CSS, JavaScript, React, Node.js, Express,
MongoDB, REST APIs

Experience:
1 year internship as a Web Developer.

Projects:
- Developed responsive e-commerce websites.
- Built React web applications.
- Created REST APIs using Node.js.

Education:
B.Tech in Computer Science Engineering
""",

    "resume_05.txt": """
Sneha Patil
B.Tech Computer Science

Skills:
Python, Machine Learning, Pandas, NumPy,
Scikit-learn, SQL, Git, Data Preprocessing

Experience:
Fresher.

Projects:
- Developed a machine learning model for house price prediction.
- Performed data cleaning and preprocessing using Pandas.
- Compared classification algorithms using Scikit-learn.

Education:
B.Tech in Computer Science Engineering
""",

    "resume_06.txt": """
Ananya Rao
B.Tech Information Science

Skills:
SQL, Python, Data Analysis, Excel, Power BI,
Pandas, Statistics

Experience:
1 year experience as a Data Analyst intern.

Projects:
- Created sales dashboards using Power BI.
- Analysed business data using SQL and Python.
- Generated reports from large datasets.

Education:
B.Tech in Information Science
""",

    "resume_07.txt": """
Vikram Singh
B.Tech Computer Science

Skills:
Python, Machine Learning, NLP, SQL, Git, GitHub,
Scikit-learn, TensorFlow, APIs, Data Analysis

Experience:
2 years experience through internships and academic projects
in Artificial Intelligence and Machine Learning.

Projects:
- Developed an NLP sentiment analysis model.
- Built machine learning classification models.
- Created data preprocessing pipelines in Python.
- Used GitHub for version control.
- Integrated machine learning APIs into applications.

Education:
B.Tech in Computer Science Engineering
""",

    "resume_08.txt": """
Karan Joshi
B.Tech Computer Science

Skills:
Java, C++, JavaScript, React, Spring Boot,
MySQL, REST APIs

Experience:
1 year software development internship.

Projects:
- Developed backend services using Java and Spring Boot.
- Built web applications using React.
- Designed REST APIs and MySQL databases.

Education:
B.Tech in Computer Science Engineering
""",

    "resume_09.txt": """
Meera Nair
M.Tech Artificial Intelligence

Skills:
Python, NLP, Natural Language Processing, Machine Learning,
Deep Learning, LLMs, Transformers, SQL, Git, Data Analysis

Experience:
2 years research experience in Natural Language Processing.

Projects:
- Developed NLP text classification models.
- Experimented with transformer-based language models.
- Built a question answering system using NLP.
- Evaluated machine learning models on text datasets.

Education:
M.Tech in Artificial Intelligence
""",

    "resume_10.txt": """
Arjun Kumar
B.E. Computer Science

Skills:
Python, C, Java, SQL, Git, HTML, CSS,
Basic Machine Learning

Experience:
Fresher.

Projects:
- Developed a student management system.
- Created a basic Python data analysis project.
- Built a simple machine learning classification project.

Education:
B.E. in Computer Science Engineering
"""
}

for filename, content in resumes.items():
    file_path = output_folder / filename
    file_path.write_text(content.strip(), encoding="utf-8")

print("Successfully created 10 sample resumes!")