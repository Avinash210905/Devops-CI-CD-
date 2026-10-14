# Shipshape: CI/CD with GitHub Actions and GitHub Pages

A small static website used to learn the path from a Git push to a deployed page.

## Project files

- `index.html` — the website.
- `build.py` — copies the publishable site into `dist/`.
- `tests/test_site.py` — checks the page structure and build output.
- `.github/workflows/ci-cd.yml` — builds and tests pull requests and pushes to `main`, then deploys successful non-PR runs to GitHub Pages.

## Run locally

Requires Python 3. Run these commands from the project directory:

```sh
python build.py
python -m unittest discover -s tests -v
```

Open `index.html` in a browser to view the page. The generated Pages-ready files are in `dist/`.

## Publish with GitHub Pages

1. Create a GitHub repository and push this project to its `main` branch.
2. In the repository, open **Settings → Pages** and set **Build and deployment → Source** to **GitHub Actions**.
3. Open the **Actions** tab and wait for **Build, test, and deploy to GitHub Pages** to finish.
4. Open **Settings → Pages** to find the published site URL.

Pull requests run the build and tests. Successful pushes to `main` (and manual runs started from the Actions tab) also deploy to Pages.
