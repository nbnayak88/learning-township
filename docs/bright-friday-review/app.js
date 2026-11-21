'use strict';
const CHECKOUT='https://hub.successlabsacademy.com/web/checkout/694af8798dd872a219700dd3';
const sectors=['Energy','Materials','Industrials','Consumer Discretionary','Consumer Staples','Health Care','Financials','Information Technology','Communication Services','Utilities','Real Estate'];
const $=id=>document.getElementById(id);const requested=new URLSearchParams(location.search);let data,domain=requested.get('domain')||'HR',streamId=requested.get('stream')||'',selected=null,busy=false;
let sectorContext=sectors.includes(requested.get('sector'))?requested.get('sector'):sectors[0];
const KEY='sla-bright-friday-review-v1';
function readBookings(){try{const x=JSON.parse(localStorage.getItem(KEY)||'[]');return Array.isArray(x)?x.filter(b=>b&&typeof b.seat==='string'&&typeof b.email==='string'&&typeof b.phone==='string'):[];}catch{return [];}}
let bookings=readBookings();
const normalizeEmail=s=>s.trim().toLowerCase();
const normalizePhone=s=>s.trim().replace(/[\s().-]/g,'');
async function digest(s){return Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256',new TextEncoder().encode(s)))).map(n=>n.toString(16).padStart(2,'0')).join('');}
function changeDomain(next){domain=next;streamId='';selected=null;render();}
function render(){
 $('industry-sector-options').replaceChildren(...sectors.map(name=>{const button=document.createElement('button');button.type='button';button.textContent=name;button.setAttribute('aria-pressed',String(name===sectorContext));button.onclick=()=>{sectorContext=name;render()};return button}));
 $('industry-sector-summary').textContent='Selected industry: '+sectorContext+' · applied across all 12 streams and 20 labs';
 if(!data.mappings[domain])domain='HR';
 const domainStreams=data.mappings[domain];if(streamId&&!domainStreams.some(s=>s.id===streamId))streamId='';
 const academy=data.academies.find(a=>a.id===domain),stream=domainStreams.find(s=>s.id===streamId);
 $('domain-select').replaceChildren(...data.academies.map(a=>new Option(a.name+' ('+a.id+')',a.id,false,a.id===domain)));
 $('stream-select').replaceChildren(new Option('All 12 streams · 240 seats','',false,!streamId),...domainStreams.map(s=>new Option(s.id+' · '+s.name,s.id,false,s.id===streamId)));
 const mapPath='assets/'+domain.toLowerCase()+'-mindmap.png?v=4';$('domain-mindmap').src=mapPath;$('domain-mindmap').alt=academy.name+' — full-resolution domain mind map';$('mindmap-link').href=mapPath;$('mindmap-full').href=mapPath;
 $('mindmap-title').textContent=academy.name+' · Mind map';$('mindmap-description').textContent='Explore all 12 workstreams. '+academy.theme+'. Select the image to open it at full size.';
 $('selection-summary').textContent=stream?domain+' / '+stream.id+' · '+stream.name+' · 20 lab seats':domain+' · All 12 workstreams · 240 lab seats';
 const route=new URL(location.href);route.searchParams.set('domain',domain);route.searchParams.set('sector',sectorContext);if(streamId)route.searchParams.set('stream',streamId);else route.searchParams.delete('stream');history.replaceState(null,'',route);

 $('domains').replaceChildren(...data.academies.map(a=>{const b=document.createElement('button');b.textContent=a.id;b.title=a.name;b.setAttribute('aria-pressed',String(domain===a.id));b.onclick=()=>changeDomain(a.id);return b;}));
 const head=document.createElement('tr');let th=document.createElement('th');th.scope='col';th.textContent='Workstream / Lab';head.append(th);
 data.labs.forEach(l=>{th=document.createElement('th');th.scope='col';th.textContent=l.id.replace('SL','L')+' · '+l.code;th.title=l.official;const span=document.createElement('span');span.textContent=l.name;th.append(span);head.append(th);});$('head').replaceChildren(head);
 const streams=data.mappings[domain],rows=[];
 for(const s of streams.filter(s=>!streamId||s.id===streamId)){const row=document.createElement('tr'),label=document.createElement('th');label.scope='row';label.textContent=s.id;const span=document.createElement('span');span.textContent=s.name+' · '+sectorContext;label.append(span);row.append(label);
 for(const l of data.labs){const id=domain+'-'+s.id+'-'+l.id,allocated=bookings.some(b=>b.seat===id),td=document.createElement('td'),b=document.createElement('button');b.innerHTML='<svg class="flight-seat" viewBox="0 0 56 64" aria-hidden="true" focusable="false"><defs><linearGradient id="upholstery-'+id+'" x1="0" y1="0" x2="1" y2="1"><stop class="seat-light" offset="0"/><stop class="seat-dark" offset="1"/></linearGradient></defs><path class="seat-shell" d="M12 9Q12 3 20 3H36Q44 3 44 9V44Q44 54 37 57H19Q12 54 12 44Z"/><rect class="seat-back" x="16" y="7" width="24" height="33" rx="8" fill="url(#upholstery-'+id+')"/><rect class="seat-headrest" x="20" y="10" width="16" height="8" rx="3"/><path class="seat-stitch" d="M20 22V33M36 22V33"/><rect class="seat-cushion" x="16" y="37" width="24" height="16" rx="5" fill="url(#upholstery-'+id+')"/><rect class="seat-arm" x="8" y="29" width="7" height="22" rx="3"/><rect class="seat-arm" x="41" y="29" width="7" height="22" rx="3"/><path class="seat-belt" d="M18 43L27 47L38 42"/><rect class="seat-buckle" x="26" y="44" width="5" height="4" rx="1"/><path class="seat-base" d="M21 57H35L38 61H18Z"/></svg>';const code=document.createElement('span');code.className='seat-number';code.textContent=l.id.replace('SL','L');const labCode=document.createElement('span');labCode.className='seat-lab';labCode.textContent=l.code;b.append(code,labCode);b.className=allocated?'allocated':selected?.id===id?'selected':'';b.setAttribute('aria-label',`${id}, ${sectorContext}, ${l.official}, ${allocated?'demo allocated':'available'}`);b.dataset.seat=id;b.title=b.getAttribute('aria-label');b.onclick=()=>openSeat({id,stream:s,lab:l,allocated});td.append(b);row.append(td);}rows.push(row);}
 $('seats').replaceChildren(...rows);const taken=bookings.filter(b=>b.seat.startsWith(domain+'-')).length;
 $('count').textContent=`${domain}: ${240-taken} available · ${taken} demo allocated · 240 total · ${rows.length} of 12 workstreams shown`;
 $('caption').textContent=data.academies.find(a=>a.id===domain).name+' · 12 × 20 seat inventory';
}
let trigger;
function openSeat(seat){trigger=document.activeElement;selected=seat;$('booking-title').textContent=seat.id;$('seat-detail').textContent=seat.stream.name+' · '+seat.lab.official+' · '+sectorContext+(seat.allocated?' · Already demo allocated':' · Available in this demo');$('result').textContent='';$('application').reset();$('sector').value=sectorContext;$('application').querySelector('button').disabled=seat.allocated;$('checkout').src=CHECKOUT;$('booking').showModal();render();}
function closeSeat(){$('booking').close();$('checkout').removeAttribute('src');const seatButton=Array.from(document.querySelectorAll('[data-seat]')).find(b=>b.dataset.seat===selected?.id);if(seatButton)seatButton.focus();}
$('close').onclick=closeSeat;$('booking').addEventListener('cancel',()=>{$('checkout').removeAttribute('src');});
$('domain-select').onchange=e=>changeDomain(e.target.value);$('stream-select').onchange=e=>{streamId=e.target.value;selected=null;render();};
$('reset').onclick=()=>{try{localStorage.removeItem(KEY);bookings=[];selected=null;render();}catch{$('load-error').textContent='Browser storage is unavailable. Reset could not be saved.';}};
$('sector').replaceChildren(...sectors.map(s=>new Option(s,s)));
$('application').onsubmit=async e=>{e.preventDefault();if(busy||!selected)return;const f=new FormData(e.target),button=e.target.querySelector('button');
 if(f.get('membership')==='existing'){$('result').textContent='Existing members are ineligible for campaign seats. Your current community access is unchanged.';return;}
 const email=normalizeEmail(f.get('email')),phone=normalizePhone(f.get('phone')),linkedin=f.get('linkedin').trim();
 if(!/^\+[1-9]\d{7,14}$/.test(phone)){$('result').textContent='Use international phone format, including + and country code.';return;}
 if(linkedin){try{const u=new URL(linkedin);if(u.protocol!=='https:'||!['linkedin.com','www.linkedin.com'].includes(u.hostname)||!u.pathname.startsWith('/in/'))throw Error();}catch{$('result').textContent='Use a LinkedIn profile URL beginning https://www.linkedin.com/in/';return;}}
 busy=true;button.disabled=true;
 try{const [eh,ph]=await Promise.all([digest(email),digest(phone)]);bookings=readBookings();
 if(bookings.some(b=>b.email===eh||b.phone===ph))throw Error('Duplicate blocked: this email OR mobile already has a demo seat in the campaign, including other domains.');
 if(bookings.some(b=>b.seat===selected.id))throw Error('This seat was already demo allocated. Choose another seat.');
 const next=[...bookings,{seat:selected.id,email:eh,phone:ph}];localStorage.setItem(KEY,JSON.stringify(next));bookings=next;
 $('result').textContent='Demo allocated: '+selected.id+'. No real seat or access was granted. The live system will verify both contacts and membership before confirmation.';render();
 }catch(err){$('result').textContent=err.message||'Could not save the demo allocation.';button.disabled=false;}finally{busy=false;}
};
window.addEventListener('storage',e=>{if(e.key===KEY){bookings=readBookings();if(data)render();}});
let scheduled=false;function progress(){if(scheduled)return;scheduled=true;requestAnimationFrame(()=>{const d=document.documentElement,range=d.scrollHeight-d.clientHeight;$('progress').style.transform=`scaleX(${range>0?Math.min(1,Math.max(0,d.scrollTop/range)):0})`;scheduled=false;});}
addEventListener('scroll',progress,{passive:true});addEventListener('resize',progress);new ResizeObserver(progress).observe(document.body);
fetch('catalog.json').then(r=>{if(!r.ok)throw Error('Catalog unavailable');return r.json();}).then(d=>{data=d;render();renderLabExplorer();progress();}).catch(()=>{$('load-error').textContent='Seat catalog could not be loaded. Please reload the page.';});

function renderLabExplorer(){
 $('explore-lab-cards').replaceChildren(...data.labs.map(l=>{
  const card=document.createElement('article'),title=document.createElement('h3'),official=document.createElement('p'),purpose=document.createElement('p'),outcome=document.createElement('p'),open=document.createElement('button');
  title.textContent=l.id.replace('SL','L')+' · '+l.code+' · '+l.name;official.className='lab-official';official.textContent=l.official;purpose.textContent=l.purpose;outcome.textContent='You create: '+l.outcome;
  open.type='button';open.textContent='Explore '+l.code;open.dataset.exploreLab=l.id;open.onclick=()=>openLab(l,open);card.append(title,official,purpose,outcome,open);return card;
 }));
}
let labTrigger=null;
function openLab(l,trigger){
 labTrigger=trigger;$('lab-explorer-title').textContent=l.id.replace('SL','L')+' · '+l.code+' · '+l.official;$('lab-explorer-purpose').textContent=l.purpose;$('lab-explorer-external').href=l.url;$('lab-explorer-frame').title=l.official+' app';$('lab-explorer-frame').src=l.url;$('lab-explorer').showModal();
}
function cleanupLab(){$('lab-explorer-frame').removeAttribute('src');if(labTrigger?.isConnected)labTrigger.focus();}
$('lab-explorer-close').onclick=()=>$('lab-explorer').close();
$('lab-explorer').addEventListener('close',cleanupLab);
