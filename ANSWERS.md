## Running the code/tests
Install `pytest`, `pytest-benchmark`, and `numpy` using your package manager of choice.

```
conda install pytest pytest-benchmark numpy
```
or
```
pip install pytest pytest-benchmark numpy
```

The tests and benchmarks can be run simply with
```
pytest .
```

## Question 1
In `answers.py` I've added 3 different solutions to the problem.

`brute_force` is the most simple solution where we compute each pairwise difference between the 2 lists. For very large inputs, we quickly run into performance issues with this approach.

`two_pointers` is a more optimized approach that sorts the 2 lists and then uses 2 pointers to compare elements that are closest in value. For very large inputs or strict performance requirements, this would be the approach to use.

`numpy_subtract` uses the same idea as the brute force approach, however we leverage numpy's vectorization to compute the pairwise difference faster. This result in a significant speedup over the brute force approach, but still not quite as fast as the two pointer approach. This solution is a good middle ground that was quick to write and probably fast enough more most use cases.

## Question 2

I've added benchmarks for each of the 3 methods in `test_answers.py`. This is the output of those benchmarks:

```

-------------------------------------------------------------------------------------------------- benchmark: 3 tests --------------------------------------------------------------------------------------------------
Name (time in us)                      Min                     Max                    Mean              StdDev                  Median                 IQR            Outliers         OPS            Rounds  Iterations
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_two_pointers_bench           488.6070 (1.0)        1,369.6500 (1.0)          507.4914 (1.0)       69.2814 (1.0)          492.9885 (1.0)        3.7025 (1.0)         36;82  1,970.4768 (1.0)         672           1
test_numpy_subtract_bench       3,103.5710 (6.35)       4,893.9220 (3.57)       3,453.4706 (6.80)     235.0914 (3.39)       3,512.6430 (7.13)     361.4123 (97.61)        97;5    289.5638 (0.15)        315           1
test_brute_force_bench        107,353.3580 (219.71)   108,004.8640 (78.86)    107,678.7087 (212.18)   260.0997 (3.75)     107,615.7455 (218.29)   554.6210 (149.80)        6;0      9.2869 (0.00)         10           1
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```

Just as mentioned above, `brute_force` is the slowest by a large margin, then `numpy_subtract`, then `two_pointers`.

Using `m` and `n` as the length of each list `brute_force` is O(m\*n), numpy is also O(m\*n) but vectorization makes it very fast, and `two_pointers` is O(mlogm + nlogn).

## Question 3
Just as we parallelized the diff calculation between elements of the list in the numpy approach above, we can parrelelize the entire computation for each pair of the 1 million lists. We can use a different programming language that allows us to split the computations among multiple CPU cores, or libraries like numpy that enable this from Python. Similarly, we could parrelelize the computation among multiple machines using a tool like Spark.
