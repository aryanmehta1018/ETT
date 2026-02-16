def match_skills(resume_skills, job_skills):
    resume_set = set(skill.lower() for skill in resume_skills)
    job_set = set(skill.lower() for skill in job_skills)

    matched = resume_set & job_set
    missing = job_set - resume_set

    coverage = (len(matched) / len(job_set)) * 100 if job_set else 0

    return matched, missing, round(coverage, 2)
