# TWO PATHS TO A ROSTER

**Operator-supplied versus discovered rosters**

![two-paths-to-a-roster](../../assets/exports/two-paths-to-a-roster.png)

| | |
| :--- | :--- |
| Vector | [`assets/vectors/diagrams/two-paths-to-a-roster.svg`](../../assets/vectors/diagrams/two-paths-to-a-roster.svg) |
| Raster | [`assets/exports/two-paths-to-a-roster.png`](../../assets/exports/two-paths-to-a-roster.png) |
| Canvas | 1300 x 980 |
| Type range | 12px - 36px |
| Text nodes | 22 |
| Solid background | yes |
| Blur filters | none |
| Accessible title + desc | yes |

## WHAT IT SHOWS

Path A: the master supplies every chamber title. Path B: he names only the target, and a discovery pass proposes the roster. Both converge on the same research-and-gate pipeline.

## DESIGN NOTE

The ratification box is drawn in the hard-stop colour and given the heaviest stroke on the canvas, because it is the single element that separates a useful discovery pass from an agent granting itself scope. An earlier version drew Path A's connector with an arrowhead that then continued into an elbow - a head mid-path reads as a terminus that is not one, so a headless line() primitive was added.

---

Regenerate with `python3 lib/build_diagrams.py`. The generator refuses to write an
asset that overflows its canvas, uses an invalid text anchor, carries a blur filter,
or drops type below 12px.
