+++
title = "A backend that translates Bril into C"
extra.author = "Wen-Ding Li"
extra.author_link = "https://www.cs.cornell.edu/~wdli/"
extra.bio = """
  [Wen-Ding Li](https://www.cs.cornell.edu/~wdli/) is a PhD student who is currently taking cs6120 at Cornell.
"""
+++

Bril is an educational compiler intermediate representation that is designed for this compiler course. While there is already an interpreter written in
typescript, it would be interesting to have other backends so that we can compare the performance and the implementation complexity. In this first project,
I built a backend that translates Bril into C language and then use GCC to compile and execute the program.

Why choose C?
---
Translating to C provides some benefits such as portability, good performance, and easier integration with other C library and tools. C language is a widely used language in many embedded device. We can also get native performance and leverage GCC compiler's optimization. I'm curious about its performance compared to other backends. By translating to C, we can easily integrate it with other C library. Plus, because the Bril instructions (as it is now) can be map to C statements, we can also potentially use gdb as an debugger.
It would be also beneficial to people who are not familiar with assembly, LLVM IR or Java bytecode, but also want to get the native performance.
Finally, Translating to C is very common in programming community and can be a fun project for many people.

Implementation
---
something

Example
---
something

Usage
---
something

Benchmark
---
something


Conclusion
---
something
