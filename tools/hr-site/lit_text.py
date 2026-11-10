"""Series-specific text for the LIT (Leadership and Identity Transformation) academy catalog records.
Personal-practice wording; no therapy or outcome claims."""
S = {
 "LIT01": ("personal purpose and identity", "a purpose-and-values statement that you test in real choices at work and at home", "supporting others to explore purpose and identity without imposing answers", "purpose-and-identity portfolio with values, commitments and evidence", "purpose and identity"),
 "LIT02": ("a growth mindset", "a learning-from-setbacks routine with small experiments and honest review", "building a culture where feedback and mistakes are used for learning", "growth-mindset portfolio with experiments, feedback and reflections", "growth mindset"),
 "LIT03": ("emotional awareness and freedom", "a daily practice for noticing, naming and responding to emotions", "creating safe spaces for honest conversation and knowing when to point to professional help", "emotional-freedom portfolio with practices, reflections and boundaries", "emotional freedom"),
 "LIT04": ("authentic leadership", "a leadership practice that aligns your values, words and actions", "leading with integrity, listening and accountability across a team", "authentic-leadership portfolio with commitments, feedback and evidence", "authentic leadership"),
 "LIT05": ("an intentional life", "a weekly planning and review rhythm linked to what matters most", "helping others set intentions and review them without pressure", "intentional-life portfolio with priorities, rhythms and reviews", "an intentional life"),
 "LIT06": ("continuous learning", "a learning plan with goals, resources, practice and review", "building learning habits and knowledge-sharing in a team or community", "continuous-learning portfolio with a plan, practice evidence and reflections", "continuous learning"),
 "LIT07": ("a balanced digital life", "digital habits and boundaries that protect attention, sleep and relationships", "setting healthy technology norms for families, teams and communities", "digital-balance portfolio with habits, boundaries and reviews", "a balanced digital life"),
 "LIT08": ("meaningful relationships", "listening, repair and boundary practices in key relationships", "building trust and handling conflict across teams and communities", "relationship portfolio with practices, conversations and reflections", "meaningful relationships"),
 "LIT09": ("integrity and values", "a values-in-action practice for hard choices, with a record of decisions", "leading ethical conversations and speaking up safely", "integrity portfolio with decisions, reasons and reflections", "integrity and values"),
 "LIT10": ("a fulfilling life", "a review of the five life areas with commitments and a balance check", "helping others define fulfilment on their own terms", "fulfilment portfolio with a life-area review, commitments and evidence", "a fulfilling life"),
 "LIT11": ("inner transformation", "a reflective practice that connects insight to small, repeatable changes", "guiding reflective practice responsibly, without therapy or outcome claims", "inner-transformation portfolio with practices, reflections and changes", "inner transformation"),
 "LIT12": ("contribution to a better world", "a contribution project that serves a real need in your community", "mobilizing others in service while respecting consent and local context", "contribution portfolio with a project, partners and reflections", "contribution to a better world"),
}
def objective(code, lv):
    t, w, g, c, _ = S[code]
    return {1: f"Build the shared vocabulary and a first honest self-picture for {t}.",
            2: f"Learn the core principles and practices for {t}, and test them against one real decision.",
            3: f"Work through {w}, gathering evidence across your spiritual, social, academic, professional and personal goals.",
            4: f"Lead others in {g}.",
            5: f"Complete a capstone {c}, reflecting on what changed and what did not."}[lv]
def output(code, lv):
    s = S[code][4]
    return {1: f"Personal baseline note for {s}", 2: f"Principles-and-practices summary for {s}", 3: f"Practice log with evidence for {s}", 4: f"Leadership practice guide for {s}", 5: f"Capstone portfolio for {s}"}[lv]
