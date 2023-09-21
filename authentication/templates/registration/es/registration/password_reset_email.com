{% load i18n %}
{% autoescape off %}
{% blocktrans %}
Estás recibiendo este correo electrónico porque has solicitado restablecer la contraseña de tu cuenta en {{ site_name }}.

Por favor, ve a la siguiente página y elige una nueva contraseña:
 <a href="http://127.0.0.1:8000{% url 'password_reset_confirm' uidb64=uid token=token %}">Reset Password</a>



{% endblocktrans %}