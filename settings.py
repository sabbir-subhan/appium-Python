class Settings(object):
    _platform = None

    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, val):
        self._platform = val


class SettingsPort(object):
    _port = None

    @property
    def port(self):
        return self._port

    @port.setter
    def port(self, val):
        self._port = val

