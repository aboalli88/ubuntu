---
name: omniroute-run
description: Set up and run the OmniRoute server locally (install deps, generate .env secrets, start dev/prod). Use when the user asks to run, start, launch, or test the OmniRoute app/server in this repo.
---

# Running OmniRoute locally

OmniRoute is a Next.js 16 app (App Router, `src/app/`) that runs as a
single-process AI router. Default port: `20128`.

## 1. First-time setup

```bash
# Install dependencies (also runs postinstall + husky prepare)
npm install

# Create .env from the contract and fill in required secrets
cp .env.example .env
sed -i "s|^JWT_SECRET=.*|JWT_SECRET=$(openssl rand -base64 48)|" .env
sed -i "s|^API_KEY_SECRET=.*|API_KEY_SECRET=$(openssl rand -hex 32)|" .env
sed -i "s|^STORAGE_ENCRYPTION_KEY=.*|STORAGE_ENCRYPTION_KEY=$(openssl rand -hex 32)|" .env
sed -i "s|^INITIAL_PASSWORD=.*|INITIAL_PASSWORD=ChangeMe123!|" .env
sed -i "s|^NODE_ENV=.*|NODE_ENV=development|" .env
```

`.env` is gitignored — never commit it. `JWT_SECRET`, `API_KEY_SECRET`, and
`STORAGE_ENCRYPTION_KEY` are required or the app will refuse to start.

## 2. Known gotcha: stray root `app/` directory

`scripts/postinstall.mjs` used to unconditionally create a root-level
`app/node_modules/@swc/helpers` directory. Because Next.js's App Router
prefers a root `app/` over `src/app/` when both exist, that stray folder
shadowed the real app and made every route 404. This is fixed (the
postinstall step now only touches `app/` if it already exists, i.e. the
published package's bundled standalone build). If you ever see every
route 404 in dev, check for a root-level `app/` directory that only
contains `node_modules` and move it aside — it isn't part of the source.

## 3. Start the server

```bash
npm run dev     # dev server, hot reload, http://localhost:20128
npm run build   # production build (isolated)
npm run start   # run the production build
```

## 4. Verify it's up

```bash
curl -sL -o /dev/null -w "%{http_code}\n" http://localhost:20128/
# -> 200 (redirects / -> /dashboard -> /login when unauthenticated)
```

Log in with the admin password from `INITIAL_PASSWORD` in `.env`.

## 5. Stopping it

Find and kill the `node scripts/run-next.mjs` process (or the job you
started it as), e.g. `pkill -f "run-next.mjs"`.
