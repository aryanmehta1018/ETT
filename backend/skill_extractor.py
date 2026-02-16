from google import genai

def extract_skills_with_llm(resume_text):

    client = genai.Client()

    prompt = f"""
    Extract all technical skills from the following resume text.
    Return them as a comma-separated list only.

    Resume:
    {resume_text}
    """

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )

    skills_text = response.text


    skills = [s.strip() for s in skills_text.split(",") if s.strip()]

    return skills


