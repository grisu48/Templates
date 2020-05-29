# SUSE's openQA tests
#
# Copyright © 2020 SUSE LLC
#
# Copying and distribution of this file, with or without modification,
# are permitted in any medium without royalty provided the copyright
# notice and this notice are preserved.  This file is offered as-is,
# without any warranty.

# Summary: [...]
# Maintainer: Felix Niederwanger <felix.niederwanger@suse.de>

use base 'consoletest';
use strict;
use warnings;
use testapi;
use utils;
use version_utils;

sub run {
    # Preparation
    my $self = shift;
    $self->select_serial_terminal;
    # install requirements
    zypper_call 'in [PACKAGEs]';
    assert_script_run 'echo Hello World';
    validate_script_output "echo Hello World", sub { m/Hello World/ };
}


sub post_fail_hook {

}

sub post_run_hook {

}

1;
