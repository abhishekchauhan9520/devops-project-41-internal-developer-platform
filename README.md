# Project 41 — Internal Developer Platform

A production-oriented Internal Developer Platform (IDP) blueprint built around Backstage concepts: Software Catalog, Software Templates/Scaffolder, and TechDocs.

## Platform model

```text
Developer
   |
   v
Backstage Portal
   |
   +--> Software Catalog
   +--> Golden Path Templates
   +--> TechDocs
   +--> Ownership / metadata
   +--> CI/CD links
   +--> Kubernetes / runtime links
   |
   v
GitHub Repository
   |
   +--> CI
   +--> Container
   +--> Kubernetes manifests
   +--> catalog-info.yaml
   +--> TechDocs
```

## Golden paths

- Python API service
- Node.js API service
- Static web service

Every generated service contains:

- `catalog-info.yaml`
- `mkdocs.yml`
- `docs/index.md`
- Dockerfile
- Kubernetes Deployment/Service
- health probes
- non-root runtime defaults
- CI workflow
- ownership metadata

## Backstage integration

The `backstage/` directory contains configuration examples and the three Scaffolder templates consumed by a Backstage instance.

The repository also includes a dependency-free local `platform-cli` so the golden paths can be validated and rendered without standing up Backstage.

## Local quick start

```bash
python platform-cli/cli.py validate-catalog
python platform-cli/cli.py validate-templates
python platform-cli/cli.py render --template python-api --name orders-api --owner group:platform
```

The generated output is written under `.generated/` and is ignored by Git.

## Industry patterns represented

Backstage's current Software Catalog centralizes ownership and metadata; Software Templates create standardized components; TechDocs keeps documentation next to code. citeturn885838search3turn885838search5turn885838search2

## Production evolution

- Replace local catalog ownership with your GitHub/enterprise identity provider.
- Use GitHub App/OIDC credentials instead of long-lived tokens.
- Publish TechDocs to external object storage from CI for scale.
- Add policy checks before template publication.
- Add Kubernetes, Argo CD, cost, security, and observability plugins.
- Add platform SLOs and developer-experience metrics.

## License

MIT
