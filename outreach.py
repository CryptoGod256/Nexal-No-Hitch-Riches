def format_email(client_name, niche, proposal_text):
    """Formats the raw proposal into a high-converting email."""
    email_body = f"""
    Subject: Quick Proposal: Boosting {niche} for {client_name}
    
    Hi {client_name},
    
    I've been analyzing your market presence and identified a specific automation gap:
    
    {proposal_text}
    
    I specialize in closing this exact gap. Are you open to a 5-minute audit?
    
    Best,
    NEXAL Intelligence
    """
    return email_body

# Save this to the outreach folder
def save_outreach(email_content, client_name):
    filename = f"outreach_{client_name.replace(' ', '_')}.txt"
    with open(f"web/outreach/{filename}", "w") as f:
        f.write(email_content)
