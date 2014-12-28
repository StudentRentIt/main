=====TESTS=====
We use a modular approach to the tests. Each different section/app has their own setups
that are dependent upon other modules. For example, to test Real Estate functionality,
you need school functionality, which also requires User functionality. These are separated
into classes and each class inherits the setUp function of their parent. This in turn
makes a modular testing environment.