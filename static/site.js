/* Frest Homes — site behaviour (vanilla, no dependencies) */
(function(){
'use strict';
const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
const L=document.documentElement.lang||'lv';
const fmtEur=n=>new Intl.NumberFormat(L==='lv'?'lv-LV':'en-GB',{style:'currency',currency:'EUR',maximumFractionDigits:0}).format(n);

/* ---------- nav ---------- */
$$('.nav-links > li').forEach(li=>{
  const b=$('button.nl',li); if(!b) return;
  b.addEventListener('click',e=>{e.stopPropagation();const o=li.classList.contains('open');$$('.nav-links > li.open').forEach(x=>x.classList.remove('open'));if(!o)li.classList.add('open');});
  li.addEventListener('mouseenter',()=>{$$('.nav-links > li.open').forEach(x=>x!==li&&x.classList.remove('open'));li.classList.add('open')});
  li.addEventListener('mouseleave',()=>li.classList.remove('open'));
});
document.addEventListener('click',()=>$$('.nav-links > li.open').forEach(x=>x.classList.remove('open')));
const mob=$('#mobile');
$('#burger')&&$('#burger').addEventListener('click',()=>{mob.classList.add('open');document.body.classList.add('noscroll')});
$$('[data-close-mobile]').forEach(b=>b.addEventListener('click',()=>{mob.classList.remove('open');document.body.classList.remove('noscroll')}));
document.addEventListener('keydown',e=>{if(e.key==='Escape'){mob&&mob.classList.remove('open');document.body.classList.remove('noscroll');closeModal();closeLb();}});

/* ---------- hero slider ---------- */
const hero=$('.hero[data-slider]');
if(hero){
  const slides=$$('.slide',hero), copies=$$('.hero-copy',hero), dots=$$('.dots button',hero);
  let i=0, t;
  const show=n=>{i=(n+slides.length)%slides.length;slides.forEach((s,k)=>s.classList.toggle('on',k===i));copies.forEach((c,k)=>c.hidden=k!==i);dots.forEach((d,k)=>d.classList.toggle('on',k===i));};
  const auto=()=>{clearInterval(t);t=setInterval(()=>show(i+1),6500)};
  $('.hero-nav .pv',hero).addEventListener('click',()=>{show(i-1);auto()});
  $('.hero-nav .nx',hero).addEventListener('click',()=>{show(i+1);auto()});
  dots.forEach((d,k)=>d.addEventListener('click',()=>{show(k);auto()}));
  let x0=null;hero.addEventListener('touchstart',e=>x0=e.touches[0].clientX,{passive:true});
  hero.addEventListener('touchend',e=>{if(x0===null)return;const dx=e.changedTouches[0].clientX-x0;if(Math.abs(dx)>50){show(i+(dx<0?1:-1));auto()}x0=null});
  show(0);auto();
}

/* ---------- personaliser (facade colour × roof) ---------- */
$$('[data-personalise]').forEach(pz=>{
  const data=JSON.parse(pz.dataset.personalise); // {models:{slug:{name,facades:{roof:{color:src}}}}, colors:[...], roofs:[...]}
  const stage=$('.stage',pz), out=$('.cfg-now b',pz);
  let model=pz.dataset.model||Object.keys(data.models)[0], roof='tile', color=pz.dataset.color||'nordic-gray';
  const cache={};
  function src(m,r,c){return data.models[m].facades[r][c]}
  function render(){
    const s=src(model,roof,color);
    let img=cache[s];
    if(!img){img=new Image();img.alt='';img.src=s.src;img.srcset=s.srcset;img.sizes='(max-width:900px) 100vw, 60vw';cache[s]=img;stage.appendChild(img);}
    $$('img',stage).forEach(x=>x.classList.toggle('on',x===img));
    $$('.sw',pz).forEach(b=>b.classList.toggle('on',b.dataset.color===color));
    $$('.seg button',pz).forEach(b=>b.classList.toggle('on',b.dataset.roof===roof));
    $$('.models-pick button',pz).forEach(b=>b.classList.toggle('on',b.dataset.model===model));
    const cn=data.colors.find(c=>c.id===color).name, rn=data.roofs.find(r=>r.id===roof).name;
    if(out) out.textContent=data.models[model].name+' · '+cn+' · '+rn;
    $$('a[data-model-link]',pz).forEach(a=>a.href=data.models[model].url);
    // preload neighbours
    data.colors.forEach(c=>{const k=src(model,roof,c.id);if(!cache[k]){const p=new Image();p.src=k.src;}});
  }
  $$('.sw',pz).forEach(b=>b.addEventListener('click',()=>{color=b.dataset.color;render()}));
  $$('.seg button',pz).forEach(b=>b.addEventListener('click',()=>{roof=b.dataset.roof;render()}));
  $$('.models-pick button',pz).forEach(b=>b.addEventListener('click',()=>{model=b.dataset.model;render()}));
  render();
});

/* ---------- plan viewer ---------- */
$$('[data-plan]').forEach(pl=>{
  const imgs=$$('.stage img',pl), tabs=$$('.tabs button',pl);
  const show=id=>{imgs.forEach(i=>i.classList.toggle('on',i.dataset.id===id));tabs.forEach(t=>t.classList.toggle('on',t.dataset.id===id));};
  tabs.forEach(t=>t.addEventListener('click',()=>show(t.dataset.id)));
  show(tabs[0]&&tabs[0].dataset.id);
});

/* ---------- add-on selector ---------- */
$$('[data-addons]').forEach(ad=>{
  const base=+ad.dataset.base, btns=$$('.addon-list button',ad), imgs=$$('.stage img',ad), sum=$('.addon-sum b',ad), area=$('.addon-sum [data-area]',ad), baseArea=+ad.dataset.area;
  const pick=id=>{btns.forEach(b=>b.classList.toggle('on',b.dataset.id===id));imgs.forEach(i=>i.classList.toggle('on',i.dataset.id===id));const b=btns.find(x=>x.dataset.id===id);sum.textContent=fmtEur(base+(+b.dataset.price));if(area)area.textContent=(baseArea+(+b.dataset.area))+' m²';};
  btns.forEach(b=>b.addEventListener('click',()=>pick(b.dataset.id)));pick(btns[0].dataset.id);
});

/* ---------- quiz ---------- */
$$('[data-quiz]').forEach(q=>{
  const models=JSON.parse(q.dataset.quiz); const steps=$$('.step',q), prog=$$('.prog i',q), res=$('.res',q); let ans={},n=0;
  const show=k=>{n=k;steps.forEach((s,i)=>s.classList.toggle('on',i===k));prog.forEach((p,i)=>p.classList.toggle('on',i<=k));res.classList.remove('on');};
  const decide=()=>{
    const big=ans.who==='family-big', small=ans.who==='couple';
    let series=ans.style||'aura'; let size=big?'110':small?'70':(ans.budget==='gt140'?'110':'70');
    if(ans.budget==='lt140') size='70';
    return series+'-'+size;
  };
  $$('.opts button',q).forEach(b=>b.addEventListener('click',()=>{ans[b.dataset.q]=b.dataset.v;if(n<steps.length-1)show(n+1);else{const slug=decide(),m=models[slug];steps.forEach(s=>s.classList.remove('on'));prog.forEach(p=>p.classList.add('on'));$('[data-r-name]',res).textContent=m.name;$('[data-r-why]',res).textContent=m.why;$('[data-r-facts]',res).textContent=m.facts;$('img',res).src=m.img;$('img',res).srcset=m.srcset;$('a[data-r-link]',res).href=m.url;res.classList.add('on');}}));
  $('[data-restart]',q).addEventListener('click',()=>{ans={};show(0)});
  show(0);
});

/* ---------- compare: differences only ---------- */
const diff=$('#diffOnly');
if(diff){diff.addEventListener('change',()=>$$('.cmp tr.same').forEach(r=>r.classList.toggle('hide',diff.checked)));}

/* ---------- gallery filters ---------- */
$$('[data-gallery]').forEach(g=>{
  const btns=$$('.filters button',g), items=$$('.gitem',g);
  btns.forEach(b=>b.addEventListener('click',()=>{btns.forEach(x=>x.classList.toggle('on',x===b));const f=b.dataset.f;items.forEach(it=>it.classList.toggle('hide',f!=='all'&&!(' '+it.dataset.tags+' ').includes(' '+f+' ')));}));
  if(location.hash){const b=btns.find(x=>'#'+x.dataset.f===location.hash);b&&b.click();}
});

/* ---------- lightbox (any [data-lb] group) ---------- */
let lbItems=[],lbI=0; const lb=$('#lb');
function openLb(items,i){lbItems=items;lbI=i;lbShow();lb.classList.add('open');document.body.classList.add('noscroll');}
function lbShow(){const it=lbItems[lbI];$('img',lb).src=it.src;$('img',lb).srcset=it.srcset||'';$('.cap',lb).textContent=it.cap||'';}
function closeLb(){lb&&lb.classList.remove('open');document.body.classList.remove('noscroll');}
if(lb){
  $('.x',lb).addEventListener('click',closeLb);lb.addEventListener('click',e=>{if(e.target===lb)closeLb()});
  $('.pv',lb).addEventListener('click',e=>{e.stopPropagation();lbI=(lbI-1+lbItems.length)%lbItems.length;lbShow()});
  $('.nx',lb).addEventListener('click',e=>{e.stopPropagation();lbI=(lbI+1)%lbItems.length;lbShow()});
  document.addEventListener('keydown',e=>{if(!lb.classList.contains('open'))return;if(e.key==='ArrowRight')$('.nx',lb).click();if(e.key==='ArrowLeft')$('.pv',lb).click();});
  $$('[data-lb]').forEach(group=>{
    const figs=$$('[data-full]',group);
    figs.forEach((f,i)=>f.addEventListener('click',()=>{const vis=figs.filter(x=>!x.classList.contains('hide'));openLb(vis.map(x=>({src:x.dataset.full,srcset:x.dataset.fullset,cap:x.dataset.cap})),vis.indexOf(f));}));
  });
}

/* ---------- enquiry modal ---------- */
const modal=$('#enquiry');
function openModal(model){if(!modal)return;const sel=$('select[name=model]',modal);if(sel&&model){[...sel.options].forEach(o=>o.selected=o.value===model);}modal.classList.add('open');document.body.classList.add('noscroll');setTimeout(()=>{const f=$('input[name=name]',modal);f&&f.focus()},50);}
function closeModal(){modal&&modal.classList.remove('open');document.body.classList.remove('noscroll');}
$$('[data-enquire]').forEach(b=>b.addEventListener('click',e=>{e.preventDefault();openModal(b.dataset.enquire)}));
if(modal){
  $('.x',modal).addEventListener('click',closeModal);modal.addEventListener('click',e=>{if(e.target===modal)closeModal()});
  if(location.hash==='#contact')openModal();
  const form=$('form',modal);
  form.addEventListener('submit',async e=>{
    e.preventDefault();const btn=$('button[type=submit]',form);btn.disabled=true;
    const fd=new FormData(form);
    try{
      const r=await fetch(form.action.replace('formsubmit.co/','formsubmit.co/ajax/'),{method:'POST',headers:{'Accept':'application/json'},body:fd});
      if(!r.ok)throw new Error('http');
      $('.f-body',modal).hidden=true;$('.f-thanks',modal).hidden=false;
      try{localStorage.setItem('frest_lead',JSON.stringify({name:fd.get('name'),email:fd.get('email'),model:fd.get('model'),t:Date.now()}))}catch(_){}
    }catch(err){form.submit();}
    btn.disabled=false;
  });
  try{const prev=JSON.parse(localStorage.getItem('frest_lead')||'null');if(prev){$('input[name=name]',modal).value=prev.name||'';$('input[name=email]',modal).value=prev.email||'';}}catch(_){}
}

/* ---------- UTM capture into hidden field ---------- */
try{const p=new URLSearchParams(location.search);const utm=['utm_source','utm_medium','utm_campaign','utm_content'].filter(k=>p.get(k)).map(k=>k+'='+p.get(k)).join('&');if(utm)sessionStorage.setItem('frest_utm',utm);const u=sessionStorage.getItem('frest_utm');$$('input[name=_utm]').forEach(i=>i.value=u||'');}catch(_){}

/* ---------- subnav scroll spy ---------- */
const sub=$('.subnav');
if(sub){const links=$$('a[href^="#"]',sub);const secs=links.map(a=>$(a.getAttribute('href'))).filter(Boolean);
  const io=new IntersectionObserver(es=>{es.forEach(en=>{if(en.isIntersecting){links.forEach(a=>a.classList.toggle('on',a.getAttribute('href')==='#'+en.target.id))}})},{rootMargin:'-30% 0px -60% 0px'});secs.forEach(s=>io.observe(s));}

/* ---------- reveal ---------- */
const rv=$$('.rv');
if(rv.length&&'IntersectionObserver' in window){const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.08});rv.forEach(el=>io.observe(el));}else rv.forEach(el=>el.classList.add('in'));

/* ---------- strip drag scroll ---------- */
$$('.strip').forEach(s=>{let down=false,x,sl;s.addEventListener('pointerdown',e=>{down=true;x=e.clientX;sl=s.scrollLeft});s.addEventListener('pointermove',e=>{if(!down)return;s.scrollLeft=sl-(e.clientX-x)});['pointerup','pointerleave'].forEach(ev=>s.addEventListener(ev,()=>down=false));});
})();
