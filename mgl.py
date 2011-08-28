#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gtk
import webkit

from optparse import OptionParser


class Browser(object):
    def __init__(self, options, args):
        self.url = args[0]
        self.title = options.title
        self.fullscreen = options.fullscreen
        self.width = options.width
        self.height = options.height

        gtk.gdk.threads_init()
        self.build_window()
        self.window.show_all()
        gtk.main()

    def build_window(self):
        # Main window and event
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
        self.window.connect('delete_event', self.close_application)
        self.window.set_default_size(self.width, self.height)

        # Add webkit view
        self.scrolled_window = gtk.ScrolledWindow()
        self.webview = webkit.WebView()
        self.scrolled_window.add(self.webview)
        self.window.add(self.scrolled_window)

        # Load content
        if self.title:
            self.window.set_title(self.title)
        else:
            self.window.set_title(self.url)
        self.webview.open(self.parse_url(self.url))

        if self.fullscreen:
            self.window.fullscreen()

    def parse_url(self, url):
        if not url.startswith('http'):
            url = 'http://%s' % url
        return url

    def close_application(self, widget, event, data=None):
        gtk.main_quit()


class Parser(object):
    def __init__(self):
        parser = OptionParser('usage: %prog [options or -h] url')
        parser.add_option('-t', '--title', dest='title', help='window title')
        parser.add_option('-f', '--fullscreen', dest='fullscreen',
                          default=False, action="store_true",
                          help='start the launcher at fullscreen')
        parser.add_option('--width', dest='width', default=800,
                          type='int', help='window width')
        parser.add_option('--height', dest='height', default=600,
                          type='int', help='window height')
        parser.add_option('-u', '--url', dest='url',
                          type='string',
                          help='specify url to the game')
        (self.options, self.args) = parser.parse_args()
        if not self.args:
            parser.error('the url is mandatory')


if __name__ == '__main__':
    parser = Parser()
    browser = Browser(parser.options, parser.args)
