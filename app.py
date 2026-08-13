from pathlib import Path

from resume_parser import load_all_resumes
from scorer import rank_resumes, save_results
from llm_reasoning import generate_candidate_reasoning


def main():

    print("=" * 70)
    print("       AI RESUME SCREENING AGENT")
    print("=" * 70)

    # Load job description
    job_description_path = Path("data/job_description.txt")

    if not job_description_path.exists():
        print("ERROR: Job description not found.")
        return

    job_description = job_description_path.read_text(
        encoding="utf-8"
    )

    print("\n✓ Job description loaded.")

    # Load resumes
    resumes = load_all_resumes("data/resumes")

    print(f"✓ Found {len(resumes)} resumes.")

    if not resumes:
        print("ERROR: No resumes found.")
        return

    # Calculate rankings
    print("\nProcessing candidates...")

    results = rank_resumes(
        job_description,
        resumes
    )

    print("\n✓ Candidate scoring completed.")

    # Generate AI reasoning
    print("\nGenerating AI explanations...")

    resume_lookup = {
        resume["filename"]: resume["text"]
        for resume in resumes
    }

    for result in results:

        resume_text = resume_lookup[result["filename"]]

        try:
            explanation = generate_candidate_reasoning(
                job_description=job_description,
                resume_text=resume_text,
                score=result["final_score"],
                matched_skills=result["matched_skills"],
                missing_skills=result["missing_skills"]
            )

            result["ai_reasoning"] = explanation

            print(
                f"✓ AI explanation generated for "
                f"{result['filename']}"
            )

        except Exception as error:

            result["ai_reasoning"] = (
                f"AI reasoning unavailable: {error}"
            )

            print(
                f"⚠ Could not generate explanation for "
                f"{result['filename']}"
            )

    # Save ranking results
    save_results(results)

    print("\n" + "=" * 70)
    print("              FINAL CANDIDATE RANKING")
    print("=" * 70)

    for result in results:

        print(
            f"\n{result['rank']}. "
            f"{result['filename']} "
            f"- {result['final_score']}%"
        )

        print(
            f"Matched skills: "
            f"{result['matched_skills']}"
        )

        print("\nAI Reasoning:")
        print(result["ai_reasoning"])

    print("\n" + "=" * 70)
    print("Results saved to:")
    print("output/ranked_candidates.csv")
    print("output/ranked_candidates.json")
    print("=" * 70)


if __name__ == "__main__":
    main()