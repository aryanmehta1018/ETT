from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

SYNONYMS = {
    "dsa": ["data structures", "data structures and algorithms"],
    "ml": ["machine learning"],
    "ai": ["artificial intelligence"],
    "nlp": ["natural language processing"],
    "js": ["javascript"],
    "dbms": ["database management system"],
    "oop": ["object oriented programming"],
    "os": ["operating system"],
    "sql": ["structured query language"]
}

def normalize(skill):
    return skill.lower().strip()


def expand_skill(skill):
    skill = normalize(skill)

    expanded = set([skill])

    for key, values in SYNONYMS.items():
        if skill == key or skill in values:
            expanded.add(key)
            expanded.update(values)

    return list(expanded)


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

    matched = []
    missing = []

    for req in required:

        req_variants = expand_skill(req)
        found = False

        for variant in req_variants:

            variant_embedding = model.encode([variant], convert_to_tensor=True)

            similarities = util.cos_sim(variant_embedding, extracted_embeddings)
            max_score = similarities.max().item()

            if max_score > 0.6:
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