## 2026-06-07 - Tables as Layout in GitHub Profiles
**Learning:** Because GitHub Markdown lacks flexbox/grid support, developers frequently use HTML `<table>` elements to create multi-column layouts for badges, stats, and text. Screen readers interpret these as complex data tables, causing significant auditory noise and confusion.
**Action:** When reviewing GitHub profile READMEs or similar markdown files that heavily mix HTML for layout, always check for `<table>` elements and add `role="presentation"` to them. Also, remember to set `alt=""` and `aria-hidden="true"` on decorative dividing lines.
## 2025-02-13 - Layout Table Accessibility in Markdown
**Learning:** When using HTML `<table>` elements purely for visual layout (like side-by-side columns) in a GitHub README, screen readers will incorrectly announce them as tabular data.
**Action:** Always add `role="presentation"` to layout tables to ensure they are read linearly and accessible to screen reader users.
