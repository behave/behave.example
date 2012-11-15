# -*- coding: UTF-8 -*-
"""
Based on ``behave tutorial``

  Scenario Outline: Blenders
     Given I put <thing> in a blender
     When I switch the blender on
     Then it should transform into <other thing>

   Examples: Amphibians
     | thing         | other thing |
     | Red Tree Frog | mush        |
     | apples        | apple juice |

   Examples: Consumer Electronics
     | thing         | other thing |
     | iPhone        | toxic waste |
     | Galaxy Nexus  | toxic waste |

"""

# @mark.domain_model
# -----------------------------------------------------------------------------
# DOMAIN-MODEL:
# -----------------------------------------------------------------------------
class Blender(object):
    TRANSFORMATION_MAP = {
        "Red Tree Frog": "mush",
        "apples": "apple juice",
        "iPhone": "toxic waste",
        "Galaxy Nexus": "toxic waste",
    }
    def __init__(self):
        self.thing  = None
        self.result = None

    @classmethod
    def select_result_for(cls, thing):
        return cls.TRANSFORMATION_MAP.get(thing, "DIRT")

    def add(self, thing):
        self.thing = thing

    def switch_on(self):
        self.result = self.select_result_for(self.thing)

