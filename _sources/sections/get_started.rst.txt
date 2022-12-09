Getting Started
=================================


Installation
-----------------------------------------

Install using the command:

.. code-block:: bash

    pip3 install git+https://github.com/l-gorman/pyona



Basic Usage
-----------------------------------------

.. code-block:: python

    from pyona import onaRequest

    r = onaRequest(username='ONAusername', password='onaPassword')

    r.fetch_data("ESSA - KE -  Contributor Enrolment")

    results = r.submissions_dataframe()
