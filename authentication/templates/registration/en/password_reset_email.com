Hello,

You have requested to reset your password for your account. Please click the link below to reset your password:

Reset Password: <a href="http://127.0.0.1:8000{% url 'password_reset_confirm' uidb64=uid token=token %}">Reset Password</a>

If you did not request a password reset, please ignore this email. Your password will remain unchanged.

Thank you,