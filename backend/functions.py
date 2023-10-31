def role_skill_match(staff_skills, role_skills):
    skill_match_list = []
    overall_match = 0
    all_skills = []
    count = 0

    for role_skill in role_skills:
        r_skill = role_skill["skill"].upper()

        for staff_skill in staff_skills:
            s_skill = staff_skill["skill"].upper()

            if r_skill == s_skill and r_skill not in all_skills:
                all_skills.append(r_skill)
                match = 100

                if role_skill["proficiency"] > 0:
                    match = min(staff_skill["proficiency"] / role_skill["proficiency"], 1) * 100

                out = {
                    "skill": role_skill["skill"],
                    "proficiency": role_skill["proficiency"],
                    "match": round(match)
                }
                skill_match_list.append(out)
                overall_match += match
                count += 1

        if r_skill not in all_skills:
            all_skills.append(r_skill)
            out = {
                "skill": role_skill["skill"],
                "proficiency": role_skill["proficiency"],
                "match": 0
            }
            skill_match_list.append(out)
            count += 1

    if count > 0:
        overall_match = overall_match / count
    elif len(role_skills) == 0:
        overall_match = 100

    overall_match = round(overall_match)

    return skill_match_list, overall_match
