import subprocess


def input(input: str, format: str | None = None):
    return Stream().input(input, format)


def seek(ss: str, to: str):
    return Stream().seek(ss, to)


def hwaccel(typ: str):
    return Stream().hwaccel(typ)


class Stream:
    def __init__(self):
        self.cmd = ["ffmpeg"]

    def seek(self, ss: str, to: str):
        self.cmd.append(f"-ss {ss} -to {to}")
        return self

    def hwaccel(self, typ: str):
        self.cmd.append(f"-hwaccel {typ}")
        return self

    def input(self, input: str, format: str | None = None):
        self.cmd.append(f"-i {input}")
        return self

    def output(self, output: str, format: str | None = None):
        self.cmd.append(f"{output}")
        return self

    def copy(self):
        self.cmd.append("-c copy")
        return self

    def cv(self, typ: str):
        self.cmd.append(f"-c:v {typ}")
        return self

    def cv_h264_nvenc(self):
        self.cmd.append("-c:v h264_nvenc")
        return self

    def ca(self, typ: str):
        self.cmd.append(f"-c:a {typ}")
        return self

    def overwrite(self):
        self.cmd.append("-y")
        return self

    def raw(self):
        return " ".join(self.cmd)

    def display(self):
        print(self.raw())

    def run(self):
        subprocess.run(self.raw(), shell=True)
