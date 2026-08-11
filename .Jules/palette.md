## 2026-06-07 - Tables as Layout in GitHub Profiles
**Learning:** Because GitHub Markdown lacks flexbox/grid support, developers frequently use HTML `<table>` elements to create multi-column layouts for badges, stats, and text. Screen readers interpret these as complex data tables, causing significant auditory noise and confusion.
**Action:** When reviewing GitHub profile READMEs or similar markdown files that heavily mix HTML for layout, always check for `<table>` elements and add `role="presentation"` to them. Also, remember to set `alt=""` and `aria-hidden="true"` on decorative dividing lines.
## 2024-05-19 - Adding Accessible Multi-Column Layouts in Markdown
**Learning:** Purely visual `<table>` elements used for multi-column layouts in markdown files (like profile READMEs) can be read as tabular data by screen readers, creating a confusing experience.
**Action:** Always add `role="presentation"` to `<table>` elements that are used purely for layout/presentation purposes to prevent screen readers from announcing them as data tables.
