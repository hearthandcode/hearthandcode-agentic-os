# Pi-Ember plus the inert Agentic OS installer source.
# Profiles and skills are not installed into Pi until guided-install runs.
ARG PI_EMBER_BASE_IMAGE=pi-codex-container:pi-ember-dev
FROM ${PI_EMBER_BASE_IMAGE}

USER root
RUN apt-get update \
    && apt-get install -y --no-install-recommends python3 \
    && chown -R 10001:10001 /home/pi \
    && rm -rf /var/lib/apt/lists/*

COPY --chown=10001:10001 . /opt/hearthandcode-agentic-os
RUN chmod -R a-w /opt/hearthandcode-agentic-os

USER 10001:10001
WORKDIR /home/pi
