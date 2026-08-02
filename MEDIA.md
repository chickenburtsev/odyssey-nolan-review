# Медиа: что стоит и что можно добавить

Все файлы лежат в `assets/` и подхватываются по имени. Файла нет — блок просто не показывается или показывается запасной вариант; страница не ломается.

## Уже на месте

| Файл | Где | Откуда |
|---|---|---|
| `scrub-horse.mp4` | Акт I, сцена под управлением прокрутки | Veo, пересжато с опорным каждым кадром |
| `scrub-storm.mp4` | Акт II, сцена под управлением прокрутки | Veo, так же |
| `hero-loop.mp4` | фон первого экрана | Veo, склеен в петлю с кроссфейдом |
| `still-threshold.jpg` | Акт I, у определения ксении | Gemini, приведено к палитре |
| `still-cyclops.jpg` | Акт II, пещера с факелом | Gemini |
| `still-scylla.jpg` | Акт II, пролив | Gemini |
| `still-penelope.jpg` | Акт III, зал с луком | Gemini |
| `poster.jpg` | постер проекта | своя графика |
| `still-drag.jpg` | Акт I, коня тащат к воротам (сверхширокий) | кадр фильма |
| `still-troy.jpg` | Акт I, крупный план | кадр фильма |
| `still-sack.jpg` | Акт I, ночь падения Трои | кадр фильма |
| `still-marble.jpg` | Акт I, мрамор и искры | кадр фильма |
| `still-cyclops.jpg` | Акт II, Полифем — работает факелом | кадр фильма |
| `still-bowship.jpg` | Акт II, перебивка про настоящее море | кадр фильма |
| `still-stacks.jpg` | Акт II, скалы в проливе | кадр фильма |
| `still-ramparts.jpg` | Акт III, те, кто держал закон | кадр фильма |
| `still-face.jpg` | Акт III, перед открытым вопросом | кадр фильма |
| `still-imaxset.jpg` | Глава о плёнке, камера на рельсах | кадр со съёмок |
| `still-nolan.jpg` | Глава о плёнке, финальный разворот | кадр со съёмок |

Не вошли: несколько кадров оказались слишком мелкими для полосы во всю ширину (445–640 px)
или дублировали уже занятые смысловые точки. Они лежат у меня, если понадобится замена.

## Чего не хватает

| Файл | Что это | Обязателен? |
|---|---|---|
| `score.mp3` | музыка под кнопкой «Звук» | нет, сейчас играет синтезированное море |
| `clip-troy.mp4` | фрагмент трейлера, Акт I | нет, блок скрыт без файла |
| `clip-bow.mp4` | фрагмент трейлера, Акт III | нет, то же |
| `still-horse.jpg` | запасной кадр, если видео не загрузится | желательно |
| `hero.jpg` | запасной фон первого экрана | желательно |

Кадры из фильма подписаны как промоматериал с указанием правообладателя и приведены в объёме, обычном для критического разбора. Если правообладатель попросит их убрать — достаточно удалить файлы из `assets/`, вёрстка не сломается.

**Музыка.** Нужен один файл `score.mp3`. Рекомендую **«Zeus's Law»** — первый трек альбома Горансона: одноимённ проекту, построен на нарастании из тишины, а не на кульминации, и не перетягивает внимание с текста. Пришлите — обрежу до 60–90 секунд по музыкальной фразе и сделаю петлю с кроссфейдом, чтобы стык не был слышен.

**Фрагменты трейлера.** По 3–5 секунд, без звука, из официального трейлера. Кадрирование и приведение к палитре — на мне.

---

## Промты с учётом того, что уже выяснилось

Что сработало в прошлый раз и почему — стоит повторять. **Масштаб через людей**: в кадре пещеры сработали три крошечные фигуры с факелами, они сделали пространство огромным. **Недосказанность вместо анатомии**: циклоп читается как отблеск на плече и одна точка света, и это страшнее, чем показанное чудовище; Сцилла удалась потому, что её «шеи» — гладкие безликие формы, а не щупальца. **Одно непрерывное движение камеры** в видео: никаких склеек, иначе прокрутка будет дёргаться.

Чего избегать. Не просите «эпично» и «кинематографично» — модель уходит в глянец. Не описывайте монстров анатомически. Не забывайте, что генератор ставит в углу мелкую метку — берите чуть шире, чем нужно, я обрежу.

Ко всем промтам добавляйте хвост:

```
Shot on IMAX 65mm film, natural light only, muted Aegean palette: deep blue-black sea, terracotta, bronze, bone white. Heavy film grain, gentle halation, deep shadows with detail. Bronze Age Mediterranean authenticity, archaeological realism. Photographic, not illustrated. No text, no logos, no recognizable faces.
```

Негативный промт, где есть отдельное поле:

```
text, watermark, logo, modern objects, CGI sheen, video game render, fantasy armor, glowing magic, oversaturated, HDR, cartoon, 3D render, recognizable actor, movie still
```

### `hero.jpg` — 16:9, запасной фон первого экрана

```
A vast dark Aegean sea at night seen from a low cliff, long moonlight path breaking on slow heavy swells, distant horizon barely visible, faint stars, cold blue-black water, completely empty — no boats, no people. The upper third of the frame must stay dark and empty, reserved for a title.
```

### `still-horse.jpg` — 21:9 или шире

```
A colossal weathered wooden horse built from massive timber beams, standing half-buried in wet sand on an empty beach at cold dawn. Low sea mist around its legs, gentle surf, a broken spear shaft in the foreground. Rim light along its back against a pale sunrise. Low camera angle looking slightly up.
```

### Если захотите ещё сцены

Свободные места есть в Акте II и Акте III — скажите, добавлю слоты.

**Пир женихов, 21:9.** `A Bronze Age hall at night, long tables wrecked by a feast that never ends: gnawed bones, spilled wine, overturned cups, dogs under the benches. A dozen men eating, seen from a low angle from the doorway, their faces in shadow. One woman at the far end of the hall, upright and still.`

**Аид, 16:9.** `A pale grey shoreline under a sunless sky, a still black river, and a crowd of indistinct figures standing in the shallows facing the camera — none in focus, none with visible faces. One living man with a bronze sword stands apart in the foreground, seen from behind.`

**Итака на рассвете, 21:9.** `A rocky Greek island seen from the sea at first light: terraced slopes, a few stone houses, olive trees bent by wind, one thin column of smoke. Empty foreground of dark water. Quiet, unremarkable, home.`

### Видео

Все ролики: 8–10 секунд, без звука, 16:9, **одно непрерывное движение камеры, никаких склеек**.

**`clip`-заменители, если трейлер брать не станете.** Вместо фрагментов трейлера можно сгенерировать свои: `Slow lateral tracking shot through a dim Bronze Age great hall lit by wall torches: wrecked tables, spilled wine, empty benches, a loom in the far shadows. Camera glides steadily left to right, single unbroken take.`

Присылайте как есть — пересжатие под прокрутку (`-g 1`, каждый кадр опорный), кадрирование и грейд под палитру страницы сделаю я.
