""" Edit form
"""

from zope.formlib.form import Fields
from eea.app.visualization.facets.edit import Edit as EditForm
from eea.exhibit.facets.numeric.interfaces import INumericProperties

class Edit(EditForm):
    """ Edit form
    """
    form_fields = Fields(INumericProperties)
