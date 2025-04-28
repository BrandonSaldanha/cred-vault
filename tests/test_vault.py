import pytest
from vault import Vault
from entry import Entry

# Test adding and listing entries
def test_add_entry():
    vault = Vault("TestUser")

    # Add an entry
    vault.add_entry("facebook.com", "testuser1", "password123")

    # Assert that the entry is added correctly
    assert len(vault.entries) == 1
    assert vault.entries[0].site == "facebook.com"
    assert vault.entries[0].username == "testuser1"
    assert vault.entries[0].password == "password123"

# Test listing entries
def test_list_entries():
    vault = Vault("TestUser")

    # Add multiple entries
    vault.add_entry("facebook.com", "testuser1", "password123")
    vault.add_entry("twitter.com", "testuser2", "password456")

    # Capture output to verify listing
    from io import StringIO
    import sys
    captured_output = StringIO()
    sys.stdout = captured_output

    vault.list_entries()

    # Assert that the printed output matches the expected result
    assert "facebook.com" in captured_output.getvalue()
    assert "testuser1" in captured_output.getvalue()
    assert "twitter.com" in captured_output.getvalue()

    sys.stdout = sys.__stdout__  # Reset stdout