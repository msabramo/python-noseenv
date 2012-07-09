import os
from nose.plugins import Plugin

class NoseEnvPlugin(Plugin):
    name = 'noseenv'
    enabled = False

    def add_options(self, parser, env=os.environ):
        '''Add command-line options for plugin'''
        parser.add_option('--env',
                          action='append',
                          default=[],
                          dest='env',
                          help='Add environment variable settings of the form KEY=VALUE')

    def configure(self, options, conf):
        """Configure the plugin"""
        Plugin.configure(self, options, conf)

        for setting_str in options.env:
            env_variable, value = setting_str.split('=')
            os.environ[env_variable] = value
