(async () => {
const { chromium } = require("playwright"); const fs = require("fs"); const path = require("path");
const b = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium" }).catch(async () => chromium.launch());
const ctx = await b.newContext({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 2 });
const page = await ctx.newPage();
fs.mkdirSync("out2x", { recursive: true });
for (const f of fs.readdirSync("html").filter(x => x.endsWith(".html")).sort()) {
  await page.goto("file://" + path.resolve("html", f), { waitUntil: "load" });
  await page.evaluate(() => document.fonts.ready); await page.waitForTimeout(250);
  await page.screenshot({ path: "out2x/" + f.replace(".html", ".png") });
  console.log("rendered", f);
}
await b.close();
})();
