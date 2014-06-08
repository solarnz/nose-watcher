# -*- coding: utf-8 -*-
import os
import select
from subprocess import Popen
import sys

from nose.plugins import Plugin
import inotify
import inotify.watcher

PLUGIN_NAME = 'watcher'


class WatcherPlugin(Plugin):
    # The name of the plugin
    name = PLUGIN_NAME

    # The inotify events we want to listen for
    inotify_events = (
        inotify.IN_ATTRIB | inotify.IN_CLOSE_WRITE | inotify.IN_CREATE |
        inotify.IN_DELETE | inotify.IN_DELETE_SELF | inotify.IN_MODIFY |
        inotify.IN_MOVE | inotify.IN_MOVED_FROM | inotify.IN_MOVED_TO |
        inotify.IN_MOVE_SELF | inotify.IN_UNMOUNT
    )

    # Files ending with these suffixes will cause us to run nostests again.
    python_files = ('.py', '.pyx')
    testing = False

    def call(self):
        args = self.get_commandline_arguments()
        Popen(args).wait()

    def check_files(self, files):
        return any(f.endswith(self.python_files) for f in files)

    def get_commandline_arguments(self, argv=None):
        if argv is None:
            argv = sys.argv

        # The arguments we want to run nose with again.
        args = [a for a in argv if a != '--with-%s' % PLUGIN_NAME]
        return args

    def print_status(self):  # pragma:nocover
        print('Watching for changes...\n')

    def finalize(self, result):
        watcher = inotify.watcher.AutoWatcher()
        watcher.add_all(os.getcwd(), self.inotify_events)

        if not watcher.num_watches():
            return

        poll = select.poll()
        poll.register(watcher, select.POLLIN)

        threshold = inotify.watcher.Threshold(watcher, 512)
        timeout = None

        self.print_status()

        while True:
            events = poll.poll(timeout)
            files = set()

            if threshold() or not events:
                for event in watcher.read(0):
                    files.add(event.fullpath)

            if files:
                if self.check_files(files):
                    self.call()
                    self.print_status()
                timeout = None
                poll.register(watcher, select.POLLIN)
            else:
                timeout = 1000
                poll.unregister(watcher)

            if self.testing:
                break
