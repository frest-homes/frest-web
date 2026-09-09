/* Frest Homes — editorial runtime (shared patterns with elsoco.com) */
(function(){
'use strict';
const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
const L=document.documentElement.lang||'lv';
const fmtEur=n=>new Intl.NumberFormat(L==='lv'?'lv-LV':'en-GB',{style:'currency',currency:'EUR',maximumFractionDigits:0}).format(n);

/* nav */
$$('.nav li.dd').forEach(li=>{const b=$('button',li);b.addEventListener('click',e=>{e.stopPropagation();const o=li.classList.contains('open');$$('.nav li.dd.open').forEach(x=>x.classList.remove('open'));if(!o)li.classList.add('open');});
  li.addEventListener('mouseenter',()=>{$$('.nav li.dd.open').forEach(x=>x!==li&&x.classList.remove('open'));li.classList.add('open')});li.addEventListener('mouseleave',()=>li.classList.remove('open'));});
document.addEventListener('click',()=>$$('.nav li.dd.open').forEach(x=>x.classList.remove('open')));
const bg=$('[data-burger]'),mn=$('#mnav');
if(bg&&mn){bg.addEventListener('click',()=>{const o=mn.classList.toggle('open');bg.setAttribute('aria-expanded',o);bg.textContent=o?bg.dataset.close:bg.dataset.open;document.body.style.overflow=o?'hidden':''});}

/* contact modal (El Soco pattern) */
const m=$('#contact');
function openC(model){if(!m)return;if(mn){mn.classList.remove('open');if(bg)bg.textContent=bg.dataset.open}const sel=$('select[name=model]',m);if(sel&&model){[...sel.options].forEach(o=>o.selected=o.value===model)}m.classList.add('open');document.body.style.overflow='hidden';const f=$('input[name=name]',m);f&&f.focus();try{sessionStorage.setItem('frest_contact','1')}catch(e){}}
function closeC(){if(!m)return;m.classList.remove('open');document.body.style.overflow=''}
$$('[data-open-contact]').forEach(a=>a.addEventListener('click',e=>{e.preventDefault();openC(a.dataset.openContact||'')}));
$$('[data-close-contact]').forEach(a=>a.addEventListener('click',closeC));
if(m){m.addEventListener('click',e=>{if(e.target===m)closeC()});
  if(location.hash==='#contact')openC();
  if(/[?&]sent=1/.test(location.search)){const t=document.createElement('div');t.className='toast';t.textContent=m.dataset.thanks;document.body.appendChild(t);setTimeout(()=>t.classList.add('off'),7000);try{history.replaceState(null,'',location.pathname)}catch(e){}}
  let seen=false;try{seen=sessionStorage.getItem('frest_contact')==='1'}catch(e){}
  if(!seen&&document.body.dataset.autocontact==='1'){setTimeout(()=>{if(!m.classList.contains('open')&&document.visibilityState==='visible'&&!$('.lb.open'))openC();},45000);}
  try{const p=new URLSearchParams(location.search);const utm=['utm_source','utm_medium','utm_campaign','utm_content'].filter(k=>p.get(k)).map(k=>k+'='+p.get(k)).join('&');if(utm)sessionStorage.setItem('frest_utm',utm);const u=sessionStorage.getItem('frest_utm');$$('input[name=_utm]').forEach(i=>i.value=u||'');}catch(e){}
}
document.addEventListener('keydown',e=>{if(e.key==='Escape'){closeC();closeLb();if(mn&&mn.classList.contains('open')){mn.classList.remove('open');bg.textContent=bg.dataset.open;document.body.style.overflow=''}}});

/* audience selector */
const aud=$('#aud');
if(aud){const data=JSON.parse(aud.dataset.aud);const h=$('#audh'),p=$('#audp'),l=$('#audl');
  const show=k=>{$$('button',aud).forEach(b=>b.classList.toggle('on',b.dataset.aud===k));const d=data[k];h.textContent=d.h;p.textContent=d.p;l.innerHTML='<a href="'+d.href+'">'+d.link+'</a>';try{localStorage.setItem('frest_aud',k)}catch(e){}};
  $$('button',aud).forEach(b=>b.addEventListener('click',()=>show(b.dataset.aud)));
  let k='all';try{k=localStorage.getItem('frest_aud')||'all'}catch(e){}if(!data[k])k='all';show(k);}

/* personaliser */
$$('[data-personalise]').forEach(pz=>{
  const data=JSON.parse(pz.dataset.personalise);const stage=$('.stage',pz),out=$('.cfg-now b',pz),capEl=$('.stage figcaption',pz);
  let model=pz.dataset.model||Object.keys(data.models)[0],roof='tile',color=pz.dataset.color||'nordic-gray';const cache={};
  const src=(mm,r,c)=>data.models[mm].facades[r][c];
  function render(){const s=src(model,roof,color);let img=cache[s.src];if(!img){img=new Image();img.alt='';img.src=s.src;img.srcset=s.srcset;img.sizes='(max-width:900px) 100vw, 58vw';cache[s.src]=img;stage.insertBefore(img,capEl)}
    $$('img',stage).forEach(x=>x.classList.toggle('on',x===img));$$('.sw',pz).forEach(b=>b.classList.toggle('on',b.dataset.color===color));$$('.seg button',pz).forEach(b=>b.classList.toggle('on',b.dataset.roof===roof));$$('.models-pick button',pz).forEach(b=>b.classList.toggle('on',b.dataset.model===model));
    const cn=data.colors.find(c=>c.id===color).name,rn=data.roofs.find(r=>r.id===roof).name;const txt=data.models[model].name+' · '+cn+' · '+rn;if(out)out.textContent=txt;if(capEl)capEl.textContent=txt;$$('a[data-model-link]',pz).forEach(a=>a.href=data.models[model].url);
    data.colors.forEach(c=>{const k=src(model,roof,c.id);if(!cache[k.src]){const pi=new Image();pi.src=k.src}});}
  $$('.sw',pz).forEach(b=>b.addEventListener('click',()=>{color=b.dataset.color;render()}));$$('.seg button',pz).forEach(b=>b.addEventListener('click',()=>{roof=b.dataset.roof;render()}));$$('.models-pick button',pz).forEach(b=>b.addEventListener('click',()=>{model=b.dataset.model;render()}));render();});

/* plan viewer */
$$('[data-plan]').forEach(pl=>{const imgs=$$('.stage img',pl),tabs=$$('.tabs button',pl);const show=id=>{imgs.forEach(i=>i.classList.toggle('on',i.dataset.id===id));tabs.forEach(t=>t.classList.toggle('on',t.dataset.id===id))};tabs.forEach(t=>t.addEventListener('click',()=>show(t.dataset.id)));show(tabs[0]&&tabs[0].dataset.id);});

/* add-ons */
$$('[data-addons]').forEach(ad=>{const base=+ad.dataset.base,btns=$$('.addon-list button',ad),imgs=$$('.stage img',ad),sum=$('.addon-sum b',ad),area=$('.addon-sum [data-area]',ad),baseArea=+ad.dataset.area;
  const pick=id=>{btns.forEach(b=>b.classList.toggle('on',b.dataset.id===id));imgs.forEach(i=>i.classList.toggle('on',i.dataset.id===id));const b=btns.find(x=>x.dataset.id===id);sum.textContent=fmtEur(base+(+b.dataset.price));if(area)area.textContent=(baseArea+(+b.dataset.area))+' m²'};
  btns.forEach(b=>b.addEventListener('click',()=>pick(b.dataset.id)));pick(btns[0].dataset.id);});

/* quiz */
$$('[data-quiz]').forEach(q=>{const models=JSON.parse(q.dataset.quiz);const steps=$$('.step',q),prog=$$('.prog i',q),res=$('.res',q);let ans={},n=0;
  const show=k=>{n=k;steps.forEach((s,i)=>s.classList.toggle('on',i===k));prog.forEach((p,i)=>p.classList.toggle('on',i<=k));res.classList.remove('on')};
  const decide=()=>{const big=ans.who==='family-big',small=ans.who==='couple';let series=ans.style||'aura';let size=big?'110':small?'70':(ans.budget==='gt140'?'110':'70');if(ans.budget==='lt140')size='70';return series+'-'+size};
  $$('.opts button',q).forEach(b=>b.addEventListener('click',()=>{ans[b.dataset.q]=b.dataset.v;if(n<steps.length-1)show(n+1);else{const slug=decide(),mm=models[slug];steps.forEach(s=>s.classList.remove('on'));prog.forEach(p=>p.classList.add('on'));$('[data-r-name]',res).textContent=mm.name;$('[data-r-why]',res).textContent=mm.why;$('[data-r-facts]',res).textContent=mm.facts;const im=$('img',res);im.src=mm.img;im.srcset=mm.srcset;$('a[data-r-link]',res).href=mm.url;res.classList.add('on')}}));
  $('[data-restart]',q).addEventListener('click',()=>{ans={};show(0)});show(0);});

/* compare */
const diff=$('#diffOnly');if(diff){diff.addEventListener('change',()=>$$('.cmp tr.same').forEach(r=>r.classList.toggle('hide',diff.checked)))}

/* gallery filters */
$$('[data-gallery]').forEach(g=>{const btns=$$('.filters button',g),items=$$('.gitem',g);btns.forEach(b=>b.addEventListener('click',()=>{btns.forEach(x=>x.classList.toggle('on',x===b));const f=b.dataset.f;items.forEach(it=>it.classList.toggle('hide',f!=='all'&&!(' '+it.dataset.tags+' ').includes(' '+f+' ')))}));if(location.hash){const b=btns.find(x=>'#'+x.dataset.f===location.hash);b&&b.click()}});

/* lightbox */
let lbItems=[],lbI=0;const lb=$('#lb');
function openLb(items,i){lbItems=items;lbI=i;lbShow();lb.classList.add('open');document.body.style.overflow='hidden'}
function lbShow(){const it=lbItems[lbI];$('img',lb).src=it.src;$('img',lb).srcset=it.srcset||'';$('.cap',lb).innerHTML=(it.cap?'<b>'+it.cap+'</b>':'')+(it.desc||'')}
function closeLb(){if(lb&&lb.classList.contains('open')){lb.classList.remove('open');document.body.style.overflow=''}}
if(lb){$('.x',lb).addEventListener('click',closeLb);lb.addEventListener('click',e=>{if(e.target===lb)closeLb()});
  $('.pv',lb).addEventListener('click',e=>{e.stopPropagation();lbI=(lbI-1+lbItems.length)%lbItems.length;lbShow()});$('.nx',lb).addEventListener('click',e=>{e.stopPropagation();lbI=(lbI+1)%lbItems.length;lbShow()});
  document.addEventListener('keydown',e=>{if(!lb.classList.contains('open'))return;if(e.key==='ArrowRight')$('.nx',lb).click();if(e.key==='ArrowLeft')$('.pv',lb).click()});
  $$('[data-lb]').forEach(group=>{const figs=$$('[data-full]',group);figs.forEach(f=>f.addEventListener('click',()=>{const vis=figs.filter(x=>!x.classList.contains('hide'));openLb(vis.map(x=>({src:x.dataset.full,srcset:x.dataset.fullset,cap:x.dataset.cap,desc:x.dataset.desc})),vis.indexOf(f))}))});}

/* subnav spy, reveal, strip drag */
const sub=$('.subnav');if(sub){const links=$$('a[href^="#"]',sub);const secs=links.map(a=>$(a.getAttribute('href'))).filter(Boolean);const io=new IntersectionObserver(es=>{es.forEach(en=>{if(en.isIntersecting)links.forEach(a=>a.classList.toggle('on',a.getAttribute('href')==='#'+en.target.id))})},{rootMargin:'-30% 0px -60% 0px'});secs.forEach(s=>io.observe(s))}
const rv=$$('.rv');if(rv.length&&'IntersectionObserver' in window){const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.08});rv.forEach(el=>io.observe(el))}else rv.forEach(el=>el.classList.add('in'));
$$('.strip').forEach(s=>{let down=false,x,sl;s.addEventListener('pointerdown',e=>{down=true;x=e.clientX;sl=s.scrollLeft});s.addEventListener('pointermove',e=>{if(!down)return;s.scrollLeft=sl-(e.clientX-x)});['pointerup','pointerleave'].forEach(ev=>s.addEventListener(ev,()=>down=false))});
/* enquiry form AJAX (FormSubmit) */
const cf=m&&$('form',m);
if(cf){cf.addEventListener('submit',async e=>{e.preventDefault();const btn=$('button[type=submit]',cf);btn.disabled=true;const fd=new FormData(cf);
  try{const r=await fetch(cf.action.replace('formsubmit.co/','formsubmit.co/ajax/'),{method:'POST',headers:{'Accept':'application/json'},body:fd});if(!r.ok)throw 0;$('.cform .f-body',m).hidden=true;$('.cform .f-thanks',m).hidden=false;try{localStorage.setItem('frest_lead',JSON.stringify({name:fd.get('name'),email:fd.get('email')}))}catch(_){}}
  catch(err){cf.submit()}btn.disabled=false});
  try{const prev=JSON.parse(localStorage.getItem('frest_lead')||'null');if(prev){$('input[name=name]',cf).value=prev.name||'';$('input[name=email]',cf).value=prev.email||''}}catch(_){}}
})();
