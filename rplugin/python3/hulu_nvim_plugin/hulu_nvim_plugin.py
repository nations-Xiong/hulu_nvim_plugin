import pynvim


@pynvim.plugin
class Plugin(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command('Test')
    def test(self):
        self.nvim.command('echo "hello from hulu_nvim_plugin"')
