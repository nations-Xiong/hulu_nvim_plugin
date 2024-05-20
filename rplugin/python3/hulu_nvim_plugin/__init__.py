from .package import ANSWER 

import pynvim


@pynvim.plugin
class Plugin(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command('Test')
    def test(self):
        self.nvim.command(f"echo 'answer from hulu_nvim_plugin: {ANSWER}'")

    @pynvim.command('PrintRange')
    def print_range(self):
        for line in self.nvim.current.range:
            print(line)

    @pynvim.command('PrintBuffer')
    def print_buffer(self):
        for line in self.nvim.current.buffer:
            print(line)
