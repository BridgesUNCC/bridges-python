from bridges.line_chart import *
import random
from datetime import datetime


class SortingBenchmark:


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
        self.debug = False

    @property
    def plot(self):
        return self._plot

    @plot.setter
    def plot(self, p):
        self._plot = p

    @property
    def max_size(self):
        return self._max_size

    @max_size.setter
    def max_size(self, size):
        self._max_size = size

    @property
    def base_size(self):
        return self._base_size

    @base_size.setter
    def base_size(self, size):
        self._base_size = size

    @property
    def increment(self):
        return self._increment

    @increment.setter
    def increment(self, inc):
        self._increment = inc

    @property
    def geometric(self):
        return self._geo_base

    @geometric.setter
    def geometric(self, base):
        self._geo_base = base

    @property
    def time_cap(self):
        return self._time_cap_ms

    @time_cap.setter
    def time_cap(self, cap_in_ms):
        self._time_cap_ms = cap_in_ms

    def linear_range(self, base_sz, max_sz, nb_point):
        self.base_size = base_sz
        self.max_size = max_sz
        self.increment = ((max_sz - base_sz) / nb_point)
        self.geometric = 1.0

    def geometric_range(self, base_sz, max_sz, base):
        self.base_size = base_sz
        self.max_size = max_sz
        self.increment = 0
        self.geometric = base
        if base <= 1.0:
            print("base should be > 1.0")

    def generate(self, arr, n):
        for i in range(0, n):
            arr[i] = self.r.randint(0, 2*n)

    def check(self, arr, n):
        ok = True
        for i in range(1, n):
            if arr[i] < arr[i -1]:
                ok = False
                break
        return ok

    def run(self, algo_name, runnable):
        time = []
        x_data = []

        if self.debug:
            print(self.geometric)
            print(self.increment)

        for n in range(self.base_size, self.max_size):
            n = max(self.geometric * n + self.increment, n + 1)
            arr = []
            self.generate(arr, n)

            start = datetime.now().microsecond
            runnable(arr)
            end = datetime.now().microsecond
            runtime = end - start

            if self.check(arr, n) == False:
                print("Sorting algorithm " + algo_name + " is incorrect")

            time.append(float(runtime))
            x_data.append(float(n))

            if runtime > self.time_cap:
                break

        self.plot.set_x_data(algo_name, x_data)
        self.plot.set_y_data(algo_name, time)
