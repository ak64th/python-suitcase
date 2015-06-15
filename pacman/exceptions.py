# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (c) 2015 Digi International Inc. All Rights Reserved.

"""Define an exception hierarchy used within Pacman

The basic rule is that users of the Pacman library should always
be able to catch the base ``PacmanException`` and be confident
that they will not get some other random exception.  Catching
more specific subclasses of this exception should then be possible.

There are still some cases (especially when constructing a field) that
base exceptions (like TypeError, ValueError, or TypeError) might still be
raised.  In general, however, any case where things are dynamic, we do
our best to raise a ``PacmanException`` with meaningful information.

"""


class PacmanException(Exception):
    """Base exception acting as the root for other exceptions"""


class PacmanChecksumException(PacmanException):
    """Exception raised when a checksum does not match"""


class PacmanProgrammingError(PacmanException):
    """Exception raised when somebody is doing something wrong"""


class PacmanParseError(PacmanException):
    """Raised when there is a problem parsing bytes into a pacman schema"""


class PacmanPackException(PacmanException):
    """Raised when there is an error packing a message"""


class PacmanPackStructException(PacmanPackException):
    """Raised on an error packing a struct field"""

    def __init__(self, struct_exception):
        self.struct_exception = struct_exception

    def __repr__(self):
        return repr(self.struct_exception)

    def __str__(self):
        return str(self.struct_exception)
