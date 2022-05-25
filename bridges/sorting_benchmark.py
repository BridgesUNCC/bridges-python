import random
import time as time_


class SortingBenchmark:
    """
    @brief Benchmarks sorting algorithm

	Benchmarks sorting algorithms and add time series to a LineChart.

	The benchmark goes from an initial size controlled by
	setBaseSize() to a largest size controlled by setMaxSize(). One
	can also set a maximum time spent on a particular run using
	setTimeCap().

	The benchmark goes from a array size of n to the next one of
	geoBase  n + increment, where the base is controlled by
	geometric and increment is controlled by
	increment. For simpler use one can set a purley linear
	sampling with linear_range() or a purely geometric one with
	geometric_range().

	sorting algorithms can be passed to the run function for being benchmarked. A typical use would look something like

	\code{.py}
	def mysort(int array, int arraysize)
	lc = LineChart();
	sb SortingBenchmark(lc);
	sb.linear_range (100, 1000, 5);
	sb.run("mysortingalgorithm", mysort);
	\endcode

	@author Erik Saule
	@date 07/20/2019
    """
    def __init__(self, p):
        p.x_label = "Size of Array"
        p.y_label = "Runtime (in us)"
        self._plot = p
        self.r = random
        self._max_size = 1
        self._base_size = 1
        self._increment = 1
        self._geo_base = 1
        self._time_cap_ms = float('inf')
        self._generator = "random"
        self.debug = False

    @property
    def generator(self):
        return self._generator

    
    @generator.setter
    def generator(self, generator_name: str):
        """
        @param generator_name possible values are "random", "inorder", "reverseorder", "fewdifferentvalues", "almostsorted"
        """        
        if generator_name not in ["random", "inorder", "reverseorder", "fewdifferentvalues", "almostsorted"]:
            raise ValueError("unknown generator")
        self._generator = generator_name

    @property
    def plot(self):
        return self._plot

    @plot.setter
    def plot(self, p):
        self._plot = p

    @property
    def max_size(self):
        """
        Getter for the max_size of array
        Returns:
            the max size
        """
        return self._max_size

    @max_size.setter
    def max_size(self, size):
        """
        Puts a cap on the largest array to be used
        Args:
            size: Maximum size considered
        """
        self._max_size = size

    @property
    def base_size(self):
        return self._base_size

    @base_size.setter
    def base_size(self, size):
        """
        Smallest array to be used
        Args:
            size: size of the smallest array to use
        """
        self._base_size = size

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, inc):
        """
        Sets the increment for the benchmark size
        Args:
            inc: new value of the increment
        """
        self._increment = inc

    @property
    def geometric(self):
        return self._geo_base

    @geometric.setter
    def geometric(self, base):
        """
        Sets a geometric progression for the benchmark size
        Args:
            base: new base of the geometric progression
        """
        self._geo_base = base

    @property
    def time_cap(self):
        return self._time_cap_ms

    @time_cap.setter
    def time_cap(self, cap_in_ms):
        """
        Sets an upper bound to the time of a run.
        The benchmark will end after a run if it takes more than the
        given amount of time. So it is possible a particular run takes
        more than the alloted time, but that will be the last run.
        Args:
            cap_in_ms: time limit in seconds
        """
        self._time_cap_ms = cap_in_ms

    def linear_range(self, base_sz, max_sz, nb_point):
        """
        brief The benchmark will sample a range with a fixed number of
		points.
		The benchmark will sample about nbPoint equally distributed in
		the range [base_size, max_size]
        Args:
            base_sz: lower bound of the range sampled
            max_sz: upper bound of the range sampled
            nb_points: number of sample
        """
        self.base_size = base_sz
        self.max_size = max_sz
        self.increment = ((max_sz - base_sz) / nb_point)
        self.geometric = 1.0

    def geometric_range(self, base_sz, max_sz, base):
        """
        The benchmark will sample a range using in geometrically
		increasing sequence.
        The benchmark will sample the range [baseSize; maxSize] using a
		geometric distribution in base base. That is to say, it will
		sample base_ize, base*base_ize, base*base*base_ize, ...
        Args:
            base_sz: lower bound of the range sampled
            max_sz: upper bound of the range sampled
            base: base of the geometric increase
        """
        self.base_size = base_sz
        self.max_size = max_sz
        self.increment = 0
        self.geometric = base
        if base <= 1.0:
            print("base should be > 1.0")

    def __generate(self, arr, n):
        if self._generator == "random":
            self.__generate_random(arr, n)
        elif self._generator == "inorder":
            self.__generate_inorder(arr, n)
        elif self._generator == "reverseorder":
            self.__generate_reverseorder(arr, n)
        elif self._generator == "fewdifferentvalues":
            self.__generate_fewdifferentvalues(arr, n)
        elif self._generator == "almostsorted":
            self.__generate_almostsorted(arr, n)
        else:
            raise RuntimeError("generator unknown")
        
    def __generate_random(self, arr, n):
        for i in range(0, n):
            arr.append(self.r.randint(0, 2*n))

    def __generate_inorder(self, arr, n):
        for i in range(0, n):
            arr.append(i)

    def __generate_reverseorder(self, arr, n):
        for i in range(0, n):
            arr.append(n-i)

    def __generate_fewdifferentvalues(self, arr, n):
        for i in range(0, n):
            arr.append(self.r.randint(0, 4))

    def __generate_almostsorted(self, arr, n):
        if n < 20:
            self.__generate_random(arr, n)
        else:
            for i in range(0, n-20):
                arr.append(i)
            for i in range(0, 20):
                arr.append(self.r.randint(0, 2*n))

            
            
    def __check(self, arr, n):
        ok = True
        for i in range(1, n):
            if arr[i] < arr[i -1]:
                ok = False
                break
        return ok

    def run(self, algo_name, runnable):
        """
        benchmark one implementation
        Args:
            algo_name: screen name of the algorithm to be used in the visualization
            runnable: pointer to the sorting function to benchmark
        :return:
        """
        time = []
        x_data = []

        if self.debug:
            print(self.geometric)
            print(self.increment)

        n = self.base_size
        while n < self.max_size:
            arr = []
            self.__generate(arr, int(n))

            start = int(round(time_.time() * 1000))
            runnable(arr)
            end = int(round(time_.time() * 1000))
            runtime = end - start

            if self.__check(arr, int(n)) == False:
                print("Sorting algorithm " + algo_name + " is incorrect")

            time.append(float(runtime))
            x_data.append(float(n))

            if runtime > self.time_cap:
                break

            n = max(self.geometric * n + self.increment, n + 1)
        self.plot.set_x_data(algo_name, x_data)
        self.plot.set_y_data(algo_name, time)
