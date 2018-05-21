import os
import re
from random import SystemRandom


def generate_secret_key():
    system_random = SystemRandom()
    allowed_chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return ''.join([system_random.choice(allowed_chars) for _ in range(50)])


class EnvHelper:
    def __init__(self, env_file: str):
        self.env_file = env_file

    def read_env_file(self) -> None:  # pragma: no cover
        try:
            with open(self.env_file) as f:
                content = f.read()
        except IOError:
            pass
        else:
            for line in content.splitlines():
                match = re.match(r'\A(?P<key>[A-Za-z_0-9]+)=(?P<value>.*)\Z',
                                 re.sub(r'( +)?#(.+)?', '', line))
                if match:
                    os.environ.setdefault(*match.groupdict().values())

    def set_secret_key(self) -> None:  # pragma: no cover
        secret_key = generate_secret_key()
        os.environ.setdefault('SECRET_KEY', secret_key)

        with open(self.env_file, 'ab') as env:  # pragma: no cover
            env.write(b'SECRET_KEY=' + secret_key.encode())
