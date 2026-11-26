const CHAPTERS=[
{id:'intent',title:'Define your intent',steps:[
{title:'Describe the workforce need',message:'Start AIU-OVE-01 from an approved position. Capture the business outcome and the work the hire will cover.',view:'intent'},
{title:'Ground the request',message:'Read the approved position and workforce plan. Retain source IDs, approval evidence and the accountable owner.',view:'context'},
{title:'Clarify the boundaries',message:'Confirm location, start window and responsibilities. Missing facts remain “Not provided”; the agent stays at L1 Assist.',view:'questions'},
{title:'Review the requirements',message:'Review the demand-agent PRD, its human reviewer and acceptance criteria before moving into implementation.',view:'prd'},
{title:'Inspect the solution architecture',message:'One drafting agent reads approved inputs and returns a reviewable draft. The human owns all publication and position decisions.',view:'architecture'}]},
{id:'build',title:'Build the solution',steps:[
{title:'Define the technical specification',message:'Inspect the input contract, bounded tool interfaces, output schema and stop conditions for AIU-OVE-01.',view:'spec'},
{title:'Review the agent implementation',message:'Inspect the source prompt, schema validation and guarded drafting logic. The downloadable starter uses deterministic local rules.',view:'code'},
{title:'Refine in the developer workspace',message:'Keep prompts, fixtures and tests together. Export the design pack for tenant-specific implementation in Joule Studio.',view:'ide'}]},
{id:'explore',title:'Explore the agentic solutions',steps:[
{title:'Inspect the generated artifacts',message:'One agent, one review workflow and one draft viewer support this use case. Run local checks before exploring the preview.',view:'artifacts'},
{title:'Try the requisition drafting agent',message:'Use the sample position and workforce plan to generate a source-linked draft. Requests to publish, change positions or set budgets are blocked.',view:'preview'},
{title:'Inspect the review workflow',message:'Follow the draft through human review. The preview stores review status locally and performs no external write.',view:'workflow'},
{title:'Review the demand workspace',message:'Inspect the draft, evidence, assumptions and review state. A viewed tour position is separate from a validated agent run.',view:'dashboard'}]},
{id:'govern',title:'Deploy and govern',steps:[
{title:'Prepare the versioned handoff',message:'Download the source prompt, agent card, tool contract, evaluation cases and local starter. Repository and transport setup remain tenant-specific.',view:'git'},
{title:'Inspect deployment readiness',message:'Review the prerequisites for a real Joule Studio deployment. This experience represents a simulated development environment.',view:'deploy'},
{title:'Evaluate and monitor behaviour',message:'Run ten deterministic local cases and inspect their actual results. These checks do not establish model quality or tenant readiness.',view:'monitor'},
{title:'Register the accountable agent',message:'Review AIU-OVE-01’s purpose, autonomy, owner, data scope and limits. Keep the remaining agent use cases outside this prototype.',view:'hub'},
{title:'Your agent design is ready for review',message:'Export the design pack, revisit any chapter or restart. Real deployment requires tenant access, supported APIs and validation.',view:'complete'}]}
];
const SOURCE_URL='https://www.sap.com/products/artificial-intelligence/joule-studio/product-tour.html';
const BOOTCAMP_URL='https://nbnayak88.github.io/learning-township/01-HR-Human-Capital-Capability-Academy-Workforce-Monday/HR02-ATA2-Architecting-Autonomous-Talent-Acquisition/01-HR02-ENE-energy/05-Ultimate/bootcamp/omniverse-smartrecruiters/#delivery-pack';
