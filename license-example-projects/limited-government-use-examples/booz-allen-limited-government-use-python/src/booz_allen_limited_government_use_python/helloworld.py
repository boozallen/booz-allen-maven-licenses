###
# #%L
# aiSSEMBLE License::Example::Limited Government Use::Python
# %%
# Copyright (C) 2021 Ministry of Magic
# %%
# The content of this solution is a trade secret developed at private expense, is the
# intellectual property of Booz Allen Hamilton Inc. (“BAH”), and is subject to copyright
# protection under the laws of the United States and other countries. You may not, copy,
# reproduce, distribute, publish, display, execute, modify, create derivative works of,
# transmit, sell or offer for resale, or in any way exploit any part of this solution
# without Booz Allen Hamilton’s express written permission. This solution is subject to
# the license restrictions noted in Contract No. C1234567890,
# License No. L-9876321. This solution may be used only within
# Ministry of Magic.  This solution may not be used or disclosed outside the
# Ministry of Magic without the written permission of Booz Allen Hamilton Inc.
# #L%
###
import string
import random

print("I'm alive!")


def generate_random_string(n):
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(n)
    )
