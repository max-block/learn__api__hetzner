set dotenv-load := false

get_reset_status:
    python -m app.get_reset_status

get_firewall:
    python -m app.get_firewall

on_firewall:
    python -m app.on_firewall

off_firewall:
    python -m app.off_firewall