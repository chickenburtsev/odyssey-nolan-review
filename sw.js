const C='xenia-0b8b002a';
const CORE=['./','./en/','./manifest.webmanifest','./en/manifest.webmanifest',
 './assets/still-threshold.jpg','./assets/still-cyclops.jpg','./assets/still-scylla.jpg','./assets/still-penelope.jpg',
 './assets/still-horse.jpg','./assets/still-storm.jpg'];
self.addEventListener('install',e=>{self.skipWaiting();
  e.waitUntil(caches.open(C).then(c=>Promise.allSettled(CORE.map(u=>c.add(u)))));});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(k=>
  Promise.all(k.filter(x=>x!==C).map(x=>caches.delete(x)))).then(()=>self.clients.claim()));});
self.addEventListener('fetch',e=>{
  const r=e.request; if(r.method!=='GET') return;
  if(r.headers.get('range')) return;           // видео отдаём сети
  e.respondWith(caches.match(r).then(hit=>hit||fetch(r).then(res=>{
    if(res.ok && res.type==='basic' && !/\.(mp4|webm|mp3)$/i.test(new URL(r.url).pathname)){
      const cp=res.clone(); caches.open(C).then(c=>c.put(r,cp));
    } return res;
  }).catch(()=>caches.match(/\/en\//.test(new URL(r.url).pathname)?'./en/':'./'))));});
