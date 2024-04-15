###
# #%L
# aiSSEMBLE License::Example::BAPL::Python
# %%
# Copyright (C) 2021 Booz Allen Hamilton Inc.
# %%
# This software package is licensed under the Booz Allen Public License. All Rights Reserved.
# #L%
###
import string
import random

print("I'm alive!")


def generate_random_string(n):
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(n)
    )
