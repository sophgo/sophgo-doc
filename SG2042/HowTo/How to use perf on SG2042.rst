================
How to use perf
================

1. Install perf
=======================

-   on Fedora

.. highlights::

   .. code:: sh

      $ sudo dnf install perf

-   on Ubuntu

.. highlights::

   .. code:: sh

      $ cd tools
      $ cd perf
      $ sudo chmod +x build-perf.sh -R
      $./build-perf.sh

2. How to use perf
=======================

-   View Available Performance Counters

    This command lists all available events and hardware performance counters.

.. highlights::

   .. code:: sh

      $ perf list



- Record Performance Data

  Run [command] and record its performance data. The -g option is used to record the call graph.

.. highlights::

   .. code:: sh

      $ perf record -g [command]

-  Report Performance Data

   Analyze the data collected by perf record and display an interactive performance report.

.. highlights::

   .. code:: sh


      $ perf report

-  Real-time Performance Statistics

   Run [command] and display some basic performance statistics, such as CPU cycles and cache misses.

.. highlights::

   .. code:: sh


      $ perf stat [command]

-  Monitor Specific Events

   Monitor specific events (in this case, cache misses and cache references).

.. highlights::

   .. code:: sh


      $ perf stat -e cache-misses,cache-references [command]

-  Dynamic Tracing

   Used for tracing system calls and related events.

.. highlights::

   .. code:: sh


      $ perf trace [command]

-  Performance Data Sampling

   Displays the busiest functions in the system in real-time.

.. highlights::

   .. code:: sh


      $ perf top

-  Analyze CPU Cycles

   Record CPU cycle events for a specific command.

.. highlights::

   .. code:: sh


      $ perf record -e cycles [command]

-  Analyze Specific Process

   Record performance data for a specific process.

.. highlights::

   .. code:: sh


      $ perf record -p [pid]

-  Record Performance Data for a Specific Time Period

   Use -a to monitor all CPUs and --sleep to set the sampling duration (10 seconds in this case).

.. highlights::

   .. code:: sh


      $ perf record -a -g [command] -- sleep 10

-  Specifying Sampling Frequency

   The perf record -F command is used to specify the sampling frequency for the perf record operation. 

.. highlights::

   .. code:: sh


      $ perf record -F 1000 [command]

   This command samples the execution of [command] at a frequency of 1000 times per second.

2. Known Issues with Perf:

=======================

-   When using perf stat -e to monitor the events branch:u, branches-misses:u, dcache-loads, and L1-icache-load-misses, no data is sampled.
-   When using perf record -F with a specified sampling frequency less than 2000, there are issues with system crashes.