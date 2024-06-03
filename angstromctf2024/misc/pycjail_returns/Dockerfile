FROM pwn.red/jail

COPY --from=python:3.12-slim-bookworm / /srv
COPY chall.py /srv/app/run
COPY flag.txt /srv/app/flag.txt
RUN chmod 755 /srv/app/run

