# Food Log for Android

A private food diary for people with gluten allergy. When you think you have been
contaminated, the **Export** button makes an Excel file of what you ate, how much, and
where it came from, so the likely source can be worked out on a computer.

It is a web app that installs on the phone from the browser and then works without a
connection. It runs in Firefox and in Chrome.

## Install

1. Open the app's address on the Android phone. (https://torste1n.github.io/food_log_android/)
2. In Firefox: three-dot menu, then "Add app to Home screen" (or "Install").
   In Chrome: three-dot menu, then "Install app", or use the Install button under Settings.
3. Open it from the home screen from then on.

## What it does

- Log a food with amount (grams or pieces), meal, where it came from, date, time and a note.
- Times are on a 24-hour clock, with no AM or PM.
- The Today screen has seven boxes: Food, Exercise (with an intensity slider and a note),
  Period (with a pain slider and a note), General condition (a slider from 0, bad, to
  10, good, and a note), Bloating (with a severity slider and a note), Contaminated (with
  a time and a note) and Ring (with the date of its next removal). Under Settings each
  box can be switched off or moved, and what is shown is included in the Excel file.
- Saved foods with a portion size, favourites, and saved meals logged with one tap.
- Export: asks "Do you want to generate a file?", then the number of days, and makes an
  Excel file with three sheets: the food log, a row per day, and a row per source.
- History with days logged, the logging streak and the days since each box was last
  ticked, in-app reminders for meals not logged, and a backup file that restores
  the whole app. A backup from the iPhone version can be restored here, and the reverse.
- The back button closes an open form instead of leaving the screen.

## Privacy

The log is stored only on the phone. The app sends nothing anywhere, loads no code from
other sites, and is not allowed to contact any other server. The only contact with its
host is the browser checking for a newer version of the app.

## Files

`index.html`, `styles.css` and `app.js` are the screens; `db.js` is the storage;
`xlsx.js` and `export.js` write the Excel file; `sw.js`
keeps the app available offline. Open `tests.html` to run the app's own checks.
After changing any file, raise `VERSION` in `sw.js` so phones pick up the change.
