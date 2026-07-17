import json
import os

# keep contacts.json in the same directory as this file
FILE = os.path.join(os.path.dirname(__file__), "contacts.json")

def load():
    if os.path.exists(FILE):
        with open(FILE) as f:
            return json.load(f)
    return {}

def save(contacts):
    with open(FILE, "w") as f:
        json.dump(contacts, f, indent=2)

def add(name, phone, email):
    contacts = load()
    contacts[name] = {"phone": phone, "email": email}
    save(contacts)
    return f"Saved {name}."

def search(name):
    contact = load().get(name)
    if contact is None:
        return f"No contact called {name}"
    return f"{name}: {contact['phone']}, {contact['email']}"

def delete(name):
    contacts = load()
    if name not in contacts:
        return f"No contact called {name}."
    del contacts[name]
    save(contacts)
    return f"Deleted {name}."

def list_all():
    contacts = load()
    if not contacts:
        return "No contacts yet."
    return "\n".join(f"{n}: {c['phone']} | {c['email']}" for n, c in contacts.items())