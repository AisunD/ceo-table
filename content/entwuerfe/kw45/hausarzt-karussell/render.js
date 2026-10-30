// Rendert alle Slides. Aufruf: node render.js <ordner-mit-html>
const { chromium } = require('playwright');
const dir = process.argv[2];
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome'});
const jobs=[...Array(10)].map((_,i)=>[String(i+1),i+1,`Hausarzt-Kuechentisch-${String(i+1).padStart(2,'0')}.jpg`]);
jobs.push(['5o',5,'Hausarzt-Kuechentisch-Slide-05-ohne-zitate.jpg']);
for(const [k,n,f] of jobs){const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto(`file://${dir}/kuechentisch.html#${k}_${n}_10`);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(1500);
await p.screenshot({path:`${dir}/zum-posten/${f}`,type:'jpeg',quality:90});await p.close();}
await b.close();})();
