def init_layout(self):
        """Initialize the each windows with their size and shape"""
        self.height, self.width = self.window.getmaxyx()

        # Title section
        self.window.addstr(0, 0, '[awesome-{}] Find awesome things!'.format(self.awesome_title), curses.color_pair(1))
        self.window.hline(1, 0, curses.ACS_HLINE, self.width)

        # Search result section
        self.result_window = curses.newwin(self.height - 4, self.width, 2, 0)
        self.result_window.keypad(True)

        # Search bar section
        self.window.hline(self.height - 2, 0, curses.ACS_HLINE, self.width)
        self.window.addch(self.height - 1, 0, '>')
        self.search_window = curses.newwin(1, self.width - 1, self.height - 1, 2)
        self.search_window.keypad(True)

        self.window.refresh() 