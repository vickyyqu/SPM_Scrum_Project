from functions import role_skill_match;
import unittest;


class TestRoleSkillMatchStaff1(unittest.TestCase):
    def testMatch(self):
        staffSkill = [
            {
                "id": 140001,
                "isVisible": False,
                "Proficiency_Level": 0,
                "Skill_Name": "Account Management"
            },
            {
                "id": 140001,
                "isVisible": False,
                "Proficiency_Level": 0,
                "Skill_Name": "Business Development"
            },
            {
                "id": 140001,
                "isVisible": False,
                "Proficiency_Level": 0,
                "Skill_Name": "Customer Acquisition Management"
            },
            {
                "id": 140001,
                "isVisible": False,
                "Proficiency_Level": 0,
                "Skill_Name": "Database Administration"
            },
            {
                "id": 140001,
                "isVisible": False,
                "Proficiency_Level": 0,
                "Skill_Name": "Financial Statements Analysis"
            },
            {
                "id": 140001,
                "isVisible": False,
                "Proficiency_Level": 0,
                "Skill_Name": "Pricing Strategy"
            },
            {
                "id": 140001,
                "isVisible": False,
                "Proficiency_Level": 0,
                "Skill_Name": "Product Management"
            },
            {
                "id": 140001,
                "isVisible": False,
                "Proficiency_Level": 0,
                "Skill_Name": "Technology Integration"
            }
        ]

        roleSkill = [
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Account Management"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Budgeting"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Development"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Needs Analysis"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Negotiation"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Collaboration"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Communication"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Data Analytics"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Pricing Strategy"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Problem Solving"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Product Management"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Sales Strategy"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Stakeholder Management"
                }
            ]
        self.assertEqual(role_skill_match(staffSkill, roleSkill)[1], 31)

class TestRoleSkillMatchStaff2(unittest.TestCase):
    def testMatch(self):
        staffSkill = [
                    {
                        "id": 140002,
                        "isVisible": False,
                        "Proficiency_Level": 0,
                        "Skill_Name": "Accounting and Tax Systems"
                    },
                    {
                        "id": 140002,
                        "isVisible": False,
                        "Proficiency_Level": 0,
                        "Skill_Name": "Business Environment Analysis"
                    },
                    {
                        "id": 140002,
                        "isVisible": False,
                        "Proficiency_Level": 0,
                        "Skill_Name": "Customer Relationship Management"
                    },
                    {
                        "id": 140002,
                        "isVisible": False,
                        "Proficiency_Level": 0,
                        "Skill_Name": "Professional and Business Ethics"
                    }
                ]
        roleSkill = [
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Account Management"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Budgeting"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Development"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Needs Analysis"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Negotiation"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Collaboration"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Communication"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Data Analytics"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Pricing Strategy"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Problem Solving"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Product Management"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Sales Strategy"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Stakeholder Management"
                }
            ]
        self.assertEqual(role_skill_match(staffSkill, roleSkill)[1], 0)

class TestRoleSkillMatchStaff3(unittest.TestCase):
    def testMatch(self):
        staffSkill = [
                    {
                        "id": 140003,
                        "isVisible": False,
                        "Proficiency_Level": 0,
                        "Skill_Name": "Accounting Standards"
                    },
                    {
                        "id": 140003,
                        "isVisible": False,
                        "Proficiency_Level": 0,
                        "Skill_Name": "Data Analytics"
                    },
                    {
                        "id": 140003,
                        "isVisible": False,
                        "Proficiency_Level": 0,
                        "Skill_Name": "Digital Fluency"
                    },
                    {
                        "id": 140003,
                        "isVisible": False,
                        "Proficiency_Level": 0,
                        "Skill_Name": "Problem Solving"
                    },
                    {
                        "id": 140003,
                        "isVisible": False,
                        "Proficiency_Level": 0,
                        "Skill_Name": "Project Management"
                    }
                ]

        roleSkill = [
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Account Management"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Budgeting"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Development"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Needs Analysis"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Negotiation"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Collaboration"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Communication"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Data Analytics"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Pricing Strategy"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Problem Solving"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Product Management"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Sales Strategy"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Stakeholder Management"
                }
            ]
        self.assertEqual(role_skill_match(staffSkill, roleSkill)[1], 15)

class TestRoleSkillMatchStaff4(unittest.TestCase):
    def testMatch(self):
        staffSkill = [
                {
                    "id": 140004,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Account Management"
                },
                {
                    "id": 140004,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Applications Development"
                },
                {
                    "id": 140004,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Negotiation"
                },
                {
                    "id": 140004,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Database Administration"
                },
                {
                    "id": 140004,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Product Management"
                }
            ]

        roleSkill = [
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Account Management"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Budgeting"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Development"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Needs Analysis"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Negotiation"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Collaboration"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Communication"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Data Analytics"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Pricing Strategy"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Problem Solving"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Product Management"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Sales Strategy"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Stakeholder Management"
                }
            ]
        self.assertEqual(role_skill_match(staffSkill, roleSkill)[1], 23)

class TestRoleSkillMatchStaffEmpty(unittest.TestCase):
    def testMatch(self):
        staffSkill = []

        roleSkill = [
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Account Management"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Budgeting"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Development"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Needs Analysis"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Negotiation"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Collaboration"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Communication"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Data Analytics"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Pricing Strategy"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Problem Solving"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Product Management"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Sales Strategy"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Stakeholder Management"
                }
            ]
        self.assertEqual(role_skill_match(staffSkill, roleSkill)[1], 0)

class TestRoleSkillMatchStaff5(unittest.TestCase):
    def testMatch(self):
        staffSkill = [
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Applications Integration"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Presentation Delivery"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Developing People"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Infrastructure Support"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Professional and Business Ethics"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "SOP Development and Implementation"
                }
            ]

        roleSkill = [
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Account Management"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Budgeting"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Development"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Needs Analysis"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Negotiation"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Collaboration"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Communication"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Data Analytics"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Pricing Strategy"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Problem Solving"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Product Management"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Sales Strategy"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Stakeholder Management"
                }
            ]
        self.assertEqual(role_skill_match(staffSkill, roleSkill)[1], 0)

class TestRoleSkillMatchRole1(unittest.TestCase):
    def testMatch(self):
        staffSkill = [
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Applications Integration"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Presentation Delivery"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Developing People"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Infrastructure Support"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Professional and Business Ethics"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "SOP Development and Implementation"
                }
            ]

        roleSkill = [
                    {
                        "Proficiency_Level": 0,
                        "Skill_Name": "Call Centre Management"
                    },
                    {
                        "Proficiency_Level": 0,
                        "Skill_Name": "Collaboration"
                    },
                    {
                        "Proficiency_Level": 0,
                        "Skill_Name": "Communication"
                    },
                    {
                        "Proficiency_Level": 0,
                        "Skill_Name": "Customer Relationship Management"
                    },
                    {
                        "Proficiency_Level": 0,
                        "Skill_Name": "Digital Fluency"
                    },
                    {
                        "Proficiency_Level": 0,
                        "Skill_Name": "Problem Solving"
                    },
                    {
                        "Proficiency_Level": 0,
                        "Skill_Name": "Stakeholder Management"
                    },
                    {
                        "Proficiency_Level": 0,
                        "Skill_Name": "Technology Application"
                    }
                ]

        self.assertEqual(role_skill_match(staffSkill, roleSkill)[1], 0)

class TestRoleSkillMatchRole2(unittest.TestCase):
    def testMatch(self):
        staffSkill = [
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Applications Integration"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Presentation Delivery"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Developing People"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Infrastructure Support"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Professional and Business Ethics"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "SOP Development and Implementation"
                }
            ]

        roleSkill = [
                    {
                        "Proficiency_Level": 0,
                        "Skill_Name": "Developing People"
                    },
                    {
                        "Proficiency_Level": 0,
                        "Skill_Name": "Collaboration"
                    },
                    {
                        "Proficiency_Level": 0,
                        "Skill_Name": "Communication"
                    },
                    {
                        "Proficiency_Level": 0,
                        "Skill_Name": "Customer Relationship Management"
                    },
                    {
                        "Proficiency_Level": 0,
                        "Skill_Name": "Digital Fluency"
                    },
                    {
                        "Proficiency_Level": 0,
                        "Skill_Name": "Problem Solving"
                    },
                    {
                        "Proficiency_Level": 0,
                        "Skill_Name": "Stakeholder Management"
                    },
                    {
                        "Proficiency_Level": 0,
                        "Skill_Name": "Technology Application"
                    }
                ]
        self.assertEqual(role_skill_match(staffSkill, roleSkill)[1], 12)


class TestRoleSkillMatchRole3(unittest.TestCase):
    def testMatch(self):
        staffSkill = [
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Applications Integration"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Presentation Delivery"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Developing People"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Infrastructure Support"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Professional and Business Ethics"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "SOP Development and Implementation"
                }
            ]

        roleSkill = [
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Account Management"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Budgeting"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Development"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Needs Analysis"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Negotiation"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Collaboration"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Communication"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Data Analytics"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Pricing Strategy"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Problem Solving"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Product Management"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Sales Strategy"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Stakeholder Management"
                }
            ]
        self.assertEqual(role_skill_match(staffSkill, roleSkill)[1], 0)


class TestRoleSkillMatchRole4(unittest.TestCase):
    def testMatch(self):
        staffSkill = [
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Applications Integration"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Presentation Delivery"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Developing People"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Infrastructure Support"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "Professional and Business Ethics"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "Proficiency_Level": 0,
                    "Skill_Name": "SOP Development and Implementation"
                }
            ]

        roleSkill = [
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Account Management"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Budgeting"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Development"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Needs Analysis"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Business Negotiation"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Collaboration"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Communication"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Data Analytics"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Pricing Strategy"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Problem Solving"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Product Management"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Sales Strategy"
                },
                {
                    "Proficiency_Level": 0,
                    "Skill_Name": "Stakeholder Management"
                }
            ]
        self.assertEqual(role_skill_match(staffSkill, roleSkill)[1], 0)



class TestRoleSkillMatchInv(unittest.TestCase):
    def test_Match(self):
        self.assertEqual(role_skill_match(None, None)[1], None)

if __name__ == "__main__":
    unittest.main()
