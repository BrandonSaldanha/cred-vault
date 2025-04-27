from vault import Vault
from entry import Entry

def test_add_entry():
    v = Vault("Alice")
    e = Entry("Gmail", "alice123", "pass")
    v.add_entry(e)
    assert len(v.enteries) == 1
    assert v.enteries[0].site == "Gmail"
