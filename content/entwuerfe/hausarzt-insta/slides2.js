const { chromium } = require('playwright');
const order=['1a','2','3','4','4a','4b','5','6','7','8','9'];
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome'});
for(let i=0;i<order.length;i++){const p=await b.newPage({viewport:{width:1080,height:1350}});await p.goto(`file:///tmp/claude-0/shots/slides.html#${order[i]}_${i+1}_${order.length}`);await p.waitForTimeout(1200);await p.screenshot({path:`/tmp/claude-0/shots/k-${String(i+1).padStart(2,'0')}.jpg`,type:'jpeg',quality:86});await p.close();}
for(const v of ['1b','1c']){const p=await b.newPage({viewport:{width:1080,height:1350}});await p.goto(`file:///tmp/claude-0/shots/slides.html#${v}_1_11`);await p.waitForTimeout(1200);await p.screenshot({path:`/tmp/claude-0/shots/slide-${v}.jpg`,type:'jpeg',quality:88});await p.close();}
await b.close();})();
