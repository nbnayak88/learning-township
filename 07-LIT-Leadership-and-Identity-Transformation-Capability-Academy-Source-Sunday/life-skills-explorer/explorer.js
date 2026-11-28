'use strict';

const byId = id => document.getElementById(id);
const {pathways, personas, challenges} = lifeSkills;
const people = new Map(personas.map(person => [person.id, person]));
const pathwayCode = number => 'LIT' + String(number).padStart(2, '0');
const persona = byId('persona');
const search = byId('search');
const previous = byId('previous');
const next = byId('next');
const restart = byId('restart');
const directory = byId('directory');
const opener = byId('directory-open');
const heading = byId('challenge-title');
const nav = byId('pathways');
const buttons = [];
let pathway = 0;
let index = 0;
let matches = [];

if (matchMedia('(max-width: 700px)').matches) nav.closest('details').open = false;
for (const person of personas) persona.add(new Option(person.name + ' · ' + person.age, person.id));
for (const [number, title] of [[0, 'All pathways'], ...pathways.map(([name], i) => [i + 1, name])]) {
  const button = document.createElement('button');
  button.type = 'button';
  button.textContent = number ? pathwayCode(number) + ' · ' + title : title;
  button.addEventListener('click', () => {
    pathway = number;
    filter();
    if (matchMedia('(max-width: 700px)').matches) {
      nav.closest('details').open = false;
      if (matches.length) heading.focus();
      else search.focus();
    }
  });
  buttons.push(button);
  nav.append(button);
}

function filter() {
  const query = search.value.toLowerCase().trim();
  matches = challenges.filter(item => {
    const person = people.get(item.persona);
    const searchable = [item.title,item.situation,item.action,person.name,pathways[item.pathway - 1][0]].join(' ').toLowerCase();
    return (!pathway || item.pathway === pathway) && (!persona.value || item.persona === persona.value) && searchable.includes(query);
  });
  index = 0;
  render();
}

function render() {
  buttons.forEach((button, i) => button.setAttribute('aria-current', String(i === pathway)));
  const item = matches[index];
  byId('matches').textContent = matches.length ? matches.length + ' matching challenges' : 'No matches. Try another pathway, persona, or search phrase.';
  byId('challenge').hidden = !item;
  previous.disabled = !item || index === 0;
  next.disabled = !item || index === matches.length - 1;
  restart.hidden = matches.length < 2 || !next.disabled;
  opener.disabled = !matches.length;
  byId('position').textContent = item ? 'Challenge ' + (index + 1) + ' of ' + matches.length : '';
  if (!item) return;
  const person = people.get(item.persona);
  const [title,reflection] = pathways[item.pathway - 1];
  byId('context').textContent = pathwayCode(item.pathway) + ' · ' + title + ' / ' + person.name + ' · ' + person.age;
  heading.textContent = item.title;
  byId('situation').textContent = item.situation;
  byId('reflection').textContent = reflection;
  byId('action').textContent = item.action;
  byId('signal').textContent = item.signal;
}
function step(to) {
  index = to;
  render();
  heading.focus({preventScroll:true});
}
previous.addEventListener('click', () => step(index - 1));
next.addEventListener('click', () => step(index + 1));
restart.addEventListener('click', () => step(0));
persona.addEventListener('change', filter);
search.addEventListener('input', filter);
let jump = false;
opener.addEventListener('click', () => {
  const list = byId('directory-list');
  list.replaceChildren(...matches.map((item, i) => {
    const li = document.createElement('li');
    const button = document.createElement('button');
    button.type = 'button';
    button.textContent = pathwayCode(item.pathway) + ' · ' + item.title + ' · ' + people.get(item.persona).name;
    button.addEventListener('click', () => {
      jump = true;
      step(i);
      directory.close();
    });
    li.append(button);
    return li;
  }));
  directory.showModal();
});
directory.addEventListener('close', () => {
  (jump ? heading : opener).focus({preventScroll:true});
  jump = false;
});

let frame;
function updateReading() {
  cancelAnimationFrame(frame);
  frame = requestAnimationFrame(() => {
    const root = document.scrollingElement;
    const distance = root.scrollHeight - root.clientHeight;
    const progress = distance > 0 ? Math.min(1, Math.max(0, root.scrollTop / distance)) : 0;
    byId('reading').style.width = progress * 100 + '%';
  });
}
window.addEventListener('scroll', updateReading, {passive:true});
window.addEventListener('resize', updateReading);
new ResizeObserver(updateReading).observe(document.body);
filter();
