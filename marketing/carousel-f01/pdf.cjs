(async () => {
const { chromium } = require("playwright"); const fs = require("fs"); const path = require("path");
const b = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium" }).catch(async () => chromium.launch());
const page = await (await b.newContext({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 2 })).newPage();
let html = "<!doctype html><html><head><meta charset='utf-8'><style>body{margin:0}</style></head><body>";
for (const f of fs.readdirSync("out2x").filter(x => x.startsWith("F01-")).sort()) { const b64 = fs.readFileSync("out2x/"+f).toString("base64"); html += `<div style="page-break-after:always;width:1080px;height:1350px;overflow:hidden"><img src="data:image/png;base64,${b64}" style="display:block;width:1080px;height:1350px"></div>`; }
html += "</body></html>"; fs.writeFileSync("html/_all.html", html);
await page.goto("file://" + path.resolve("html/_all.html"), { waitUntil: "load" }); await page.waitForTimeout(300);
await page.pdf({ path: "final/F01-whats-inside.pdf", width: "1080px", height: "1350px", printBackground: true, margin: {top:0,right:0,bottom:0,left:0} });
fs.unlinkSync("html/_all.html"); await b.close(); console.log("pdf ok");
})();
