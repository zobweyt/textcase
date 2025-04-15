# Changelog

All notable changes to this project will be documented in this file.

## [0.4.1](https://github.com/zobweyt/textcase/compare/0.4.0...0.4.1) (2025-04-15)

Performance and documentation enhancements.

### <!-- 2 -->Performance <!-- omit in toc -->

- optimize build ([`a79cb84`](https://github.com/zobweyt/textcase/commit/a79cb84082d1b3d7ba717fe7059c7ca3fa713f4b))

## [0.4.0](https://github.com/zobweyt/textcase/compare/0.3.1...0.4.0) (2025-04-14)

Rewrite.

### <!-- 1 -->Features <!-- omit in toc -->

- rewrite ([`4816c0e`](https://github.com/zobweyt/textcase/commit/4816c0e4edfef6f7255439fed1dec15eb5763d99))

### <!-- 2 -->Performance <!-- omit in toc -->

- optimize `pattern.camel` and `pattern.sentence` ([`a5d1731`](https://github.com/zobweyt/textcase/commit/a5d17310fd749a5dac943be51a4dc385506d2c31))

## [0.3.1](https://github.com/zobweyt/textcase/compare/0.3.0...0.3.1) (2025-04-13)

Adds `py.typed` file.

### <!-- 0 -->Bug Fixes <!-- omit in toc -->

- add `py.typed` file ([`a2611af`](https://github.com/zobweyt/textcase/commit/a2611af1300d3f0aa22a0e41f31ede261e55d2bd))

## [0.3.0](https://github.com/zobweyt/textcase/compare/0.2.3...0.3.0) (2025-04-13)

Simplification of custom `Boundary` creation from a delimiter, and addition of the new `MIDDOT` case.

### <!-- 1 -->Features <!-- omit in toc -->

- add `Boundary.from_delimiter` (#10) ([`ff46f04`](https://github.com/zobweyt/textcase/commit/ff46f04051347fca94d3f2dde191c881d8b024bf))
- add `INTERPUNCT` boundary and `MIDDOT` case (#11) ([`8cf450b`](https://github.com/zobweyt/textcase/commit/8cf450b140a032684d36069710404c76809ab052))

## [0.2.3](https://github.com/zobweyt/textcase/compare/0.2.2...0.2.3) (2025-04-13)

Acronym identification fixes.

### <!-- 0 -->Bug Fixes <!-- omit in toc -->

- update ACRONYM to correctly identify acronym boundaries ([`dd604b0`](https://github.com/zobweyt/textcase/commit/dd604b0725329ae71be2212e694087216d57d388))

## [0.2.2](https://github.com/zobweyt/textcase/compare/0.2.1...0.2.2) (2025-04-12)

Performance and documentation enhancements.

### <!-- 2 -->Performance <!-- omit in toc -->

- optimize boundary conditions ([`27cbbb2`](https://github.com/zobweyt/textcase/commit/27cbbb2643ba957f4318f150a109e728610dee73))

## [0.2.1](https://github.com/zobweyt/textcase/compare/0.2.0...0.2.1) (2025-04-02)

Expands test coverage with new tests for edge cases and conversions.

### <!-- 4 -->Testing <!-- omit in toc -->

- add boundary custom tests ([`5602ed0`](https://github.com/zobweyt/textcase/commit/5602ed019ebfae8ea5df6fe17f2593bac4e99e9e))
- add case custom tests ([`b26a3c1`](https://github.com/zobweyt/textcase/commit/b26a3c1020f046b0c57399ddb03b1b3953d44dcc))
- add converter complex test ([`4b1f3a9`](https://github.com/zobweyt/textcase/commit/4b1f3a91a72a928cc81dac6966899b961aff3547))
- add is_case tests ([`8f9b2d3`](https://github.com/zobweyt/textcase/commit/8f9b2d3bbc6137ca261a758781734ab2240b38a5))
- add convert cases tests ([`4b5c110`](https://github.com/zobweyt/textcase/commit/4b5c11091c036ef21aa56ce0ea85f23b8d531229))
- add convert acronyms tests ([`cc3cdcc`](https://github.com/zobweyt/textcase/commit/cc3cdcc965c87b75eb85d68d4c99cf9801dadd71))
- add convert non ascii tests ([`c4fdd55`](https://github.com/zobweyt/textcase/commit/c4fdd55eb01aabe39667e87fc07950d7fa439dab))
- add case precision tests ([`6055e41`](https://github.com/zobweyt/textcase/commit/6055e41ff0b8a68102c60ec5578bede838a7461f))
- add test special tests ([`ad2a3ec`](https://github.com/zobweyt/textcase/commit/ad2a3ecd03796fc356c5d70c0236e22578b188eb))
- add pattern tests ([`e03f54e`](https://github.com/zobweyt/textcase/commit/e03f54ecdc3554c5145ef66f1cb14e46a34e5fae))

## [0.2.0](https://github.com/zobweyt/textcase/compare/0.1.0...0.2.0) (2025-04-01)

Adds initial functionality for text case conversion, with extensibility possible.

### <!-- 0 -->Bug Fixes <!-- omit in toc -->

- use final for case constants ([`5228e8d`](https://github.com/zobweyt/textcase/commit/5228e8dda4bb4a503791b1206adc54c2664d39c2))
- use lower instead of upper for LOWER case ([`cce6ed7`](https://github.com/zobweyt/textcase/commit/cce6ed7371976e762ddf3adfe7d176635910df7f))

### <!-- 1 -->Features <!-- omit in toc -->

- add text case transformation patterns ([`b003fac`](https://github.com/zobweyt/textcase/commit/b003fac291a21dae0ca19688cb0fa2ea23aceb7b))
- add conditions for splitting an identifier into words ([`fb76228`](https://github.com/zobweyt/textcase/commit/fb762289d34080cf9bd380c66330598a428dcc9d))
- add case definitions for text transformation ([`cf32822`](https://github.com/zobweyt/textcase/commit/cf328225c81a1ab03962cb7222a6312f1d948ffa))
- add text case conversion between different case formats ([`a11044d`](https://github.com/zobweyt/textcase/commit/a11044d2545e4af41bca6a7d19b48302f3f8bfca))
- add utils ([`1f86e1a`](https://github.com/zobweyt/textcase/commit/1f86e1a0d18936a8ec3dbd81113a4dd3d3314c4f))
- add boundaries to convert function ([`0b9ea8a`](https://github.com/zobweyt/textcase/commit/0b9ea8ab20fe2f4419a13f18d68d8a9464e53da3))
- add initial functionality (#1) ([`3073ae6`](https://github.com/zobweyt/textcase/commit/3073ae63db2b50f0e673af851f2bb2b6b5f34942))

### <!-- 4 -->Testing <!-- omit in toc -->

- include doctests in pytest ([`699c5a6`](https://github.com/zobweyt/textcase/commit/699c5a6e21fcab62a22cff50c6790458727039a1))
- ignore testmod ([`04f6862`](https://github.com/zobweyt/textcase/commit/04f68629afaecc402347a70f92edb4e82f1ffa4d))
- add converter tests ([`d045a97`](https://github.com/zobweyt/textcase/commit/d045a974b9506256e1045fbf88199261f3fbd33c))

### Build <!-- omit in toc -->

- use python >=3.9 ([`a30d61c`](https://github.com/zobweyt/textcase/commit/a30d61c40cd246fad26f95a2659c9d70a1b31c43))

## [0.1.0](https://github.com/zobweyt/textcase/commits/0.1.0) (2025-03-31)

Initial release.

### <!-- 1 -->Features <!-- omit in toc -->

- init ([`22ec6ca`](https://github.com/zobweyt/textcase/commit/22ec6ca462445c19b8de9a3e378905d4be7ca94a))

### New Contributors <!-- omit in toc -->

- [@zobweyt](https://github.com/zobweyt) made their first contribution
