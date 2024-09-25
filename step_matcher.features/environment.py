# -*- coding: UTF-8 -*-

import behave.active_tag.python
import behave.active_tag.python_feature
from behave.fixture import use_fixture_by_tag
from behave.tag_matcher import (
    ActiveTagMatcher, setup_active_tag_values, print_active_tags
)


# -----------------------------------------------------------------------------
# ACTIVE TAGS:
# -----------------------------------------------------------------------------
# -- MATCHES ANY TAGS: @use.with_{category}={value}
# NOTE: active_tag_value_provider provides category values for active tags.
active_tag_value_provider = {}
active_tag_value_provider.update(behave.active_tag.python.ACTIVE_TAG_VALUE_PROVIDER)
active_tag_value_provider.update(behave.active_tag.python_feature.ACTIVE_TAG_VALUE_PROVIDER)
active_tag_matcher = ActiveTagMatcher(active_tag_value_provider)


def print_active_tags_summary():
    print_active_tags(active_tag_value_provider, ["python.version", "os"])


# -----------------------------------------------------------------------------
# -- SETUP: Use cfparse as default matcher
# -----------------------------------------------------------------------------
from behave import use_step_matcher
use_step_matcher("cfparse")


# -----------------------------------------------------------------------------
# HOOKS:
# -----------------------------------------------------------------------------
def before_all(context):
    context.config.setup_logging()
    print_active_tags_summary()
