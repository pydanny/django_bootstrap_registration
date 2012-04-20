from bootstrap.forms import BootstrapForm, Fieldset
from django.contrib.auth.forms import SetPasswordForm


class BootstrapSetPasswordForm(BootstrapForm, SetPasswordForm):
    """
    Thin wrapper over the usual SetPasswordForm appending the bootstrap
    benefits to it.
    """

    class Meta:
        layout = (
            Fieldset(None, 'new_password1', 'new_password2'),
            )
