###
# #%L
# aiSSEMBLE License::Example::Government Use::Python
# %%
# Copyright (C) 2021 Booz Allen Hamilton Inc.
# %%
# The content of this solution is a trade secret developed at private expense, is the
# intellectual property of Booz Allen Hamilton Inc. (“BAH”), and is subject to copyright
# protection under the laws of the United States and other countries. You may not, copy,
# reproduce, distribute, publish, display, execute, modify, create derivative works of,
# transmit, sell or offer for resale, or in any way exploit any part of this solution
# without Booz Allen Hamilton’s express written permission. The Government's rights to
# use, modify, reproduce, release, perform, display, or disclose this solution is
# restricted by Contract No. C1234567890,
# License No.L-9876321.  Any authorized reproduction of
# this solution, or portions thereof marked with this legend must also reproduce
# the markings.
# #L%
###
import string
import random

print("I'm alive!")


def generate_random_string(n):
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(n)
    )
