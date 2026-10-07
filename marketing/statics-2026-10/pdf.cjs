(async () => {
const { chromium } = require("playwright"); const fs = require("fs"); const path = require("path");
const b = await chromium.launch({ executablePath: "/opt/pw-browsers/chromium" }).catch(async () => chromium.launch());
const ctx = await b.newContext({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 2 });
const page = await ctx.newPage();
const names = ["S1","S2","S3","S4","S5","S6","S7","S8","I1","I2"];
// one combined document for the PDF: each static as a page
let html = fs.readFileSync("html/S1.html","utf8").split("<body>")[0] + "<body>";
for (const n of names) { const body = fs.readFileSync("html/"+n+".html","utf8").split("<body>")[1].split("</body>")[0]; html += `<div style="page-break-after:always;width:1080px;height:1350px;overflow:hidden">${body}</div>`; }
html += "</body></html>";
fs.writeFileSync("html/all.html", html.replace(/body\{margin:0;width:1080px;height:1350px;overflow:hidden;/, "body{margin:0;width:1080px;"));
await page.goto("file://" + path.resolve("html/all.html"), { waitUntil: "load" });
await page.evaluate(() => document.fonts.ready); await page.waitForTimeout(300);
await page.pdf({ path: "final/noyau-statics-october.pdf", width: "1080px", height: "1350px", printBackground: true, margin: {top:0,right:0,bottom:0,left:0}, preferCSSPageSize: false });
fs.unlinkSync("html/all.html");
await b.close(); console.log("pdf ok");
})();
