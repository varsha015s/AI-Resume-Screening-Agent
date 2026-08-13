from pathlib import Path
import pymupdf
from docx import Document


def extract_text_from_pdf(file_path):
    """Extract text from a PDF resume."""
    text = ""

    with pymupdf.open(file_path) as pdf:
        for page in pdf:
            text += page.get_text()

    return text


def extract_text_from_docx(file_path):
    """Extract text from a DOCX resume."""
    document = Document(file_path)

    text = []

    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            text.append(paragraph.text)

    return "\n".join(text)


def extract_text_from_txt(file_path):
    """Extract text from a TXT resume."""
    return Path(file_path).read_text(encoding="utf-8")


def extract_resume_text(file_path):
    """
    Detect the resume file type and extract its text.
    Supports TXT, PDF and DOCX.
    """

    file_path = Path(file_path)

    extension = file_path.suffix.lower()

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    elif extension == ".docx":
        return extract_text_from_docx(file_path)

    elif extension == ".txt":
        return extract_text_from_txt(file_path)

    else:
        raise ValueError(
            f"Unsupported file type: {extension}. "
            "Use PDF, DOCX or TXT."
        )


def load_all_resumes(folder="data/resumes"):
    """
    Read all supported resume files from a folder.
    Returns a list of dictionaries containing filename and text.
    """

    folder = Path(folder)

    supported_extensions = {".pdf", ".docx", ".txt"}

    resumes = []

    for file_path in sorted(folder.iterdir()):

        if file_path.is_file() and file_path.suffix.lower() in supported_extensions:

            try:
                text = extract_resume_text(file_path)

                resumes.append({
                    "filename": file_path.name,
                    "text": text
                })

            except Exception as error:
                print(f"Could not read {file_path.name}: {error}")

    return resumes


if __name__ == "__main__":

    resumes = load_all_resumes()

    print(f"Found {len(resumes)} resumes.")

    for resume in resumes:
        print("\n" + "=" * 60)
        print(resume["filename"])
        print("=" * 60)
        print(resume["text"][:500])