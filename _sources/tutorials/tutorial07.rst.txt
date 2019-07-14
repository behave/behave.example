.. raw:: pdf

    PageBreak

.. _id.tutorial07:

Tutorial 7: Result Table
==============================================================================

.. index:: result-table, use-table, table

:Goal: Use *result tables* to simplify comparison of an expected dataset.

The usage of **result tables** come in variations.
It often depends what you want to compare.
These variations in the *test automation layer* are:

* ordered   dataset comparison
* unordered dataset comparison
* ordered   subset  comparison (result table contains subset)
* unordered subset  comparison (result table contains subset)

.. hint::

    The `FIT`_ test framework provides similar concepts via Fixtures.
    An extension of `FIT`_, the `FitLibrary`_, provides even more
    advanced fixtures classes/tables.

    +----------+-----------------------------+----------------------------+
    | Dataset  | Unordered comparison        | Ordered Comparison         |
    +==========+=============================+============================+
    | Subset   | `fitlibrary.SubsetFixture`_,| `fitlibrary.ArrayFixture`_ |
    |          | `fit.RowFixture`_           | (variant)                  |
    |          | (with table args)           |                            |
    +----------+-----------------------------+----------------------------+
    | Complete | `fit.RowFixture`_,          | `fitlibrary.ArrayFixture`_ |
    |          | `fitlibrary.SetFixture`_    |                            |
    +----------+-----------------------------+----------------------------+

    Besides other descriptions of these Fixtures,
    the `Fixture Gallery`_ project provides examples for these fixture
    in several languages.

.. _FIT:        http://fit.c2.com/
.. _FitLibrary: https://sourceforge.net/projects/fitlibrary/
.. _fitnesse:   http://fitnesse.org/
.. _Fixture Gallery: https://sourceforge.net/projects/fixturegallery/

.. _fit.RowFixture: http://fitnesse.org/FitNesse.FullReferenceGuide.UserGuide.FixtureGallery.BasicFitFixtures.RowFixture
.. _fitlibrary.ArrayFixture:  http://fitnesse.org/FitNesse.FullReferenceGuide.UserGuide.FixtureGallery.FitLibraryFixtures.ArrayFixture
.. _fitlibrary.SetFixture:    http://fitnesse.org/FitNesse.FullReferenceGuide.UserGuide.FixtureGallery.FitLibraryFixtures.SetFixture
.. _fitlibrary.SubsetFixture: http://fitnesse.org/FitNesse.FullReferenceGuide.UserGuide.FixtureGallery.FitLibraryFixtures.SubsetFixture

.. broken-links:

    http://gojko.net/fitnesse/fixturegallery/

Both, **unordered dataset comparison** and
**unordered subset comparison** are used in this tutorial
in two different scenarios.


Write the Feature Test
------------------------

.. literalinclude:: ../../features/tutorial07_step_result_table.feature
    :prepend:   # file:features/tutorial07_step_result_table.feature
    :language: gherkin


Provide the Test Automation
-----------------------------

.. literalinclude:: ../../features/steps/step_tutorial07.py
    :prepend:   # file:features/steps/step_tutorial07.py
    :language: python
    :start-after: @mark.steps

Provide the Domain Model
-----------------------------

.. literalinclude:: ../../features/steps/company_model.py
    :prepend:   # file:features/steps/company_model.py
    :language: python
    :start-after: @mark.domain_model

Run the Feature Test
-----------------------------

When you run the feature file from above:

.. ifconfig:: ansiterm_supported

    .. command-output:: behave ../features/tutorial07_step_result_table.feature
        :shell:

.. ifconfig:: not ansiterm_supported

    .. command-output:: behave -c ../features/tutorial07_step_result_table.feature
        :shell:
