# GitHub Profile Setup & Automation Guide

## Architecture Overview
This profile uses a combination of static assets and dynamic GitHub Actions to provide a comprehensive view of a developer's activity, impact, and persona.
- **Frontend**: README.md powered by raw HTML (primarily tables for grid layouts) and dynamic SVGs.
- **Backend/Automation**: GitHub Actions workflows running on schedules (cron) to fetch data from APIs (GitHub, WakaTime, Dev.to) and inject it into README.md or generate new SVG assets.

## GitHub Actions Workflows
1. **Activity Feed** (`activity.yml`): Updates the README with recent GitHub activity.
2. **Profile 3D Contrib** (`profile-3d.yml`): Generates a 3D commit graph.
3. **Metrics** (`metrics.yml`): Uses `lowlighter/metrics` to generate a comprehensive GitHub stats dashboard (`github-metrics.svg`).
4. **Snake Animation** (`snake.yml`): Uses `Platane/snk` to generate a snake game from the contribution graph, saving it to the `output` branch.
5. **WakaTime Sync** (`waka.yml`): Injects WakaTime coding stats into the `<!--START_SECTION:waka-->` block in the README.
6. **Blog Sync** (`blog.yml`): Fetches the latest Dev.to posts and injects them into the `<!-- BLOG-POST-LIST:START -->` block.

## Secrets List
To enable all automations, the following Repository Secrets must be configured under **Settings > Secrets and variables > Actions**:

- `GITHUB_TOKEN`: Automatically provided by GitHub Actions (ensure "Read and write permissions" are enabled in **Settings > Actions > General > Workflow permissions**).
- `METRICS_TOKEN`: A Personal Access Token (PAT) with `repo` and `read:user` scopes required by `lowlighter/metrics`.
- `WAKATIME_API_KEY`: Your API key from WakaTime (Settings > Account > Secret API Key).

## Maintenance Guide
- **Pinned Dependencies**: All GitHub Actions workflows use pinned commit SHAs rather than mutable tags (like `@v3` or `@master`) to ensure supply-chain security. To update an action, fetch the latest commit SHA and replace the old one.
- **Rate Limits**: If widgets hosted on external APIs (like LeetCode or Holopin) fail to load, consider removing them or deploying your own instance to bypass rate limits.
- **HTML/CSS Formatting**: GitHub Flavored Markdown restricts inline CSS (`style="..."`). Always use HTML tables and `bgcolor` attributes for custom layouts.
