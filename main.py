
# AI Job Matcher - Version 1.0
# A simple Python-based job skill analyzer

job_description = """
We are looking for a working student.
Python programming skills are required.
LLM experience is preferred.
Experience with SQL is a plus.
"""

skills = ["Python", "LLM", "SQL", "Java"]

print("=== AI Job Matcher ===")

for skill in skills:
    if skill.lower() in job_description.lower():
        print(f"Found: {skill}")
    else:
        print(f"Not found: {skill}")
