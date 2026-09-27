# Domain Collector with Selenium

A small Selenium automation project (2024) that collects recently deleted `.com` domains and estimates their value.

## How it works

The code lives in `MoneyHunter/` and runs in two steps:

1. **`main.py`** logs in to [expireddomains.net](https://www.expireddomains.net/) and opens the *Deleted .com* list. It applies filters: no hyphens, letters only, at most 3 words, at most 20 characters, dropped in the last 24 hours, and matching a keyword list (tech, shop, travel, finance…). It then walks through every result page and saves the domain names to `domain_names_YYYY-MM-DD.txt`.
2. **`valueChecker.py`** looks up each collected domain on [pc.domains](https://pc.domains) to get an estimated price. It keeps domains valued above $170 and writes them, sorted by price, to `domain_values_YYYY-MM-DD.txt`.

`sort.py` is a small helper that prints a values file sorted by price.

## Setup

```bash
pip install -r requirements.txt
```

`main.py` reads your expireddomains.net credentials from environment variables:

```bash
export EXPIRED_DOMAINS_USER="your-username"
export EXPIRED_DOMAINS_PASSWORD="your-password"
```

Run the steps from inside `MoneyHunter/`:

```bash
python main.py
python valueChecker.py
```

## Notes

- The scripts locate page elements with absolute XPaths, so they break whenever either site changes its layout. This project is archived and has not been updated for the current version of those sites.
- Automated appraisals are rough estimates. In practice they were a poor predictor of what a domain actually sells for.
