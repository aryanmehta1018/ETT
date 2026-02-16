import re

def normalize(skill):
    return skill.lower().strip()

def skill_in_text(skill, text):
    # Match full word only
    pattern = r'\b' + re.escape(skill) + r'\b'
    return re.search(pattern, text) is not None

def match_skills(extracted_skills, required_skills):

    extracted = [normalize(skill) for skill in extracted_skills]
    required = [normalize(skill) for skill in required_skills]

    matched = []
    missing = []

    for req in required:
        found = False

        for ext in extracted:

            # Exact match
            if req == ext:
                matched.append(req)
                found = True
                break

            # Word boundary match (safe)
            if skill_in_text(req, ext):
                matched.append(req)
                found = True
                break

        if not found:
            missing.append(req)

    match_percentage = (len(matched) / len(required)) * 100

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "match_percentage": round(match_percentage, 2)
    }
