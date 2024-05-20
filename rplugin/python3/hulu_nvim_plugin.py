import pynvim


@pynvim.plugin
class Plugin(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command('Test', nargs='*', range='')
    def test(self, args, range):
        self.nvim.out_write('hello from hulu_nvim_plugin')
