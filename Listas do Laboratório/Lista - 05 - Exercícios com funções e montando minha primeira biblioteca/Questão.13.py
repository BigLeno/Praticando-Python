def build_profile(first, last, location, field, **user_info):
    """Construindo um dicionário que contém todas as informações do usuário"""
    user_info['first_name'] = first.title()
    user_info['last_name'] = last.title()
    user_info['location'] = location.title()
    user_info['field'] = field.title()
    return user_info

user_profile = build_profile(input('Enter your first name: '), input('Enter your last name: '), input('Enter your location: '), input('Enter your field: '), raça = 'Humanóide')

print(user_profile)