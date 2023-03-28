from django.core.mail import send_mail


def send_confirmation_email(user):
    code = user.activation_code
    full_link = f'http://34.94.9.208/api/v1/account/activate/{code}/'
    to_email = user.email
    send_mail(
        'Hello, please activate your account!',
        f'To activate your account, follow the link: {full_link}',
        'alatoo.library@gmail.com',
        [to_email, ],
        fail_silently=False
    )


def send_reset_password(user):
    code = user.activation_code
    to_email = user.email
    send_mail(
        'Subject', f'Your code for reset password: {code}',
        'admin@admin.com', [to_email, ], fail_silently=False
    )