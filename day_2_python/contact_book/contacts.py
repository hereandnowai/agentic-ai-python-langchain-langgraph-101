# ==========================================================================
# DAY 2 · Project 2 · Contact Book — the BACKEND (all the real Python)
# --------------------------------------------------------------------------
# This is where the logic you learned this week comes together:
#   • dicts        -> each contact is  {"phone": ..., "email": ...}
#   • functions    -> load / save / add / search / delete / list_all
#   • JSON files   -> data is stored in contacts.json so it survives restarts
# The screen (app.py) only CALLS these functions. This is the file to study.
# ==========================================================================

import json  # brings in Python's toolkit for reading and writing JSON
import os  # brings in tools for working with file paths and folders

# __file__ is the path to THIS file. We build the path to contacts.json in the
# SAME folder, so the app works no matter where you run it from.
FILE = os.path.join(os.path.dirname(__file__), "contacts.json")  # builds the full path to the data file next to this one

def load():  # defines a function that reads all the saved contacts
    """Read all contacts from the JSON file and return them as a dict.

    If the file does not exist yet (first run), return an empty dict {}.
    """
    if os.path.exists(FILE):  # if the data file already exists on disk
        with open(FILE) as f:  # opens the file for reading
            return json.load(f)   # JSON text on disk -> Python dict
    return {}  # if there is no file yet, hand back an empty dictionary

def save(contacts):  # defines a function that writes all contacts to disk
    """Write the whole contacts dict back to the JSON file.

    indent=2 makes the saved file human-readable (nicely spaced).
    """
    with open(FILE, "w") as f:  # opens the file for writing (making a new empty one)
        json.dump(contacts, f, indent=2)   # Python dict -> JSON text on disk

def add(name, phone, email):  # defines a function that adds or updates one contact
    """Add a new contact (or update one that already has this name).

    Pattern used everywhere here: load -> change the dict -> save.
    """
    contacts = load()  # reads the current contacts from disk
    contacts[name] = {"phone": phone, "email": email}   # add/replace this key
    save(contacts)  # writes the updated contacts back to disk
    return f"Saved {name}."  # hands back a short confirmation message

def search(name):  # defines a function that looks up one contact by name
    """Look up one contact by name and return a readable line of text."""
    contact = load().get(name)          # .get() returns None if not found
    if contact is None:  # if no contact with that name was found
        return f"No contact called {name}"  # hands back a "not found" message
    return f"{name}: {contact['phone']}, {contact['email']}"  # hands back the name with its phone and email

def delete(name):  # defines a function that removes one contact by name
    """Remove a contact by name, if it exists."""
    contacts = load()  # reads the current contacts from disk
    if name not in contacts:            # guard: don't crash on a missing name
        return f"No contact called {name}."  # hands back a "not found" message
    del contacts[name]                  # remove the key from the dict
    save(contacts)  # writes the shortened contacts back to disk
    return f"Deleted {name}."  # hands back a short confirmation message

def list_all():  # defines a function that returns every contact as text
    """Return every contact as one multi-line string (one contact per line)."""
    contacts = load()  # reads the current contacts from disk
    if not contacts:  # if there are no contacts at all
        return "No contacts yet."  # hands back a friendly empty message
    # loop over every name/details pair and build one line each, joined by \n
    return "\n".join(f"{n}: {c['phone']} | {c['email']}" for n, c in contacts.items())  # builds one line per contact and joins them into a block of text


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