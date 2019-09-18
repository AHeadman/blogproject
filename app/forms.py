import wtforms
from wtforms.validators import DataRequired
from models import User


class LoginForm(wtforms.Form):
    email = wtforms.StringField("Email", validators=[DataRequired()])
    password = wtforms.PasswordField("Password", validators=[DataRequired()])
    remember_me = wtforms.BooleanField("Remember me?", default=True)

    def validate(self):
        if not super().validate():
            return False

        self.user = User.authenticate(self.email.data, self.password.data)
        if not self.user:
            self.email.errors.append("Invalid email or password.")
            return False

        return True
