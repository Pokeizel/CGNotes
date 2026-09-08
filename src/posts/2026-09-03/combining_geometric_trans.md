---
title: Combining Geometric Transformations
lecture_date: 2026/09/03
index: 1
---
Performing operations one after another can be costly, specially with polygons of many points. Fortunately, scale and rotation both involve linear transformations between matrices, so, <img height="21px" src="https://cdn3.emoji.gg/emojis/1685-nerd.png"> <i>by the associative property of matrix multiplication</i>, they can be calculated together before multiplying the point vector with the result and we can <a target="_blank" href="https://youtu.be/6ERddYRZU0E?t=60">save dort processing time</a>.  
<br>
An example: we want to scale a scene with a gazillion points and then rotate it. Instead of computing the same operation for all gazillion points, we calculate the products of transformation first, and then multiply that result with each point. It's still around 4 gazillion operations, but it's much better than 8 gazillion, which is how many it would take without this optimization.  
<br>
What about translations, though? Can they join the optimization club along with scale and rotation, or are they not cool enough? Since a translation does not involve a matrix multiplication, it can't be easily lumped together with the rest of operations to calculate beforehand. For that, we'll have to take a different approach.  
<br>
<a href="/posts/2026-09-03/homogeneous_coordinates">==> Homogeneous Coordinates</a>  
<br>
<a href="/posts/2026-09-03/polygon_rotation">Go Back</a>