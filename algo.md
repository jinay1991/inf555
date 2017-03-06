#Preprocessing
The following paragraph is iterated on the images.

## Processing an image

### Generating projection directions
Number of directions: `d = 100`.
Selection of points on a fine mesh of a sphere.
* K-means * (Lloyd algorithm with `k = d`) to determine` centroids' corresponding to the directions. We retain the corresponding directions of the image (among the set of key points linked to this image).

### Rendering of lines
Projection of depth maps of 3D models seen from previously calculated directions.
Application of the Canny filter to extract the contours.

### Calculation of the local characteristic vector
We randomly draw 10 ^ 6 / (Nd) key points on the image.
For each key point, the local characteristic vector (a component vectors n * n *) is computed and stored in a suitable vector structure (`vector`?).


##Representation

### Classification of local feature vectors
An unsupervised classification (* k-means *) is performed on the previously computed VCL, with `k = 1000` (or better` k = 2500`).

### Construction of visual histograms
For each model of the library, and each view of this model, a visual histogram is calculated.
For each view, we create a vector ** h **, histogram. The VCL is computed and the class to which it belongs is noted. The component of the vector ** h ** is then incremented by one unit.
The histogram thus calculated is stored in a reversed data structure (to search the histograms and find corresponding views).



#Querying
Nothing yet ...



# Ideas for Implementation

* A `Histogram` class to store histograms, measure similarity, etc.
* A hash table structure: `Histogram => Model3D` where the 3D model is represented simply by its filename OFF.
* * To be completed ... *: p