from functions import role_skill_match;
import unittest;


class TestRoleSkillMatchStaff1(unittest.TestCase):
    def testMatch(self):
        staffSkill = [
            {
                "id": 140001,
                "isVisible": False,
                "proficiency": 0,
                "skill": "Account Management"
            },
            {
                "id": 140001,
                "isVisible": False,
                "proficiency": 0,
                "skill": "Business Development"
            },
            {
                "id": 140001,
                "isVisible": False,
                "proficiency": 0,
                "skill": "Customer Acquisition Management"
            },
            {
                "id": 140001,
                "isVisible": False,
                "proficiency": 0,
                "skill": "Database Administration"
            },
            {
                "id": 140001,
                "isVisible": False,
                "proficiency": 0,
                "skill": "Financial Statements Analysis"
            },
            {
                "id": 140001,
                "isVisible": False,
                "proficiency": 0,
                "skill": "Pricing Strategy"
            },
            {
                "id": 140001,
                "isVisible": False,
                "proficiency": 0,
                "skill": "Product Management"
            },
            {
                "id": 140001,
                "isVisible": False,
                "proficiency": 0,
                "skill": "Technology Integration"
            }
        ]

        roleSkill = [
                {
                    "proficiency": 0,
                    "skill": "Account Management"
                },
                {
                    "proficiency": 0,
                    "skill": "Budgeting"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Development"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Needs Analysis"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Negotiation"
                },
                {
                    "proficiency": 0,
                    "skill": "Collaboration"
                },
                {
                    "proficiency": 0,
                    "skill": "Communication"
                },
                {
                    "proficiency": 0,
                    "skill": "Data Analytics"
                },
                {
                    "proficiency": 0,
                    "skill": "Pricing Strategy"
                },
                {
                    "proficiency": 0,
                    "skill": "Problem Solving"
                },
                {
                    "proficiency": 0,
                    "skill": "Product Management"
                },
                {
                    "proficiency": 0,
                    "skill": "Sales Strategy"
                },
                {
                    "proficiency": 0,
                    "skill": "Stakeholder Management"
                }
            ]
        self.assertEqual(role_skill_match(staffSkill, roleSkill)[1], 31)

class TestRoleSkillMatchStaff2(unittest.TestCase):
    def testMatch(self):
        staffSkill = [
                    {
                        "id": 140002,
                        "isVisible": False,
                        "proficiency": 0,
                        "skill": "Accounting and Tax Systems"
                    },
                    {
                        "id": 140002,
                        "isVisible": False,
                        "proficiency": 0,
                        "skill": "Business Environment Analysis"
                    },
                    {
                        "id": 140002,
                        "isVisible": False,
                        "proficiency": 0,
                        "skill": "Customer Relationship Management"
                    },
                    {
                        "id": 140002,
                        "isVisible": False,
                        "proficiency": 0,
                        "skill": "Professional and Business Ethics"
                    }
                ]
        roleSkill = [
                {
                    "proficiency": 0,
                    "skill": "Account Management"
                },
                {
                    "proficiency": 0,
                    "skill": "Budgeting"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Development"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Needs Analysis"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Negotiation"
                },
                {
                    "proficiency": 0,
                    "skill": "Collaboration"
                },
                {
                    "proficiency": 0,
                    "skill": "Communication"
                },
                {
                    "proficiency": 0,
                    "skill": "Data Analytics"
                },
                {
                    "proficiency": 0,
                    "skill": "Pricing Strategy"
                },
                {
                    "proficiency": 0,
                    "skill": "Problem Solving"
                },
                {
                    "proficiency": 0,
                    "skill": "Product Management"
                },
                {
                    "proficiency": 0,
                    "skill": "Sales Strategy"
                },
                {
                    "proficiency": 0,
                    "skill": "Stakeholder Management"
                }
            ]
        self.assertEqual(role_skill_match(staffSkill, roleSkill)[1], 0)

class TestRoleSkillMatchStaff3(unittest.TestCase):
    def testMatch(self):
        staffSkill = [
                    {
                        "id": 140003,
                        "isVisible": False,
                        "proficiency": 0,
                        "skill": "Accounting Standards"
                    },
                    {
                        "id": 140003,
                        "isVisible": False,
                        "proficiency": 0,
                        "skill": "Data Analytics"
                    },
                    {
                        "id": 140003,
                        "isVisible": False,
                        "proficiency": 0,
                        "skill": "Digital Fluency"
                    },
                    {
                        "id": 140003,
                        "isVisible": False,
                        "proficiency": 0,
                        "skill": "Problem Solving"
                    },
                    {
                        "id": 140003,
                        "isVisible": False,
                        "proficiency": 0,
                        "skill": "Project Management"
                    }
                ]

        roleSkill = [
                {
                    "proficiency": 0,
                    "skill": "Account Management"
                },
                {
                    "proficiency": 0,
                    "skill": "Budgeting"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Development"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Needs Analysis"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Negotiation"
                },
                {
                    "proficiency": 0,
                    "skill": "Collaboration"
                },
                {
                    "proficiency": 0,
                    "skill": "Communication"
                },
                {
                    "proficiency": 0,
                    "skill": "Data Analytics"
                },
                {
                    "proficiency": 0,
                    "skill": "Pricing Strategy"
                },
                {
                    "proficiency": 0,
                    "skill": "Problem Solving"
                },
                {
                    "proficiency": 0,
                    "skill": "Product Management"
                },
                {
                    "proficiency": 0,
                    "skill": "Sales Strategy"
                },
                {
                    "proficiency": 0,
                    "skill": "Stakeholder Management"
                }
            ]
        self.assertEqual(role_skill_match(staffSkill, roleSkill)[1], 15)

class TestRoleSkillMatchStaff4(unittest.TestCase):
    def testMatch(self):
        staffSkill = [
                {
                    "id": 140004,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Account Management"
                },
                {
                    "id": 140004,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Applications Development"
                },
                {
                    "id": 140004,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Business Negotiation"
                },
                {
                    "id": 140004,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Database Administration"
                },
                {
                    "id": 140004,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Product Management"
                }
            ]

        roleSkill = [
                {
                    "proficiency": 0,
                    "skill": "Account Management"
                },
                {
                    "proficiency": 0,
                    "skill": "Budgeting"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Development"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Needs Analysis"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Negotiation"
                },
                {
                    "proficiency": 0,
                    "skill": "Collaboration"
                },
                {
                    "proficiency": 0,
                    "skill": "Communication"
                },
                {
                    "proficiency": 0,
                    "skill": "Data Analytics"
                },
                {
                    "proficiency": 0,
                    "skill": "Pricing Strategy"
                },
                {
                    "proficiency": 0,
                    "skill": "Problem Solving"
                },
                {
                    "proficiency": 0,
                    "skill": "Product Management"
                },
                {
                    "proficiency": 0,
                    "skill": "Sales Strategy"
                },
                {
                    "proficiency": 0,
                    "skill": "Stakeholder Management"
                }
            ]
        self.assertEqual(role_skill_match(staffSkill, roleSkill)[1], 23)

class TestRoleSkillMatchStaffEmpty(unittest.TestCase):
    def testMatch(self):
        staffSkill = []

        roleSkill = [
                {
                    "proficiency": 0,
                    "skill": "Account Management"
                },
                {
                    "proficiency": 0,
                    "skill": "Budgeting"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Development"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Needs Analysis"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Negotiation"
                },
                {
                    "proficiency": 0,
                    "skill": "Collaboration"
                },
                {
                    "proficiency": 0,
                    "skill": "Communication"
                },
                {
                    "proficiency": 0,
                    "skill": "Data Analytics"
                },
                {
                    "proficiency": 0,
                    "skill": "Pricing Strategy"
                },
                {
                    "proficiency": 0,
                    "skill": "Problem Solving"
                },
                {
                    "proficiency": 0,
                    "skill": "Product Management"
                },
                {
                    "proficiency": 0,
                    "skill": "Sales Strategy"
                },
                {
                    "proficiency": 0,
                    "skill": "Stakeholder Management"
                }
            ]
        self.assertEqual(role_skill_match(staffSkill, roleSkill)[1], 0)

class TestRoleSkillMatchStaff5(unittest.TestCase):
    def testMatch(self):
        staffSkill = [
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Applications Integration"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Business Presentation Delivery"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Developing People"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Infrastructure Support"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Professional and Business Ethics"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "SOP Development and Implementation"
                }
            ]

        roleSkill = [
                {
                    "proficiency": 0,
                    "skill": "Account Management"
                },
                {
                    "proficiency": 0,
                    "skill": "Budgeting"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Development"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Needs Analysis"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Negotiation"
                },
                {
                    "proficiency": 0,
                    "skill": "Collaboration"
                },
                {
                    "proficiency": 0,
                    "skill": "Communication"
                },
                {
                    "proficiency": 0,
                    "skill": "Data Analytics"
                },
                {
                    "proficiency": 0,
                    "skill": "Pricing Strategy"
                },
                {
                    "proficiency": 0,
                    "skill": "Problem Solving"
                },
                {
                    "proficiency": 0,
                    "skill": "Product Management"
                },
                {
                    "proficiency": 0,
                    "skill": "Sales Strategy"
                },
                {
                    "proficiency": 0,
                    "skill": "Stakeholder Management"
                }
            ]
        self.assertEqual(role_skill_match(staffSkill, roleSkill)[1], 0)

class TestRoleSkillMatchRole1(unittest.TestCase):
    def testMatch(self):
        staffSkill = [
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Applications Integration"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Business Presentation Delivery"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Developing People"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Infrastructure Support"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Professional and Business Ethics"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "SOP Development and Implementation"
                }
            ]

        roleSkill = [
                    {
                        "proficiency": 0,
                        "skill": "Call Centre Management"
                    },
                    {
                        "proficiency": 0,
                        "skill": "Collaboration"
                    },
                    {
                        "proficiency": 0,
                        "skill": "Communication"
                    },
                    {
                        "proficiency": 0,
                        "skill": "Customer Relationship Management"
                    },
                    {
                        "proficiency": 0,
                        "skill": "Digital Fluency"
                    },
                    {
                        "proficiency": 0,
                        "skill": "Problem Solving"
                    },
                    {
                        "proficiency": 0,
                        "skill": "Stakeholder Management"
                    },
                    {
                        "proficiency": 0,
                        "skill": "Technology Application"
                    }
                ]

        self.assertEqual(role_skill_match(staffSkill, roleSkill)[1], 0)

class TestRoleSkillMatchRole2(unittest.TestCase):
    def testMatch(self):
        staffSkill = [
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Applications Integration"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Business Presentation Delivery"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Developing People"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Infrastructure Support"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Professional and Business Ethics"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "SOP Development and Implementation"
                }
            ]

        roleSkill = [
                    {
                        "proficiency": 0,
                        "skill": "Developing People"
                    },
                    {
                        "proficiency": 0,
                        "skill": "Collaboration"
                    },
                    {
                        "proficiency": 0,
                        "skill": "Communication"
                    },
                    {
                        "proficiency": 0,
                        "skill": "Customer Relationship Management"
                    },
                    {
                        "proficiency": 0,
                        "skill": "Digital Fluency"
                    },
                    {
                        "proficiency": 0,
                        "skill": "Problem Solving"
                    },
                    {
                        "proficiency": 0,
                        "skill": "Stakeholder Management"
                    },
                    {
                        "proficiency": 0,
                        "skill": "Technology Application"
                    }
                ]
        self.assertEqual(role_skill_match(staffSkill, roleSkill)[1], 12)


class TestRoleSkillMatchRole3(unittest.TestCase):
    def testMatch(self):
        staffSkill = [
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Applications Integration"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Business Presentation Delivery"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Developing People"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Infrastructure Support"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Professional and Business Ethics"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "SOP Development and Implementation"
                }
            ]

        roleSkill = [
                {
                    "proficiency": 0,
                    "skill": "Account Management"
                },
                {
                    "proficiency": 0,
                    "skill": "Budgeting"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Development"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Needs Analysis"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Negotiation"
                },
                {
                    "proficiency": 0,
                    "skill": "Collaboration"
                },
                {
                    "proficiency": 0,
                    "skill": "Communication"
                },
                {
                    "proficiency": 0,
                    "skill": "Data Analytics"
                },
                {
                    "proficiency": 0,
                    "skill": "Pricing Strategy"
                },
                {
                    "proficiency": 0,
                    "skill": "Problem Solving"
                },
                {
                    "proficiency": 0,
                    "skill": "Product Management"
                },
                {
                    "proficiency": 0,
                    "skill": "Sales Strategy"
                },
                {
                    "proficiency": 0,
                    "skill": "Stakeholder Management"
                }
            ]
        self.assertEqual(role_skill_match(staffSkill, roleSkill)[1], 0)


class TestRoleSkillMatchRole4(unittest.TestCase):
    def testMatch(self):
        staffSkill = [
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Applications Integration"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Business Presentation Delivery"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Developing People"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Infrastructure Support"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "Professional and Business Ethics"
                },
                {
                    "id": 140008,
                    "isVisible": False,
                    "proficiency": 0,
                    "skill": "SOP Development and Implementation"
                }
            ]

        roleSkill = [
                {
                    "proficiency": 0,
                    "skill": "Account Management"
                },
                {
                    "proficiency": 0,
                    "skill": "Budgeting"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Development"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Needs Analysis"
                },
                {
                    "proficiency": 0,
                    "skill": "Business Negotiation"
                },
                {
                    "proficiency": 0,
                    "skill": "Collaboration"
                },
                {
                    "proficiency": 0,
                    "skill": "Communication"
                },
                {
                    "proficiency": 0,
                    "skill": "Data Analytics"
                },
                {
                    "proficiency": 0,
                    "skill": "Pricing Strategy"
                },
                {
                    "proficiency": 0,
                    "skill": "Problem Solving"
                },
                {
                    "proficiency": 0,
                    "skill": "Product Management"
                },
                {
                    "proficiency": 0,
                    "skill": "Sales Strategy"
                },
                {
                    "proficiency": 0,
                    "skill": "Stakeholder Management"
                }
            ]
        self.assertEqual(role_skill_match(staffSkill, roleSkill)[1], 0)



class TestRoleSkillMatchInv(unittest.TestCase):
    def test_Match(self):
        self.assertEqual(role_skill_match(None, None)[1], None)

if __name__ == "__main__":
    unittest.main()
