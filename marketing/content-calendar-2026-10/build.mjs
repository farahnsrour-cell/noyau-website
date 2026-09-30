// Builds index.html (the interactive calendar) and CALENDAR.md (the readable version)
// from calendar-data.mjs and template.html. Run: node build.mjs
import { readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import * as data from "./calendar-data.mjs";

const here = dirname(fileURLToPath(import.meta.url));
const D = { ...data };

// ---------- index.html ----------
const template = readFileSync(join(here, "template.html"), "utf8");
const json = JSON.stringify(D).replace(/<\/script/gi, "<\\/script");
if (!template.includes("/*__DATA__*/{}")) throw new Error("template marker missing");
writeFileSync(join(here, "index.html"), template.replace("/*__DATA__*/{}", json));

// ---------- CALENDAR.md ----------
const DOW = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
const MON = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
const d = s => { const [y, m, dd] = s.split("-").map(Number); return new Date(Date.UTC(y, m - 1, dd)); };
const iso = dt => dt.toISOString().slice(0, 10);
const long = s => { const dt = d(s); return `${DOW[(dt.getUTCDay() + 6) % 7]} ${dt.getUTCDate()} ${MON[dt.getUTCMonth()]}`; };
const short = s => { const dt = d(s); return `${DOW[(dt.getUTCDay() + 6) % 7].slice(0, 3)} ${dt.getUTCDate()} ${MON[dt.getUTCMonth()].slice(0, 3)}`; };
const esc = s => String(s).replace(/\|/g, "\\|");

const L = [];
const p = (...x) => L.push(...x, "");

p(`# ${D.meta.title}`, `Instagram ${D.meta.handle} · ${D.meta.range} · times in ${D.meta.timezone} · updated ${D.meta.updated}`);
p(D.meta.summary);
p("The interactive version of this calendar (month grid, per-post briefs, shared status tracker) is built from the same data as this file. Open `index.html`, or the published artifact.");

const counts = {};
D.formats.forEach(f => counts[f.key] = D.posts.filter(x => x.format === f.key).length);
p("## At a glance", `| Feed posts | Reels | Carousels | Statics | Creator Collab reels | Days with stories |`, `|---|---|---|---|---|---|`, `| ${D.posts.length} | ${counts.Reel} | ${counts.Carousel} | ${counts.Static} | ${counts["Collab reel"]} | ${Object.keys(D.stories).length} |`);

p("## Four priorities");
D.priorities.forEach(pr => {
  const ids = D.posts.filter(x => x.priority.includes(pr.key)).map(x => x.id).join(", ");
  p(`### ${pr.name}`, pr.how, `Posts: ${ids}`);
});

p("## Phases", `| Phase | Dates | Feed posts | Goal |`, `|---|---|---|---|`);
D.phases.forEach(ph => L.push(`| ${ph.n} · ${ph.name} | ${ph.dates} | ${D.posts.filter(x => x.phase === ph.n).length} | ${esc(ph.goal)} |`));
L.push("");

p("## Content pillars", `| Pillar | What it is |`, `|---|---|`);
D.pillars.forEach(pl => L.push(`| ${pl.key} | ${esc(pl.what)} |`));
L.push("");
p("## Formats", `| Format | Mark | Note |`, `|---|---|---|`);
D.formats.forEach(f => L.push(`| ${f.key} | ${f.mark} | ${esc(f.note)} |`));
L.push("");

// month table
p("## The month at a glance", `| Date | Feed | Stories |`, `|---|---|---|`);
const byDate = {};
D.posts.forEach(x => (byDate[x.date] ||= []).push(x));
for (let cur = d(D.meta.start); cur <= d(D.meta.end); cur.setUTCDate(cur.getUTCDate() + 1)) {
  const k = iso(cur);
  const feed = (byDate[k] || []).map(x => `${x.id} ${x.time} · ${x.format} · ${x.title}`).join("<br>") || "—";
  const st = D.stories[k] ? `${D.stories[k].length} frames` : "—";
  L.push(`| ${short(k)}${k === D.meta.launch ? " · Launch" : ""} | ${esc(feed)} | ${st} |`);
}
L.push("");

// full briefs
p("## Every post, in full");
D.phases.forEach(ph => {
  p(`### Phase ${ph.n} · ${ph.name} · ${ph.dates}`, ph.goal);
  for (let cur = d(ph.start); cur <= d(ph.end); cur.setUTCDate(cur.getUTCDate() + 1)) {
    const k = iso(cur);
    const posts = byDate[k] || [];
    if (!posts.length && !D.stories[k]) continue;
    p(`#### ${long(k)}${k === D.meta.launch ? " · Launch day" : ""}`);
    posts.forEach(x => {
      p(`**${x.id} · ${x.time} · ${x.format} · ${x.title}**`,
        `- Pillar: ${x.pillar} · Serves: ${x.priority.join(", ")} · Effort: ${x.effort}${x.flex ? " · Flex (may slip to stories)" : ""} · Status: ${x.status}`,
        `- Hook: ${x.hook}`,
        `- Brief: ${x.brief}`,
        `- Asset: ${x.asset}`,
        `- Caption: ${x.caption}`,
        `- Call to order: ${x.cta}`,
        `- Notes: ${x.notes}`);
    });
    if (D.stories[k]) p(`Stories${posts.length ? "" : " only"}:`, ...D.stories[k].map(s => `- ${s}`));
  }
});

p("## Stories playbook", "Daily:", ...D.storiesPlaybook.daily.map(s => `- ${s}`));
p("Weekly fixtures:", `| Day | Fixture | What |`, `|---|---|---|`);
D.storiesPlaybook.weekly.forEach(w => L.push(`| ${w.day} | ${w.name} | ${esc(w.what)} |`));
L.push("");
p("Highlights to build: " + D.storiesPlaybook.highlights.join(" · "));
p("Rules:", ...D.storiesPlaybook.rules.map(s => `- ${s}`));

p("## Creator collaborations", "Principles:", ...D.creators.principles.map(s => `- ${s}`));
D.creators.waves.forEach(w => p(`### ${w.name}`, `| When | What |`, `|---|---|`, ...w.steps.map(s => `| ${s.when} | ${esc(s.what)} |`)));
p("The brief, in five lines:", ...D.creators.brief.map(s => `- ${s}`));

p("## Spas, clinics and salons", `| When | What |`, `|---|---|`, ...D.wholesale.map(s => `| ${s.when} | ${esc(s.what)} |`));

p("## Voice and claims", "Rules:", ...D.voice.rules.map(s => `- ${s}`));
p("Allowed: " + D.voice.allowed.join(" · "));
p("Avoided: " + D.voice.avoid.join(" · "));
p("Claims to hold back:", ...D.voice.claims.map(s => `- ${s}`));

p("## Timing, cadence and hashtags", `All times are ${D.meta.timezone}.`, `| Slot | Time | Why |`, `|---|---|---|`, ...D.timing.slots.map(s => `| ${s.slot} | ${s.time} | ${esc(s.why)} |`));
p("Cadence:", ...D.timing.cadence.map(s => `- ${s}`));
p("House hashtags: " + D.timing.hashtags.house.join(" "), "Rotating: " + D.timing.hashtags.rotate.join(" "), D.timing.hashtags.rule);
p("Search terms for the first two lines: " + D.timing.keywords.join(", "));

p("## Measurement", D.measurement.weekly, `| Priority | Metric | Where | Working target |`, `|---|---|---|---|`, ...D.measurement.metrics.map(m => `| ${m.priority} | ${esc(m.metric)} | ${esc(m.where)} | ${esc(m.target)} |`));

p("## Pre-flight checklist", ...D.checklist.map(s => `- [ ] ${s}`));

p("## Dependencies and open items", `| Item | Needed | Who |`, `|---|---|---|`, ...D.dependencies.map(x => `| ${esc(x.item)} | ${x.needed} | ${x.who} |`));

p("With care, Noyau");
writeFileSync(join(here, "CALENDAR.md"), L.join("\n"));

// sanity
const ids = new Set();
for (const x of D.posts) {
  if (ids.has(x.id)) throw new Error("duplicate id " + x.id);
  ids.add(x.id);
  if (!D.pillars.find(pl => pl.key === x.pillar)) throw new Error(`${x.id}: unknown pillar ${x.pillar}`);
  if (!D.formats.find(f => f.key === x.format)) throw new Error(`${x.id}: unknown format ${x.format}`);
  for (const pr of x.priority) if (!D.priorities.find(q => q.key === pr)) throw new Error(`${x.id}: unknown priority ${pr}`);
  const text = [x.title, x.hook, x.brief, x.asset, x.caption, x.cta, x.notes].join(" ");
  if (/!/.test(text)) throw new Error(`${x.id}: exclamation mark`);
}
for (const [k, frames] of Object.entries(D.stories)) { if (/!/.test(frames.join(" "))) throw new Error(`stories ${k}: exclamation mark`); }
console.log(`built index.html and CALENDAR.md: ${D.posts.length} posts, ${Object.keys(D.stories).length} story days`);
