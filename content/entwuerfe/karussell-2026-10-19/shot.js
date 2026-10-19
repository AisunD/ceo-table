const {chromium}=require('/opt/node-tools/node_modules/playwright');
(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1350}});
await p.goto('file://'+__dirname+'/slides.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(1500);
console.log(await p.evaluate(()=>[...document.fonts].filter(f=>f.status=='loaded').map(f=>f.family).join(',')));
for(let i=1;i<=8;i++){await (await p.$('#s'+i)).screenshot({path:`slide-${i}.png`});
 console.log(i,await p.evaluate(i=>{const e=document.getElementById('s'+i);return [...e.querySelectorAll('*')].some(c=>c.getBoundingClientRect().bottom>e.getBoundingClientRect().bottom+1)},i));}
await b.close()})();
