import re
from pathlib import Path

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def clean_text(text):
    """Clean text for NLP processing."""
    text = text.lower()
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def calculate_similarity(job_description, resume_text):
    """Calculate TF-IDF cosine similarity between JD and resume."""

    documents = [
        clean_text(job_description),
        clean_text(resume_text)
    ]

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

    return similarity * 100


def extract_skills(text):
    """Find important skills mentioned in the text."""

    skill_list = [
        "python",
        "machine learning",
        "nlp",
        "natural language processing",
        "llm",
        "llms",
        "large language models",
        "generative ai",
        "data analysis",
        "sql",
        "git",
        "github",
        "apis",
        "tensorflow",
        "pandas",
        "scikit-learn",
        "deep learning",
        "transformers",
        "rag",
        "prompt engineering"
    ]

    text_lower = text.lower()

    found_skills = []

    for skill in skill_list:
        if skill in text_lower:
            found_skills.append(skill)

    return found_skills


def calculate_skill_match(job_description, resume_text):
    """Calculate percentage of required skills found in resume."""

    job_skills = extract_skills(job_description)
    resume_skills = extract_skills(resume_text)

    if not job_skills:
        return 0, [], []

    matched_skills = [
        skill for skill in job_skills
        if skill in resume_skills
    ]

    missing_skills = [
        skill for skill in job_skills
        if skill not in resume_skills
    ]

    score = (len(matched_skills) / len(job_skills)) * 100

    return score, matched_skills, missing_skills


def calculate_final_score(job_description, resume_text):
    """
    Calculate final candidate score.

    70% = required skill match
    30% = NLP similarity
    """

    skill_score, matched_skills, missing_skills = calculate_skill_match(
        job_description,
        resume_text
    )

    similarity_score = calculate_similarity(
        job_description,
        resume_text
    )

    final_score = (
        0.70 * skill_score
        + 0.30 * similarity_score
    )

    return {
        "skill_score": round(skill_score, 2),
        "similarity_score": round(similarity_score, 2),
        "final_score": round(final_score, 2),
        "matched_skills": ", ".join(matched_skills),
        "missing_skills": ", ".join(missing_skills)
    }


def rank_resumes(job_description, resumes):
    """Score and rank all resumes."""

    results = []

    for resume in resumes:

        scores = calculate_final_score(
            job_description,
            resume["text"]
        )

        result = {
            "filename": resume["filename"],
            **scores
        }

        results.append(result)

    results.sort(
        key=lambda item: item["final_score"],
        reverse=True
    )

    for rank, result in enumerate(results, start=1):
        result["rank"] = rank

    return results


def save_results(results, output_folder="output"):
    """Save ranking results to CSV and JSON."""

    output_folder = Path(output_folder)
    output_folder.mkdir(parents=True, exist_ok=True)

    dataframe = pd.DataFrame(results)

    columns = [
        "rank",
        "filename",
        "final_score",
        "skill_score",
        "similarity_score",
        "matched_skills",
        "missing_skills"
    ]

    dataframe = dataframe[columns]

    dataframe.to_csv(
        output_folder / "ranked_candidates.csv",
        index=False
    )

    dataframe.to_json(
        output_folder / "ranked_candidates.json",
        orient="records",
        indent=4
    )

    return dataframe