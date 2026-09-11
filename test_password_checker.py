from password_checker import is_valid_password

assert is_valid_password("aaaaaaa1A"), "aaaaaaa1A"
assert not is_valid_password("a"), "a"
assert not is_valid_password("aaaaaaaaa"), "aaaaaaaaa"
assert not is_valid_password("aaaaaaaa1"), "aaaaaaaa1"
assert not is_valid_password("aaaaaaaaA"), "aaaaaaaaA"
assert not is_valid_password("aaaaaaaaA"), "aaaaaaaaA"

assert not is_valid_password("1"), "1"
assert not is_valid_password("A"), "A"
assert not is_valid_password("A1"), "A1" 
