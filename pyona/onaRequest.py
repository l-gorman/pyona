import requests
import json
import pandas as pd

__all__ = ["onaRequest"]  # making sure that the class gets imported


class onaRequest:
    """Class for requesting data from the ONA platform

    Example:
        r = onaRequest("test_user", test_password")




    Returns:
        _type_: _description_
    """
    # =======================================================================

    def __init__(self, username, password, url="https://api.ona.io/api/v1"):
        """Init class by setting the basic things needed for an ONA request. 
        User name, password, and URL.

        Args:
            username (str): Username for ONA site
            password (str): Password for ONA site
            url (str, optional): Base URL for ONA API. Defaults to "https://api.ona.io/api/v1".
        """
        self.username = username
        self.password = password
        self.url = url

        self.attributes = set(['username', 'password', 'url'])
    # =======================================================================

    # =======================================================================
    def __str__(self):
        """Method for printing an object of class 'onaRequest'

        Returns:
            string: String of the main attributes of the ona query object
        """

        json_object = {
            'attributes': self.attributes,
            'username': self.username,
            'url': self.url}
        json_str = json.dumps(json_object)

        return json_str
    # =======================================================================

    # =======================================================================
    def get_endpoints(self):
        """Lists the data endpoints accessible to requesting user
        """

        result = requests.get('https://api.ona.io/api/v1/data',
                              auth=(self.username, self.password))
        self.endpoints = result.json()
        self.attributes.add('enpoints')
        return json.dumps(self.endpoints)
    # =======================================================================

    # =======================================================================
    def identify_dataset(self, form_name):
        """There can be multiple form versions
        associated with a project. This method
        identifies all of the endpoints associated
        with a particular form

        Args:
            form_name (str): Name of a form ex

        Raises:
            KeyError: This error is raised when the form specified does not exist on ONA
        """
        if not hasattr(self, 'endpoints'):
            self.get_endpoints()

        datasets = []
        for dataset in self.endpoints:
            if dataset["title"] == form_name:
                datasets.append(dataset)

        if len(datasets) > 0:
            self.attributes.add("datasets")
            self.datasets = datasets
        else:
            raise KeyError("Form not found")
    # =======================================================================

    # =======================================================================
    def fetch_data(self, form_name):
        """Fetch 

        Args:
            form_name (_type_): _description_

        Raises:
            KeyError: _description_
        """
        if not hasattr(self, 'datasets'):
            self.identify_dataset(form_name)

        submissions = []
        for dataset in self.datasets:
            form_submission = requests.get('https://api.ona.io/api/v1/data/710107',
                                           auth=(self.username, self.password)).json()[0]
            submissions.append(form_submission)

        if len(submissions) > 0:
            self.attributes.add("submissions")
            self.submissions = submissions
        else:
            raise KeyError("No submissions for this form")
    # =======================================================================

    # =======================================================================
    def submissions_dataframe(self, form_name=None):

        if not hasattr(self, 'submissions'):
            if form_name is None:
                raise AttributeError(
                    "onaRequest has no attribute 'submissions'. Need to specify a form name if searching for submissions")

            else:
                self.fetch_data(form_name)

        else:
            return (pd.DataFrame(self.submissions))
    # =======================================================================

    # =======================================================================

    # =======================================================================
