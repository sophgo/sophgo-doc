TRNG
----

Overview
~~~~~~~~

True Random Number Generator (TRNG) generates random numbers that are intended to be statistically equivalent to a uniformly distributed random data stream. . The circuit includes a Deterministic Random Bit Generator (DRBG). When seed is created and fed into the DRBG, the TRNG generates random numbers.

Features
~~~~~~~~

The TRNG module has the following functional features:

- Internal random seeding operation
- 128-bit random number generation
- 128 bits of security strength

Way of Working
~~~~~~~~~~~~~~

Loop test STAT.BUSY, till it is idle.

Write GEN_NOISE to CTRL.CMD to generate full-entropy seed from noise.

Loop test ISTAT.DONE, till last command is completed.

Clear ISTAT.DONE by writing 1 to it.

Write CREATE_STATE to CTRL.CMD to move DRBG to create state.

Loop test ISTAT.DONE, till last command is completed.

Clear ISTAT.DONE by writing 1 to it.

Write GEN_RANDOM to CTRL.CMD to generate a random number.

Loop test ISTAT.DONE, till last command is completed.

Clear ISTAT.DONE by writing 1 to it.

Read the random data word 0 from RAND0.

Read the random data word 1 from RAND1.

Read the random data word 2 from RAND2.

Read the random data word 3 from RAND3.

TRNG Register Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. include:: ../../contents-share/security/trng_registers_overview.table.rst

TRNG Register Description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(Base address: 0x02070000)

.. include:: ../../contents-share/security/trng_registers_description.table.rst
