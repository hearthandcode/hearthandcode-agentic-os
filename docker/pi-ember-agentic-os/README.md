# Pi-Ember Agentic OS sandbox

This Compose surface is a dedicated, bounded Pi-Ember container that carries an inert copy of the package source for its guided installer.

It builds `pi-ember-agentic-os:local` from the existing `pi-codex-container:pi-ember-dev` image, adding Python 3 plus a read-only-in-practice copy of this package under `/opt/hearthandcode-agentic-os`. The running container deliberately has **no mounts or volumes at all**: no `pi-exocore-plugin-dev`, host home/profile/session, Docker socket, provider environment file, or external network.

## Persistent state

The named container `pi-ember-agentic-os` owns all mutable state in its writable container layer. It starts fresh with Pi-Ember only: no Agentic OS profile or skill is installed until the guided installer runs.

The package source is copied into the image at `/opt/hearthandcode-agentic-os`; it is not mounted from the host.

## Launcher

`~/.local/bin/pi-ember-agentic-os.sh` is the user-facing entry point.

```bash
pi-ember-agentic-os.sh start
pi-ember-agentic-os.sh reset --yes
pi-ember-agentic-os.sh guided-install
pi-ember-agentic-os.sh verify
pi-ember-agentic-os.sh shell
pi-ember-agentic-os.sh pi
pi-ember-agentic-os.sh profile pathfinder
pi-ember-agentic-os.sh status
```

`reset --yes` discards every file created inside the current container, rebuilds the image from the current package checkout, and starts a fresh Pi-Ember container. Use it before `guided-install` when the installer or its bundled sources have changed. `guided-install` opens the package's original ten-step installer inside the container. Choose Pi, then accept or customize the hub root and component selections. It copies profiles to Pi's user-agent location, copies skills to Pi's user-skill location, writes the scope configuration, and records an installation manifest entirely inside the container.

Pi automatically discovers skills from `/home/pi/.pi/agent/skills`, whose `SKILL.md` files have the standard `name` and `description` frontmatter. The `profile` command makes an installed profile Pi's explicit `--system-prompt`; this provides a direct main-session profile mode without installing any unrelated Pi extension. The profile markdown remains compatible with Pi-Ember's documented user-agent directory for subagent extensions.

## Verification

`verify` executes both the source verifier and an in-container verifier. The latter checks all 8 profiles and 16 skill directories against the source hashes, validates Pi-facing frontmatter, checks the manifest and isolated hub scope, and confirms that an outbound socket cannot be opened.

## Rollback

To remove the **dedicated container state only**, run:

```bash
pi-ember-agentic-os.sh destroy --yes
```

This removes only the named `pi-ember-agentic-os` container and its writable layer. It does not touch the image, package source checkout, existing Pi containers, Pi-Exocore development state, host Pi state, provider credentials, or any host volume.
