from faker import Faker


fake = Faker()


def generation_login():
    gen_login = fake.user_name()
    return gen_login


def generation_password():
    gen_password = fake.random_number(8)
    return gen_password


def generation_first_name():
    gen_first_name = fake.first_name()
    return gen_first_name
