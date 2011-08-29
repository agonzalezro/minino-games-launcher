#!/usr/bin/env python
# -*- coding: utf-8 -*-

import gtk
import webkit

from optparse import OptionParser, OptionGroup


class Browser(object):
    def __init__(self, options, args):
        self.url = args[0]
        self.title = options.title
        self.maximized = options.maximized
        self.fullscreen = options.fullscreen
        self.width = options.width
        self.height = options.height

    def __call__(self):
        gtk.gdk.threads_init()
        self.build_window()
        self.window.show_all()
        gtk.main()

    def build_window(self):
        # Main window and event
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_position(gtk.WIN_POS_CENTER_ALWAYS)
        self.window.set_default_size(self.width, self.height)
        self.window.connect("key-press-event", self.keypress)
        self.window.connect('delete_event', self.close_application)

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

        if self.maximized:
            self.window.maximize()

        if self.fullscreen:
            self.window.fullscreen()

    def parse_url(self, url):
        if url.startswith('/'):
            url = 'file://%s' % url
        elif not url.startswith('http') and not url.startswith('file'):
            url = 'http://%s' % url
        return url

    def close_application(self, widget, event, data=None):
        gtk.main_quit()

    def keypress(self, widget, event) :
        if event.keyval == gtk.keysyms.Escape :
            self.close_application(widget, event)


class Shortcut(object):
    def __init__(self, options, args):
        self.options = options
        self.args = args

    def create(self):
        name = self.get_name()
        handler = open(name, "w")
        handler.write('[Desktop Entry]\n'
                      'Name=%(title)s\n'
                      'Exec=/usr/bin/mgl.py %(params)s %(url)s\n'
                      'Icon=%(icon)s\n'
                      'Encoding=UTF-8\n'
                      'Type=Applications\n'
                      'Categories=%(categories)s\n' % self.get_icon_info())
        handler.close()

    def get_name(self):
        name = self.options.shortcut
        if not name.endswith('.desktop'):
            name = name + '.desktop'
        return name

    def get_icon_info(self):
        import ipdb;ipdb.set_trace()
        return {'title': self.options.title or self.args[0],
                'url': self.args[0],
                'params': '-m',
                'icon': self.options.icon or 'gnome-panel-launcher',
                'categories': self.options.categories or 'Minino;XogosRede;'}


class Parser(object):
    def __init__(self):
        parser = OptionParser('usage: %prog [options or -h] url')
        self.add_options(parser)
        (self.options, self.args) = parser.parse_args()
        if not self.args:
            parser.error('the url is mandatory')

    def add_options(self, parser):
        parser.add_option('-f', '--fullscreen', dest='fullscreen',
                          default=False, action="store_true",
                          help='start the launcher at fullscreen')
        parser.add_option('-m', '--maximized', dest='maximized',
                          default=False, action="store_true",
                          help='start the launcher maximized')
        parser.add_option('-t', '--title', dest='title', help='window title')
        parser.add_option('--width', dest='width', default=800, type='int',
                          help='window width')
        parser.add_option('--height', dest='height', default=600, type='int',
                          help='window height')

        group = OptionGroup(parser, "Creating .desktop icons")
        group.add_option('-c', '--categories',
                         help='; separated categories to the icon')
        group.add_option('-s', '--shortcut', help='path to save the .desktop')
        group.add_option('-i', '--icon',
                         help='icon to use at the .desktop file')
        parser.add_option_group(group)


if __name__ == '__main__':
    parser = Parser()
    if parser.options.shortcut:
        shortcut = Shortcut(parser.options, parser.args)
        shortcut.create()
    else:
        browser = Browser(parser.options, parser.args)
        browser()
