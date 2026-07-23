with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Ensure standard section IDs are present for the navigation anchors
sections = ["dashboard", "marketplace", "console", "affiliates"]
for sec in sections:
    if f'id="{sec}"' not in html:
        # Inject the id into the corresponding header or section tag if found
        name = sec.capitalize()
        if name in html:
            # Replace first instance of tag containing the name
            html = html.replace(f'<{sec}', f'<{sec} id="{sec}"', 1)

# Add a lightweight script to handle smooth switching/scrolling if missing
if "script" not in html or "smooth" not in html:
    nav_script = """
    <script>
    document.addEventListener("DOMContentLoaded", () => {
        const links = document.querySelectorAll('header a, nav a, .nav-links a');
        links.forEach(link => {
            link.addEventListener('click', (e) => {
                const targetId = link.getAttribute('href');
                if (targetId && targetId.startsWith('#')) {
                    e.preventDefault();
                    const targetEl = document.querySelector(targetId);
                    if (targetEl) {
                        targetEl.scrollIntoView({ behavior: 'smooth' });
                    }
                }
            });
        });
    });
    </script>
    """
    html = html.replace("</body>", f"{nav_script}</body>")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Navigation successfully patched!")
