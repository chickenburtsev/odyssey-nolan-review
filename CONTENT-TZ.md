# ТЗ по контенту: что ещё нужно

## Срочное: замена второй скролл-сцены

Сцена с конём вышла плавной, потому что там **одно медленное движение камеры вдоль одной оси и почти неподвижный объект**. Штормовая сцена дёргается по обратной причине: камера ходит вместе с плотом, вода движется быстро и хаотично, и при перемотке каждый кадр отличается от соседнего слишком сильно. Скролл-скраббинг усиливает любую тряску: зритель управляет временем рывками, и высокочастотное движение превращается в мельтешение.

**Правило для скролл-видео:** камера идёт по одной оси, медленно и без остановок; в кадре не должно быть быстрого хаотичного движения (брызги, рябь, толпа); никаких склеек и смены плана; никакой дрожащей съёмки с рук.

### Промт для замены (`scrub-storm.mp4` → `scrub-doorway.mp4`)

Смысл сцены — второй акт: «десять лет чужих порогов». Камера медленно отъезжает от освещённой двери, и вокруг разрастается темнота: человек, стоящий у чужого входа, становится всё меньше.

```
Slow continuous dolly-back, single unbroken take, locked horizon: a lone figure in a rough cloak stands at a lit doorway of a stone house at night, seen from outside. The camera retreats steadily and evenly, revealing more and more darkness around the small warm rectangle of the door, until the figure is tiny in a black field. No camera shake, no cuts, no fast motion in frame, no rain, no crowd. Shot on IMAX 65mm film, natural firelight only, deep shadows with detail, heavy film grain, Bronze Age Mediterranean authenticity, photographic realism. No text, no logos.
```

Длина 10–12 секунд, 16:9, без звука. Пришлите исходник — пересжатие с опорным каждым кадром сделаю я.

### Запасной вариант, если первый не выйдет

```
Slow continuous push-in, single unbroken take, camera locked and level: an empty stone threshold at night with a clay oil lamp burning beside it, the doorway dark and open. The camera advances steadily toward the doorway until the dark opening fills the frame. Nothing else moves except the flame. Shot on IMAX 65mm film, firelight only, heavy grain, deep shadows.
```

---

## Замена иллюстрации Сциллы

Прежний вариант забракован: гладкие вертикальные столбы читаются не как шеи чудовища, а как что-то постороннее, и кадр вызывает не тот эффект. Пока на его месте стоит фотография скал. Промт на замену — с опорой на то, что уже сработало: недосказанность сильнее анатомии, масштаб задают люди, чудовище не показывать целиком.

```
Low angle from the deck of a small wooden ship passing through a narrow strait at dusk, seen from among the rowers. High cliffs on both sides. On the left cliff face, high above the men, six long shadows fall across the rock — cast by something outside the frame that is never shown. Spray and mist. Three tiny oarsmen in the foreground for scale, looking up. Shot on IMAX 65mm film, last daylight only, deep shadows with detail, heavy film grain, Bronze Age Mediterranean authenticity, photographic realism. No creature visible, no tentacles, no CGI sheen. No text, no logos.
```

Запасной вариант — со стороны Харибды, без Сциллы вовсе:

```
A wooden ship seen from directly above, tiny against a vast slow whirlpool that fills the frame — smooth concentric rings of dark water, no foam chaos, no monster. Cliffs at the edge of frame for scale. Shot on IMAX 65mm film, flat overcast light, heavy grain, muted Aegean palette. No text, no logos.
```

Формат 21:9 или 16:9, кадрирование и грейд — на мне.

---

## Что ещё нужно, по приоритету

### 1. Музыка — `assets/score.mp3`

Один файл. Рекомендую трек **«Zeus's Law»** (первый в альбоме Горансона): одноимённ проекту, построен на нарастании из тишины, а не на кульминации, и не перетягивает внимание с текста. Пришлите — обрежу до 60–90 секунд по музыкальной фразе и сделаю петлю с кроссфейдом, чтобы стык не был слышен.

### 2. Фрагменты трейлера — `clip-troy.mp4`, `clip-bow.mp4`

По 3–5 секунд, без звука, из официального трейлера. Слоты уже стоят в первом и третьем актах; без файлов блоки просто не показываются. Кадрирование под 2.39:1 и грейд — на мне.

### 3. Запасные кадры — `hero.jpg`, `still-horse.jpg`

На случай, если видео не загрузится (медленная сеть, режим экономии трафика). 16:9 и 21:9 соответственно. Промты есть в `MEDIA.md`.

### 4. Кадры под пустующие смысловые точки

Есть три места, где текст сильный, а изображения нет.

**Пир женихов** — Акт III, к пассажу о том, что женихи это конь наизнанку. 21:9.
```
A Bronze Age hall at night, long tables wrecked by a feast that never ends: gnawed bones, spilled wine, overturned cups, dogs under the benches. A dozen men eating, seen from a low angle from the doorway, faces in shadow. One woman at the far end of the hall, upright and still. Shot on IMAX 65mm film, torchlight only, heavy grain, deep shadows.
```

**Аид** — Акт II, к остановке у мёртвых. 16:9.
```
A pale grey shoreline under a sunless sky, a still black river, and a crowd of indistinct figures standing in the shallows facing the camera — none in focus, none with visible faces. One living man with a bronze sword stands apart in the foreground, seen from behind. Shot on IMAX 65mm film, flat overcast light, heavy grain, no colour saturation.
```

**Итака на рассвете** — Акт III, к возвращению. 21:9.
```
A rocky Greek island seen from the sea at first light: terraced slopes, a few stone houses, olive trees bent by wind, one thin column of smoke. Empty foreground of dark water. Quiet, unremarkable, home. Shot on IMAX 65mm film, natural dawn light, heavy grain.
```

Скажете — добавлю под них слоты.

---

## Общие правила, выведенные из того, что уже сработало

**Масштаб задают люди.** В кадре пещеры сработали три крошечные фигуры с факелами: без них пространство было бы просто тёмным пятном.

**Недосказанность сильнее анатомии.** Циклоп читается как отблеск на плече и одна точка света — и это страшнее показанного чудовища. Сцилла удалась потому, что её «шеи» гладкие и безликие, а не щупальца.

**Не просите «эпично» и «кинематографично».** Модель уходит в глянец, и кадр начинает выглядеть как обложка игры.

**Берите чуть шире нужного.** Генератор ставит в углу мелкую метку, я её обрезаю.

Общий стилевой хвост ко всем промтам:

```
Shot on IMAX 65mm film, natural light only, muted Aegean palette: deep blue-black sea, terracotta, bronze, bone white. Heavy film grain, gentle halation, deep shadows with detail. Bronze Age Mediterranean authenticity, archaeological realism. Photographic, not illustrated. No text, no logos, no recognizable faces.
```

Негативный промт, где есть поле:

```
text, watermark, logo, modern objects, CGI sheen, video game render, fantasy armor, glowing magic, oversaturated, HDR, cartoon, 3D render, recognizable actor, movie still
```

---

## Куда класть

Всё в `assets/` под точными именами. Файла нет — блок не показывается, страница не ломается. После добавления: `python3 tools/build.py`.
