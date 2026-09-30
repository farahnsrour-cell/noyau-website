# Noyau · Instagram content calendar · 25 September – 31 October 2026

Tracker item d10 in the Noyau Document Plan.

Interactive version: https://claude.ai/artifact/YN6e6k4XqpuLAzEbVDoZ6i

| File | What it is |
|---|---|
| `calendar-data.mjs` | The single source: every post, the stories for every day, the creator programme, wholesale steps, voice rules, timing, measurement, checklist and dependencies. Edit this file. |
| `template.html` | The interactive page's markup, styles and script, with a `/*__DATA__*/` marker where the data is injected. |
| `build.mjs` | Builds `index.html` and `CALENDAR.md` from the two files above, and fails if a post uses an unknown pillar, format or priority, or contains an exclamation mark. |
| `index.html` | The interactive calendar (month grid, list view, filters, per-post drawer with caption copy, shared status tracker). Published as a claude.ai artifact. |
| `CALENDAR.md` | The same calendar as a readable document. |

Rebuild after editing the data or the template:

```
node build.mjs
```

The status of each post (planned, drafted, scheduled, published) is stored in the published artifact's database, collection `status`, one document per post id, shaped `{s, at}`. Only the artifact's owner and editors can change it.
