import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


def create_client():
    """Create the Groq client using the API key from .env."""

    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError(
            "GROQ_API_KEY was not found. "
            "Please check your .env file."
        )

    return Groq(api_key=api_key)


def generate_candidate_reasoning(
    job_description,
    resume_text,
    score,
    matched_skills,
    missing_skills
):
    """
    Generate an explanation for a candidate's screening result.
    The LLM explains the calculated score; it does not calculate the score.
    """

    client = create_client()

    prompt = f"""
You are an AI recruitment screening assistant.

Analyze the candidate against the job description.

IMPORTANT:
The candidate score has already been calculated by a deterministic
NLP scoring system. Do NOT change or invent the score.

Provide a concise explanation containing:
1. Overall assessment
2. Why the candidate matches
3. Important strengths
4. Missing or weaker requirements
5. Recommendation: Strong Match, Moderate Match, or Weak Match

JOB DESCRIPTION:
{job_description}

CANDIDATE RESUME:
{resume_text}

CALCULATED SCORE:
{score}%

MATCHED SKILLS:
{matched_skills}

MISSING SKILLS:
{missing_skills}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a careful recruitment assistant. "
                    "Only use information provided in the job description "
                    "and candidate resume. Never invent qualifications "
                    "or experience."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.2,
        max_tokens=500
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    test_result = generate_candidate_reasoning(
        job_description="We need a Python and Machine Learning fresher with NLP knowledge.",
        resume_text="Candidate has Python, Machine Learning, NLP and SQL skills.",
        score=85,
        matched_skills="python, machine learning, nlp",
        missing_skills="generative ai"
    )

    print("\nAI REASONING:\n")
    print(test_result)