class ConfigValidationError(Exception):
    def __init__(self, message):
        super().__init__(message)


class ConfigUniqueTelegramCommandsError(ConfigValidationError):
    def __init__(self, message, cmd):
        self.cmd = cmd
        super().__init__(message)
