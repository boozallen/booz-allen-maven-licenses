###
# #%L
# aiSSEMBLE License::Example::Closed Source::Python
# %%
# Copyright (C) 2021 Booz Allen Hamilton Inc.
# %%
# All Rights Reserved. You may not copy, reproduce, distribute, publish, display,
# execute, modify, create derivative works of, transmit, sell or offer for resale,
# or in any way exploit any part of this solution without Booz Allen Hamilton’s
# express written permission.
# #L%
###
import string
import random

print("I'm alive!")


def generate_random_string(n):
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(n)
    )
