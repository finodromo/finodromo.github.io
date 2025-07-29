
// js/app.js
// Usa estrutura gerada em data/structure.js em window.structure

document.addEventListener('DOMContentLoaded', () => {
  buildNavbar();
  routeTo(window.location.hash || '#');
  window.addEventListener('hashchange', () => routeTo(window.location.hash));
});

function buildNavbar() {
  document.querySelectorAll('.dropdown').forEach(el => {
    const dept = el.dataset.dept;
    const menu = el.querySelector('.dropdown-menu');
    (structure[dept] ? Object.keys(structure[dept]) : []).forEach(d => {
      const li = document.createElement('li');
      li.textContent = d;
      li.onclick = () => location.hash = `#${dept}/${encodeURIComponent(d)}`;
      menu.appendChild(li);
    });
  });
}

function routeTo(hash) {
  const view = document.querySelector('#view');
  // remove layout de período antigo
  view.classList.remove('period-view');
  view.innerHTML = '';
  const parts = hash.slice(1).split('/');

  if (parts[0] === '') {
    renderDepartments(view);
  } else if (parts.length === 1) {
    renderDisciplines(view, parts[0]);
  } else if (parts.length === 2) {
    renderProfessors(view, parts[0], decodeURIComponent(parts[1]));
  } else if (parts.length === 3) {
    renderPeriods(view,
      parts[0], // dept
      decodeURIComponent(parts[1]), // disc
      decodeURIComponent(parts[2])  // prof
    );
  } else {
    view.innerHTML = '<p>Página não encontrada.</p>';
  }
}

function renderDepartments(container) {
  container.innerHTML = '';
  ['decom','demat','outras'].forEach(dept => {
    const card = makeCard(dept.charAt(0).toUpperCase() + dept.slice(1), () => {
      location.hash = `#${dept}`;
    });
    const img = document.createElement('img');
    img.src = `assets/logos/${dept}.png`;
    card.prepend(img);
    container.appendChild(card);
  });
}

function renderDisciplines(container, dept) {
  container.innerHTML = '';
  Object.keys(structure[dept] || {}).forEach(disc => {
    const [code, name] = disc.split(' - ');
    const card = makeCard(code, () => location.hash = `#${dept}/${encodeURIComponent(disc)}`);
    const p = document.createElement('p'); p.textContent = name;
    card.appendChild(p);
    container.appendChild(card);
  });
}

function renderProfessors(container, dept, disc) {
  container.innerHTML = '';
  const profs = structure[dept][disc] || {};
  Object.keys(profs)
    .sort((a,b) => profs[a].length - profs[b].length)
    .forEach(prof => {
      const card = makeCard(prof, () => {
        location.hash = `#${dept}/${encodeURIComponent(disc)}/${encodeURIComponent(prof)}`;
      });
      container.appendChild(card);
    });
}


function renderPeriods(container, dept, disc, prof) {
  console.clear()
  console.log('>>> renderPeriods', { dept, disc, prof });
  // limpa e ativa modo período
  container.innerHTML = '';
  container.classList.add('period-view');

  const periodMap = structure[dept][disc][prof] || {};
  console.log('periodMap:', periodMap);
  const periods = Object.keys(periodMap);
  console.log('periods keys:', periods);
  if (!periods.length) {
    container.innerHTML = `
      <p>Não há finas cadastradas para <strong>${prof}</strong> em <strong>${disc}</strong>.</p>
      <p><a href="https://github.com/vodiniz/finodromo.github.io" target="_blank">
        Contribua abrindo um Pull Request!
      </a></p>`;
    return;
  }

  periods.forEach((period, pidx) => {
    // Cabeçalho grande do período
    const header = document.createElement('h2');
    header.textContent = `Período ${period}`;
    header.className = 'period-header';
    container.appendChild(header);

    const items = periodMap[period];
    console.log('Itens em prova', period, items);  // debug

    items.forEach((item, idx) => {
      // Título da Prova
      const subHeader = document.createElement('h3');
      subHeader.textContent = `Prova ${idx+1}`;
      subHeader.className = 'proof-header';
      container.appendChild(subHeader);

      // Se for arquivo direto
      if (item.type === 'file') {
        renderFile(container, dept, disc, prof, period, item.name);

      // Se for pasta, percorre todos os arquivos internos
      } else if (item.type === 'folder') {
        // Mostra as imagens dentro da pasta
        item.files.forEach(fileName => {
          renderFile(
            container,
            dept, disc, prof, period,
            `${item.name}/${fileName}`
          );
        });
      }

      // Separador visual entre provas
      if (idx < items.length - 1) {
        const hr = document.createElement('hr');
        container.appendChild(hr);
      }
    });

    // Separador entre períodos, se houver mais de um
    if (pidx < periods.length - 1) {
      const sep = document.createElement('hr');
      sep.className = 'period-sep';
      container.appendChild(sep);
    }
  });
}
// Função auxiliar que lida com encoding de caminho e tipos
function renderFile(container, dept, disc, prof, period, relativePath) {
  const parts = relativePath.split('/');
  const encodedParts = parts.map(p => encodeURIComponent(p));
  const urlParts = [
    dept,
    encodeURIComponent(disc),
    encodeURIComponent(prof),
    'Provas',
    period,
    ...encodedParts
  ];
  const url = urlParts.join('/');
  const ext = parts[parts.length - 1].split('.').pop().toLowerCase();

  if (ext === 'pdf') {
    const embed = document.createElement('embed');
    embed.src = url;
    embed.className = 'pdf-embed';
    container.appendChild(embed);
  } else {
    const img = document.createElement('img');
    img.src = url;
    img.className = 'img-preview';
    container.appendChild(img);
  }
}

function makeCard(title, onClick) {
  const card = document.createElement('div');
  card.className = 'card';
  card.onclick = onClick;
  const h3 = document.createElement('h3');
  h3.textContent = title;
  card.appendChild(h3);
  return card;
}

