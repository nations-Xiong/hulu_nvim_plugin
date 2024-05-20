import pynvim


@pynvim.plugin
class Plugin(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command('Test')
    def test(self, args):
        self.nvim.command('echo "test"')
