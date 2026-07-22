"""Gradio FRONTEND for the contact book — a full CRM-style directory UI.

Run: python app.py   (needs: pip install gradio)

NOTE FOR LEARNERS: you do NOT need to understand this file. It is given to
you, like a website template. The Python you are learning lives in
contacts.py — this file only *calls* those functions:

    contacts.load()  contacts.add()  contacts.delete()

Everything else here is presentation (HTML/CSS) served by Gradio.
"""

import html  # brings in a helper for making text safe to show inside web pages

import gradio as gr  # brings in Gradio, the toolkit that builds the web screen
from gradio.themes import Soft  # brings in a ready-made soft look for the screen

import contacts  # brings in our own contacts.py file so we can call its functions

# ---------------------------------------------------------------------------
# Look & feel tokens
# ---------------------------------------------------------------------------

# Avatar tints: (background, text). Picked deterministically from the name so
# the same contact always gets the same colour.
AVATAR_PALETTE = [  # a list of colour pairs (background, text) for the round name badges
    ("#F6DFDF", "#8E1D1D"),  # red
    ("#F2E7C8", "#7C4A10"),  # amber
    ("#D8EBDF", "#0F5F42"),  # green
    ("#D9E4F4", "#1E3F8A"),  # blue
    ("#E4DEF4", "#4C2696"),  # purple
    ("#F1DDE8", "#8A1748"),  # pink
    ("#D3EAEB", "#0A5E68"),  # teal
    ("#E2E3E8", "#3B3D46"),  # slate
]

HEAD = """
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@500;600;700&display=swap" rel="stylesheet">
"""

# Pin the design to its own palette even when the OS/browser prefers dark:
# Gradio re-applies its `dark` class after page load, so a one-shot removal
# is not enough — keep stripping it whenever it reappears.
FORCE_LIGHT_JS = """
() => {
    const strip = () => {
        try {
            document.documentElement.classList.remove('dark');
            if (document.body) document.body.classList.remove('dark');
        } catch (e) {}
    };
    strip();
    const watch = (el) => new MutationObserver(strip)
        .observe(el, { attributes: true, attributeFilter: ['class'] });
    watch(document.documentElement);
    if (document.body) watch(document.body);
}
"""

CSS = """
/* ============================================================
   Contact Book — mini CRM  ·  "graphite" surface
   Palette:  ink #24242E · paper #E2E3E7 · card #F1F1F4
             field #E8E9ED · line #D2D4DA · accent #FFE600
   Type:     Archivo (display) · Inter (UI) · IBM Plex Mono (data)
   Rhythm:   8px grid · 24px panel padding · 14px column gap
   ============================================================ */

:root, .dark {
    --crm-ink: #24242E;
    --crm-paper: #E2E3E7;
    --crm-card: #F1F1F4;
    --crm-field: #E8E9ED;
    --crm-line: #D2D4DA;
    --crm-muted: #63656D;
    --crm-faint: #8A8C94;
    --crm-accent: #FFE600;
    --crm-display: 'Archivo', 'Inter', system-ui, sans-serif;
    --crm-body: 'Inter', system-ui, sans-serif;
    --crm-mono: 'IBM Plex Mono', ui-monospace, monospace;
    --crm-shadow: 0 1px 2px rgba(22, 22, 32, 0.05);
}

/* Belt-and-braces: if Gradio's dark class survives a frame, its own
   variables resolve to our light values, so nothing ever flashes dark. */
.dark {
    --body-background-fill: var(--crm-paper) !important;
    --background-fill-primary: var(--crm-card) !important;
    --background-fill-secondary: var(--crm-field) !important;
    --input-background-fill: var(--crm-field) !important;
    --block-background-fill: transparent !important;
    --body-text-color: var(--crm-ink) !important;
    --block-label-text-color: var(--crm-muted) !important;
    --border-color-primary: var(--crm-line) !important;
}

/* ---- shell ------------------------------------------------- */

html, body, gradio-app, .gradio-container, .dark .gradio-container {
    background: var(--crm-paper) !important;
}
.gradio-container {
    max-width: 1240px !important;
    margin: 0 auto !important;
    padding: 20px 24px 40px 24px !important;
    font-family: var(--crm-body) !important;
    color: var(--crm-ink) !important;
}
footer { display: none !important; }

/* ---- top command bar --------------------------------------- */

.crm-topbar {
    display: flex;
    align-items: center;
    gap: 14px;
    background: var(--crm-ink);
    border-radius: 14px;
    padding: 16px 20px;
    margin-bottom: 8px;
}
.crm-logo {
    width: 36px;
    height: 36px;
    border-radius: 8px;
    background: var(--crm-accent);
    color: #14141A;
    font-family: var(--crm-display);
    font-weight: 800;
    font-size: 18px;
    display: flex;
    align-items: center;
    justify-content: center;
    flex: none;
}
.crm-wordmark {
    font-family: var(--crm-display);
    font-weight: 700;
    font-size: 18px;
    letter-spacing: -0.01em;
    color: #F4F4F6;
    line-height: 1.2;
}
.crm-wordmark small {
    display: block;
    font-family: var(--crm-body);
    font-weight: 400;
    font-size: 11.5px;
    color: #94949E;
    letter-spacing: 0.01em;
    margin-top: 1px;
}
.crm-topbar .crm-live {
    margin-left: auto;
    font-family: var(--crm-mono);
    font-size: 11.5px;
    font-weight: 500;
    color: #B9B9C2;
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.10);
    padding: 6px 12px;
    border-radius: 999px;
    white-space: nowrap;
}
.crm-live b { color: var(--crm-accent); font-weight: 600; }

/* ---- columns ------------------------------------------------ */

.crm-panel {
    background: var(--crm-card) !important;
    border: 1px solid var(--crm-line) !important;
    border-radius: 14px !important;
    padding: 24px !important;
    gap: 12px !important;
    box-shadow: var(--crm-shadow);
    align-self: flex-start;
}
.crm-main { gap: 14px !important; }
.crm-main .block, .crm-panel .block, .crm-panel .form {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    padding: 0 !important;
}

/* ---- panel headings ------------------------------------------ */

.crm-panel-title {
    font-family: var(--crm-display);
    font-weight: 700;
    font-size: 15px;
    letter-spacing: -0.005em;
    color: var(--crm-ink);
    margin: 0;
}
.crm-panel-kicker {
    font-size: 12.5px;
    line-height: 1.45;
    color: var(--crm-muted);
    margin: 3px 0 10px 0;
}
.crm-divider {
    border: none;
    border-top: 1px solid var(--crm-line);
    margin: 18px 0 12px 0;
}

/* ---- form fields ---------------------------------------------- */

.crm-panel label span[data-testid="block-info"],
.crm-panel span[data-testid="block-info"] {
    font-size: 11px !important;
    font-weight: 600 !important;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    color: var(--crm-muted) !important;
    background: transparent !important;
    margin-bottom: 4px !important;
}
.crm-panel input, .crm-panel textarea {
    background: var(--crm-field) !important;
    border: 1.5px solid var(--crm-line) !important;
    border-radius: 10px !important;
    padding: 10px 13px !important;
    font-family: var(--crm-body) !important;
    font-size: 14px !important;
    color: var(--crm-ink) !important;
    box-shadow: none !important;
}
.crm-panel input::placeholder, .crm-panel textarea::placeholder {
    color: var(--crm-faint) !important;
}
.crm-panel input:focus, .crm-panel textarea:focus {
    border-color: var(--crm-ink) !important;
    box-shadow: 0 0 0 3px var(--crm-accent) !important;
}

/* dropdown (remove picker) matches the text fields */
.crm-panel .wrap-inner, .crm-panel .secondary-wrap {
    background: var(--crm-field) !important;
    border-radius: 10px !important;
    box-shadow: none !important;
}
.crm-panel .wrap-inner { border: 1.5px solid var(--crm-line) !important; }
.crm-panel .wrap-inner input { border: none !important; background: transparent !important; }
.crm-panel ul.options {
    background: var(--crm-card) !important;
    border: 1px solid var(--crm-line) !important;
    border-radius: 10px !important;
    box-shadow: 0 8px 24px rgba(22, 22, 32, 0.14) !important;
}
.crm-panel ul.options li {
    color: var(--crm-ink) !important;
    font-size: 13.5px !important;
}
.crm-panel ul.options li:hover, .crm-panel ul.options li.selected {
    background: var(--crm-field) !important;
}

/* ---- buttons ------------------------------------------------ */

#crm-save {
    background: var(--crm-accent) !important;
    color: #14141A !important;
    border: none !important;
    border-radius: 10px !important;
    min-height: 44px !important;
    margin-top: 6px;
    font-family: var(--crm-body) !important;
    font-weight: 700 !important;
    font-size: 14px !important;
    letter-spacing: 0.01em;
    box-shadow: var(--crm-shadow) !important;
    transition: filter 120ms ease, transform 120ms ease;
}
#crm-save:hover { filter: brightness(0.96); transform: translateY(-1px); }
#crm-remove {
    background: transparent !important;
    color: #A5211A !important;
    border: 1.5px solid #DBB6B2 !important;
    border-radius: 10px !important;
    min-height: 40px !important;
    font-weight: 600 !important;
    font-size: 13.5px !important;
    box-shadow: none !important;
}
#crm-remove:hover { background: #EFE2E0 !important; }

button:focus-visible, input:focus-visible, a:focus-visible {
    outline: 3px solid var(--crm-accent) !important;
    outline-offset: 1px;
}

/* ---- status pill -------------------------------------------- */

.crm-pill {
    display: inline-flex;
    align-items: center;
    gap: 7px;
    font-size: 13px;
    font-weight: 600;
    padding: 7px 13px;
    border-radius: 999px;
    margin-top: 8px;
}
.crm-pill::before {
    content: '';
    width: 7px;
    height: 7px;
    border-radius: 50%;
    background: currentColor;
}
.crm-pill-ok   { background: #D8E8DE; color: #14573C; }
.crm-pill-warn { background: #F0E4C4; color: #75470E; }

/* ---- search -------------------------------------------------- */

#crm-search input, #crm-search textarea {
    height: 46px !important;
    font-family: var(--crm-body) !important;
    font-size: 14.5px !important;
    color: var(--crm-ink) !important;
    padding: 12px 16px 12px 42px !important;
    background: var(--crm-card) !important;
    border: 1.5px solid var(--crm-line) !important;
    border-radius: 12px !important;
    box-shadow: var(--crm-shadow) !important;
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='none' stroke='%2363656D' stroke-width='2.4' stroke-linecap='round'%3E%3Ccircle cx='11' cy='11' r='7'/%3E%3Cline x1='21' y1='21' x2='16.5' y2='16.5'/%3E%3C/svg%3E") !important;
    background-repeat: no-repeat !important;
    background-position: 15px center !important;
    resize: none;
}
#crm-search input::placeholder, #crm-search textarea::placeholder {
    color: var(--crm-faint) !important;
}
#crm-search input:focus, #crm-search textarea:focus {
    border-color: var(--crm-ink) !important;
    box-shadow: 0 0 0 3px var(--crm-accent) !important;
}

/* ---- stat tiles ---------------------------------------------- */

.crm-stats {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 12px;
}
.crm-stat {
    background: var(--crm-card);
    border: 1px solid var(--crm-line);
    border-radius: 12px;
    padding: 14px 18px;
    min-height: 84px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    box-shadow: var(--crm-shadow);
}
.crm-stat .lbl {
    font-size: 11px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.07em;
    color: var(--crm-muted);
}
.crm-stat .num {
    font-family: var(--crm-mono);
    font-size: 24px;
    font-weight: 700;
    color: var(--crm-ink);
    line-height: 1.2;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
.crm-stat .num.is-text { font-size: 16px; padding-bottom: 3px; }

/* ---- directory ------------------------------------------------ */

.crm-dir-head {
    display: flex;
    align-items: baseline;
    gap: 10px;
    margin: 6px 2px 0 2px;
}
.crm-dir-head h2 {
    font-family: var(--crm-display);
    font-weight: 700;
    font-size: 14px;
    letter-spacing: -0.005em;
    color: var(--crm-ink);
    margin: 0;
}
.crm-dir-head span {
    font-family: var(--crm-mono);
    font-size: 11.5px;
    color: var(--crm-muted);
}

.crm-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(235px, 1fr));
    gap: 12px;
    margin-top: 10px;
}
.crm-card {
    display: flex;
    flex-direction: column;
    background: var(--crm-card);
    border: 1px solid var(--crm-line);
    border-radius: 12px;
    padding: 18px;
    min-height: 158px;
    box-shadow: var(--crm-shadow);
    transition: transform 130ms ease, box-shadow 130ms ease;
}
.crm-card:hover {
    transform: translateY(-2px);
    box-shadow: inset 3px 0 0 var(--crm-accent), 0 8px 20px rgba(22, 22, 32, 0.12);
}
.crm-card-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 10px;
    margin-bottom: 12px;
}
.crm-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: var(--crm-display);
    font-weight: 700;
    font-size: 14px;
    flex: none;
}
.crm-domain {
    font-family: var(--crm-mono);
    font-size: 10px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: var(--crm-muted);
    background: var(--crm-field);
    border: 1px solid var(--crm-line);
    padding: 3px 9px;
    border-radius: 999px;
    max-width: 55%;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
.crm-name {
    font-family: var(--crm-display);
    font-weight: 700;
    font-size: 15px;
    letter-spacing: -0.01em;
    color: var(--crm-ink);
    margin: 0 0 5px 0;
}
.crm-phone {
    font-family: var(--crm-mono);
    font-size: 13px;
    font-weight: 500;
    color: var(--crm-ink);
}
.crm-card-foot { margin-top: auto; padding-top: 10px; }
.crm-email {
    display: inline-block;
    font-size: 12px;
    font-weight: 500;
    color: #1E3F8A;
    background: #DFE6F3;
    padding: 4px 10px;
    border-radius: 999px;
    text-decoration: none;
    max-width: 100%;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}
.crm-email:hover { background: #D3DDF0; }
.crm-none { color: var(--crm-faint); font-family: var(--crm-body); font-size: 12.5px; }

/* ---- empty / no-result states ---------------------------------- */

.crm-empty {
    border: 1.5px dashed #B9BBC3;
    border-radius: 14px;
    background: transparent;
    text-align: center;
    padding: 56px 20px;
    margin-top: 10px;
    color: var(--crm-muted);
}
.crm-empty .big { font-size: 32px; margin-bottom: 10px; }
.crm-empty h3 {
    font-family: var(--crm-display);
    font-weight: 700;
    font-size: 15px;
    color: var(--crm-ink);
    margin: 0 0 4px 0;
}
.crm-empty p { font-size: 13px; margin: 0; }

/* ---- responsive + motion ----------------------------------------- */

@media (max-width: 900px) {
    .crm-stats { grid-template-columns: 1fr; }
    .crm-stat { min-height: 0; }
    .crm-topbar .crm-live { display: none; }
    .gradio-container { padding: 12px 12px 32px 12px !important; }
}
@media (prefers-reduced-motion: reduce) {
    .crm-card, #crm-save { transition: none !important; }
    .crm-card:hover, #crm-save:hover { transform: none; }
}
"""

# ---------------------------------------------------------------------------
# HTML renderers — turn backend data into presentation
# ---------------------------------------------------------------------------


def _avatar(name):  # defines a helper that picks initials and colours for a name
    """Deterministic initials + colours for a contact name."""
    initials = "".join(w[0] for w in name.split()[:2]).upper() or "?"  # takes the first letter of the first two words, in capitals
    bg, fg = AVATAR_PALETTE[sum(ord(c) for c in name) % len(AVATAR_PALETTE)]  # picks a colour pair based on the name, so it is always the same
    return initials, bg, fg  # hands back the initials and the two colours


def _domain(email):  # defines a helper that pulls the company part out of an email
    return email.split("@", 1)[1].strip().lower() if "@" in email else ""  # returns the bit after the @, or empty text if there is no @


def render_topbar():  # defines a function that builds the HTML for the top bar
    return """
    <div class="crm-topbar">
        <div class="crm-logo">C</div>
        <div class="crm-wordmark">Contact Book
            <small>mini CRM &middot; Python backend &middot; JSON storage &middot; Gradio frontend</small>
        </div>
        <div class="crm-live">backend: <b>contacts.py</b> &middot; data: <b>contacts.json</b></div>
    </div>"""


def render_stats():  # defines a function that builds the three summary tiles
    data = contacts.load()  # reads all the contacts from the backend
    domains = {_domain(c.get("email", "")) for c in data.values()} - {""}  # collects the unique company domains, dropping blanks
    newest = html.escape(list(data)[-1]) if data else "—"  # takes the most recently added name, or a dash if there are none
    return f"""
    <div class="crm-stats">
        <div class="crm-stat"><div class="lbl">Contacts</div><div class="num">{len(data)}</div></div>
        <div class="crm-stat"><div class="lbl">Companies</div><div class="num">{len(domains)}</div></div>
        <div class="crm-stat"><div class="lbl">Newest</div><div class="num is-text">{newest}</div></div>
    </div>"""


def render_card(name, contact):  # defines a function that builds the HTML card for one contact
    initials, bg, fg = _avatar(name)  # gets the initials and colours for this name
    phone = html.escape(contact.get("phone", "").strip())  # gets the phone number, tidied and made safe to show
    email = contact.get("email", "").strip()  # gets the email address with spaces trimmed off
    domain = html.escape(_domain(email))  # gets the company part of the email, made safe to show
    email_html = (  # builds the email link (or a "no email" note), all in one piece of HTML
        f'<a class="crm-email" href="mailto:{html.escape(email)}">{html.escape(email)}</a>'
        if email else '<span class="crm-none">no email</span>'
    )
    return f"""
    <article class="crm-card">
        <div class="crm-card-top">
            <div class="crm-avatar" style="background:{bg};color:{fg}">{initials}</div>
            {f'<span class="crm-domain">{domain}</span>' if domain else ''}
        </div>
        <h3 class="crm-name">{html.escape(name)}</h3>
        <div class="crm-phone">{phone or '<span class="crm-none">no phone</span>'}</div>
        <div class="crm-card-foot">{email_html}</div>
    </article>"""


def render_grid(query=""):  # defines a function that builds the grid of contact cards
    """The directory: all contacts as cards, filtered by the search query."""
    data = contacts.load()  # reads all the contacts from the backend
    q = query.strip().lower()  # tidies the search text: trims spaces and makes it lowercase
    matches = {  # keeps only the contacts whose name, phone or email contains the search text
        name: c for name, c in sorted(data.items(), key=lambda kv: kv[0].lower())
        if q in f"{name} {c.get('phone', '')} {c.get('email', '')}".lower()
    }

    if not data:  # if there are no contacts saved at all
        return """
        <div class="crm-empty">
            <div class="big">📇</div>
            <h3>No contacts yet</h3>
            <p>Add your first contact with the form on the left.</p>
        </div>"""
    if not matches:  # if there are contacts but none matched the search
        return f"""
        <div class="crm-empty">
            <div class="big">🔍</div>
            <h3>No matches for &ldquo;{html.escape(query.strip())}&rdquo;</h3>
            <p>Try a different name, phone number, or company domain.</p>
        </div>"""

    head = (  # builds the small heading that shows how many contacts are being shown
        f'<div class="crm-dir-head"><h2>Directory</h2>'
        f'<span>{len(matches)} of {len(data)} shown</span></div>'
    )
    cards = "".join(render_card(n, c) for n, c in matches.items())  # builds a card for each matching contact and joins them together
    return f'{head}<div class="crm-grid">{cards}</div>'  # hands back the heading plus all the cards as one piece of HTML


def render_pill(message, ok=True):  # defines a function that builds a small status message badge
    kind = "crm-pill-ok" if ok else "crm-pill-warn"  # picks a green style for good news or an amber one for warnings
    return f'<div class="crm-pill {kind}">{html.escape(message)}</div>'  # hands back the badge HTML with the message inside


# ---------------------------------------------------------------------------
# Event handlers — the only place that talks to the backend
# ---------------------------------------------------------------------------


def _refresh(query):  # defines a helper that rebuilds everything after the data changes
    """Everything that changes when the data changes."""
    names = sorted(contacts.load(), key=str.lower)  # gets all contact names sorted A to Z, ignoring capitals
    return render_grid(query), render_stats(), gr.Dropdown(choices=names, value=None)  # hands back the fresh grid, tiles and remove-menu


def on_save(name, phone, email, query):  # defines what happens when the Save button is clicked
    name = name.strip()  # trims spaces off the typed name
    if not name:  # if the name box was left empty
        return render_pill("Name is required.", ok=False), *_refresh(query), name, phone, email  # shows a warning and keeps what was typed
    message = contacts.add(name, phone.strip(), email.strip())  # saves the contact through the backend
    return render_pill(message), *_refresh(query), "", "", ""  # shows the result, refreshes, and clears the boxes


def on_remove(selected, query):  # defines what happens when the Remove button is clicked
    if not selected:  # if no contact was picked from the menu
        return render_pill("Pick a contact to remove.", ok=False), *_refresh(query)  # shows a warning and refreshes
    message = contacts.delete(selected)  # deletes the chosen contact through the backend
    return render_pill(message, ok="Deleted" in message), *_refresh(query)  # shows the result and refreshes


def on_search(query):  # defines what happens as the user types in the search box
    return render_grid(query)  # rebuilds just the grid, filtered by the search text


def on_load(query):  # defines what happens when the page first loads
    return (*_refresh(query),)  # refreshes the grid, tiles and remove-menu once at the start


# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------

with gr.Blocks(title="Contact Book — mini CRM") as demo:  # starts building the whole web page and calls it demo
    gr.HTML(render_topbar)  # puts the top bar at the top of the page

    with gr.Row(equal_height=False):  # arranges the next things side by side in a row
        # Left rail — the form
        with gr.Column(scale=1, min_width=300, elem_classes="crm-panel"):  # makes the narrow left column for the form
            gr.HTML(  # puts a small heading and note at the top of the form
                '<h2 class="crm-panel-title">New contact</h2>'
                '<p class="crm-panel-kicker">Saving an existing name updates that contact.</p>'
            )
            name = gr.Textbox(label="Name", placeholder="Priya Raman")  # adds the Name text box
            phone = gr.Textbox(label="Phone", placeholder="98400 12345")  # adds the Phone text box
            email = gr.Textbox(label="Email", placeholder="priya@example.com")  # adds the Email text box
            save_btn = gr.Button("Save contact", elem_id="crm-save")  # adds the Save button
            status = gr.HTML()  # adds an empty spot where the status message will appear

            gr.HTML('<hr class="crm-divider"><h2 class="crm-panel-title">Remove a contact</h2>')  # adds a divider and the "Remove a contact" heading
            picker = gr.Dropdown(choices=[], show_label=False, container=False)  # adds the drop-down menu for choosing who to remove
            remove_btn = gr.Button("Remove selected", elem_id="crm-remove")  # adds the Remove button

        # Main — the directory
        with gr.Column(scale=3, elem_classes="crm-main"):  # makes the wider right column for the contact list
            search = gr.Textbox(  # adds the search box across the top of the list
                show_label=False, container=False, elem_id="crm-search",
                placeholder="Search by name, phone, email, or company…",
            )
            stats = gr.HTML(render_stats)  # adds the three summary tiles
            grid = gr.HTML(render_grid)  # adds the grid of contact cards

    # Wiring: which function runs, what goes in, what comes out
    save_btn.click(on_save, [name, phone, email, search], [status, grid, stats, picker, name, phone, email])  # runs on_save when Save is clicked
    remove_btn.click(on_remove, [picker, search], [status, grid, stats, picker])  # runs on_remove when Remove is clicked
    search.change(on_search, [search], [grid])  # runs on_search whenever the search text changes
    demo.load(on_load, [search], [grid, stats, picker])  # runs on_load once when the page first opens

if __name__ == "__main__":  # only runs the next line when this file is started directly
    demo.launch(theme=Soft(), css=CSS, head=HEAD, js=FORCE_LIGHT_JS)  # opens the web page in the browser


# ==========================================================================
# 🏋️  PRACTICE ACTIVITIES  —  small, SAFE tweaks to the frontend
# --------------------------------------------------------------------------
# You do NOT need to understand all the CSS to do these. Change the code,
# then re-run:  python app.py   and refresh the browser.
#
# 1. In render_topbar(), change the wordmark text "Contact Book" to your own
#    app name, then reload the page.
# 2. In the CSS, find  --crm-accent: #FFE600;  and change it to another
#    colour (e.g. #00B4D8). Notice every highlight updates at once.
# 3. Change the three placeholders in the "New contact" form (name / phone /
#    email) to your own example values.
# 4. In render_stats(), add a FOURTH stat tile that shows how many contacts
#    have an email address (hint: count contacts where c.get("email")).
# 5. THINK: to add an "Edit contact" button, which backend function would
#    you need in contacts.py?  (Hint: that's activity 1 in contacts.py.)
# ==========================================================================
