---
title: Geometric Transformations with Homogeneous Coordinates
lecture_date: 2026/09/03
index: 3
---
When expressing two-dimensional points in homogeneous coordinates, the resulting points after transformations will also be in homogeneous coordinates. We'll use this to our advantage to optimize translations.
<div class="image-frame">
    <img src="/CGNotes/assets/hc_scale.png" width="100%"><br>
    <p>Scale matrix using homogeneous coordinates.</p>
</div> 
<div class="image-frame">
    <img src="/CGNotes/assets/hc_rotate.png" width="100%"><br>
    <p>Rotation matrix using homogeneous coordinates.</p>
</div> 
<div class="image-frame">
    <img src="/CGNotes/assets/hc_translate.png" width="100%"><br>
    <p>Translation matrix using homogeneous coordinates.</p>
</div> <br>
Having all three basic operations in homogeneous coordinates with matrix representations, we are now able to include translations into our optimization technique.  
<div class="image-frame">
    <img src="/CGNotes/assets/rotate_anchor.png" width="100%"><br>
    <p>Matrix for rotating around an anchor point (xc, yc).</p>
</div>
We can also use homogeneous coordinates to do other operations around an anchor point.
<div class="image-frame">
    <img src="/CGNotes/assets/scale_anchor.png" width="100%"><br>
    <p>Matrix for scaling around an anchor point (xc, yc).</p>
</div> 
<div class="image-frame">
    <img src="/CGNotes/assets/zoom_anchor.png" width="100%"><br>
    <p>Matrix for zooming from an anchor point (xc, yc) by a scale factor z.</p>
</div>
<br>
<a href="/posts/2026-09-03/matrix_to_transformation">==> Matrix to Transformation</a><br>
<br>
<a href="/posts/2026-09-03/homogeneous_coordinates">Go Back</a>