"use strict";
const byId = id => document.getElementById(id);
const put = (id, value) => { byId(id).textContent = value ?? ""; };
const steps = capstonePhases.flatMap((phase, group) =>
  phase.steps.map((step, index) => ({...step, phase, group, index})));
const phaseButtons = capstonePhases.map((phase, group) => {
  const button = document.createElement("button");
  button.type = "button";
  button.textContent = phase.name + " · " + phase.steps.length;
  button.addEventListener("click", () => show(steps.findIndex(step => step.group === group)));
  byId("phases").append(button);
  return button;
});
steps.forEach((step, position) => {
  byId("activity").add(new Option(step.fields.Day + " · " + step.title, position));
});
put("overview-count", capstonePhases.length + " phases · " + steps.length + " activities · " +
  steps.filter(step => step.prompt).length + " AI practice prompts");
let current = 0;
function show(position, focus = true) {
  if (!Number.isInteger(position) || !steps[position]) return;
  current = position;
  const step = steps[position];
  document.documentElement.style.scrollPaddingTop = (document.querySelector("header").offsetHeight + 12) + "px";
  byId("overview").hidden = true;
  byId("tour").hidden = false;
  byId("activity").value = String(position);
  put("quote", step.phase.quote);
  put("position", step.phase.name + " " + (step.index + 1) + "/" + step.phase.steps.length +
    " · Activity " + (position + 1) + " of " + steps.length);
  put("step-title", step.title);
  put("notes", step.fields.Notes);
  put("deliverable", step.fields["Key Deliverable"]);
  put("prompt", step.prompt);
  put("extra", step.extra?.replace(/^## /gm, ""));
  put("copy-status", "");
  byId("prompt-area").hidden = !step.prompt;
  byId("prompt-area").open = false;
  byId("source").hidden = !step.source;
  if (step.source) byId("source").href = step.source;
  const metadata = ["Day", "Task ID", "Activity Type", "Priority", "Status"].flatMap(label => {
    if (!step.fields[label]) return [];
    const item = document.createElement("div");
    const term = document.createElement("dt");
    const value = document.createElement("dd");
    term.textContent = label === "Status" ? "Source status" : label;
    value.textContent = step.fields[label];
    item.append(term, value);
    return [item];
  });
  byId("metadata").replaceChildren(...metadata);
  phaseButtons.forEach((button, index) => {
    if (index === step.group) button.setAttribute("aria-current", "step");
    else button.removeAttribute("aria-current");
  });
  byId("previous").disabled = position === 0;
  put("next", position === steps.length - 1 ? "Finish tour" : "Next");
  if (focus) {
    byId("step-title").focus({preventScroll:true});
    byId("step-title").scrollIntoView({block:"start"});
  }
  scheduleReading();
}
byId("start").addEventListener("click", () => show(0));
byId("previous").addEventListener("click", () => show(current - 1));
byId("next").addEventListener("click", () => {
  if (current === steps.length - 1) byId("finish").showModal();
  else show(current + 1);
});
byId("activity").addEventListener("change", event => show(Number(event.target.value)));
byId("review").addEventListener("click", () => byId("finish").close());
byId("restart").addEventListener("click", () => {
  byId("finish").close();
  show(0);
});
byId("copy").addEventListener("click", async () => {
  try {
    await navigator.clipboard.writeText(steps[current].prompt);
    put("copy-status", "Copied.");
  } catch {
    put("copy-status", "Select the prompt text to copy it.");
    byId("prompt").focus();
  }
});
let pending = false;
function scheduleReading() {
  if (pending) return;
  pending = true;
  requestAnimationFrame(() => {
    pending = false;
    const scroller = document.scrollingElement;
    const range = scroller.scrollHeight - scroller.clientHeight;
    const fraction = range > 0 ? Math.max(0, Math.min(1, scroller.scrollTop / range)) : 0;
    document.querySelector(".reading span").style.transform = "scaleX(" + fraction + ")";
  });
}
addEventListener("scroll", scheduleReading, {passive:true});
addEventListener("resize", scheduleReading);
const sizeObserver = new ResizeObserver(() => {
  document.documentElement.style.scrollPaddingTop = (document.querySelector("header").offsetHeight + 12) + "px";
  scheduleReading();
});
sizeObserver.observe(document.querySelector("header"));
sizeObserver.observe(byId("main"));
scheduleReading();
