from os import getenv

__all__ = [
    "UndefinedEnvError",
    "StrEnv",
    "BoolEnv",
    "IntEnv",
    "IntListEnv",
]


class UndefinedEnvError(Exception):
    """Raise when cannot read env variable and getenv return None."""

    def __init__(self, env_name: str) -> None:
        msg = f'Env name="{env_name}"'
        super().__init__(msg)


class StrEnv(str):
    def __new__(cls, env_name: str):
        env = getenv(env_name, None)
        if env is None:
            raise UndefinedEnvError(env_name)
        obj = str.__new__(cls, env)
        return obj


class BoolEnv:
    def __new__(cls, env_name: str):
        env = getenv(env_name, None)
        if env is None:
            raise UndefinedEnvError(env_name)
        return env.lower() in ("true", "1")


class IntEnv(int):
    def __new__(cls, env_name: str):
        env = getenv(env_name, None)
        if env is None:
            raise UndefinedEnvError(env_name)
        obj = super().__new__(cls, int(env))
        return obj


class IntListEnv(list[int]):
    def __init__(self, env_name: str) -> None:
        env = getenv(env_name, None)
        if env is None:
            raise UndefinedEnvError(env_name)

        super().__init__(map(int, env.split()))
        