"""Domain-specific learning objectives and student outputs for each HR and CRM series.
Replaces the one generic template that was reused for every series (AI/agents stay a minor thread)."""
import re
S = {
 "HR01": ("workforce foundations: employee records, organization and position data", "a governed employee-record and organization-change workflow with clear data owners", "data ownership, access control and cross-system integration for core workforce data", "workforce-foundation blueprint with ownership, controls and a value case", "employee record and organization data"),
 "HR02": ("talent acquisition: recruiting and onboarding", "a requisition-to-offer-to-onboarding workflow with clear handoffs and readiness checks", "candidate-data governance, fair selection controls and onboarding integrations across teams", "talent-acquisition blueprint covering hiring decisions, onboarding readiness and measures", "recruiting and onboarding"),
 "HR03": ("organization design and performance management", "a goal-setting, check-in and review cycle that managers can run consistently", "calibration, rating governance and performance-data controls across business units", "performance-management blueprint with calibration rules, fairness checks and a measure set", "performance management"),
 "HR04": ("leadership, succession and talent development", "a talent-review and succession workflow with transparent criteria and owners", "talent-data governance, succession-risk controls and leadership-pipeline scaling", "leadership-pipeline blueprint with succession coverage, development paths and measures", "leadership and succession"),
 "HR05": ("compensation, rewards and recognition", "a compensation-cycle workflow with budgets, eligibility rules and approvals", "pay-governance, equity checks and reward-data controls across regions", "total-rewards blueprint with pay rules, fairness checks and a cost view", "compensation and rewards"),
 "HR06": ("learning, skills and internal mobility", "a skills-to-learning-to-mobility workflow with clear role and skill data", "learning-data governance, skills-taxonomy ownership and mobility scaling", "learning-and-mobility blueprint with skills evidence, pathways and measures", "learning and mobility"),
 "HR07": ("payroll operations and compliance", "a payroll-run workflow with input checks, cut-offs, approvals and exception handling", "payroll controls, statutory change management and cross-system reconciliation", "payroll-operations blueprint with control points, recovery paths and a cost and risk view", "payroll operations"),
 "HR08": ("time, attendance and scheduling", "a time-capture, absence and scheduling workflow with rule ownership", "time-rule governance, labor-law variation and payroll-handoff integration", "time-operations blueprint with rules, exception paths and a service-level view", "time and attendance"),
 "HR09": ("workforce analytics and reporting", "a trusted workforce-metrics workflow with definitions, lineage and refresh rules", "metric governance, privacy controls and decision-ownership for people analytics", "workforce-intelligence blueprint with metric definitions, access rules and decision use", "workforce analytics"),
 "HR10": ("employee experience, listening and HR service delivery", "an employee-listening and case-handling workflow with clear service ownership", "experience-data governance, consent and action-follow-through across HR and managers", "employee-experience blueprint with journeys, feedback loops and measures", "employee experience"),
 "HR11": ("AI-assisted HR services", "a governed AI-assisted HR workflow with a named decision, owner, evidence and human review", "AI governance for HR: agent identity, access limits, monitoring and recovery", "AI-in-HR blueprint with decision rights, safeguards, test evidence and a value case", "AI-assisted HR"),
 "HR12": ("connected HR systems and integrations", "a cross-system HR event workflow with contracts, monitoring and error handling", "integration architecture, access propagation and exception recovery across HR platforms", "connected-HR blueprint with event contracts, ownership and recovery design", "connected HR"),
 "CRM01": ("a connected customer view: profile, consent and identity", "a customer-profile and consent workflow with identity rules and clear data owners", "customer-data governance, identity resolution and consent enforcement across systems", "connected-customer blueprint with data ownership, consent controls and a value case", "the connected customer view"),
 "CRM02": ("customer engagement and campaign journeys", "a segmented, consent-aware engagement journey with clear ownership and measures", "engagement governance, frequency and preference controls across channels", "customer-engagement blueprint with journeys, consent rules and measures", "customer engagement"),
 "CRM03": ("sales and revenue operations", "a lead-to-opportunity-to-order workflow with stage rules and forecast ownership", "pipeline governance, territory and pricing controls and forecast integrity", "revenue-operations blueprint with stage rules, controls and measures", "sales and revenue operations"),
 "CRM04": ("digital commerce: catalog, pricing, checkout and fulfilment", "a browse-to-checkout-to-fulfilment workflow with price, stock and promise rules", "commerce governance, pricing integrity and order-orchestration integration", "digital-commerce blueprint with catalog and price ownership, fulfilment promises and measures", "digital commerce"),
 "CRM05": ("customer service and case resolution", "a case intake, routing and resolution workflow with service-level ownership", "service-knowledge governance, escalation rules and case-data controls", "customer-service blueprint with resolution rules, escalation paths and measures", "customer service"),
 "CRM06": ("end-to-end customer experience and journeys", "a journey-mapping and moments-that-matter workflow with named owners", "experience governance, feedback-to-action loops and cross-team accountability", "customer-experience blueprint with journeys, owners and measures", "customer experience"),
 "CRM07": ("subscriptions, billing and renewals", "a subscription, billing and renewal workflow with clear entitlement rules", "revenue-recognition handoffs, dunning controls and renewal-risk governance", "recurring-revenue blueprint with billing rules, renewal paths and measures", "recurring revenue"),
 "CRM08": ("customer operations and fulfilment handoffs", "an order-to-service handoff workflow with clear ownership at each step", "operations governance, exception handling and cross-system reconciliation", "customer-operations blueprint with handoff rules, recovery paths and a service view", "customer operations"),
 "CRM09": ("customer analytics and insight", "a trusted customer-metrics workflow with definitions, lineage and refresh rules", "metric governance, privacy controls and decision-ownership for customer insight", "customer-intelligence blueprint with metric definitions, access rules and decision use", "customer analytics"),
 "CRM10": ("digital customer channels and self-service", "a self-service journey across web and app channels with accessible design and clear ownership", "channel governance, accessibility, identity and session controls across digital touchpoints", "digital-experience blueprint with channel rules, accessibility and measures", "digital customer channels"),
 "CRM11": ("AI-assisted customer services", "a governed AI-assisted customer workflow with a named decision, owner, evidence and human review", "AI governance for customer services: agent identity, access limits, monitoring and recovery", "AI-in-customer-service blueprint with decision rights, safeguards, test evidence and a value case", "AI-assisted customer services"),
 "CRM12": ("partner and customer-ecosystem integration", "a partner-and-customer event workflow with contracts, monitoring and error handling", "ecosystem integration architecture, access propagation and exception recovery across partners", "connected-ecosystem blueprint with event contracts, ownership and recovery design", "customer ecosystems"),
}
GENERIC = ("Establish conceptual taxonomy", "Master core principles, APQC", "Implement high-velocity workflows", "Orchestrate enterprise governance", "Deliver capstone architectural digital twin")


def objective(code, level_no):
    t, w, g, c, _ = S[code]
    ai = code.endswith("11")
    if level_no == 1: return f"Establish the shared vocabulary, roles and readiness picture for {t}."
    if level_no == 2: return f"Master the core principles, APQC-aligned baseline processes and data contracts for {t}."
    if level_no == 3: return f"Implement {w}" + (", with AI assistance bounded by human review." if ai else ", using automation or AI assistance only where it adds clear value.")
    if level_no == 4: return f"Orchestrate {g}" + ("." if ai else ", including where agents and automation should and should not act.")
    return f"Deliver a capstone {c}" + (", with a simulation or digital-twin view of the design where useful." if not ai else ", tested against a synthetic scenario.")


def student_output(code, text):
    topic = S[code][4]
    text = re.sub(r"\bfor (HR|CRM)\d\d\b", f"for {topic}", text)
    return text.replace("Functional autonomous prototype", "Working prototype")


def is_generic(obj):
    return obj.startswith(GENERIC)
