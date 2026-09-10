/* Frest Homes — editorial runtime (shared patterns with elsoco.com) */
(function(){
'use strict';
const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];
const L=document.documentElement.lang||'lv';
const fmtEur=n=>new Intl.NumberFormat(L==='lv'?'lv-LV':'en-GB',{style:'currency',currency:'EUR',maximumFractionDigits:0}).format(n);

/* nav */
/* dropdowns: hover-intent with a close delay so the pointer can travel to the menu */
$$('.nav li.dd').forEach(li=>{const b=$('button',li);let t=null;
  const open=()=>{clearTimeout(t);$$('.nav li.dd.open').forEach(x=>x!==li&&x.classList.remove('open'));li.classList.add('open');b.setAttribute('aria-expanded','true')};
  const close=()=>{li.classList.remove('open');b.setAttribute('aria-expanded','false')};
  const later=()=>{clearTimeout(t);t=setTimeout(close,260)};
  b.setAttribute('aria-expanded','false');b.setAttribute('aria-haspopup','true');
  b.addEventListener('click',e=>{e.stopPropagation();li.classList.contains('open')?close():open()});
  li.addEventListener('mouseenter',open);li.addEventListener('mouseleave',later);
  li.addEventListener('focusin',open);li.addEventListener('focusout',e=>{if(!li.contains(e.relatedTarget))close()});
  $$('a',li).forEach(a=>a.addEventListener('click',e=>e.stopPropagation()));});
document.addEventListener('click',()=>$$('.nav li.dd.open').forEach(x=>{x.classList.remove('open');const b=$('button',x);b&&b.setAttribute('aria-expanded','false')}));
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
  const pick=id=>{btns.forEach(b=>b.classList.toggle('on',b.dataset.id===id));imgs.forEach(i=>i.classList.toggle('on',i.dataset.id===id));const b=btns.find(x=>x.dataset.id===id);sum.textContent=fmtEur(base+(+b.dataset.price));if(area)area.textContent=(baseArea+(+b.dataset.area))+' m²';const nm=$('[data-addon-name]',ad),tx=$('[data-addon-text]',ad);if(nm)nm.textContent=b.dataset.name||'';if(tx)tx.textContent=b.dataset.text||''};
  btns.forEach(b=>b.addEventListener('click',()=>pick(b.dataset.id)));pick(btns[0].dataset.id);});

/* ---- house finder -------------------------------------------------------------------
   Three questions, one recommendation. The rail doubles as a back control: an answered
   step stays clickable so a visitor can change their mind without starting over. */
$$('[data-qz]').forEach(qz=>{
  const models=JSON.parse(qz.dataset.qz);
  const steps=$$('.qz-step',qz), rails=$$('.qz-rail button',qz), res=$('.qz-res',qz);
  const back=$('[data-qz-back]',qz), again=$('[data-qz-restart]',qz);
  const ids=steps.map(s=>$('.qz-opt',s).dataset.q);
  let ans={}, n=0;

  const label=(i)=>{const b=$('.qz-opt[data-v="'+ans[ids[i]]+'"]',steps[i]);return b?$('b',b).textContent:''};
  const paint=()=>{
    steps.forEach((s,i)=>s.classList.toggle('on',i===n && !res.classList.contains('on')));
    rails.forEach((r,i)=>{
      const answered=ans[ids[i]]!==undefined;
      r.classList.toggle('on',i===n && !res.classList.contains('on'));
      r.classList.toggle('done',answered && i!==n);
      r.disabled = !answered && i!==n;
      $('[data-qz-ans]',r).textContent = answered ? label(i) : '';
    });
    steps.forEach((s,i)=>$$('.qz-opt',s).forEach(b=>b.classList.toggle('picked',b.dataset.v===ans[ids[i]])));
    back.hidden = res.classList.contains('on') || n===0;
    again.hidden = !res.classList.contains('on');
  };
  const go=k=>{res.classList.remove('on');n=Math.max(0,Math.min(steps.length-1,k));paint()};

  const decide=()=>{const big=ans.who==='family-big',small=ans.who==='couple';
    let series=ans.style||'aura';
    let size=big?'110':small?'70':(ans.budget==='gt140'?'110':'70');
    if(ans.budget==='lt140')size='70';
    return series+'-'+size};

  const finish=()=>{
    const m=models[decide()]; if(!m)return;
    $('[data-r-name]',res).textContent=m.name;
    $('[data-r-tag]',res).textContent=m.tagline||'';
    $('[data-r-why]',res).textContent=m.why||'';
    $('[data-r-pills]',res).innerHTML=(m.pills||[]).map(x=>'<span>'+x+'</span>').join('');
    const im=$('img',res); im.src=m.img; im.srcset=m.srcset||''; im.alt=m.name;
    $('a[data-r-link]',res).href=m.url;
    steps.forEach(s=>s.classList.remove('on'));
    res.classList.add('on');
    rails.forEach(r=>{r.classList.remove('on');r.classList.add('done')});
    paint();
  };

  $$('.qz-opt',qz).forEach(b=>b.addEventListener('click',()=>{
    ans[b.dataset.q]=b.dataset.v;
    if(n<steps.length-1 && ids.slice(0,n+2).some(id=>ans[id]===undefined)) go(n+1);
    else if(ids.some(id=>ans[id]===undefined)) go(ids.findIndex(id=>ans[id]===undefined));
    else finish();
  }));
  rails.forEach((r,i)=>r.addEventListener('click',()=>{if(!r.disabled)go(i)}));
  back.addEventListener('click',()=>go(n-1));
  again.addEventListener('click',()=>{ans={};res.classList.remove('on');go(0)});
  paint();
});

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
const sub=$('.subnav');if(sub){const links=$$('a[href^="#"]',sub);const secs=links.map(a=>$(a.getAttribute('href'))).filter(Boolean);const io=new IntersectionObserver(es=>{es.forEach(en=>{if(en.isIntersecting)links.forEach(a=>a.classList.toggle('on',a.getAttribute('href')==='#'+en.target.id))})},{rootMargin:'-30% 0px -60% 0px'});secs.forEach(s=>io.observe(s));if(links[0]&&scrollY<40)links.forEach((a,i)=>a.classList.toggle('on',i===0));addEventListener('scroll',()=>{if(scrollY<40)links.forEach((a,i)=>a.classList.toggle('on',i===0))},{passive:true})}
const rv=$$('.rv');if(rv.length&&'IntersectionObserver' in window){const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}}),{threshold:.08});rv.forEach(el=>io.observe(el))}else rv.forEach(el=>el.classList.add('in'));
$$('.strip').forEach(s=>{let down=false,x,sl;s.addEventListener('pointerdown',e=>{down=true;x=e.clientX;sl=s.scrollLeft});s.addEventListener('pointermove',e=>{if(!down)return;s.scrollLeft=sl-(e.clientX-x)});['pointerup','pointerleave'].forEach(ev=>s.addEventListener(ev,()=>down=false))});
/* enquiry form AJAX (FormSubmit) */
const cf=m&&$('form',m);
if(cf){cf.addEventListener('submit',async e=>{e.preventDefault();const btn=$('button[type=submit]',cf);btn.disabled=true;const fd=new FormData(cf);
  try{const r=await fetch(cf.action.replace('formsubmit.co/','formsubmit.co/ajax/'),{method:'POST',headers:{'Accept':'application/json'},body:fd});if(!r.ok)throw 0;$('.cform .f-body',m).hidden=true;$('.cform .f-thanks',m).hidden=false;try{localStorage.setItem('frest_lead',JSON.stringify({name:fd.get('name'),email:fd.get('email')}))}catch(_){}}
  catch(err){cf.submit()}btn.disabled=false});
  try{const prev=JSON.parse(localStorage.getItem('frest_lead')||'null');if(prev){$('input[name=name]',cf).value=prev.name||'';$('input[name=email]',cf).value=prev.email||''}}catch(_){}}
/* ---- hero slideshow ---------------------------------------------------------------- */
$$('[data-hs]').forEach(hs=>{
  const slides=$$('.hs-slide',hs), caps=$$('.hs-cap',hs), dots=$$('.hs-dots button',hs);
  if(slides.length<2){return}
  let i=0, timer=null, paused=false;
  const DUR=6500, reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
  const show=n=>{i=(n+slides.length)%slides.length;
    slides.forEach((s,k)=>s.classList.toggle('on',k===i));
    caps.forEach((c,k)=>c.classList.toggle('on',k===i));
    dots.forEach((d,k)=>{d.classList.toggle('on',k===i);d.setAttribute('aria-selected',k===i)});
    const im=slides[i].querySelector('img'); if(im&&im.loading==='lazy'){im.loading='eager'}
    const nx=slides[(i+1)%slides.length].querySelector('img'); if(nx&&nx.loading==='lazy'){nx.loading='eager'}};
  const play=()=>{if(reduce||paused)return;clearInterval(timer);timer=setInterval(()=>show(i+1),DUR)};
  const stop=()=>clearInterval(timer);
  $('.hs-arrow.n',hs).addEventListener('click',()=>{show(i+1);play()});
  $('.hs-arrow.p',hs).addEventListener('click',()=>{show(i-1);play()});
  dots.forEach((d,k)=>d.addEventListener('click',()=>{show(k);play()}));
  hs.addEventListener('mouseenter',()=>{paused=true;stop()});
  hs.addEventListener('mouseleave',()=>{paused=false;play()});
  hs.addEventListener('focusin',()=>{paused=true;stop()});
  hs.addEventListener('focusout',e=>{if(!hs.contains(e.relatedTarget)){paused=false;play()}});
  document.addEventListener('visibilitychange',()=>document.hidden?stop():play());
  document.addEventListener('keydown',e=>{if(e.key==='ArrowRight'&&!$('.cmodal.open')){show(i+1);play()}if(e.key==='ArrowLeft'&&!$('.cmodal.open')){show(i-1);play()}});
  let x0=null;hs.addEventListener('touchstart',e=>{x0=e.touches[0].clientX},{passive:true});
  hs.addEventListener('touchend',e=>{if(x0===null)return;const dx=e.changedTouches[0].clientX-x0;if(Math.abs(dx)>44){show(i+(dx<0?1:-1));play()}x0=null},{passive:true});
  show(0);play();
});



/* ---- custom-design hero rotation: quick enough that a visitor notices it move ---- */
$$('[data-chero]').forEach(el=>{
  const slides=$$('.chero-slide',el), dots=$$('.chero-dots button',el);
  if(slides.length<2)return;
  const reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
  let i=0,timer=null,paused=false;
  const show=n=>{i=(n+slides.length)%slides.length;
    slides.forEach((s,k)=>s.classList.toggle('on',k===i));
    dots.forEach((d,k)=>d.classList.toggle('on',k===i))};
  const start=()=>{if(reduce||paused)return;clearInterval(timer);timer=setInterval(()=>show(i+1),3400)};
  dots.forEach((d,k)=>d.addEventListener('click',()=>{show(k);start()}));
  el.addEventListener('pointerenter',()=>{paused=true;clearInterval(timer)});
  el.addEventListener('pointerleave',()=>{paused=false;start()});
  document.addEventListener('visibilitychange',()=>document.hidden?clearInterval(timer):start());
  start();
});
})();
