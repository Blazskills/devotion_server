from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.relations import RelatedField
from rest_framework import serializers


class UUIDRelatedField(RelatedField):
    """
    A read-write field that represents the target of the relationship
    by a unique 'slug' attribute.
    """

    default_error_messages = {
        "does_not_exist": _("Object with {uuid_field}={value} does not exist."),
        "invalid": _("Invalid value."),
    }

    def __init__(self, uuid_field=None, **kwargs):
        assert uuid_field is not None, "The `uuid_field` argument is required."
        self.uuid_field = uuid_field
        super().__init__(**kwargs)

    def to_internal_value(self, data):
        try:
            return self.get_queryset().get(**{self.uuid_field: data})
        except ObjectDoesNotExist:
            raise serializers.ValidationError(
                self.error_messages["does_not_exist"].format(
                    uuid_field=self.uuid_field, value=str(data)
                )
            )
        except (TypeError, ValueError):
            raise serializers.ValidationError(self.error_messages["invalid"])
