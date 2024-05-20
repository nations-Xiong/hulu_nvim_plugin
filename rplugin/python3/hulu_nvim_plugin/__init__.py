from package import ANSWER 

import pynvim


@pynvim.plugin
class Plugin(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command('Test')
    def test(self):
        self.nvim.command(f"echo 'answer from hulu_nvim_plugin: {ANSWER}'")
