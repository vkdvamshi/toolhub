from django import forms
from django.utils.translation import ugettext_lazy as _
from django_filters import FilterSet, filters

from .forms import UserToolFilterForm
from .models import UserTool


class UserToolFilterSet(FilterSet):
    name = filters.CharFilter(field_name='title', lookup_expr='icontains', label=_('Tool name'))

    class Meta:
        model = UserTool
        fields = ("name", "visibility", "clearance", "taxonomies")

    def get_form_class(self):
        default_class = super().get_form_class()
        fields = default_class.base_fields
        return type(
            str("%sForm" % self.__class__.__name__), (UserToolFilterForm,), fields
        )
