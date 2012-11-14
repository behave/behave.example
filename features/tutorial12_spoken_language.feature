# language: de
Funktionalität: Using Languages other than English (tutorial12)

  Als Deutscher
  will ich BDD-Tests auch in Deutsch schreiben und ausführen.

    Szenario: Run a simple test with German Keywords
        Angenommen we have behave installed
        Wenn we implement a test
        Dann behave will test it for us!

    Szenario: Run a simple test completely in German
        Angenommen wir haben "behave" installiert
        Wenn wir einen Test implementieren
        Dann wird "behave" ihn für uns testen!

# @mark.description
# =============================================================================
# Execute Tests written in German Language (language=de)
# =============================================================================
# behave --lang-help=de
#  Translations for German / Deutsch
#              And: Und
#              Then: Dann
#  Scenario Outline: Szenariogrundriss
#               But: Aber
#          Examples: Beispiele
#        Background: Grundlage
#             Given: Angenommen, Gegeben sei
#          Scenario: Szenario
#              When: Wenn
#           Feature: Funktionalität
#
# SEE ALSO: http://packages.python.org/behave/gherkin.html#languages-other-than-english
# -----------------------------------------------------------------------------
# MISSING FEATURE: step_mapping-${lang}.json (or similar)
#   Mapping from language into English language to write step definitions
#   only once. Mappings are step aliases for the given language.
# -----------------------------------------------------------------------------
