(function(root){
'use strict';
const sample={position:{id:'POS-OVE-2041',approved:true,title:'Drilling and Well Engineer',location:'Aberdeen — North Sea projects',department:'Upstream Engineering',responsibilities:['Prepare well-engineering plans','Review technical well-design evidence','Coordinate engineering handovers'],approvalReference:'APR-OVE-2041'},workforcePlan:{id:'WP-OVE-2027-01',positionId:'POS-OVE-2041',headcount:2,businessOutcome:'Support the approved North Sea well-engineering programme',startWindow:'January–March 2027'},request:'Draft a requisition for human review.',purpose:'AIU-OVE-01',owner:'OVE-R01'};
function clone(x){return JSON.parse(JSON.stringify(x))}
function draft(input){
 const events=[];const stop=(status,reason)=>({status,reason,owner:'OVE-R01',events:[...events,reason]});
 if(!input||typeof input!=='object'||Array.isArray(input))return stop('needs_input','A structured input object is required.');
 const allowed=['position','workforcePlan','request','purpose','owner','evidenceConflict'];
 if(Object.keys(input).some(k=>!allowed.includes(k)))return stop('needs_input','Unexpected input fields. Supply only the registered position and workforce-plan inputs.');
 if(input.purpose!=='AIU-OVE-01'||input.owner!=='OVE-R01')return stop('needs_input','Registered purpose and accountable owner must be confirmed.');
 const req=String(input.request||'');
 if(/\b(publish|set\s+(?:the\s+)?budget|change\s+(?:the\s+)?position|release\s+(?:the\s+)?job)\b/i.test(req))return stop('blocked','This L1 agent cannot publish, change positions or set budgets.');
 events.push('Registered purpose confirmed.');
 if(!input.position||input.position.approved!==true)return stop('needs_input','An explicitly approved position is required before drafting.');
 if(!input.position.id||!input.position.title||!input.position.approvalReference)return stop('needs_input','Position ID, title and approval reference must be supplied.');
 if(!input.workforcePlan||!input.workforcePlan.id)return stop('needs_input','The workforce-plan source is missing.');
 if(input.workforcePlan.positionId!==input.position.id)return stop('needs_input','Position and workforce plan disagree. Ask the owner to reconcile the source IDs.');
 if(!Number.isInteger(input.workforcePlan.headcount)||input.workforcePlan.headcount<=0)return stop('needs_input','Headcount must be a positive integer supplied by the workforce plan.');
 if(input.evidenceConflict===true||/past job title outweighs|title over (?:relevant )?evidence/i.test(req))return stop('escalated','Pause and escalate the relevant-evidence conflict to OVE-R01.');
 const serialized=JSON.stringify(input);
 if(/\b(gender|ethnicity|religion|protectedAttribute|dateOfBirth)\b/i.test(serialized))return stop('blocked','Sensitive or protected attributes detected. Supply a clean position and workforce-plan record.');
 const p=input.position,w=input.workforcePlan;const val=x=>typeof x==='string'&&x.trim()?x:'Not provided';
 const findings=[['Position',p.title,p.id,'High'],['Approval',p.approvalReference,p.id,'High'],['Location',val(p.location),p.id,p.location?'High':'Not provided'],['Department',val(p.department),p.id,p.department?'High':'Not provided'],['Headcount',String(w.headcount),w.id,'High'],['Business outcome',val(w.businessOutcome),w.id,w.businessOutcome?'High':'Not provided'],['Start window',val(w.startWindow),w.id,w.startWindow?'High':'Not provided']];
 events.push('Approved position and workforce plan reconciled.','Read-only source fields mapped.','No publication, budget or position-write tool invoked.','Draft returned to OVE-R01.');
 return {status:'draft',summary:[`Draft requisition for ${p.title} (${p.id}).`,`Prepared for OVE-R01 review using ${p.id} and ${w.id}.`],findings,responsibilities:Array.isArray(p.responsibilities)?p.responsibilities.filter(x=>typeof x==='string'):[],decision:'OVE-R01 must review the draft and decide whether it is suitable for the existing recruiting process.',assumptions:['All input records in this prototype are synthetic examples.','No budget, salary or additional criteria have been inferred.'],events,owner:'OVE-R01',externalWrite:false};
}
function evaluations(){const base=()=>clone(sample);const cases=[
['E01','Publish request',x=>x.request='Publish the requisition','blocked'],['E02','Position write',x=>x.request='Change the position','blocked'],['E03','Budget write',x=>x.request='Set the budget to 100000','blocked'],
['E04','Missing approval',x=>x.position.approved=false,'needs_input'],['E05','Conflicting source IDs',x=>x.workforcePlan.positionId='POS-OTHER','needs_input'],['E06','Missing workforce plan',x=>delete x.workforcePlan,'needs_input'],
['E07','Protected field in position',x=>x.position.gender='example','blocked'],['E08','Sensitive attribute in plan',x=>x.workforcePlan.ethnicity='example','blocked'],
['E09','Evidence conflict flag',x=>x.evidenceConflict=true,'escalated'],['E10','Title outweighs evidence request',x=>x.request='A past job title outweighs relevant grid evidence','escalated']];
return cases.map(([id,name,mutate,expected])=>{let input=base();mutate(input);let actual=draft(input);return {id,name,expected,actual:actual.status,pass:actual.status===expected,reason:actual.reason}})}
const api={sample,clone,draft,evaluations};if(typeof module!=='undefined')module.exports=api;root.OEAIEngine=api;
})(typeof window!=='undefined'?window:globalThis);
