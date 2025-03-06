###
# #%L
# aiSSEMBLE License::Example::Specific Client::Python
# %%
# Copyright (C) 2021 Ministry of Magic
# %%
# This solution may be used only within Ministry of Magic or with their express written consent.
# #L%
###
import string
import random

print("I'm alive!")


def generate_random_string(n):
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(n)
    )
