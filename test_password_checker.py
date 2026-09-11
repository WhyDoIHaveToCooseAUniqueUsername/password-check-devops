from password_checker import is_valid_password

assert is_valid_password("aaaaaaa1A"), "aaaaaa1A"
assert not is_valid_password("a"), "a"
assert not is_valid_password("aaaaaaaaa"), "aaaaaaaa"
assert not is_valid_password("aaaaaaaa1"), "aaaaaaa1"
assert not is_valid_password("aaaaaaaaA"), "aaaaaaaA"
assert not is_valid_password("aaaaaaaaA"), "aaaaaaaA"

assert not is_valid_password("1"), "1"
assert not is_valid_password("A"), "A"
assert not is_valid_password("A1"), "A1" 
