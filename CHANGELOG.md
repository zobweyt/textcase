# Changelog

All notable changes to this project will be documented in this file.

## Unreleased

### Documentation

- add CHANGELOG.md for 0.2.1 ([17b5dcb](17b5dcb775a05b425643633a5ec7584d0035728d))

## [0.2.1](https://github.com/zobweyt/textcase/commits/0.2.1) (2025-04-02)

[3073ae6](3073ae63db2b50f0e673af851f2bb2b6b5f34942)...[63d3d0f](63d3d0f942bc04e1e690eeaf79762b459a4931f7)

### Documentation

- fix usage example typo ([1620f2a](1620f2a7ea166508ac6abb0b1de076ec8f8a2758))
- add CODE_OF_CONDUCT.md and CONTRIBUTING.md ([ef86c84](ef86c84bb65eb5f78c5ac70d5bacb2559984be7c))
- fix link typos ([f31023a](f31023ac6ca750b39fd86e9af9faf2518c87cc4c))
- fix usage example typo ([b10803a](b10803a623b1ad30742204b1d54c3586a2924c3b))
- fix typo in CONTRIBUTING.md ([2a6e031](2a6e0316acf8a1b8a5c220aec2918093a176dbcc))
- add dependencies badge ([168a5e0](168a5e039de9668e0444226451b06086a613f2a5))
- fix typo in CONTRIBUTING.md ([eda6b0b](eda6b0bf226a1073023763819e7c478af463a38d))
- add features section ([e0cd95a](e0cd95a8343d3320dc86f755bc07d7e739eaa930))
- add zero dependencies point ([c752b23](c752b2324a6104a6c0ed959f3e6fc58f39cb66cf))
- improve documentation on language inference and non-ASCII support ([31d0dc6](31d0dc65433c5b1510d47cce975249ed0a5a7b9d))
- add more project keywords ([0dfb7d3](0dfb7d3f7c68c4115106c7c858fd6ca486656872))
- add note about non-ASCII support to feature list ([02d8b46](02d8b461480ddc11c92f620273717cf8f60a0d0c))
- correct sections about non-ASCII characters ([30418ee](30418eea763fe44ae185e387cd9b9810ec16727c))
- add AUR badge ([ddf738f](ddf738ff79c81ef3fa9877d76c8d2073337a17e7))
- add mkdocs material (#3) ([d4f5170](d4f5170b0280427a953191f2987890d0ded7be92))
- add blank line between links ([1ee870c](1ee870c11bd6c08a4dfd4a86b8f039a730a7212b))
- remove link to code ([0bf4a69](0bf4a69cbfd8016f7caa53a47fa412934fe4b2c6))

### Miscellaneous

- bump version to 0.2.0 ([d7bb5b4](d7bb5b48fa3182968d79dd274102a58430a7e375))
- bump development status classifier ([26ea5ce](26ea5ce594368e60b652c94890dad23f1732a8ba))
- add shell.nix ([dff71a6](dff71a6acd512908fa87f0a652d07f88c4813443))
- fix just-version ([20cc406](20cc4065d00877d82d12a26f7237aac1ec402afd))
- add bug report github issue template ([2bc1f7f](2bc1f7f51fc2c1dec660255633adf25fb519b43e))
- add feature request github issue template ([be8dbc3](be8dbc340fe0a8df7f71cd7709d43e031ee1ef92))
- add bug label to bug report github issue template issues link ([0313ed5](0313ed58c19238fa964de76bd12181726335c436))
- add enhancement label to feature request github issue template issues link ([629fa02](629fa02076a7e95583ee085993bef65475a2687e))
- add pull request github template ([d72393f](d72393fe84a54d504c8046607a95bc9e1abec15b))
- add SECURITY.md ([ce59d90](ce59d90da124ea253c32c322f8d90089876edaa2))
- exec zsh in nix only if it exists ([f247d6c](f247d6c87c1b27895adfd4fc5d7e670057a25a6c))
- change feature complete to feature-rich in project description ([53b34d8](53b34d8d8d8d221fafd6715480a26fc29954f1d9))
- bump version to 0.2.1 ([63d3d0f](63d3d0f942bc04e1e690eeaf79762b459a4931f7))

### Styling

- fix changelog timestamp format ([caa08bd](caa08bd0988e219b9ce682d0715189dbfa73b8b5))

### Testing

- add boundary custom tests ([5602ed0](5602ed019ebfae8ea5df6fe17f2593bac4e99e9e))
- add case custom tests ([b26a3c1](b26a3c1020f046b0c57399ddb03b1b3953d44dcc))
- add converter complex test ([4b1f3a9](4b1f3a91a72a928cc81dac6966899b961aff3547))
- add is_case tests ([8f9b2d3](8f9b2d3bbc6137ca261a758781734ab2240b38a5))
- add convert cases tests ([4b5c110](4b5c11091c036ef21aa56ce0ea85f23b8d531229))
- add convert acronyms tests ([cc3cdcc](cc3cdcc965c87b75eb85d68d4c99cf9801dadd71))
- add convert non ascii tests ([c4fdd55](c4fdd55eb01aabe39667e87fc07950d7fa439dab))
- add case precision tests ([6055e41](6055e41ff0b8a68102c60ec5578bede838a7461f))
- add test special tests ([ad2a3ec](ad2a3ecd03796fc356c5d70c0236e22578b188eb))
- add pattern tests ([e03f54e](e03f54ecdc3554c5145ef66f1cb14e46a34e5fae))

## [0.2.0](https://github.com/zobweyt/textcase/commits/0.2.0) (2025-04-01)

### Bug Fixes

- use final for case constants ([5228e8d](5228e8dda4bb4a503791b1206adc54c2664d39c2))
- use lower instead of upper for LOWER case ([cce6ed7](cce6ed7371976e762ddf3adfe7d176635910df7f))

### Documentation

- fill readme ([d4952f8](d4952f8fa58d7f5f6d8f60683ca4db108682ef78))

### Features

- init ([22ec6ca](22ec6ca462445c19b8de9a3e378905d4be7ca94a))
- add text case transformation patterns ([b003fac](b003fac291a21dae0ca19688cb0fa2ea23aceb7b))
- add conditions for splitting an identifier into words ([fb76228](fb762289d34080cf9bd380c66330598a428dcc9d))
- add case definitions for text transformation ([cf32822](cf328225c81a1ab03962cb7222a6312f1d948ffa))
- add text case conversion between different case formats ([a11044d](a11044d2545e4af41bca6a7d19b48302f3f8bfca))
- add utils ([1f86e1a](1f86e1a0d18936a8ec3dbd81113a4dd3d3314c4f))
- add boundaries to convert function ([0b9ea8a](0b9ea8ab20fe2f4419a13f18d68d8a9464e53da3))
- add initial functionality (#1) ([3073ae6](3073ae63db2b50f0e673af851f2bb2b6b5f34942))

### Miscellaneous

- add mypy to justfile ([c3835d6](c3835d6d6b483dac749d690dfa56ad091e327b59))
- add coveralls workflow ([88403e1](88403e16311cc86bacdc2c3357e672a9d1216b4b))
- fix coverage job name ([dbabb67](dbabb67017d2a00e09d035e7c054ac26df0be80c))
- add style workflow ([5df3c49](5df3c4947c91da99d62cfc6770291e53cb725818))
- add test workflow ([816490c](816490c0e55bbd127b263de12fda4d497e49263c))
- add git cliff ([ed503e4](ed503e4a0a02a02d88cf7a6be02a564ca37a9ac9))
- run coverage only on push in main branch ([01ff262](01ff262ba6de29dfc4ae040fe6ad0360ad0faf29))

### Styling

- remove blank line ([0d03071](0d03071fe72092d9e59ff38b2e1ae72bba2b4328))
- add space between comments ([86e1af7](86e1af7365c506214e69adbc98844107148b5ec7))

### Testing

- include doctests in pytest ([699c5a6](699c5a6e21fcab62a22cff50c6790458727039a1))
- ignore testmod ([04f6862](04f68629afaecc402347a70f92edb4e82f1ffa4d))
- add converter tests ([d045a97](d045a974b9506256e1045fbf88199261f3fbd33c))

### Build

- use python >=3.9 ([a30d61c](a30d61c40cd246fad26f95a2659c9d70a1b31c43))

<!-- generated by git-cliff -->
