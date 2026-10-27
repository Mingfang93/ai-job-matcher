
# AI Job Matcher - Version 1.1

requirements = [
    "Python programming skills are required",
    "LLM experience is preferred",
    "SQL knowledge is required"
]

skills = ["Python", "LLM", "SQL", "Java"]

print("=== AI Job Matcher ===")

for skill in skills:
    found = False

    for requirement in requirements:
        if skill.lower() in requirement.lower():
            found = True

            if "required" in requirement.lower():
                print(f"{skill}: Mandatory")
            elif "preferred" in requirement.lower():
                print(f"{skill}: Preferred")
            else:
                print(f"{skill}: Mentioned")

    if not found:
        print(f"{skill}: Not found")
