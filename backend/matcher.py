from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')


def normalize(skill):
    return skill.lower().strip()


def match_skills(extracted_skills, required_skills):
    extracted = list(set([normalize(skill) for skill in extracted_skills]))
    required = list(set([normalize(skill) for skill in required_skills]))

    if not extracted or not required:
        return {
            "matched_skills": [],
            "missing_skills": required,
            "match_percentage": 0
        }

    extracted_embeddings = model.encode(extracted, convert_to_tensor=True)
    required_embeddings = model.encode(required, convert_to_tensor=True)

    matched = []
    missing = []

    for i, req_skill in enumerate(required):
       
        similarities = util.cos_sim(required_embeddings[i], extracted_embeddings)

        max_score = similarities.max().item()

        if max_score > 0.6:  
            matched.append(req_skill)
        else:
            missing.append(req_skill)

    match_percentage = (len(matched) / len(required)) * 100

    return {
        "matched_skills": matched,
        "missing_skills": missing,
        "match_percentage": round(match_percentage, 2)
    }