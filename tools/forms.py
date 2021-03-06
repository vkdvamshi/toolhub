from crispy_forms.layout import Button, Layout, Fieldset, Submit, Field, Div
from django import forms
from django.utils.translation import ugettext_lazy as _

from tools.models import UserTool
from utils.forms import CrispyFormMixin


class CreateUserToolForm(CrispyFormMixin, forms.ModelForm):
    class Meta:
        fields = ("title", "description", "taxonomies", "visibility", "clearance")
        model = UserTool

    def __init__(self, *args, **kwargs):
        super(CreateUserToolForm, self).__init__(*args, **kwargs)
        self.helper.form_action = "tools:create"
        self.helper.form_class = "form-horizontal"
        self.helper.label_class = "col-md-2"
        self.helper.field_class = "col-md-8"
        self.helper.layout = Layout(
            Fieldset(
                _("Add a tool"),
                Field("title"),
                Field("description"),
                Field("taxonomies"),
                Field("visibility"),
                Field("clearance"),
            ),
            Div(
                Div(
                    Submit("create", _("add tool")),
                    css_class="offset-md-2",
                ),
                css_class="form-group",
            ),
        )


class UserToolFilterForm(CrispyFormMixin, forms.Form):
    has_columns = False

    def layout_args(self, helper):
        helper.form_method = 'GET'
        return (
            Field("name"),
            Field("taxonomies"),
            Submit('action', _("Filter")),
        )
