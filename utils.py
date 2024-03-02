from django.core.mail import send_mail


def send_activation_code(email,activation_code):
    message = f'''Вы успешно зарегистрировались на нашем сайте.
    Пройдите активацию аккаунта, кода активации {activation_code}
    '''
    send_mail(
        'Активация аккаунта',
        message,
        'test@gmail.com',
        [email]
    )