# ==========================================================================
# DAY 2 · Project 2 · Contact Book — the BACKEND (all the real Python)
# --------------------------------------------------------------------------
# This is where the logic you learned this week comes together:
#   • dicts        -> each contact is  {"phone": ..., "email": ...}
#   • functions    -> load / save / add / search / delete / list_all
#   • JSON files   -> data is stored in contacts.json so it survives restarts
# The screen (app.py) only CALLS these functions. This is the file to study.
# ==========================================================================

import json
import os

# __file__ is the path to THIS file. We build the path to contacts.json in the
# SAME folder, so the app works no matter where you run it from.
FILE = os.path.join(os.path.dirname(__file__), "contacts.json")

def load():
    """Read all contacts from the JSON file and return them as a dict.

    If the file does not exist yet (first run), return an empty dict {}.
    """
    if os.path.exists(FILE):
        with open(FILE) as f:
            return json.load(f)   # JSON text on disk -> Python dict
    return {}

def save(contacts):
    """Write the whole contacts dict back to the JSON file.

    indent=2 makes the saved file human-readable (nicely spaced).
    """
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=2)   # Python dict -> JSON text on disk

def add(name, phone, email):
    """Add a new contact (or update one that already has this name).

    Pattern used everywhere here: load -> change the dict -> save.
    """
    contacts = load()
    contacts[name] = {"phone": phone, "email": email}   # add/replace this key
    save(contacts)
    return f"Saved {name}."

def search(name):
    """Look up one contact by name and return a readable line of text."""
    contact = load().get(name)          # .get() returns None if not found
    if contact is None:
        return f"No contact called {name}"
    return f"{name}: {contact['phone']}, {contact['email']}"

def delete(name):
    """Remove a contact by name, if it exists."""
    contacts = load()
    if name not in contacts:            # guard: don't crash on a missing name
        return f"No contact called {name}."
    del contacts[name]                  # remove the key from the dict
    save(contacts)
    return f"Deleted {name}."

def list_all():
    """Return every contact as one multi-line string (one contact per line)."""
    contacts = load()
    if not contacts:
        return "No contacts yet."
    # loop over every name/details pair and build one line each, joined by \n
    return "\n".join(f"{n}: {c['phone']} | {c['email']}" for n, c in contacts.items())


# ==========================================================================
# 🏋️  PRACTICE ACTIVITIES  —  the contact-book backend
# --------------------------------------------------------------------------
# Add your functions to this file. You can test them WITHOUT the web app by
# adding a few calls at the bottom and running:  python contacts.py
# For example:   print(add("Test", "12345", "test@mail.com"))
#
# 1. Add  update(name, phone, email)  that changes an EXISTING contact only,
#    and returns "No contact called <name>." if the name is not found.
# 2. Add  count()  that returns how many contacts are stored.
# 3. Make search() case-INSENSITIVE, so "priya" also finds "Priya".
# 4. Change add() so it REFUSES to overwrite an existing name unless you
#    pass an extra argument  overwrite=True.
# 5. Add a "company" field to each contact (in add) and include it in the
#    line that list_all() builds.
# ==========================================================================