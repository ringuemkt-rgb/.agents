# BDC Runtime v7.1

## Commands

```bash
npm install
npm run typecheck
npm test
npm run validate
npm run build:fixture
```

Compile a plan:

```bash
npx tsx src/cli.ts compile examples/biomechanics-jab.plan.json dist/output
```

Output:
- one autonomous 25-block Markdown prompt per slide;
- caption-prompt.md;
- build-manifest.json with SHA-256 content hash.

## Production model

Research/evidence can be performed interactively by ChatGPT or an external provider through the forensic AI interface.
The deterministic runtime owns validation, canonical locks, prompt compilation, risk routing, SVG charts/text layers, provenance, metrics and tests.
