## 2026-06-07 - Hide Decorative Images for Accessibility
**Learning:** In GitHub Readmes, purely decorative images (like dividers or animations) should be hidden from screen readers. Using `alt=""` along with `aria-hidden="true"` prevents screen readers from announcing unnecessary noise to users.
**Action:** Always check if an image adds semantic value. If it's just for visual flair, hide it using `alt="" aria-hidden="true`.
