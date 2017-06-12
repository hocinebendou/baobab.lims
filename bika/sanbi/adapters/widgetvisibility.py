"""Archetypes widgets have a .visible property.

By default it may be True or False, or it may contain a dictionary:

            visible={'edit': 'visible',
                     'view': 'visible'}

Values may be 'visible', 'invisible', or 'hidden' depending on how we want
the widget to display in different modes.

The adapters in WidgetVisibility extend the possibilities of this variable.
To define rules for showing/hiding fields at runtime, this is the best way.

For simpler field visibility configuration examine extenders/analysisrequest.py
where the widget.visible flag is used to control adapters in bika.lims.
"""
from zope.interface import implements

from bika.lims.interfaces import IATWidgetVisibility
from bika.sanbi.interfaces import IAliquot, IBiospecimen
from bika.sanbi import bikaMessageFactory as _

class ARFieldWidgetVisibility(object):
    """Forces a set of AnalysisRequest fields to be invisible depending on
    some arbitrary condition.
    """
    implements(IATWidgetVisibility)

    def __init__(self, context):
        self.context = context
        self.sort = 10
        self.hidden_fields = [
            'AdHoc', 'Composite', 'InvoiceExclude',
            'SamplingDate', 'SampleType', 'SamplePoint',
            'StorageLocation', 'Batch', 'SamplingRound',
            'SamplingDeviation', 'SampleCondition',
            'Template', 'ClientReference', 'Profiles',
            'DefaultContainerType', 'ClientSampleID',
        ]
        self.random = 4  # fair dice roll

    def __call__(self, context, mode, field, default):
        state = default if default else 'hidden'
        fieldName = field.getName()
        client = self.context.getClient()
        if not client.hasObject(self.context.getId()):
            if fieldName == 'Sample':
                field.widget.base_query = {
                    'cancellation_state': 'active',
                    'review_state': ['sample_received'],
                    # 'path': {'query': '/'.join(self.context.aq_parent.getPhysicalPath()),
                    #          'level': 0}
                    'getProjectUID': self.context.aq_parent.UID()
                }
        if fieldName in self.hidden_fields:
            field.required = False
            return 'invisible'

        return state

class SampleFieldWidgetVisibility(object):
    """Forces a set of Sample fields to be invisible depending on
    if context implement IBiospecimen or IAliquot
    """
    implements(IATWidgetVisibility)

    def __init__(self, context):
        self.context = context
        self.sort = 10
        self.random = 4
        self.hidden_fields = [
            'ClientReference',
            'PreparationWorkflow',
            'ClientSampleID',
            'SamplingWorkflowEnabled',
            'Sampler',
            'Composite',
            'AdHoc',
            'EnvironmentalConditions',
            'ScheduledSamplingSampler',
            'SamplePoint',
            'SamplingDeviation',
            'DisposalDate',
            'DateSampled',
            'DateCreated']

        self.show_fields = [
            'SampleType',
            'SampleCondition'
        ]
    def __call__(self, context, mode, field, default):
        state = default if default else 'hidden'
        field_name = field.getName()

        wftool = self.context.portal_workflow
        review_state = wftool.getInfoFor(self.context, 'review_state')

        if field_name in self.hidden_fields:
            field.required = False
            return 'invisible'

        if field_name in self.show_fields:
            field.widget.visible['sample_received'] = {'view': 'visible', 'edit': 'visible'}
            field.widget.visible['sample_due'] = {'view': 'visible', 'edit': 'visible'}

        if review_state == 'sample_registered' and not context.aq_parent.hasObject(context.getId()):
            field.widget.render_own_label = False
        else:
            field.widget.render_own_label = True
        return state


class PriceListWidgetVisibility(object):
    """Forces a set of Sample fields to be invisible depending on
    if context implement IBiospecimen or IAliquot
    """
    implements(IATWidgetVisibility)

    def __init__(self, context):
        self.context = context
        self.sort = 10
        self.hidden_fields = [
            'BulkDiscount',
            'BulkPrice'
        ]
        self.random = 4  # fair dice roll

    def __call__(self, context, mode, field, default):
        state = default if default else 'hidden'
        fieldName = field.getName()
        if fieldName in self.hidden_fields:
            field.required = False
            return 'invisible'

        return state

class ProductWidgetVisibility(object):
    """Forces a set of Sample fields to be invisible depending on
    if context implement IBiospecimen or IAliquot
    """
    implements(IATWidgetVisibility)

    def __init__(self, context):
        self.context = context
        self.sort = 10
        self.hidden_fields = [
            'CAS', 'SupplierCatalogueID'
        ]
        self.random = 4  # fair dice roll

    def __call__(self, context, mode, field, default):
        state = default if default else 'hidden'
        fieldName = field.getName()
        if fieldName in self.hidden_fields:
            field.required = False
            return 'invisible'

        return state