from vault import Vault
from entry import Entry

def test_add_entry():
    v = Vault("Alice")
    v.add_entry("Gmail", "alice123", "pass")
    assert len(v.entries) == 1
    assert v.entries[0].site == "Gmail"
