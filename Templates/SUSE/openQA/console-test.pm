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

use base 'consoletest';
use strict;
use warnings;
use testapi;
use utils;
#use version_utils qw(is_sle is_opensuse is_leap is_tumbleweed);
#use registration qw(cleanup_registration register_product add_suseconnect_product get_addon_fullname remove_suseconnect_product);

sub run {
    # Preparation
    my $self = shift; # $_[0];
    #select_console 'root-console';
    $self->select_serial_terminal;
    zypper_call 'in [PACKAGEs]';
    # Run some tests
    assert_script_run 'echo Hello World';
    validate_script_output "echo Hello World", sub { m/Hello World/ };
}


sub post_fail_hook {
    my $self = shift;
	# ... 
	$self->SUPER::post_fail_hook;
}

sub post_run_hook {
    my $self = shift;
    # ...
    $self->SUPER::post_run_hook;
}

1;
