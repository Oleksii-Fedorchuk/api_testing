class BasePage:
    def __init__(self, env):
        self._env = env

    def base_url(self):
        return self._env.base_url

