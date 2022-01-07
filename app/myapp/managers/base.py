from django.db import models


class BaseModelManager(models.Manager):
    def get_queryset(self):
        return (
            super(BaseModelManager, self)
            .get_queryset()
            .filter(is_deleted=False)
        )

    def deleted(self, *args, **kwargs):
        return BaseDatedQuerySet(
            self.model, using=self._db).deleted(*args, **kwargs)