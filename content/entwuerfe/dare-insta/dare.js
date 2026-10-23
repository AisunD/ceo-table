const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium-1194/chrome-linux/chrome'});
for(let i=1;i<=9;i++){const p=await b.newPage({viewport:{width:1080,height:1350}});await p.goto(`file:///tmp/claude-0/shots/dare.html#${i}_${i}_9`);await p.waitForTimeout(1200);await p.screenshot({path:`/tmp/claude-0/shots/d-0${i}.jpg`,type:'jpeg',quality:86});await p.close();}
await b.close();})();
