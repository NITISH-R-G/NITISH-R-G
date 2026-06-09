## 2026-06-07 - Tables as Layout in GitHub Profiles
**Learning:** Because GitHub Markdown lacks flexbox/grid support, developers frequently use HTML `<table>` elements to create multi-column layouts for badges, stats, and text. Screen readers interpret these as complex data tables, causing significant auditory noise and confusion.
**Action:** When reviewing GitHub profile READMEs or similar markdown files that heavily mix HTML for layout, always check for `<table>` elements and add `role="presentation"` to them. Also, remember to set `alt=""` and `aria-hidden="true"` on decorative dividing lines.

## 2026-06-09 - Accessibility in Dynamic SVG Banners
**Learning:** Tools like `readme-typing-svg` pass parameters via the URL which result in dynamic text content visually, but this content is completely inaccessible to screen readers unless the `alt` tag explicitly duplicates the URL-encoded text parameters. Users default to generic `alt="Typing SVG"`, hiding critical intro context.
**Action:** When reviewing auto-generated profile widgets or SVGs that accept text parameters via query strings, explicitly extract those parameters and inject them into the `alt` tag of the parent `<img>`.
