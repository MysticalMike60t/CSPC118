class SuccessCode(int):
    Ok: int = 0


class ErrorCode(int):
    Failed: int = 1


class ExitCode(int):
    OK: int = SuccessCode.Ok
    ERR: int = ErrorCode.Failed
