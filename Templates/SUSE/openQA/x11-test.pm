# SUSE's openQA tests
#
# Copyright © 2021 SUSE LLC
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.

# Summary: [...]
# Maintainer: Felix Niederwanger <felix.niederwanger@suse.de>

use base 'x11test';
use strict;
use warnings;
use testapi;
use utils;
use version_utils;

sub run {
	select_console 'root-console';
	zypper_call('in tigervnc xorg-x11-Xvnc');
	# ...
    select_console 'x11';
    ensure_unlocked_desktop;
    ensure_installed 'steam';
    x11_start_program('xterm');
    turn_off_gnome_screensaver;
    script_run 'my-program', 0;
    wait_still_screen(3);
    script_run 'exit', 0;
}

1;
