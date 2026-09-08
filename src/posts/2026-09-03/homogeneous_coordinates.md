---
title: Homogeneous Coordinates
lecture_date: 2026/09/03
index: 1
---
<div class="subcard">
	<h3 class="icon">Definition</h3>
	<p>Given a point Q = [ x, y, w ] in homogeneous coordinates, Q corresponds to a point P = [ x / w, y / w ], where w represents a weight that can be any number <span class="keyword"><b>(even 1 or 0)</b></span>.</p>
	<p>This concept applies for any number of dimensions.</p>
</div><br> 
Some examples:
<div class="comment">
    <p>Q = [90, 30, 10] ⇒ P = [9, 3]</p>
</div>
<div class="comment">
    <p>Q = [1, 2, 2] ⇒ P = [0.5, 1]</p>
</div>
<div class="comment">
    <p>Q = [4, 1, 3] ⇒ P = [1.33..., 0.33...]</p>
</div>
<div class="comment">
    <p>Q = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] ⇒</p>
    <p>P = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]</p>
</div>
Note that the last element in homogeneous coordinates represents the weight in non-homogeneous coordinates no matter the amount of dimensions.
<br>
<br>
<a href="/posts/2026-09-03/geometric_transformations_with_hc">==> Geometric Transformations with Homogeneous Coordinates</a><br> 
<br> 
<a href="/posts/2026-09-03/combining_geometric_trans">Go Back</a>