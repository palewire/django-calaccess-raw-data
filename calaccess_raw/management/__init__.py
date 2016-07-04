#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Utilities for our custom managment commands.
"""
from django.utils.encoding import force_text


def handle_command(command_cls, *args, **options):
    """
    Executes the provided command class on the fly.
    """
    # Simulate argument parsing to get the option defaults (see #10080 for details).
    command = command_cls()
    command_name = command_cls.__class__.__module__.split('.')[-1]
    parser = command.create_parser('', command_name)
    # Use the `dest` option name from the parser option
    opt_mapping = {
        sorted(s_opt.option_strings)[0].lstrip('-').replace('-', '_'): s_opt.dest
        for s_opt in parser._actions if s_opt.option_strings
    }
    arg_options = {opt_mapping.get(key, key): value for key, value in options.items()}
    defaults = parser.parse_args(args=[force_text(a) for a in args])
    defaults = dict(defaults._get_kwargs(), **arg_options)
    # Move positional args out of options to mimic legacy optparse
    args = defaults.pop('args', ())
    if 'skip_checks' not in options:
        defaults['skip_checks'] = True

    return command.execute(*args, **defaults)
