# worst

The worst possible implementation of a container class

---

## Motivation

A friend and I were talking before class about a poorly designed language of some kind or another, and wanted to know what the worst possible container class would be. We ultimately decided that it would be a quirky container whose only interface would be the `__getitem__` and `__setitem__` methods, where depending on the index you accessed, the container could clear itself, delete the first item, or solve world hunger. We further discussed the possibility of requiring the user to use only prime indices so as to provide flexibility for future versions to add more capabilities.

This is my attempt at such a container.

## Design

### The `Worst` Container

The `Worst` container is a flexible container, whose implementation was inspired by a friend of mine in the middle of Hell week - the week right before final exams when every project, homework, paper, and presentation of the entire semester is due. It's a week filled with stress, drinking, and hair-brained ideas.

`Worst` is an index-based container, very much like an array, though not stored contiguously in memory. `Worst` is thread-safe (one an item is saved at an index, it may not be modified unless certain conditions are met). Internally, `Worst` is implemented as a `dict`; the most powerful and flexible container in standard Python. Here, we improve `dict` and add a certain amount of mathematical rigour and flexibility (both) so that otherwise lax developers continue to grow and develop in the professional world.

### A Broad Overview of Index types

* Negative indices.

  Python convention for negative indices is to access the container in reverse order. This is too intuitive, so this container will rather...

* Zero

  Accessing the zeroth index will delete every element in the container. Writing an index to the zeroth index will delete that element.

* One

  [SD Mines](https:sdsmt.edu) counts down to the beginning of an event with the sequence `1`, `3`, `5` rather than the more common `1`, `2`, `3`. The justification I was given was that `1`, `3`, and `5` are the first three prime numbers, and Mines students are sufficiently nerdy that this reflects well on them. I didn't mention that the first three prime numbers are actually `2`, `3`, and `5`.

  Anyways, the point is, to honor my prime-challenged degree-granting institution, I treat one as a prime number. Further, being both the oddest prime, and apparently not even a prime at all, I will not treat two as a prime number.

* Slices

  Slices work as expected (so not at all expected)

* Prime indices

  Prime (as defined above) indices are the only indices that can be accessed and written to.

* Composite indices

  Accessing composite indices is the primary way a user can manipulate the `Worst` container type.

### Indexing

We define several special indices and their behavior below.

* Accessing `0` will delete every item in the container. Writing an index to `0` will delete the item at the index given. If there is not an item saved at the given index, every item will be deleted to ensure that the intended item is deleted.
* Instead of raising an exception, `Worst` will indicate an error by writing an error code to index `13`, which, being so unlucky, will not be counted as a prime number. Writing to index `13` will result in an error code being written to index `13`.
* Any results returned by a command will save their results in index `42`. Once index `42` is accessed, its value will be deleted.
* Accessing an index with no value is undefined behavior and will helpfully return a random number.
* Accessing `2` will return a random prime number.
* For convenience, writing an integer to `2` will run a probabilistic primality check on the value.

## Dependencies

* `coverage`
* `nose`
* `gmpy2`

## TODO

* Sphinx documentation?
* Slices
* Negative indices
* Handle immutability, potentially by writing the index to clear to a special composite index
* Somehow incorporate randomness, factoring, and Jacobi Symbols
* Define error codes
* Enforce private attributes and methods. Will probably need to do some hacky shit for this.
