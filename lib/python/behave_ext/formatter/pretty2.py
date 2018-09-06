# -*- coding: utf8 -*-
"""
Provides a PrettyFormatter that uses a terminal styles.
"""

from __future__ import absolute_import
from behave_ext.terminal import select_terminal_class, get_terminal_size
from behave_ext.__termwriter0 import StyledTerminalWriter
from behave.model_describe import ModelDescriptor
from behave.formatter.base import Formatter
from behave.textutil import indent, make_indentation
import six

try:
    # -- SINCE: behave 1.2.6
    from behave.model_core import Status
except ImportError:
    Status = None


class ModelPrinter(object):
    SHOW_SCENARIO_DESCRIPTION = True
    DEFAULT_INDENT_SIZE = 2
    INDENT_FEATURE = 0
    INDENT_FEATURE_DESCRIPTION = 1
    INDENT_SCENARIO = 2
    INDENT_SCENARIO_DESCRIPTION = 3
    INDENT_STEP = 4
    INDENT_MULTILINE = 5

    def __init__(self, styled_writer, config, terminal_width):
        self.writer = styled_writer
        self.terminal_width = terminal_width
        self.show_source = config.show_source
        self.show_timings = config.show_timings
        self.show_multiline = config.show_multiline
        self.show_location = self.show_source or self.show_timings
        self.show_scenario_description = self.SHOW_SCENARIO_DESCRIPTION
        self.indent_size = self.DEFAULT_INDENT_SIZE

        self.location_indentations = []
        indent_levels = [0, 1, 1, 2, 2, 3]
        self.indentations = self.build_indentations(indent_levels)
        assert self.INDENT_MULTILINE < len(self.indentations)

    def reset_statement(self):
        self.location_indentations = []
        self.step_lines = 0

    def build_indentations(self, levels):
        return [ make_indentation(level * self.indent_size)
                 for level in levels]

    def location_text(self, text, indent_size=0):
        if not text:
            return u''
        indentation = make_indentation(indent_size)
        return u'%s # %s' % (indentation, text)

    def calculate_terminal_lines(self, text):
        lines = text.splitlines()
        lines_count = len(lines)
        wrapped_lines = 0
        use_wrapped_lines = True
        if use_wrapped_lines:
            for line in lines:
                if len(line) >= self.terminal_width:
                    wrapped_lines += 1
        # XXX import sys
        # XXX sys.__stdout__.write("XXX wrapped lines: %s (terminal_width=%s)\n" % (wrapped_lines, self.terminal_width))
        return lines_count + wrapped_lines

    def calculate_location_indentations(self, statement, steps):
        line_widths = []
        for s in [statement] + steps:
            text = s.keyword + ' ' + s.name
            line_widths.append(len(text))
        max_line_width = max(line_widths)
        self.location_indentations = [max_line_width - width
                                      for width in line_widths]

    def print_feature_head(self, feature):
        #self.print_comments(feature.comments, '')
        indentation = self.indentations[self.INDENT_FEATURE]
        self.print_tags(feature.tags, indentation)
        text = u"%s%s: %s" % (indentation, feature.keyword, feature.name)
        self.writer.write(text, style="feature")
        if self.show_source:
            text = self.location_text(six.text_type(feature.location), 2)
            self.writer.write(text, style="comments")
        self.writer.write("\n")
        indentation = self.indentations[self.INDENT_FEATURE_DESCRIPTION]
        self.print_description(feature.description, indentation, True)
        self.writer.flush()

    def print_statement_head(self, statement, steps=None):
        self.writer.write(u"\n")
        #self.print_comments(self.statement.comments, '  ')
        indentation = self.indentations[self.INDENT_SCENARIO]
        if hasattr(statement, 'tags'):
            self.print_tags(statement.tags, indentation)
        text = u"%s%s: %s " % (indentation, statement.keyword,
                               statement.name)
        self.writer.write(text, style="scenario")

        if self.show_location:
            steps = steps or []
            self.calculate_location_indentations(statement, steps)
        if self.show_source:
            assert self.show_location
            indent_size = self.location_indentations.pop(0)
            location = six.text_type(statement.location)
            text = self.location_text(location, indent_size)
            self.writer.write(text, style="comments")
        self.writer.write("\n")
        description = getattr(statement, "description", None)
        if self.show_scenario_description and description:
            indentation = make_indentation(self.indent_size*2)
            self.print_description(description, indentation)

    def print_examples(self, examples):
        indentation = self.indentations[self.INDENT_SCENARIO]
        self.writer.write("\n")
        self.print_comments(examples.comments, indentation)
        self.print_tags(examples.tags, indentation)
        self.writer.write('%s%s: %s\n' % (indentation,
                                            examples.keyword, examples.name))
        indentation = self.indentations[self.INDENT_SCENARIO_DESCRIPTION]
        self.print_description(examples.description, indentation)
        self.print_table(examples.rows)
        self.writer.flush()

    def print_step_with_proceed(self, step, status, match, proceed=True):
        location_indentsize = 0
        if self.location_indentations:
            location_indentsize = self.location_indentations[0]
            if proceed:
                self.location_indentations.pop(0)
        self.print_step_with_status(step, status, match, location_indentsize)

    def print_step_with_status(self, step, status, match=None,
                               location_indentsize=2):
        arguments = []
        location = ""
        if match:
            arguments = match.arguments
            location = six.text_type(match.location)

        style = status
        arg_style  = "%s_arg" % style

        #self.print_comments(step.comments, '    ')
        indentation = self.indentations[self.INDENT_STEP]
        self.writer.write(indentation)
        self.writer.write(step.keyword + ' ', style=style)
        line_length = 1 + len(indentation) + len(step.keyword)

        step_name = six.text_type(step.name)
        text_start = 0
        for arg in arguments:
            if arg.end <= text_start:
                # -- SKIP-OVER: Optional and nested regexp args
                #    - Optional regexp args (unmatched: None).
                #    - Nested regexp args that are already processed.
                continue
            # -- VALID, MATCHED ARGUMENT:
            assert arg.original is not None
            text = step_name[text_start:arg.start]
            self.writer.write(text, style=style)
            line_length += len(text)
            self.writer.write(arg.original, style=arg_style)
            line_length += len(arg.original)
            text_start = arg.end

        if text_start != len(step_name):
            text = step_name[text_start:]
            self.writer.write(text, style=style)
            line_length += (len(text))

        if self.show_source:
            if self.show_timings and status in ('passed', 'failed'):
                assert isinstance(location, six.text_type)
                location += " in %0.3fs" % step.duration
            text = self.location_text(location, location_indentsize)
            self.writer.write(text, style="comments")
            line_length += len(text)
        elif self.show_timings and status in ('passed', 'failed'):
            location = u"in %0.3fs" % step.duration
            text = self.location_text(location, location_indentsize)
            self.writer.write(text, style="comments")
            line_length += len(text)
        self.writer.write("\n")

        self.step_lines = int((line_length - 1) / self.terminal_width)
        if self.show_multiline:
            if step.text:
                self.print_docstring(step.text)
            if step.table:
                self.print_table(step.table)
        # import sys
        # sys.__stdout__.write("XXX line_length=%s, step_lines=%s\n" % (line_length, self.step_lines))

    def print_table(self, table):
        indentation = self.indentations[self.INDENT_MULTILINE]
        text = ModelDescriptor.describe_table(table, indentation)
        self.writer.write(text, style="table")
        self.writer.flush()
        self.step_lines += len(table.rows) + 1
        # self.step_lines += text.count("\n")
        # self.step_lines += self.calculate_terminal_lines(text)

    def print_docstring(self, docstring):
        indentation = self.indentations[self.INDENT_MULTILINE]
        text = ModelDescriptor.describe_docstring(docstring, indentation)
        self.writer.write(text, style="docstring")
        self.writer.flush()
        # self.step_lines += len(docstring.splitlines()) + 2
        # self.step_lines += text.count("\n")
        self.step_lines += self.calculate_terminal_lines(text)

    def print_exception(self, exception):
        exception_text = six.text_type(exception, encoding="utf-8")
        self.writer.write(exception_text + "\n", style="failed")
        self.writer.flush()

    def print_tags(self, tags, indentation):
        if not tags:
            return
        line = ' '.join('@' + tag for tag in tags)
        self.writer.write(indentation + line + '\n', style="tag")

    def print_comments(self, comments, indentation):
        if not comments:
            return

        text = indent([c.value for c in comments], indentation)
        self.writer.write(text, style="comments")
        self.writer.write('\n')

    def print_description(self, description, indentation, newline=True):
        if not description:
            return

        self.writer.write(indent(description, indentation),
                            style="description")
        if newline:
            self.writer.write('\n')

# -----------------------------------------------------------------------------
# CLASS: PrettyFormatter
# -----------------------------------------------------------------------------
class Pretty2Formatter(Formatter):
    name = 'pretty2'
    description = 'Standard colourised pretty formatter'
    use_new_impl = True

    def __init__(self, stream_opener, config):
        super(Pretty2Formatter, self).__init__(stream_opener, config)
        # -- ENSURE: Output stream is open.
        self.stream = self.open()
        if self.use_new_impl:
            terminal_writer_class = select_terminal_class(config.color)
            self.terminal = terminal_writer_class(self.stream, colored=config.color)
            terminal_width = get_terminal_size()[0]
            use_replay = self.terminal.has_feature("cursor_up")
        else:
            self.terminal = StyledTerminalWriter(self.stream, colored=config.color)
            terminal_width = self.terminal.width
            use_replay = self.terminal.styled
        self.printer = ModelPrinter(self.terminal, config, terminal_width)
        self.use_step_replay = use_replay

        # -- UNUSED: self.tag_statement = None
        self.current_feature = None
        self.current_scenario = None
        self.statement = None
        self.steps = []
        self._uri = None
        self._match = None

    def reset_statement(self):
        self.statement = None
        self.steps = []
        self._match = None
        self.printer.reset_statement()

    def reset(self):
        # -- UNUSED: self.tag_statement = None
        self.current_feature = None
        self.current_scenario = None
        self._uri = None
        self.reset_statement()

    def finish_last_statement(self):
        self.print_statement()
        self.print_unprocessed_steps()
        self.stream.flush()
        self.reset_statement()

    # -- FORMATTER API:
    def uri(self, uri):
        self.reset()
        self._uri = uri

    def feature(self, feature):
        self.current_feature = feature
        self.printer.print_feature_head(feature)

    def background(self, background):
        self.finish_last_statement()
        self.current_scenario = background
        self.statement = background

    def scenario(self, scenario):
        self.finish_last_statement()
        self.current_scenario = scenario
        self.statement = scenario

    def scenario_outline(self, scenario_outline):
        self.finish_last_statement()
        self.current_scenario = scenario_outline
        self.statement = scenario_outline

    def examples(self, examples):
        self.finish_last_statement()
        self.printer.print_examples(examples)

    def step(self, step):
        self.steps.append(step)

    def match(self, match):
        self._match = match
        self.print_statement()
        if self.use_step_replay:
            # -- PRINT: Mark step as executing before step.run().
            self.print_step("executing", proceed=False)
            self.terminal.flush()

    def result(self, result):
        if self.use_step_replay:
            lines = self.printer.step_lines + 1
            self.terminal.move_cursor_up(lines)

        status_name = result.status
        if Status:
            # -- SINCE: behave 1.2.6 with Status enum class
            status_name = result.status.name
        self.print_step(status_name, proceed=True)
        if result.error_message:
            error_message = indent(result.error_message.strip(), u'      ')
            self.terminal.write(error_message, style="error")
            self.terminal.write('\n\n')
        self.terminal.flush()
        self._match = None

    def eof(self):
        self.finish_last_statement()
        self.terminal.write('\n')
        self.terminal.flush()

    # -- FORMATTER-SPECIFIC PART:
    def print_statement(self):
        if self.statement:
            self.printer.print_statement_head(self.statement, self.steps)
        # -- FINALLY: Mark statement as printed (after first step, ...).
        self.statement = None

    def print_unprocessed_steps(self):
        assert not self._match
        self._match = None
        while self.steps:
            self.print_step("skipped", proceed=True)
        assert not self.steps

    def print_step(self, status, proceed=True):
        match = self._match
        step = self.steps[0]
        if proceed:
            self.steps.pop(0)
        self.printer.print_step_with_proceed(step, status, match, proceed)


class Pretty3Formatter(Pretty2Formatter):
    name = 'pretty3'
    description = 'Standard colourised pretty formatter'
    use_new_impl = False


# -----------------------------------------------------------------------------
# CLASS: SimplePrettyFormatter
# -----------------------------------------------------------------------------
class SimplePrettyFormatter(Pretty2Formatter):
    name = 'pretty1'
    description = 'Simple, colourised pretty formatter'

    def __init__(self, stream_opener, config):
        super(SimplePrettyFormatter, self).__init__(stream_opener, config)
        # -- DISABLE: Step replay.
        self.use_step_replay = False
