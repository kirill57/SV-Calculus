settings.tex="none";
settings.render=0;
settings.prc=false;

import graph3;
import solids;

size(450);
viewportmargin = (8, 12);
currentprojection = orthographic(-3.2, 1.75, -7.6, up=Y);
currentlight = light(white, specularfactor=1, (-4, 10, -6));

real R = 2;

triple F(real t) {
  return (R * cos(t), R * sin(t), 0);
}

path3 gen = graph(F, 0, pi, n=64, operator ..);
path3 genmesh = graph(F, 0, pi, n=16, operator ..);

revolution sph = revolution(genmesh, X);
pen surfpen = rgb(0.68, 0.80, 0.94) + opacity(0.28);
pen meshpen = gray(0.55) + opacity(0.40);
draw(surface(sph, 12), surfpen, meshpen=meshpen);

path3 bandarc = graph(F, 0.95, 1.25, n=8, operator ..);
draw(surface(revolution(bandarc, X), 24), rgb(0.22, 0.42, 0.82) + opacity(0.70));

draw(gen, black + 2bp);

real[] ts = {acos(0.6), pi / 2, pi - acos(0.6)};
for (real t : ts)
  draw(circle((R * cos(t), 0, 0), R * sin(t), X), dashed + 0.8bp);

xaxis3(Label("x", 1), xmin=-1.35 * R, xmax=1.55 * R, Arrow3);
yaxis3(Label("y", 1), ymin=0, ymax=1.18 * R, Arrow3);
zaxis3(Label("z", 1), zmin=-0.62 * R, zmax=0.62 * R, Arrow3);

draw(O -- (0, R, 0));
label("R", (0, 0.52 * R, 0), E);

label("x = R cos t, y = R sin t", (0, 1.45 * R, 0));
label("rotating the upper semicircle gives a sphere", (0, -1.38 * R, 0));
      