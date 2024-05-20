import pynvim


@pynvim.plugin
class Plugin(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command('Test')
    def test(self):
        self.nvim.out_write('hello from hulu_nvim_plugin')
