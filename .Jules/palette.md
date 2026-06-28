## 2026-06-07 - Tables as Layout in GitHub Profiles
**Learning:** Because GitHub Markdown lacks flexbox/grid support, developers frequently use HTML `<table>` elements to create multi-column layouts for badges, stats, and text. Screen readers interpret these as complex data tables, causing significant auditory noise and confusion.
**Action:** When reviewing GitHub profile READMEs or similar markdown files that heavily mix HTML for layout, always check for `<table>` elements and add `role="presentation"` to them. Also, remember to set `alt=""` and `aria-hidden="true"` on decorative dividing lines.
## 2024-05-19 - Layout Tables in Markdown Profiles
**Learning:** Using HTML `<table>` elements purely for visual layout in markdown (like project grids or multi-column sections) causes screen readers to incorrectly announce them as tabular data. This is a common accessibility trap in GitHub profile READMEs that use tables for complex layouts.
**Action:** Always add `role="presentation"` to `<table>` elements that are used solely for visual presentation/layout to ensure screen readers ignore the table semantics and just read the content naturally.
