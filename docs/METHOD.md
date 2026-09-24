# Computational target

A frozen classifier and fixed calibration pool define a reference quantile. Uniform queries without replacement reveal its true-label scores. The rank recursion in revision6/horizon.py computes boundary-crossing probabilities at declared checkpoints. revision6/sequential.py maps quantile brackets to nested prediction sets and stops at a mean set-size tolerance.

The confidence event conditions on the finite pool and query design. It gives reference-set containment and controls mean extra size on the monitoring batch. It does not establish a new population-coverage guarantee. Boundary tables can be constructed without data using boundary_demo.py.

Main records contain 354 cases on seven datasets. HHAR has a separate protocol and 45 cases. The four-prior and ambiguous-trial sensitivity records retain their original status and values.
