# -*- coding: UTF-8 -*-
"""
Based on ``behave tutorial``

Feature: Step Setup Table

   Scenario: Setup Table
     Given a set of specific users
        | name      | department  |
        | Barry     | Beer Cans   |
        | Pudey     | Silly Walks |
        | Two-Lumps | Silly Walks |

    When we count the number of people in each department
    Then we will find two people in "Silly Walks"
     But we will find one person in "Beer Cans"
"""

# @mark.domain_model
# -----------------------------------------------------------------------------
# DOMAIN-MODEL:
# -----------------------------------------------------------------------------
class Department(object):
    def __init__(self, name, members=None):
        if not members:
            members = []
        self.name = name
        self.members = members

    def add_member(self, name):
        assert name not in self.members
        self.members.append(name)

    @property
    def count(self):
        return len(self.members)

    def __len__(self):
        return self.count

class CompanyModel(object):
    def __init__(self):
        self.users = []
        self.departments = {}

    def add_user(self, name, deparment):
        assert name not in self.users
        if not self.departments.has_key(deparment):
            self.departments[deparment] = Department(deparment)
        self.departments[deparment].add_member(name)

    def count_persons_per_department(self):
        pass

    def get_headcount_for(self, department):
        return self.departments[department].count
