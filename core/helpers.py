import os
import re
from random import SystemRandom


class DotEnvReader:
    def __init__(self, path: str):
        self.path = path

    def read(self) -> None:  # pragma: no cover
        try:
            with open(self.path) as f:
                content = f.read()
        except IOError:
            pass
        else:
            for line in content.splitlines():
                match = re.match(r'\A(?P<key>[A-Za-z_0-9]+)=(?P<value>.*)\Z',
                                 re.sub(r'( +)?#(.+)?', '', line))
                if match:
                    os.environ.setdefault(*match.groupdict().values())


def generate_secret_key():
    system_random = SystemRandom()
    allowed_chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return ''.join([system_random.choice(allowed_chars) for _ in range(50)])


def set_secret_key_env(env_path: str) -> None:
    with open(env_path, 'ab') as env:  # pragma: no cover
        secret_key = generate_secret_key()
        os.environ.setdefault('SECRET_KEY', secret_key)
        env.write(b'SECRET_KEY=' + secret_key.encode())
