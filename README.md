# Carnegie Analytics — Marketing Campaign Dashboard

Interactive Dash app that demonstrates how I design, ship, and communicate data products. The dashboard benchmarks multi‑channel marketing performance for Carnegie using clean, reusable components and a small, cached data layer.

## Summary
- Clear data story: KPIs, ROI, and funnel from impressions → enrollments.
- Product thinking: fast filters (campaign, region, platform), responsive layout, and sensible defaults.
- Engineering hygiene: modular Dash pages/components, caching, and reproducible env files (`environment.yml` or `requirements.txt`).

## Quick start
1) Clone the repo.
2) Create env (choose one):
   - Conda: `conda env create -f environment.yml` then `conda activate carnegie-app`
   - Pip: `python -m venv .venv && .venv\\Scripts\\activate && pip install -r requirements.txt`
3) Run: `python app.py`
4) Open: http://127.0.0.1:8050

## App tour
- Top nav: Home and Analytics.
- KPI cards: revenue, spend, ROI, enrollments, CPA.
- Filters: KPI selector + multi-select for campaign, region, platform.
- Visuals:
  - Performance by Campaign (stacked by platform)
  - Monthly trend line
  - Conversion funnel (impressions → enrollments)
- Caching: `Flask-Caching` backs common queries for snappy reloads.

## Data
- Source file: `data/marketing_campaign_data.xlsx`
  - Sheets used: `CampaignPerformance` (facts), `CampaignMeta`, `ChannelRates`.
- Columns include revenue, cost, impressions, clicks, leads, applications, enrollments, region, platform, campaign, date.
- Replace with live data by keeping headers consistent.

## Project structure
- `app.py` — Dash entrypoint, global navbar, cache config.
- `pages/home.py` — landing page.
- `pages/analytics.py` — main dashboard, callbacks, figures.
- `components/cards.py` — reusable KPI card factory.
- `components/dropdowns.py` — labeled dropdown builder.
- `utils/data_loader.py` — cached Excel readers.
- `utils/formatting.py` — human-friendly number formatting.
- `utils/caching.py` — cache instance.

## Tech stack
Dash 4, Plotly, pandas, Dash Bootstrap Components, Flask-Caching, Python 3.12.

## Future enhancements
- Export current view to CSV/PDF.
- Add campaign benchmarking vs. targets.
- CI check to validate data schema before deploy.
- Swap to Postgres/Parquet backend for larger volumes.

