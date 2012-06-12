from bootstrap.forms import BootstrapForm, Fieldset
from django.contrib.auth.forms import PasswordChangeForm


class BootstrapPasswordChangeForm(BootstrapForm, PasswordChangeForm):
    """
    Thin wrapper over the usual PasswordChangeForm appending the bootstrap
    benefits to it.
    """

    class Meta:
        layout = (
            Fieldset('', 'old_password', 'new_password1', 'new_password2'),
            )
