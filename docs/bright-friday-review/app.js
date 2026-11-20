'use strict';
const CHECKOUT='https://hub.successlabsacademy.com/web/checkout/694af8798dd872a219700dd3';
const sectors=['Energy','Materials','Industrials','Consumer Discretionary','Consumer Staples','Health Care','Financials','Information Technology','Communication Services','Utilities','Real Estate'];
const $=id=>document.getElementById(id);let data,domain='HR',selected=null,busy=false;
const KEY='sla-bright-friday-review-v1';
function readBookings(){try{const x=JSON.parse(localStorage.getItem(KEY)||'[]');return Array.isArray(x)?x.filter(b=>b&&typeof b.seat==='string'&&typeof b.email==='string'&&typeof b.phone==='string'):[];}catch{return [];}}
let bookings=readBookings();
const normalizeEmail=s=>s.trim().toLowerCase();
const normalizePhone=s=>s.trim().replace(/[\s().-]/g,'');
async function digest(s){return Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256',new TextEncoder().encode(s)))).map(n=>n.toString(16).padStart(2,'0')).join('');}
function render(){
 $('domains').replaceChildren(...data.academies.map(a=>{const b=document.createElement('button');b.textContent=a.id;b.title=a.name;b.setAttribute('aria-pressed',String(domain===a.id));b.onclick=()=>{domain=a.id;render();};return b;}));
 const head=document.createElement('tr');let th=document.createElement('th');th.scope='col';th.textContent='Workstream / Lab';head.append(th);
 data.labs.forEach(l=>{th=document.createElement('th');th.scope='col';th.textContent=l.id.replace('SL','L')+' · '+l.code;th.title=l.official;const span=document.createElement('span');span.textContent=l.name;th.append(span);head.append(th);});$('head').replaceChildren(head);
 const streams=data.mappings[domain],query=$('search').value.trim().toLowerCase(),rows=[];
 for(const s of streams.filter(s=>(s.id+' '+s.name).toLowerCase().includes(query))){const row=document.createElement('tr'),label=document.createElement('th');label.scope='row';label.textContent=s.id;const span=document.createElement('span');span.textContent=s.name;label.append(span);row.append(label);
 for(const l of data.labs){const id=domain+'-'+s.id+'-'+l.id,allocated=bookings.some(b=>b.seat===id),td=document.createElement('td'),b=document.createElement('button');b.textContent=allocated?'▣':'🪑';b.className=allocated?'allocated':selected?.id===id?'selected':'';b.setAttribute('aria-label',`${id}, ${l.official}, ${allocated?'demo allocated':'available'}`);b.dataset.seat=id;b.title=b.getAttribute('aria-label');b.onclick=()=>openSeat({id,stream:s,lab:l,allocated});td.append(b);row.append(td);}rows.push(row);}
 $('seats').replaceChildren(...rows);const taken=bookings.filter(b=>b.seat.startsWith(domain+'-')).length;
 $('count').textContent=`${domain}: ${240-taken} available · ${taken} demo allocated · 240 total · ${rows.length} of 12 workstreams shown`;
 $('caption').textContent=data.academies.find(a=>a.id===domain).name+' · 12 × 20 seat inventory';
}
let trigger;
function openSeat(seat){trigger=document.activeElement;selected=seat;$('booking-title').textContent=seat.id;$('seat-detail').textContent=seat.stream.name+' · '+seat.lab.official+(seat.allocated?' · Already demo allocated':' · Available in this demo');$('result').textContent='';$('application').reset();$('application').querySelector('button').disabled=seat.allocated;$('checkout').src=CHECKOUT;$('booking').showModal();render();}
function closeSeat(){$('booking').close();$('checkout').removeAttribute('src');const seatButton=Array.from(document.querySelectorAll('[data-seat]')).find(b=>b.dataset.seat===selected?.id);if(seatButton)seatButton.focus();}
$('close').onclick=closeSeat;$('booking').addEventListener('cancel',()=>{$('checkout').removeAttribute('src');});
$('search').oninput=()=>data&&render();
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
fetch('catalog.json').then(r=>{if(!r.ok)throw Error('Catalog unavailable');return r.json();}).then(d=>{data=d;render();progress();}).catch(()=>{$('load-error').textContent='Seat catalog could not be loaded. Please reload the page.';});
