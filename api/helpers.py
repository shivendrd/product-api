from django.db import models
from datetime import datetime


class AbstractModel(models.Model):
    """_summary_

    Args:
        models (_Abstractmodel_): the logic of this model used that we can use common field and ovewrite this class to other class
    """
    created_date = models.DateTimeField(null=True, default=datetime.now())
    last_modified_date = models.DateTimeField(null=True, default=datetime.now())

    class Meta:
        abstract=True