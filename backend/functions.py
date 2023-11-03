def role_skill_match(staff_skills, role_skills):
    if staff_skills == None or role_skills == None:
        return None, None
    
    roleSkillName = ""
    staffSkillName =""
    roleProfLevel = ""
    staffProfLevel =""

   
    if len(role_skills) > 0 and len(staff_skills) > 0:
        if "Skill_Name" in role_skills[0]:
            roleSkillName = "Skill_Name"
        else:
            roleSkillName = "skill"

        if "Skill_Name" in staff_skills[0]:
            staffSkillName = "Skill_Name"
        else:
            staffSkillName = "skill"

        if "Proficiency_Level" in role_skills[0]:
            roleProfLevel = "Proficiency_Level"
        else:
            roleProfLevel = "proficiency"

        if "Proficiency_Level" in staff_skills[0]:
            staffProfLevel = "Proficiency_Level"
        else:
            staffProfLevel = "proficiency"

    elif len(role_skills) == 0:
        staffSkillName = "skill"
        staffProfLevel = "proficiency"
        roleSkillName = "Skill_Name"
        roleProfLevel = "Proficiency_Level"  

    elif len(staff_skills) == 0:
        staffSkillName = "skill"
        staffProfLevel = "proficiency"
        roleSkillName = "Skill_Name"
        roleProfLevel = "Proficiency_Level"  
    
    skill_match_list = []
    overall_match = 0
    all_skills = []
    count = 0

    for role_skill in role_skills:
        r_skill = role_skill[roleSkillName].upper()

        for staff_skill in staff_skills:
            s_skill = staff_skill[staffSkillName].upper()

            if r_skill == s_skill and r_skill not in all_skills:
                all_skills.append(r_skill)
                match = 100

                if role_skill[roleProfLevel] > 0:
                    match = min(staff_skill[staffProfLevel] / role_skill[roleProfLevel], 1) * 100

                out = {
                    "skill": role_skill[roleSkillName],
                    "proficiency": role_skill[roleProfLevel],
                    "match": round(match)
                }
                skill_match_list.append(out)
                overall_match += match
                count += 1

        if r_skill not in all_skills:
            all_skills.append(r_skill)
            out = {
                "skill": role_skill[roleSkillName],
                "proficiency": role_skill[roleProfLevel],
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
