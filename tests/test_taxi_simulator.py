#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `taxi_simulator` package."""

from click.testing import CliRunner

from taxi_simulator import cli


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help' in help_result.output
