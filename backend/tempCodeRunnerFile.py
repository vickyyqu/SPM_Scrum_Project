@app.route('/getskillsforrole/<string:role_name>', methods=['GET'])
def get_skills_for_role(role_name):
    try:
        skills_for_role = (
            db.session.query(SkillTable.Skill_Name, SkillTable.Skill_Desc)
            .join(RoleSkillTable, RoleSkillTable.Skill_Name == SkillTable.Skill_Name)
            .filter(RoleSkillTable.Role_Name == role_name)
            .all()
        )

        result = []
        for skill_name, skill_desc in skills_for_role:
            result.append({
                'skill_name': skill_name,
                'skill_desc': skill_desc
            })

        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': 'Failed to retrieve skills for role.', 'details': str(e)}), 500