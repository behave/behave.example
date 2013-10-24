# -*- coding: UTF-8 -*-
"""
Based on ``behave tutorial``

Feature: Step Result Table

   Scenario: Unordered Result Table Comparison (RowFixture Table)
     Given a set of specific users
        | name      | department  |
        | Alice     | Beer Cans   |
        | Bob       | Beer Cans   |
        | Charly    | Silly Walks |
        | Dodo      | Silly Walks |

    Then we will have the following people in "Silly Walks":
        | name    |
        | Charly  |
        | Dodo    |

    And we will have the following people in "Beer Cans":
        | name    |
        | Bob     |
        | Alice   |


   Scenario: Subset Result Table Comparison
     Given a set of specific users
        | name      | department       |
        | Alice     | Super-sonic Cars |
        | Bob       | Super-sonic Cars |

    Then we will have at least the following people in "Super-sonic Cars":
        | name    |
        | Alice   |
"""

# @mark.steps
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave   import given, when, then
from hamcrest import assert_that, has_items
from hamcrest.library.collection.issequence_containinginanyorder \
    import contains_inanyorder

@then('we will have the following people in "{department}"')
def step_impl(context, department):
    """
    Compares expected with actual persons in a department.
    NOTE: Unordered comparison (ordering is not important).
    """
    department_ = context.model.departments.get(department, None)
    if not department_:
        assert_that(False, "Department %s is unknown" % department)
    # -- NORMAl-CASE:
    expected_persons = [ row["name"]    for row in context.table ]
    actual_persons   = department_.members

    # -- UNORDERED TABLE-COMPARISON (using: pyhamcrest)
    assert_that(contains_inanyorder(*expected_persons), actual_persons)

@then('we will have at least the following people in "{department}"')
def step_impl(context, department):
    """
    Compares subset of persons with actual persons in a department.
    NOTE: Unordered subset comparison.
    """
    department_ = context.model.departments.get(department, None)
    if not department_:
        assert_that(False, "Department %s is unknown" % department)
        # -- NORMAl-CASE:
    expected_persons = [ row["name"]    for row in context.table ]
    actual_persons   = department_.members

    # -- TABLE-SUBSET-COMPARISON (using: pyhamcrest)
    assert_that(has_items(*expected_persons), actual_persons)

# @mark.more_steps
# ----------------------------------------------------------------------------
# MORE STEPS: step_tutorial06.py
# ----------------------------------------------------------------------------
# @given('a set of specific users')
# def step_impl(context):
#    model = getattr(context, "model", None)
#    if not model:
#        context.model = CompanyModel()
#    for row in context.table:
#        context.model.add_user(row["name"], deparment=row["department"])
#
# @when('we count the number of people in each department')
# def step_impl(context):
#    context.model.count_persons_per_department()

