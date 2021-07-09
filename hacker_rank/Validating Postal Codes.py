regex_integer_in_range = r"^[1-9][\d]{5}$"  # Do not delete 'r'.(\d, means after this number there will be five digit)
                                            # ($ sign says that {5} is the last digit)
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"  # Do not delete 'r'.

import re

P = input()

print(bool(re.match(regex_integer_in_range, P))
      and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)
