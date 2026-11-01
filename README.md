# Fadi Calculator 2.1
Installable mobile web calculator with an expression display, four operations, keyboard support and offline caching. The web edition uses JavaScript (12 significant digits); it is for everyday calculations, not financial precision. Operations are evaluated sequentially, like a basic calculator.

## Publish on GitHub
1. Create a repository named `fadi-calculator`. Public repositories expose all uploaded source files.
2. Extract this ZIP on your computer. Open the extracted folder containing `index.html`.
3. On the repository page select **Add file > Upload files**. Upload the contents of that folder, including the `windows` folder. Do not upload the ZIP itself or an extra enclosing folder. Commit changes.
4. Open **Settings > Pages**. Under Source choose **Deploy from a branch**; choose **main** and **/(root)**; click Save.
5. Wait for deployment and open the site link displayed by GitHub Pages.

## Install on Samsung
1. Open the published HTTPS site in Chrome while online.
2. Open Chrome's three-dot menu and select **Add to home screen > Install** (wording may vary).
3. Launch the new icon. After the first successful online load and cache setup, test in airplane mode.

This is an installable PWA, not an APK or Play Store listing. Opening a local HTML file is a preview only; installation and offline caching require HTTPS hosting (or localhost).

## Original Windows edition
The `windows` folder preserves the original Python desktop source, HTML, icon and build script. It is independent of the mobile edition. GitHub Pages serves the web edition without running Python.

## Sources
- https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
- https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Making_PWAs_installable
- https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Installing
