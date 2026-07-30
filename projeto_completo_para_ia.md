# 📂 Projeto Completo - Cardápio Pro (Varredura Total sem Filtros)

Este documento contém **absolutamente tudo** do projeto: código-fonte, configurações, banco de dados e dependências do ambiente virtual.

---

## 🌳 Mapeamento Completo da Estrutura de Pastas e Arquivos

```text
./
│   ├── .env
│   ├── alerta_mesa.py
│   ├── analise.py
│   ├── aplicar_troco.py
│   ├── app.py
│   ├── automacao_relatorio.py
│   ├── backup.py
│   ├── banco.py
│   ├── bundle_projeto_total.py
│   ├── cardapio.py
│   ├── config.py
│   ├── config_rede.json
│   ├── controle_sistema.py
│   ├── database.py
│   ├── inspetor.py
│   ├── migrar_tenant.py
│   ├── models.py
│   ├── pagamento.py
│   ├── pedidos.py
│   ├── qrcode.py
│   ├── registros.py
│   ├── rotas_administrativas.py
│   ├── run.sh
│   ├── utils_pagamento.py
│   ├── .git/
│   │   ├── COMMIT_EDITMSG
│   │   ├── FETCH_HEAD
│   │   ├── HEAD
│   │   ├── ORIG_HEAD
│   │   ├── config
│   │   ├── description
│   │   ├── index
│   │   ├── hooks/
│   │   │   ├── applypatch-msg.sample
│   │   │   ├── commit-msg.sample
│   │   │   ├── fsmonitor-watchman.sample
│   │   │   ├── post-update.sample
│   │   │   ├── pre-applypatch.sample
│   │   │   ├── pre-commit.sample
│   │   │   ├── pre-merge-commit.sample
│   │   │   ├── pre-push.sample
│   │   │   ├── pre-rebase.sample
│   │   │   ├── pre-receive.sample
│   │   │   ├── prepare-commit-msg.sample
│   │   │   ├── push-to-checkout.sample
│   │   │   ├── sendemail-validate.sample
│   │   │   ├── update.sample
│   │   ├── info/
│   │   │   ├── exclude
│   │   ├── refs/
│   │   │   ├── heads/
│   │   │   │   ├── main
│   │   │   ├── tags/
│   │   │   ├── remotes/
│   │   │   │   ├── origin/
│   │   │   │   │   ├── HEAD
│   │   │   │   │   ├── main
│   │   ├── objects/
│   │   │   ├── pack/
│   │   │   ├── info/
│   │   │   ├── 37/
│   │   │   │   ├── c90ae6fc487fb86a57de8e2a7089b62a561aeb
│   │   │   │   ├── eaa058ab02790a4d07b4d7ffd2c4d921770a6a
│   │   │   ├── 15/
│   │   │   │   ├── c4ee85f12be813d11f48b97413c97f357e3ae2
│   │   │   ├── 27/
│   │   │   │   ├── f83a8fceeb99aaca684522550b705ab3ae290e
│   │   │   ├── 42/
│   │   │   │   ├── b20cdbeea7e9fb4532454ba523c1488e8b689a
│   │   │   ├── dc/
│   │   │   │   ├── 747b9158a402b7ba5c26fda7dbb0922210de5a
│   │   │   │   ├── 94c4788409c7f4229a0438bc1950add5d63f8d
│   │   │   ├── de/
│   │   │   │   ├── 012091e2517b9e4861c2741b0294f87e77fddf
│   │   │   │   ├── 0fdc591adc65e1de0eb22f4ec481b100846f8a
│   │   │   │   ├── e3ac308dd08e8ef396d2515c78fb5eafc05ced
│   │   │   ├── 1a/
│   │   │   │   ├── 806857cc77bf0a020f04cb4c87b3f607bb5391
│   │   │   │   ├── f6aef7350663b688e6645c888d9ea6a341a769
│   │   │   ├── 16/
│   │   │   │   ├── bd5d75ec635a942665dafa3bce209fca683784
│   │   │   │   ├── f27232d7b8fe20fb5621ad3156a01cd7e1235e
│   │   │   ├── 6d/
│   │   │   │   ├── 2385f2c11aeead6d4e7ba630de09017bf4c21f
│   │   │   ├── e6/
│   │   │   │   ├── 9de29bb2d1d6434b8b29ae775ad8c2e48c5391
│   │   │   ├── 69/
│   │   │   │   ├── 392601ee0dcdae3ea7df4b83270c3d156e1d7a
│   │   │   │   ├── 94e6e569c7279e96818583f8b2974e0c1dd911
│   │   │   ├── a0/
│   │   │   │   ├── acf158ded96dd83d795aa24753be1945658aa8
│   │   │   ├── 52/
│   │   │   │   ├── a7058cebbd0d5ddf8957461bf9b3c902ef61c1
│   │   │   ├── b9/
│   │   │   │   ├── 6de7ff9de8161921041e108a5b7f7fd04a436a
│   │   │   │   ├── e943fa2e516366a29e990e197504980e5b98d6
│   │   │   ├── dd/
│   │   │   │   ├── 0429d66bf5d14d6ae16035da6c733a0e620dda
│   │   │   ├── f2/
│   │   │   │   ├── 0d61bd4c429d62b511294af8b818b84bbe1c8b
│   │   │   │   ├── 611c0a9bcda47d6e45bebe448780189bd78b06
│   │   │   │   ├── 7ca221647210e1bbcfff3d16eaf5e97b6513cb
│   │   │   │   ├── b19ddca96254b2aca677658344e87c926b7e32
│   │   │   ├── 9f/
│   │   │   │   ├── ba0e25984948008963514410bcda9ce992b9f0
│   │   │   ├── 6b/
│   │   │   │   ├── f8cb84e78abe758e0dbb0efd54d3899116f888
│   │   │   ├── b8/
│   │   │   │   ├── 48793e4b9cd213ade9a06517e582e0a04cec79
│   │   │   │   ├── 56e63c26398d329d116ab9764acc7546c48e89
│   │   │   ├── 0b/
│   │   │   │   ├── 02867b4dad4f97153cd5464146b324a11ba5bb
│   │   │   │   ├── 5f1f0b9c29a24ede9bf5c9fac39e1772a56769
│   │   │   │   ├── f3b0b584f3d4e364b23d06bea2fdb3b1b690f4
│   │   │   │   ├── fe71a37be077ab4ea370a667d6d5aa10f51aa2
│   │   │   ├── 03/
│   │   │   │   ├── d83500e1cfa7ba5b20b30f012c11f56349f1e3
│   │   │   ├── 80/
│   │   │   │   ├── baca0b33cef08a029b5ec790683968de8a898b
│   │   │   ├── 72/
│   │   │   │   ├── bc43973d066923f9860d95d4c850ff693de5c1
│   │   │   ├── 32/
│   │   │   │   ├── 4a0d1920d12ea81b363a7e701f31f3aa9f4352
│   │   │   ├── c7/
│   │   │   │   ├── 95a31d404d3a90aa124e86de85f40e2907e000
│   │   │   │   ├── b58cee40b45127f786f012a1d7e1b34ff8306d
│   │   │   ├── c8/
│   │   │   │   ├── c6253d3093a99b4ad8a9c5196a7b9809485681
│   │   │   ├── 99/
│   │   │   │   ├── 6451d46298649357c5a9c29bdcde4f2b96cdc5
│   │   │   │   ├── da355cf31d0f3484bcb3380e3819a2958d25a8
│   │   │   ├── 9c/
│   │   │   │   ├── d628a5fe5aba93e47b0eed579318068bbd394e
│   │   │   │   ├── fd47bad5123a67e8356c4bd0ac341cc6bfbe6a
│   │   │   ├── 60/
│   │   │   │   ├── 8d978c36be5b6b41da5de63f9eacd05f23a097
│   │   │   ├── fb/
│   │   │   │   ├── 0ded58fb7701a8ba7ea33dfdd7a56086546b29
│   │   │   │   ├── 44ded2bb654c6d65aea3713497b5eecf3b6df1
│   │   │   ├── d8/
│   │   │   │   ├── dc30ee0e8fa7937eb7c18822427e032feffbeb
│   │   │   ├── aa/
│   │   │   │   ├── b03e02ec302b8230dad4cbd7e6fc53e89fa6f0
│   │   │   │   ├── cbabc741ba21308a7cb3667241dc83292ee17c
│   │   │   │   ├── dc5f8c48c83fdc57064bf2fe779106ba35132a
│   │   │   ├── 97/
│   │   │   │   ├── 29b36c6985ed1755f3f1ef1bd72ec99e5b044f
│   │   │   │   ├── a9c75d753da2d99940f072650c4f68d5e14dbe
│   │   │   ├── ed/
│   │   │   │   ├── 90979c34133e75fc7474973ec0a8881d36ee6b
│   │   │   ├── e0/
│   │   │   │   ├── 4e3c6c01bca1ec9a56e65f84a277cd3b051359
│   │   │   │   ├── ec3da760ded475ff87d0a37c06f99e5941ff5d
│   │   │   ├── a3/
│   │   │   │   ├── fbab417347e109f9efc296191b3d69acc1ea64
│   │   │   ├── 5b/
│   │   │   │   ├── 58eb29a001a57d431ba9334cf7bf478b4e4da6
│   │   │   ├── 4c/
│   │   │   │   ├── 628295d5537337d647351c163a37b99ecdee85
│   │   │   ├── 21/
│   │   │   │   ├── 714b322d17b2d6565c81c0f64d2e61a1ac5e46
│   │   │   ├── 1f/
│   │   │   │   ├── 41da8914a8115c5f33138778f733e76deb8665
│   │   │   ├── ae/
│   │   │   │   ├── 1f606f8fc55eebc21b65b36feca00453afb758
│   │   │   │   ├── 94f251639d059e049e4b38aa19b25ee4d13748
│   │   │   ├── 56/
│   │   │   │   ├── 750b9d435fd664b0c122d48ea615c4f9646496
│   │   │   │   ├── 7afb65d82d592fab791ce2d487b02602ac3310
│   │   │   ├── 91/
│   │   │   │   ├── 35305e5c3f4515aec966b5044cecdce8a958d0
│   │   │   │   ├── 652ff7b40f138d7a465decf160480208a52da8
│   │   │   ├── fc/
│   │   │   │   ├── 4b85eafcab5b6f45f6948c3ac5b596b9c6a9c2
│   │   │   │   ├── 7c03a61b2d8d225065155e8660af440e0fc0ca
│   │   │   ├── c3/
│   │   │   │   ├── 24f6b38dd045d556f639b05b277ec9e4d36ccd
│   │   │   ├── 2c/
│   │   │   │   ├── a8e03704063c472e989540f1dbdfd9ec819248
│   │   │   ├── c1/
│   │   │   │   ├── 558f9728b56b28904e5a864de09da68d39c0d0
│   │   │   │   ├── f1be534b5226920d291feedef39321c82be6d4
│   │   │   ├── 98/
│   │   │   │   ├── 384aacd5bc4df883d3924f5e03b6214ff782d9
│   │   │   ├── d0/
│   │   │   │   ├── 0ead033e24858583ccc679b7579cb9f01a37be
│   │   │   │   ├── dc988e624f44b58caac590c22c30e5a98348d3
│   │   │   ├── 7d/
│   │   │   │   ├── 8245515ce2d9b927289d967e90e25857215082
│   │   │   │   ├── d592e9abfffc042cfbd4904493479227475ab3
│   │   │   ├── 78/
│   │   │   │   ├── 888db6d4a470faf56a15d0e5f9d998132ad4ad
│   │   │   ├── f7/
│   │   │   │   ├── e9a7bf4fa686959b260514d6749ea0833e68db
│   │   │   ├── 9e/
│   │   │   │   ├── 717c5c283ba4c73138860fca3fc10ff0e1dcf8
│   │   │   │   ├── e6f78debd2a059c1f03f692c44887784a8a495
│   │   │   ├── b2/
│   │   │   │   ├── 2c50ab601e474e94e8839865dcbff317f8c342
│   │   │   │   ├── fa4fa712f8693f8a88770d132894a9371e33d3
│   │   │   ├── 75/
│   │   │   │   ├── e00f964271f960c9a7596fdde8ca6a98db87b2
│   │   │   │   ├── fe95e15e9793a7c43a92502f1ff042d986b144
│   │   │   ├── c9/
│   │   │   │   ├── 3e151fa98f28028a84dad978cf002580edce60
│   │   │   │   ├── b1912702ca484a5a6bf0314ecd9084f8bb8682
│   │   │   ├── f1/
│   │   │   │   ├── ce58788a8b681cf940f80825102a22a1bc4c94
│   │   │   │   ├── d8e86884087a788b5ecd6d7ed6c5a41a619765
│   │   │   ├── 22/
│   │   │   │   ├── d61d9f5227728ae1d310464b8034d4ef5f2418
│   │   │   ├── 07/
│   │   │   │   ├── c275ff86300848d55dfeef29545be4ee9aa549
│   │   │   ├── 4a/
│   │   │   │   ├── 017e7cf6e6dca15c2a1aeea12fd3f41cf7a3a6
│   │   │   ├── a8/
│   │   │   │   ├── 1bc4ad134192ecf8ad7cb24e0cb4312f40bc24
│   │   │   │   ├── 59f615ee70af67793d96d5322c40a4890f0260
│   │   │   ├── 50/
│   │   │   │   ├── a510b9eb7695910ec35031c50ef53f17a84450
│   │   │   ├── 92/
│   │   │   │   ├── 333af78bd89a3d6430cdced833e93142edbb64
│   │   │   ├── 8d/
│   │   │   │   ├── 046d6e00cfe57c3ebce5fc5feb6a27a9d5530e
│   │   │   │   ├── a345cd61ebb3ce42d31bff7045641de7cf3ef4
│   │   │   │   ├── cf2199543012d1752f57f3c6191bd38b49bec5
│   │   │   ├── cc/
│   │   │   │   ├── c506dc856051a3659eff2a58172efaa430f5f2
│   │   │   ├── 44/
│   │   │   │   ├── 78facbb8af323ed88fbc3c1f5a8d4dcbf50da3
│   │   │   ├── 9d/
│   │   │   │   ├── 1dcfdaf1a6857c5f83dc27019c7600e1ffaff8
│   │   │   ├── c2/
│   │   │   │   ├── 5787c89ebf5480290bb665cf4dacf6f98810c6
│   │   │   │   ├── b906e4d7e888977be31f42b40f7ea5ad4b37f6
│   │   │   ├── bf/
│   │   │   │   ├── 98b844c1f085b2c2044536f72b90ab01975bf4
│   │   │   │   ├── e22a2c3867eebb0a24edf14ae8d832a43dbace
│   │   │   ├── fd/
│   │   │   │   ├── 40315965f5e6ea5d019c59e416a45d8d44e563
│   │   │   │   ├── bb52c38e49d57c0f00506dc7c71a042a3ca43c
│   │   │   │   ├── d0e0b425243c1a9e55caa328b8c4b34abc6fb6
│   │   │   ├── 3e/
│   │   │   │   ├── debac0fe91bafd1b8f9f846ab79a2df7e8d875
│   │   │   ├── 34/
│   │   │   │   ├── e0ed34c42fd730ed075492a6edd3de40fbd95b
│   │   │   ├── 12/
│   │   │   │   ├── 90976485dd1e9a5beea1ffcbb7d539f4f4fca3
│   │   │   ├── 00/
│   │   │   │   ├── 8da9f0f6cc24f35569d738d2e9571db12df7c2
│   │   │   ├── 0c/
│   │   │   │   ├── e02c718a53a34283932a4ede1ce68e15a7b779
│   │   │   ├── 53/
│   │   │   │   ├── 2b844b9bb1682d6c1a28909a27e06afac7be06
│   │   │   ├── 2a/
│   │   │   │   ├── e90d935f32cab51a1f066d96111e7aa599cc06
│   │   │   ├── 7c/
│   │   │   │   ├── 43fc83a1a8a6a210b42e0ec822774aeb215617
│   │   │   │   ├── 659c4959e6042aebd3bdba66344dfae771bff0
│   │   │   ├── 83/
│   │   │   │   ├── b530df6846ceeb2dfb55707ca206efae3bd090
│   │   │   │   ├── f12fcff2b0fa78c92100b0105497d21acf3423
│   │   │   ├── ce/
│   │   │   │   ├── e02a8a82e4acfbc41281be462954046f2e7cbc
│   │   │   ├── d5/
│   │   │   │   ├── 1a134dd2e6c7a98702a8f93c8c189f91f04223
│   │   │   ├── 14/
│   │   │   │   ├── eafc9133c8ccf1f425d3c36df518c2d232adbc
│   │   │   ├── 35/
│   │   │   │   ├── c8d991d877fe298923db5c9dffe6e3639db123
│   │   │   ├── ee/
│   │   │   │   ├── 778e2241f8a9976477c0134ed7d1e2905bc109
│   │   │   ├── 93/
│   │   │   │   ├── a354ef94a979ffa472b6e614aa5ce9af85073c
│   │   │   ├── d4/
│   │   │   │   ├── 6a4ba59df3eb954b962730de227387504d7cb8
│   │   │   ├── 95/
│   │   │   │   ├── 00b6f178af45ef0481246457e30bf382e34086
│   │   │   ├── 3b/
│   │   │   │   ├── ceb000dcdaffa51e56354f634b18a6594d94d6
│   │   │   ├── 17/
│   │   │   │   ├── 70abddc6ce3d6497cd736ab958f6534b1a0ed9
│   │   │   ├── 68/
│   │   │   │   ├── 15229f858bc3785f5dede1b69e6f882fe5d289
│   │   │   ├── 89/
│   │   │   │   ├── 36687ad52251b84432c284f5d0493076d343b5
│   │   │   ├── df/
│   │   │   │   ├── 8f461ab7f766f9af05a63b80627e541ae9f074
│   │   │   │   ├── d96d7b8d5d0fea836d4a7da442f8cdc1d39193
│   │   │   ├── e5/
│   │   │   │   ├── 7059e4b6d3c81512de0bbd9b28538faae4abf4
│   │   │   ├── 51/
│   │   │   │   ├── 8cc3bb8f07a65ee17760e950b5754d9370581b
│   │   │   ├── bc/
│   │   │   │   ├── a013aaee9bb6cec33e68481ddcfb2bdab2609a
│   │   │   ├── 19/
│   │   │   │   ├── 61b5e9a334036f05dcc1401d58dec2e38502d5
│   │   │   ├── ea/
│   │   │   │   ├── 5e545084e0ae84fb1f1ed6e7d8295837d1b059
│   │   │   ├── 6c/
│   │   │   │   ├── e82f29c3cb8411b7c2854335e27b409196ed5e
│   │   │   │   ├── f5088ee90e35eefe84c86dd584b7c011207234
│   │   │   ├── fe/
│   │   │   │   ├── 2af235ea7577df2d2a674316834f1c37e8e283
│   │   │   ├── 7f/
│   │   │   │   ├── 0d61b92cb0c37a7630dbf8139b8a6979d33823
│   │   │   ├── 7e/
│   │   │   │   ├── 608561def38e6d1db3335bf3efaac54e3fe8d1
│   │   │   ├── 1e/
│   │   │   │   ├── 16eb1f7dbc0485b7904b81454272b252fa2f62
│   │   │   │   ├── ef69da3d061046bba67a3c18b377c468c7cee2
│   │   │   ├── d7/
│   │   │   │   ├── 2543f4fc24b13214883786072f3833ffc33a4b
│   │   │   ├── 41/
│   │   │   │   ├── 08427e474a63bd22f14255829a532bc367d128
│   │   │   ├── 6f/
│   │   │   │   ├── 0599094ec87af093d75835083f5a0f0e033c9b
│   │   │   ├── 49/
│   │   │   │   ├── 6623f818805d8429ab6d9e3e2d764a7dbc68c6
│   │   │   ├── 2d/
│   │   │   │   ├── 0b7b7faf46ed747ba91c1277970c9a10cb0193
│   │   │   ├── 08/
│   │   │   │   ├── a1031f354b5d85354131b520bde36610e58771
│   │   │   ├── 5e/
│   │   │   │   ├── c0865eae2ac35458ee3c99411a98ede4e72f2a
│   │   │   ├── c5/
│   │   │   │   ├── 4760b626e2d68a31c43efbdfb0c5614ba646e4
│   │   │   ├── db/
│   │   │   │   ├── 5fb7af1a2378251086180bb6404cc5486c47e7
│   │   │   ├── 88/
│   │   │   │   ├── c5ddc8b13292b952065888bbc2a0f755fc09e9
│   │   │   ├── 7a/
│   │   │   │   ├── 9006a5d2dce88bbdb65df7377a4bc2f16fd34e
│   │   │   ├── c6/
│   │   │   │   ├── 50d325f4b616f6e450052fc3fffa932e1380c6
│   │   │   │   ├── b49a0d73c085feb6348647d56b8c78874f1057
│   │   │   ├── 84/
│   │   │   │   ├── ee8c3979974df0764c1d8d7bb5fbd90ab9c373
│   │   │   ├── eb/
│   │   │   │   ├── f1dc783bab02a873561c5de1e433f5aa694ad4
│   │   │   ├── c0/
│   │   │   │   ├── f24621842dffe3cda41dbfb3c0e1da4382bc71
│   │   │   ├── 4d/
│   │   │   │   ├── 275544deea3a9f4c89f48e57503119b520eecc
│   │   ├── logs/
│   │   │   ├── HEAD
│   │   │   ├── refs/
│   │   │   │   ├── heads/
│   │   │   │   │   ├── main
│   │   │   │   ├── remotes/
│   │   │   │   │   ├── origin/
│   │   │   │   │   │   ├── HEAD
│   │   │   │   │   │   ├── main
│   ├── static/
│   │   ├── style.css
│   │   ├── css/
│   │   │   ├── responsive.css
│   │   │   ├── style.css
│   │   ├── uploads/
│   ├── templates/
│   │   ├── analise.html
│   │   ├── backup.html
│   │   ├── base.html
│   │   ├── cardapio.html
│   │   ├── cardapio_admin.html
│   │   ├── cardapio_arquivados.html
│   │   ├── cardapio_cliente.html
│   │   ├── cardapio_digital.html
│   │   ├── configuracao.html
│   │   ├── delivery.html
│   │   ├── index.html
│   │   ├── pagamento.html
│   │   ├── painel.html
│   │   ├── pedidos.html
│   │   ├── pedidos_admin.html
│   │   ├── qr_code.html
│   │   ├── qrcodes.html
│   │   ├── registro.html
│   │   ├── registros.html
│   ├── __pycache__/
│   │   ├── app.cpython-314.pyc
│   │   ├── banco.cpython-314.pyc
│   │   ├── database.cpython-314.pyc
│   │   ├── inspetor.cpython-314.pyc
│   │   ├── main.cpython-314.pyc
│   │   ├── models.cpython-314.pyc
│   │   ├── routes.cpython-314.pyc
│   ├── utils/
│   │   ├── __init__.py
│   ├── routers/
│   │   ├── analise.py
│   │   ├── backup.py
│   │   ├── cardapio.py
│   │   ├── cardapiodigital.py
│   │   ├── cliente.py
│   │   ├── configuracao.py
│   │   ├── delivery.py
│   │   ├── pagamento.py
│   │   ├── pedidos.py
│   │   ├── qr_code.py
│   │   ├── registro.py
│   │   ├── registros.py
│   │   ├── __pycache__/
│   │   │   ├── analise.cpython-314.pyc
│   │   │   ├── backup.cpython-314.pyc
│   │   │   ├── cardapio.cpython-314.pyc
│   │   │   ├── cardapiodigital.cpython-314.pyc
│   │   │   ├── cliente.cpython-314.pyc
│   │   │   ├── configuracao.cpython-314.pyc
│   │   │   ├── delivery.cpython-314.pyc
│   │   │   ├── gerenciar_qrcode.cpython-314.pyc
│   │   │   ├── pagamento.cpython-314.pyc
│   │   │   ├── pedidos.cpython-314.pyc
│   │   │   ├── qr_code.cpython-314.pyc
│   │   │   ├── registro.cpython-314.pyc
│   │   │   ├── registros.cpython-314.pyc
```

---

## Arquivo: `./.env`

```text
PORT=5003
DB_NAME=cardapio_fastapi_db
DB_USER=u0_a330
DB_HOST=localhost
DB_PORT=5432

```

---

## Arquivo: `./alerta_mesa.py`

```text
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/alerta-mesa")
def ver_alerta_mesa(request: Request):
    alertas = [] # Substitua pela sua lógica/banco
    return templates.TemplateResponse("alerta_mesa.html", {
        "request": request, 
        "alertas": alertas
    })

```

---

## Arquivo: `./analise.py`

```text
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/analise")
def ver_analise(request: Request):
    dados_analise = {} # Substitua pela sua lógica/banco
    return templates.TemplateResponse("analise.html", {
        "request": request, 
        "analise": dados_analise
    })

```

---

## Arquivo: `./aplicar_troco.py`

```text
import os, re
base = os.path.expanduser("~/Projetos/CardapioPro_V2")

# A. Atualizar rotas_pagamento.py
rotas = os.path.join(base, "rotas_pagamento.py")
with open(rotas, "r") as f: code = f.read()
nova_funcao = """@app.route('/processar_pagamento/<int:numero_mesa>/<forma>', methods=['GET', 'POST'])
def processar_pagamento(numero_mesa, forma):
    from flask import request
    conn = conectar()
    cur = conn.cursor()

    # Busca o valor total real do pedido somando os itens
    cur.execute("SELECT SUM(i.preco) FROM itens_pedido ip JOIN itens i ON ip.item_id = i.id JOIN pedidos p ON ip.pedido_id = p.id WHERE p.mesa = %s::text AND p.status = 'cozinha'", (numero_mesa,))
    res = cur.fetchone()
    valor_total = res[0] if res and res[0] else 0

    # Se for dinheiro, pega o valor digitado no form. Se não, assume o valor total.
    valor_pago = float(request.form.get('valor_pago', valor_total)) if request.method == 'POST' and forma == 'Dinheiro' else float(valor_total)
    troco = max(0, valor_pago - float(valor_total))

    # Salva todos os dados
    cur.execute("UPDATE pedidos SET status = 'finalizado', forma_pagamento = %s, valor_total = %s, troco = %s, data_finalizacao = NOW() WHERE mesa = %s::text AND status = 'cozinha'", (forma, valor_total, troco, numero_mesa))
    cur.execute("UPDATE mesas SET status = 'livre' WHERE numero = %s", (numero_mesa,))
    conn.commit()
    cur.close(); conn.close()

    return f"<h1>Pagamento em {forma} efetuado com Sucesso!</h1><h3>Total do Pedido: R$ {valor_total:.2f}</h3><h3 style='color:green;'>Troco a devolver: R$ {troco:.2f}</h3><br><a href='/pagamento'>Voltar para as Mesas</a>"
"""
code = re.sub(r"@app\.route\('/processar_pagamento/.*", nova_funcao, code, flags=re.DOTALL)
with open(rotas, "w") as f: f.write(code)

# B. Atualizar a consulta no app.py para incluir a busca do troco
app = os.path.join(base, "app.py")
with open(app, "r") as f: app_code = f.read()
app_code = app_code.replace("SELECT mesa, valor_total, forma_pagamento, data_finalizacao FROM pedidos", "SELECT mesa, valor_total, forma_pagamento, data_finalizacao, troco FROM pedidos")
with open(app, "w") as f: f.write(app_code)

# C. Substituir o link simples de 'Dinheiro' por um campo perguntando o valor
pag = os.path.join(base, "templates", "pagamento.html")
with open(pag, "r") as f: html = f.read()
html = re.sub(r'<a href="[^"]*/Dinheiro"[^>]*>.*?</a>',
              r'<form action="/processar_pagamento/{{ mesa }}/Dinheiro" method="POST" style="margin: 10px 0;"><label>💰 Dinheiro (Cliente Pagou: R$ </label><input type="number" step="0.01" name="valor_pago" required style="width: 80px;"><button type="submit">Pagar</button>)</form>', html)
with open(pag, "w") as f: f.write(html)

print("\n✔️ Código atualizado com sucesso! O sistema agora calcula o troco.")


```

---

## Arquivo: `./app.py`

```text
import os
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import banco
import inspetor

app = FastAPI(title="Cardápio Pro API - PostgreSQL")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.middleware("http")
async def middleware_global(request: Request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        if 'inspetor' in globals() and hasattr(inspetor, 'capturar_erro'):
            inspetor.capturar_erro(e)
        raise e

# Redireciona a raiz para o caminho completo correto
@app.get("/")
def index():
    return RedirectResponse(url="/admin/joel-burguer/cardapio", status_code=303)

# Registro dos routers
try:
    from routers.configuracao import router as config_bp
    app.include_router(config_bp)
except ImportError:
    pass

try:
    from routers.cardapio import router as cardapio_bp
    app.include_router(cardapio_bp)
except ImportError:
    pass

try:
    from routers.pedidos import router as pedidos_bp
    app.include_router(pedidos_bp)
except ImportError:
    pass

try:
    from routers.analise import router as analise_bp
    app.include_router(analise_bp)
except ImportError:
    pass

try:
    from routers.pagamento import router as pagamento_bp
    app.include_router(pagamento_bp)
except ImportError:
    pass

try:
    from routers.registro import router as registro_bp
    app.include_router(registro_bp)
except ImportError:
    pass

try:
    from routers.backup import router as backup_bp
    app.include_router(backup_bp)
except ImportError:
    pass

try:
    from routers.delivery import router as delivery_bp
    app.include_router(delivery_bp)
except ImportError:
    pass

try:
    from routers.qr_code import router as qr_code_bp
    app.include_router(qr_code_bp)
except ImportError:
    pass

try:
    from routers.cliente import router as cliente_bp
    app.include_router(cliente_bp)
except ImportError:
    pass

if __name__ == '__main__':
    import uvicorn
    porta_dinamica = int(os.environ.get('PORT', 5003))
    uvicorn.run("app:app", host="0.0.0.0", port=porta_dinamica, reload=True)

```

---

## Arquivo: `./automacao_relatorio.py`

```text
import os
import zipfile
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler
from banco import conectar
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

SENHA_ZIP = "SouLivre01"

def gerar_pdf_fechamento(data_alvo_str):
    conn = conectar()
    cur = conn.cursor()
    try:
        cur.execute("SELECT SUM(valor_total) FROM historico_mesas")
        res_total = cur.fetchone()
        faturamento_total = res_total[0] if res_total and res_total[0] else 0.0

        cur.execute("SELECT forma_pagamento, SUM(valor_total) FROM historico_mesas GROUP BY forma_pagamento")
        por_forma = cur.fetchall()

        cur.execute("SELECT mesa, valor_total, forma_pagamento, troco, data_hora FROM historico_mesas ORDER BY id DESC")
        historico = cur.fetchall()

        if not historico and faturamento_total == 0.0:
            return False

        pasta_base = os.path.join(os.getcwd(), "Relatorios_Fechamento")
        os.makedirs(pasta_base, exist_ok=True)

        nome_pdf = f"Fechamento_{data_alvo_str}.pdf"
        caminho_pdf = os.path.join(pasta_base, nome_pdf)

        doc = SimpleDocTemplate(caminho_pdf, pagesize=letter)
        elementos = []
        styles = getSampleStyleSheet()

        titulo_style = ParagraphStyle(
            'Titulo',
            parent=styles['Heading1'],
            fontSize=18,
            alignment=1,
            textColor=colors.HexColor("#1e293b")
        )

        elementos.append(Paragraph(f"<b>Relatório de Fechamento Diário</b>", titulo_style))
        elementos.append(Paragraph(f"<b>Data do Fechamento:</b> {data_alvo_str}", styles['Normal']))
        elementos.append(Spacer(1, 15))

        dados_resumo = [["Faturamento Total", f"R$ {faturamento_total:.2f}"]]
        tabela_resumo = Table(dados_resumo, colWidths=[200, 200])
        tabela_resumo.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f1f5f9")),
            ('TEXTCOLOR', (0,0), (-1,-1), colors.HexColor("#0f172a")),
            ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,-1), 12),
            ('BOTTOMPADDING', (0,0), (-1,-1), 8),
            ('TOPPADDING', (0,0), (-1,-1), 8),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('GRID', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ]))
        elementos.append(tabela_resumo)
        elementos.append(Spacer(1, 15))

        elementos.append(Paragraph("<b>Faturamento por Forma de Pagamento</b>", styles['Heading3']))
        elementos.append(Spacer(1, 5))

        dados_formas = [["Forma de Pagamento", "Total"]]
        for forma, valor in por_forma:
            dados_formas.append([str(forma), f"R$ {valor:.2f}"])

        tabela_formas = Table(dados_formas, colWidths=[200, 200])
        tabela_formas.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#e2e8f0")),
            ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor("#0f172a")),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('GRID', (0,0), (-1,-1), 1, colors.HexColor("#cbd5e1")),
        ]))
        elementos.append(tabela_formas)
        elementos.append(Spacer(1, 15))

        elementos.append(Paragraph("<b>Histórico Detalhado de Mesas Fechadas</b>", styles['Heading3']))
        elementos.append(Spacer(1, 5))

        dados_hist = [["Mesa", "Valor", "Pagamento", "Troco", "Data/Hora"]]
        for h in historico:
            dados_hist.append([str(h[0]), f"R$ {h[1]:.2f}", str(h[2]), f"R$ {h[3]}", str(h[4])])

        tabela_hist = Table(dados_hist, colWidths=[70, 80, 90, 70, 130])
        tabela_hist.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#e2e8f0")),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,-1), 9),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ]))
        elementos.append(tabela_hist)

        doc.build(elementos)

        caminho_zip = os.path.join(pasta_base, f"Fechamento_{data_alvo_str}.zip")
        comando_zip = f"zip -P {SENHA_ZIP} -j {caminho_zip} {caminho_pdf}"
        os.system(comando_zip)

        if os.path.exists(caminho_pdf):
            os.remove(caminho_pdf)

        print(f"[SUCESSO] Relatório salvo e protegido em: {caminho_zip}")

        cur.execute("DELETE FROM historico_mesas")
        conn.commit()
        return True

    except Exception as e:
        print(f"[ERRO NO FECHAMENTO]: {e}")
        conn.rollback()
        return False
    finally:
        cur.close()
        conn.close()

def executar_fechamento_profissional():
    data_hoje = datetime.now().strftime('%d-%m-%Y')
    gerar_pdf_fechamento(data_hoje)

def verificar_pendencia_ao_ligar():
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM historico_mesas")
        res = cur.fetchone()
        total_registros = res[0] if res else 0

        if total_registros > 0:
            print("[INFO] Fechamento pendente detectado ao iniciar o servidor. Processando...")
            data_pendente = (datetime.now() - timedelta(days=1)).strftime('%d-%m-%Y')
            gerar_pdf_fechamento(data_pendente)
        cur.close()
        conn.close()
    except Exception as e:
        # Ignora caso a tabela ainda não exista
        pass

# Executa a verificação de forma segura
verificar_pendencia_ao_ligar()

scheduler = BackgroundScheduler()
scheduler.add_job(func=executar_fechamento_profissional, trigger="cron", hour=4, minute=0)
scheduler.start()



```

---

## Arquivo: `./backup.py`

```text
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/backup")
def ver_backup(request: Request):
    status_backup = {} # Substitua pela sua lógica/banco
    return templates.TemplateResponse("backup.html", {
        "request": request, 
        "backup": status_backup
    })

```

---

## Arquivo: `./banco.py`

```text
import os
import psycopg2
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env da instância
load_dotenv()

def conectar():
    try:
        database_url = os.getenv("DATABASE_URL")

        if database_url:
            # Conecta usando a URL completa do .env (gerada pelo script de cadastro)
            return psycopg2.connect(database_url)
        else:
            # Fallback padrão caso não haja DATABASE_URL definida
            return psycopg2.connect(
                dbname=os.getenv("DB_NAME", "cardapio_pro_db"),
                user=os.getenv("DB_USER", "postgres"),
                password=os.getenv("DB_PASSWORD", ""),
                host=os.getenv("DB_HOST", "127.0.0.1"),
                port=os.getenv("DB_PORT", "5432")
            )
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        raise e



```

---

## Arquivo: `./bundle_projeto_total.py`

```text
import os
import base64

OUTPUT_FILE = "projeto_completo_para_ia.md"

def generate_tree(startpath='.'):
    tree_str = "## 🌳 Mapeamento Completo da Estrutura de Pastas e Arquivos\n\n```text\n"
    for root, dirs, files in os.walk(startpath):
        # Remove o próprio arquivo de saída da listagem se já existir
        if OUTPUT_FILE in files:
            files.remove(OUTPUT_FILE)
        level = root.replace(startpath, '').count(os.sep)
        indent = '│   ' * level + ('├── ' if level > 0 else '')
        tree_str += f"{indent}{os.path.basename(root)}/\n"
        sub_indent = '│   ' * (level + 1) + '├── '
        for f in sorted(files):
            tree_str += f"{sub_indent}{f}\n"
    tree_str += "```\n\n---\n\n"
    return tree_str

def is_binary(file_path):
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(1024)
            if b'\0' in chunk:
                return True
    except Exception:
        return True
    return False

def bundle_project():
    print("🚀 Iniciando a varredura total do projeto (sem exclusões)...")
    
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
        outfile.write("# 📂 Projeto Completo - Cardápio Pro (Varredura Total sem Filtros)\n\n")
        outfile.write("Este documento contém **absolutamente tudo** do projeto: código-fonte, configurações, banco de dados e dependências do ambiente virtual.\n\n---\n\n")
        
        print("Mapeando a estrutura de diretórios...")
        outfile.write(generate_tree('.'))
        
        for root, dirs, files in os.walk('.'):
            for file in sorted(files):
                file_path = os.path.join(root, file)
                
                if os.path.abspath(file_path) == os.path.abspath(OUTPUT_FILE):
                    continue
                
                print(f"Processando: {file_path}")
                outfile.write(f"## Arquivo: `{file_path}`\n\n")
                
                if is_binary(file_path):
                    outfile.write("*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*\n\n")
                    try:
                        with open(file_path, 'rb') as bin_file:
                            encoded = base64.b64encode(bin_file.read()).decode('utf-8')
                            outfile.write(f"```base64\n{encoded}\n```\n\n---\n\n")
                    except Exception as e:
                        outfile.write(f"Erro ao processar arquivo binário: {e}\n\n---\n\n")
                else:
                    outfile.write("```text\n")
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as infile:
                            outfile.write(infile.read())
                    except Exception as e:
                        outfile.write(f"Erro ao ler arquivo: {e}\n")
                    outfile.write("\n```\n\n---\n\n")
                    
    print(f"\n✨ Sucesso absoluto! O arquivo `{OUTPUT_FILE}` foi gerado na raiz do projeto.")

if __name__ == "__main__":
    bundle_project()

```

---

## Arquivo: `./cardapio.py`

```text
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/cardapio")
def ver_cardapio(request: Request):
    # Insira aqui a sua consulta real ao banco de dados se necessário
    itens_do_banco = [
        {"nome": "Hambúrguer Clássico", "descricao": "Pão, carne e queijo", "preco": "25,00"},
        {"nome": "Pizza Margherita", "descricao": "Molho, mussarela e manjericão", "preco": "45,00"}
    ]
    return templates.TemplateResponse("cardapio.html", {
        "request": request, 
        "itens": itens_do_banco
    })

```

---

## Arquivo: `./config.py`

```text
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/config")
def ver_config(request: Request):
    configuracoes = {} # Substitua pela sua lógica/banco
    return templates.TemplateResponse("config.html", {
        "request": request, 
        "config": configuracoes
    })

```

---

## Arquivo: `./config_rede.json`

```text
{
    "ip_rede": "192.168.0.110",
    "porta": "5003",
    "url_base": "http://192.168.0.110:5003"
}
```

---

## Arquivo: `./controle_sistema.py`

```text
import os
from fastapi import APIRouter, Request, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from banco import conectar

controle_bp = APIRouter()

# Garante que a tabela de status do sistema existe no banco
def garantir_tabela_controle():
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS sistema_status (
                id SERIAL PRIMARY KEY,
                status VARCHAR(20) DEFAULT 'ativo',
                mensagem VARCHAR(255) DEFAULT ''
            )
        """)
        cur.execute("SELECT COUNT(*) FROM sistema_status")
        if cur.fetchone()[0] == 0:
            cur.execute("INSERT INTO sistema_status (status, mensagem) VALUES ('ativo', '')")
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(f"[AVISO] Não foi possível garantir a tabela de controle agora: {e}")

garantir_tabela_controle()

# Função auxiliar para verificar o status atual
def obter_status_sistema():
    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("SELECT status, mensagem FROM sistema_status ORDER BY id DESC LIMIT 1")
        res = cur.fetchone()
        cur.close()
        conn.close()
        if res:
            return res[0], res[1]
    except Exception:
        pass
    return 'ativo', ''

# Middleware/Função para interceptar e bloquear requisições se necessário
def verificar_bloqueio_global():
    # Evita bloquear a própria rota de comando
    # No FastAPI, o request path vem tratado no middleware global
    pass

def checar_bloqueio_requisicao(path: str):
    if path == "/api/sistema/comando":
        return None

    status, mensagem = obter_status_sistema()

    # Rotas do cliente final que devem ser bloqueadas se o sistema estiver pausado ou bloqueado
    eh_rota_cliente = path == "/" or path.startswith("/menu/") or path.startswith("/extrato/")

    if status == 'bloqueado' or (status == 'pausado' and eh_rota_cliente):
        titulo = "Sistema Bloqueado" if status == 'bloqueado' else "Estabelecimento Pausado"
        msg_padrao = "Acesso suspenso temporariamente." if status == 'bloqueado' else "O estabelecimento está pausado no momento."
        msg_final = mensagem or msg_padrao

        html_conteudo = f"""
            <html>
            <head><title>{titulo}</title><meta charset="utf-8">
            <style>body{{font-family:Arial;background:#121212;color:#ff5252;display:flex;justify-content:center;align-items:center;height:100vh;margin:0;}}
            .box{{background:#1e1e1e;padding:40px;border-radius:8px;text-align:center;box-shadow:0 4px 15px rgba(0,0,0,0.5);}}
            h1{{margin-bottom:10px;}} p{{color:#aaa;}}</style></head>
            <body><div class="box">
                <h1>🔒 {titulo}</h1>
                <p>{msg_final}</p>
            </div></body></html>
        """
        return HTMLResponse(content=html_conteudo, status_code=403)

    if status == 'excluido':
        html_conteudo = """
            <html>
            <head><title>Sistema Desativado</title><meta charset="utf-8">
            <style>body{font-family:Arial;background:#121212;color:#ff9800;display:flex;justify-content:center;align-items:center;height:100vh;margin:0;}
            .box{background:#1e1e1e;padding:40px;border-radius:8px;text-align:center;box-shadow:0 4px 15px rgba(0,0,0,0.5);}
            h1{margin-bottom:10px;} p{color:#aaa;}</style></head>
            <body><div class="box">
                <h1>⚠️ Sistema Desativado</h1>
                <p>Os registros desta unidade foram removidos ou desativados pela matriz.</p>
            </div></body></html>
        """
        return HTMLResponse(content=html_conteudo, status_code=403)

    return None

# API para a Central enviar os comandos (Pausar, Bloquear, Excluir, Ativar)
@controle_bp.post('/api/sistema/comando')
async def receber_comando(request: Request):
    dados = await request.json() if request.headers.get("content-type") == "application/json" else {}
    print("[CLIENTE] Recebeu comando:", dados)
    novo_status = dados.get('status')
    mensagem = dados.get('mensagem', '')

    if novo_status not in ['ativo', 'pausado', 'bloqueado', 'excluido']:
        return JSONResponse({"erro": "Status inválido"}, status_code=400)

    try:
        conn = conectar()
        cur = conn.cursor()
        cur.execute("UPDATE sistema_status SET status = %s, mensagem = %s", (novo_status, mensagem))
        conn.commit()
        cur.close()
        conn.close()
        return JSONResponse({"sucesso": True, "status_atual": novo_status}, status_code=200)
    except Exception as e:
        return JSONResponse({"erro": str(e)}, status_code=500)




```

---

## Arquivo: `./database.py`

```text
import os
import psycopg2
from psycopg2.extras import RealDictCursor

DB_HOST = "localhost"
DB_NAME = "cardapio_db"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
DB_PORT = "5432"

def get_db():
    conn = psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT,
        cursor_factory=RealDictCursor
    )
    return conn

def init_db():
    conn = get_db()
    cursor = conn.cursor()
    
    # Tabela de Estabelecimentos (Tenants) com Slug único
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS estabelecimentos (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            slug VARCHAR(100) UNIQUE NOT NULL,
            quantidade_mesas INT NOT NULL DEFAULT 10,
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # Tabela de Produtos vinculada ao estabelecimento
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id SERIAL PRIMARY KEY,
            estabelecimento_id INT REFERENCES estabelecimentos(id) ON DELETE CASCADE,
            nome VARCHAR(100) NOT NULL,
            descricao TEXT,
            preco NUMERIC(10,2) NOT NULL,
            categoria VARCHAR(50) NOT NULL,
            foto VARCHAR(255),
            visivel BOOLEAN DEFAULT TRUE,
            arquivado BOOLEAN DEFAULT FALSE
        );
    """)

    # Tabela de Pedidos vinculada ao estabelecimento
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS pedidos (
            id SERIAL PRIMARY KEY,
            estabelecimento_id INT REFERENCES estabelecimentos(id) ON DELETE CASCADE,
            mesa INT NOT NULL,
            itens TEXT NOT NULL,
            total NUMERIC(10,2) NOT NULL,
            forma_pagamento VARCHAR(30) DEFAULT 'Não informada',
            status VARCHAR(30) DEFAULT 'Pendente',
            criado_em TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    conn.commit()
    cursor.close()
    conn.close()

```

---

## Arquivo: `./inspetor.py`

```text
import traceback
import sys
import os
import platform
import httpx
from banco import conectar

CENTRAL_URL = os.getenv("CENTRAL_URL", "http://localhost:8000")
CLIENTE_ID = os.getenv("CLIENTE_ID", "matriz")

class InspetorSistema:
    @staticmethod
    def diagnosticar_ambiente():
        status_banco = "Desconectado"
        try:
            conn = conectar()
            cur = conn.cursor()
            cur.execute("SELECT 1;")
            cur.close()
            conn.close()
            status_banco = "Online e Saudável"
        except Exception as e:
            status_banco = f"Erro no Banco: {str(e)}"

        return {
            "sistema_operacional": platform.system(),
            "versao_python": sys.version.split()[0],
            "banco_dados": status_banco,
            "ambiente_termux": "com.termux" in os.getenv("PREFIX", "")
        }

def capturar_erro(e):
    """Captura a exceção atual, formata no padrão esperado pela Central e envia."""
    try:
        exc_type, exc_value, exc_tb = sys.exc_info()

        # Pega o nome do módulo ou arquivo principal onde ocorreu o erro
        tb_list = traceback.extract_tb(exc_tb)
        modulo_origem = os.path.basename(tb_list[-1].filename) if tb_list else "main.py"

        # Formata o erro como string conforme exigido pela Central
        mensagem_erro = f"{exc_type.__name__ if exc_type else 'Exception'}: {str(exc_value)}"

        payload = {
            "cliente_id": CLIENTE_ID,
            "erro": mensagem_erro,
            "modulo": modulo_origem,
            "ambiente": InspetorSistema.diagnosticar_ambiente()
        }

        url = f"{CENTRAL_URL}/suporte/{CLIENTE_ID}/reportar"
        httpx.post(url, json=payload, timeout=2.0)
    except Exception:
        pass


```

---

## Arquivo: `./migrar_tenant.py`

```text
from database import get_db, init_db

def migrar():
    init_db()
    conn = get_db()
    cursor = conn.cursor()
    
    # Garante que as colunas de relacionamento existem nas tabelas antigas
    for tabela in ['produtos', 'pedidos']:
        cursor.execute(f"""
            DO $$ 
            BEGIN 
                IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name='{tabela}' and column_name='estabelecimento_id') THEN
                    ALTER TABLE {tabela} ADD COLUMN estabelecimento_id INT REFERENCES estabelecimentos(id) ON DELETE CASCADE;
                END IF;
            END $$;
        """)
    
    conn.commit()
    
    # Verifica se já existe um estabelecimento padrão
    cursor.execute("SELECT id FROM estabelecimentos WHERE slug = 'joel-burguer';")
    est = cursor.fetchone()
    
    if not est:
        print("Criando estabelecimento padrão: Joel Burger (slug: joel-burguer)...")
        cursor.execute(
            "INSERT INTO estabelecimentos (nome, slug, quantidade_mesas) VALUES (%s, %s, %s) RETURNING id;",
            ("Joel Burger", "joel-burguer", 10)
        )
        est_id = cursor.fetchone()['id']
        conn.commit()
    else:
        est_id = est['id']
        print(f"Estabelecimento padrão já existe com ID: {est_id}")
    
    # Atualiza registros antigos que estejam sem estabelecimento_id
    cursor.execute("UPDATE produtos SET estabelecimento_id = %s WHERE estabelecimento_id IS NULL;", (est_id,))
    cursor.execute("UPDATE pedidos SET estabelecimento_id = %s WHERE estabelecimento_id IS NULL;", (est_id,))
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Migração concluída com sucesso!")

if __name__ == "__main__":
    migrar()

```

---

## Arquivo: `./models.py`

```text
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Estabelecimento(Base):
    __tablename__ = "estabelecimentos"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String, unique=True, index=True)
    nome = Column(String, nullable=False)
    quantidade_mesas = Column(Integer, default=10)

class Categoria(Base):
    __tablename__ = "categorias"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    estabelecimento_id = Column(Integer, ForeignKey("estabelecimentos.id"))

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    descricao = Column(String, nullable=True)
    estabelecimento_id = Column(Integer, ForeignKey("estabelecimentos.id"))

```

---

## Arquivo: `./pagamento.py`

```text
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/pagamento")
def ver_pagamento(request: Request):
    # Lógica de pagamento do seu projeto
    dados_pagamento = {"status": "Aguardando pagamento"}
    return templates.TemplateResponse("pagamento.html", {
        "request": request, 
        "pagamento": dados_pagamento
    })

```

---

## Arquivo: `./pedidos.py`

```text
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/pedidos")
def ver_pedidos(request: Request):
    # Insira aqui a sua consulta real ao banco de dados se necessário
    pedidos_do_banco = [
        {"id": 101, "cliente": "Carlos Silva", "status": "Pendente", "total": "70,00"},
        {"id": 102, "cliente": "Ana Souza", "status": "Em preparo", "total": "25,00"}
    ]
    return templates.TemplateResponse("pedidos.html", {
        "request": request, 
        "pedidos": pedidos_do_banco
    })

```

---

## Arquivo: `./qrcode.py`

```text
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/qrcode")
def ver_qrcode(request: Request):
    dados_qrcode = {} # Substitua pela sua lógica/banco
    return templates.TemplateResponse("qrcode.html", {
        "request": request, 
        "qrcode": dados_qrcode
    })

```

---

## Arquivo: `./registros.py`

```text
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/registros")
def ver_registros(request: Request):
    lista_registros = [] # Substitua pela sua lógica/banco
    return templates.TemplateResponse("registros.html", {
        "request": request, 
        "registros": lista_registros
    })

```

---

## Arquivo: `./rotas_administrativas.py`

```text

```

---

## Arquivo: `./run.sh`

```text
#!/bin/bash
echo "Iniciando a API do Cardápio Pro no Termux..."
python3 app.py

```

---

## Arquivo: `./utils_pagamento.py`

```text

```

---

## Arquivo: `./.git/COMMIT_EDITMSG`

```text
Backup: ajustes no painel de pedidos e mesas

```

---

## Arquivo: `./.git/FETCH_HEAD`

```text
c650d325f4b616f6e450052fc3fffa932e1380c6		branch 'main' of https://github.com/Joeltx123/clientes_cardapio_instancias

```

---

## Arquivo: `./.git/HEAD`

```text
ref: refs/heads/main

```

---

## Arquivo: `./.git/ORIG_HEAD`

```text
c650d325f4b616f6e450052fc3fffa932e1380c6

```

---

## Arquivo: `./.git/config`

```text
[core]
	repositoryformatversion = 0
	filemode = true
	bare = false
	logallrefupdates = true
[remote "origin"]
	url = https://github.com/Joeltx123/clientes_cardapio_instancias.git
	fetch = +refs/heads/*:refs/remotes/origin/*
[branch "main"]
	remote = origin
	merge = refs/heads/main

```

---

## Arquivo: `./.git/description`

```text
Unnamed repository; edit this file 'description' to name the repository.

```

---

## Arquivo: `./.git/index`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/hooks/applypatch-msg.sample`

```text
#!/data/data/com.termux/files/usr/bin/sh
#
# An example hook script to check the commit log message taken by
# applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.  The hook is
# allowed to edit the commit message file.
#
# To enable this hook, rename this file to "applypatch-msg".

. git-sh-setup
commitmsg="$(git rev-parse --git-path hooks/commit-msg)"
test -x "$commitmsg" && exec "$commitmsg" ${1+"$@"}
:

```

---

## Arquivo: `./.git/hooks/commit-msg.sample`

```text
#!/data/data/com.termux/files/usr/bin/sh
#
# An example hook script to check the commit log message.
# Called by "git commit" with one argument, the name of the file
# that has the commit message.  The hook should exit with non-zero
# status after issuing an appropriate message if it wants to stop the
# commit.  The hook is allowed to edit the commit message file.
#
# To enable this hook, rename this file to "commit-msg".

# Uncomment the below to add a Signed-off-by line to the message.
# Doing this in a hook is a bad idea in general, but the prepare-commit-msg
# hook is more suited to it.
#
# SOB=$(git var GIT_AUTHOR_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# grep -qs "^$SOB" "$1" || echo "$SOB" >> "$1"

# This example catches duplicate Signed-off-by lines and messages that
# would confuse 'git am'.

ret=0

test "" = "$(grep '^Signed-off-by: ' "$1" |
	 sort | uniq -c | sed -e '/^[ 	]*1[ 	]/d')" || {
	echo >&2 Duplicate Signed-off-by lines.
	ret=1
}

comment_re="$(
	{
		git config --get-regexp "^core\.comment(char|string)\$" ||
			echo '#'
	} | sed -n -e '
		${
			s/^[^ ]* //
			s|[][*./\]|\\&|g
			s/^auto$/[#;@!$%^&|:]/
			p
		}'
)"
scissors_line="^${comment_re} -\{8,\} >8 -\{8,\}\$"
comment_line="^${comment_re}.*"
blank_line='^[ 	]*$'
# Disallow lines starting with "diff -" or "Index: " in the body of the
# message. Stop looking if we see a scissors line.
line="$(sed -n -e "
	# Skip comments and blank lines at the start of the file.
	/${scissors_line}/q
	/${comment_line}/d
	/${blank_line}/d
	# The first paragraph will become the subject header so
	# does not need to be checked.
	: subject
	n
	/${scissors_line}/q
	/${blank_line}/!b subject
	# Check the body of the message for problematic
	# prefixes.
	: body
	n
	/${scissors_line}/q
	/${comment_line}/b body
	/^diff -/{p;q;}
	/^Index: /{p;q;}
	b body
	" "$1")"
if test -n "$line"
then
	echo >&2 "Message contains a diff that will confuse 'git am'."
	echo >&2 "To fix this indent the diff."
	ret=1
fi

exit $ret

```

---

## Arquivo: `./.git/hooks/fsmonitor-watchman.sample`

```text
#!/data/data/com.termux/files/usr/bin/perl

use strict;
use warnings;
use IPC::Open2;

# An example hook script to integrate Watchman
# (https://facebook.github.io/watchman/) with git to speed up detecting
# new and modified files.
#
# The hook is passed a version (currently 2) and last update token
# formatted as a string and outputs to stdout a new update token and
# all files that have been modified since the update token. Paths must
# be relative to the root of the working tree and separated by a single NUL.
#
# To enable this hook, rename this file to "query-watchman" and set
# 'git config core.fsmonitor .git/hooks/query-watchman'
#
my ($version, $last_update_token) = @ARGV;

# Uncomment for debugging
# print STDERR "$0 $version $last_update_token\n";

# Check the hook interface version
if ($version ne 2) {
	die "Unsupported query-fsmonitor hook version '$version'.\n" .
	    "Falling back to scanning...\n";
}

my $git_work_tree = get_working_dir();

my $json_pkg;
eval {
	require JSON::XS;
	$json_pkg = "JSON::XS";
	1;
} or do {
	require JSON::PP;
	$json_pkg = "JSON::PP";
};

launch_watchman();

sub launch_watchman {
	my $o = watchman_query();
	if (is_work_tree_watched($o)) {
		output_result($o->{clock}, @{$o->{files}});
	}
}

sub output_result {
	my ($clockid, @files) = @_;

	# Uncomment for debugging watchman output
	# open (my $fh, ">", ".git/watchman-output.out");
	# binmode $fh, ":utf8";
	# print $fh "$clockid\n@files\n";
	# close $fh;

	binmode STDOUT, ":utf8";
	print $clockid;
	print "\0";
	local $, = "\0";
	print @files;
}

sub watchman_clock {
	my $response = qx/watchman clock "$git_work_tree"/;
	die "Failed to get clock id on '$git_work_tree'.\n" .
		"Falling back to scanning...\n" if $? != 0;

	return $json_pkg->new->utf8->decode($response);
}

sub watchman_query {
	my $pid = open2(\*CHLD_OUT, \*CHLD_IN, 'watchman -j --no-pretty')
	or die "open2() failed: $!\n" .
	"Falling back to scanning...\n";

	# In the query expression below we're asking for names of files that
	# changed since $last_update_token but not from the .git folder.
	#
	# To accomplish this, we're using the "since" generator to use the
	# recency index to select candidate nodes and "fields" to limit the
	# output to file names only. Then we're using the "expression" term to
	# further constrain the results.
	my $last_update_line = "";
	if (substr($last_update_token, 0, 1) eq "c") {
		$last_update_token = "\"$last_update_token\"";
		$last_update_line = qq[\n"since": $last_update_token,];
	}
	my $query = <<"	END";
		["query", "$git_work_tree", {$last_update_line
			"fields": ["name"],
			"expression": ["not", ["dirname", ".git"]]
		}]
	END

	# Uncomment for debugging the watchman query
	# open (my $fh, ">", ".git/watchman-query.json");
	# print $fh $query;
	# close $fh;

	print CHLD_IN $query;
	close CHLD_IN;
	my $response = do {local $/; <CHLD_OUT>};

	# Uncomment for debugging the watch response
	# open ($fh, ">", ".git/watchman-response.json");
	# print $fh $response;
	# close $fh;

	die "Watchman: command returned no output.\n" .
	"Falling back to scanning...\n" if $response eq "";
	die "Watchman: command returned invalid output: $response\n" .
	"Falling back to scanning...\n" unless $response =~ /^\{/;

	return $json_pkg->new->utf8->decode($response);
}

sub is_work_tree_watched {
	my ($output) = @_;
	my $error = $output->{error};
	if ($error and $error =~ m/unable to resolve root .* directory (.*) is not watched/) {
		my $response = qx/watchman watch "$git_work_tree"/;
		die "Failed to make watchman watch '$git_work_tree'.\n" .
		    "Falling back to scanning...\n" if $? != 0;
		$output = $json_pkg->new->utf8->decode($response);
		$error = $output->{error};
		die "Watchman: $error.\n" .
		"Falling back to scanning...\n" if $error;

		# Uncomment for debugging watchman output
		# open (my $fh, ">", ".git/watchman-output.out");
		# close $fh;

		# Watchman will always return all files on the first query so
		# return the fast "everything is dirty" flag to git and do the
		# Watchman query just to get it over with now so we won't pay
		# the cost in git to look up each individual file.
		my $o = watchman_clock();
		$error = $o->{error};

		die "Watchman: $error.\n" .
		"Falling back to scanning...\n" if $error;

		output_result($o->{clock}, ("/"));
		return 0;
	}

	die "Watchman: $error.\n" .
	"Falling back to scanning...\n" if $error;

	return 1;
}

sub get_working_dir {
	my $working_dir;
	if ($^O =~ 'msys' || $^O =~ 'cygwin') {
		$working_dir = Win32::GetCwd();
		$working_dir =~ tr/\\/\//;
	} else {
		require Cwd;
		$working_dir = Cwd::cwd();
	}

	return $working_dir;
}

```

---

## Arquivo: `./.git/hooks/post-update.sample`

```text
#!/data/data/com.termux/files/usr/bin/sh
#
# An example hook script to prepare a packed repository for use over
# dumb transports.
#
# To enable this hook, rename this file to "post-update".

exec git update-server-info

```

---

## Arquivo: `./.git/hooks/pre-applypatch.sample`

```text
#!/data/data/com.termux/files/usr/bin/sh
#
# An example hook script to verify what is about to be committed
# by applypatch from an e-mail message.
#
# The hook should exit with non-zero status after issuing an
# appropriate message if it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-applypatch".

. git-sh-setup
precommit="$(git rev-parse --git-path hooks/pre-commit)"
test -x "$precommit" && exec "$precommit" ${1+"$@"}
:

```

---

## Arquivo: `./.git/hooks/pre-commit.sample`

```text
#!/data/data/com.termux/files/usr/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git commit" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message if
# it wants to stop the commit.
#
# To enable this hook, rename this file to "pre-commit".

if git rev-parse --verify HEAD >/dev/null 2>&1
then
	against=HEAD
else
	# Initial commit: diff against an empty tree object
	against=$(git hash-object -t tree /dev/null)
fi

# If you want to allow non-ASCII filenames set this variable to true.
allownonascii=$(git config --type=bool hooks.allownonascii)

# Redirect output to stderr.
exec 1>&2

# Cross platform projects tend to avoid non-ASCII filenames; prevent
# them from being added to the repository. We exploit the fact that the
# printable range starts at the space character and ends with tilde.
if [ "$allownonascii" != "true" ] &&
	# Note that the use of brackets around a tr range is ok here, (it's
	# even required, for portability to Solaris 10's /usr/bin/tr), since
	# the square bracket bytes happen to fall in the designated range.
	test $(git diff-index --cached --name-only --diff-filter=A -z $against |
	  LC_ALL=C tr -d '[ -~]\0' | wc -c) != 0
then
	cat <<\EOF
Error: Attempt to add a non-ASCII file name.

This can cause problems if you want to work with people on other platforms.

To be portable it is advisable to rename the file.

If you know what you are doing you can disable this check using:

  git config hooks.allownonascii true
EOF
	exit 1
fi

# If there are whitespace errors, print the offending file names and fail.
exec git diff-index --check --cached $against --

```

---

## Arquivo: `./.git/hooks/pre-merge-commit.sample`

```text
#!/data/data/com.termux/files/usr/bin/sh
#
# An example hook script to verify what is about to be committed.
# Called by "git merge" with no arguments.  The hook should
# exit with non-zero status after issuing an appropriate message to
# stderr if it wants to stop the merge commit.
#
# To enable this hook, rename this file to "pre-merge-commit".

. git-sh-setup
test -x "$GIT_DIR/hooks/pre-commit" &&
        exec "$GIT_DIR/hooks/pre-commit"
:

```

---

## Arquivo: `./.git/hooks/pre-push.sample`

```text
#!/data/data/com.termux/files/usr/bin/sh

# An example hook script to verify what is about to be pushed.  Called by "git
# push" after it has checked the remote status, but before anything has been
# pushed.  If this script exits with a non-zero status nothing will be pushed.
#
# This hook is called with the following parameters:
#
# $1 -- Name of the remote to which the push is being done
# $2 -- URL to which the push is being done
#
# If pushing without using a named remote those arguments will be equal.
#
# Information about the commits which are being pushed is supplied as lines to
# the standard input in the form:
#
#   <local ref> <local oid> <remote ref> <remote oid>
#
# This sample shows how to prevent push of commits where the log message starts
# with "WIP" (work in progress).

remote="$1"
url="$2"

zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')

while read local_ref local_oid remote_ref remote_oid
do
	if test "$local_oid" = "$zero"
	then
		# Handle delete
		:
	else
		if test "$remote_oid" = "$zero"
		then
			# New branch, examine all commits
			range="$local_oid"
		else
			# Update to existing branch, examine new commits
			range="$remote_oid..$local_oid"
		fi

		# Check for WIP commit
		commit=$(git rev-list -n 1 --grep '^WIP' "$range")
		if test -n "$commit"
		then
			echo >&2 "Found WIP commit in $local_ref, not pushing"
			exit 1
		fi
	fi
done

exit 0

```

---

## Arquivo: `./.git/hooks/pre-rebase.sample`

```text
#!/data/data/com.termux/files/usr/bin/sh
#
# Copyright (c) 2006, 2008 Junio C Hamano
#
# The "pre-rebase" hook is run just before "git rebase" starts doing
# its job, and can prevent the command from running by exiting with
# non-zero status.
#
# The hook is called with the following parameters:
#
# $1 -- the upstream the series was forked from.
# $2 -- the branch being rebased (or empty when rebasing the current branch).
#
# This sample shows how to prevent topic branches that are already
# merged to 'next' branch from getting rebased, because allowing it
# would result in rebasing already published history.

publish=next
basebranch="$1"
if test "$#" = 2
then
	topic="refs/heads/$2"
else
	topic=`git symbolic-ref HEAD` ||
	exit 0 ;# we do not interrupt rebasing detached HEAD
fi

case "$topic" in
refs/heads/??/*)
	;;
*)
	exit 0 ;# we do not interrupt others.
	;;
esac

# Now we are dealing with a topic branch being rebased
# on top of master.  Is it OK to rebase it?

# Does the topic really exist?
git show-ref -q "$topic" || {
	echo >&2 "No such branch $topic"
	exit 1
}

# Is topic fully merged to master?
not_in_master=`git rev-list --pretty=oneline ^master "$topic"`
if test -z "$not_in_master"
then
	echo >&2 "$topic is fully merged to master; better remove it."
	exit 1 ;# we could allow it, but there is no point.
fi

# Is topic ever merged to next?  If so you should not be rebasing it.
only_next_1=`git rev-list ^master "^$topic" ${publish} | sort`
only_next_2=`git rev-list ^master           ${publish} | sort`
if test "$only_next_1" = "$only_next_2"
then
	not_in_topic=`git rev-list "^$topic" master`
	if test -z "$not_in_topic"
	then
		echo >&2 "$topic is already up to date with master"
		exit 1 ;# we could allow it, but there is no point.
	else
		exit 0
	fi
else
	not_in_next=`git rev-list --pretty=oneline ^${publish} "$topic"`
	/usr/bin/perl -e '
		my $topic = $ARGV[0];
		my $msg = "* $topic has commits already merged to public branch:\n";
		my (%not_in_next) = map {
			/^([0-9a-f]+) /;
			($1 => 1);
		} split(/\n/, $ARGV[1]);
		for my $elem (map {
				/^([0-9a-f]+) (.*)$/;
				[$1 => $2];
			} split(/\n/, $ARGV[2])) {
			if (!exists $not_in_next{$elem->[0]}) {
				if ($msg) {
					print STDERR $msg;
					undef $msg;
				}
				print STDERR " $elem->[1]\n";
			}
		}
	' "$topic" "$not_in_next" "$not_in_master"
	exit 1
fi

<<\DOC_END

This sample hook safeguards topic branches that have been
published from being rewound.

The workflow assumed here is:

 * Once a topic branch forks from "master", "master" is never
   merged into it again (either directly or indirectly).

 * Once a topic branch is fully cooked and merged into "master",
   it is deleted.  If you need to build on top of it to correct
   earlier mistakes, a new topic branch is created by forking at
   the tip of the "master".  This is not strictly necessary, but
   it makes it easier to keep your history simple.

 * Whenever you need to test or publish your changes to topic
   branches, merge them into "next" branch.

The script, being an example, hardcodes the publish branch name
to be "next", but it is trivial to make it configurable via
$GIT_DIR/config mechanism.

With this workflow, you would want to know:

(1) ... if a topic branch has ever been merged to "next".  Young
    topic branches can have stupid mistakes you would rather
    clean up before publishing, and things that have not been
    merged into other branches can be easily rebased without
    affecting other people.  But once it is published, you would
    not want to rewind it.

(2) ... if a topic branch has been fully merged to "master".
    Then you can delete it.  More importantly, you should not
    build on top of it -- other people may already want to
    change things related to the topic as patches against your
    "master", so if you need further changes, it is better to
    fork the topic (perhaps with the same name) afresh from the
    tip of "master".

Let's look at this example:

		   o---o---o---o---o---o---o---o---o---o "next"
		  /       /           /           /
		 /   a---a---b A     /           /
		/   /               /           /
	       /   /   c---c---c---c B         /
	      /   /   /             \         /
	     /   /   /   b---b C     \       /
	    /   /   /   /             \     /
    ---o---o---o---o---o---o---o---o---o---o---o "master"


A, B and C are topic branches.

 * A has one fix since it was merged up to "next".

 * B has finished.  It has been fully merged up to "master" and "next",
   and is ready to be deleted.

 * C has not merged to "next" at all.

We would want to allow C to be rebased, refuse A, and encourage
B to be deleted.

To compute (1):

	git rev-list ^master ^topic next
	git rev-list ^master        next

	if these match, topic has not merged in next at all.

To compute (2):

	git rev-list master..topic

	if this is empty, it is fully merged to "master".

DOC_END

```

---

## Arquivo: `./.git/hooks/pre-receive.sample`

```text
#!/data/data/com.termux/files/usr/bin/sh
#
# An example hook script to make use of push options.
# The example simply echoes all push options that start with 'echoback='
# and rejects all pushes when the "reject" push option is used.
#
# To enable this hook, rename this file to "pre-receive".

if test -n "$GIT_PUSH_OPTION_COUNT"
then
	i=0
	while test "$i" -lt "$GIT_PUSH_OPTION_COUNT"
	do
		eval "value=\$GIT_PUSH_OPTION_$i"
		case "$value" in
		echoback=*)
			echo "echo from the pre-receive-hook: ${value#*=}" >&2
			;;
		reject)
			exit 1
		esac
		i=$((i + 1))
	done
fi

```

---

## Arquivo: `./.git/hooks/prepare-commit-msg.sample`

```text
#!/data/data/com.termux/files/usr/bin/sh
#
# An example hook script to prepare the commit log message.
# Called by "git commit" with the name of the file that has the
# commit message, followed by the description of the commit
# message's source.  The hook's purpose is to edit the commit
# message file.  If the hook fails with a non-zero status,
# the commit is aborted.
#
# To enable this hook, rename this file to "prepare-commit-msg".

# This hook includes three examples. The first one removes the
# "# Please enter the commit message..." help message.
#
# The second includes the output of "git diff --name-status -r"
# into the message, just before the "git status" output.  It is
# commented because it doesn't cope with --amend or with squashed
# commits.
#
# The third example adds a Signed-off-by line to the message, that can
# still be edited.  This is rarely a good idea.

COMMIT_MSG_FILE=$1
COMMIT_SOURCE=$2
SHA1=$3

/usr/bin/perl -i.bak -ne 'print unless(m/^. Please enter the commit message/..m/^#$/)' "$COMMIT_MSG_FILE"

# case "$COMMIT_SOURCE,$SHA1" in
#  ,|template,)
#    /usr/bin/perl -i.bak -pe '
#       print "\n" . `git diff --cached --name-status -r`
# 	 if /^#/ && $first++ == 0' "$COMMIT_MSG_FILE" ;;
#  *) ;;
# esac

# SOB=$(git var GIT_COMMITTER_IDENT | sed -n 's/^\(.*>\).*$/Signed-off-by: \1/p')
# git interpret-trailers --in-place --trailer "$SOB" "$COMMIT_MSG_FILE"
# if test -z "$COMMIT_SOURCE"
# then
#   /usr/bin/perl -i.bak -pe 'print "\n" if !$first_line++' "$COMMIT_MSG_FILE"
# fi

```

---

## Arquivo: `./.git/hooks/push-to-checkout.sample`

```text
#!/data/data/com.termux/files/usr/bin/sh

# An example hook script to update a checked-out tree on a git push.
#
# This hook is invoked by git-receive-pack(1) when it reacts to git
# push and updates reference(s) in its repository, and when the push
# tries to update the branch that is currently checked out and the
# receive.denyCurrentBranch configuration variable is set to
# updateInstead.
#
# By default, such a push is refused if the working tree and the index
# of the remote repository has any difference from the currently
# checked out commit; when both the working tree and the index match
# the current commit, they are updated to match the newly pushed tip
# of the branch. This hook is to be used to override the default
# behaviour; however the code below reimplements the default behaviour
# as a starting point for convenient modification.
#
# The hook receives the commit with which the tip of the current
# branch is going to be updated:
commit=$1

# It can exit with a non-zero status to refuse the push (when it does
# so, it must not modify the index or the working tree).
die () {
	echo >&2 "$*"
	exit 1
}

# Or it can make any necessary changes to the working tree and to the
# index to bring them to the desired state when the tip of the current
# branch is updated to the new commit, and exit with a zero status.
#
# For example, the hook can simply run git read-tree -u -m HEAD "$1"
# in order to emulate git fetch that is run in the reverse direction
# with git push, as the two-tree form of git read-tree -u -m is
# essentially the same as git switch or git checkout that switches
# branches while keeping the local changes in the working tree that do
# not interfere with the difference between the branches.

# The below is a more-or-less exact translation to shell of the C code
# for the default behaviour for git's push-to-checkout hook defined in
# the push_to_deploy() function in builtin/receive-pack.c.
#
# Note that the hook will be executed from the repository directory,
# not from the working tree, so if you want to perform operations on
# the working tree, you will have to adapt your code accordingly, e.g.
# by adding "cd .." or using relative paths.

if ! git update-index -q --ignore-submodules --refresh
then
	die "Up-to-date check failed"
fi

if ! git diff-files --quiet --ignore-submodules --
then
	die "Working directory has unstaged changes"
fi

# This is a rough translation of:
#
#   head_has_history() ? "HEAD" : EMPTY_TREE_SHA1_HEX
if git cat-file -e HEAD 2>/dev/null
then
	head=HEAD
else
	head=$(git hash-object -t tree --stdin </dev/null)
fi

if ! git diff-index --quiet --cached --ignore-submodules $head --
then
	die "Working directory has staged changes"
fi

if ! git read-tree -u -m "$commit"
then
	die "Could not update working tree to new HEAD"
fi

```

---

## Arquivo: `./.git/hooks/sendemail-validate.sample`

```text
#!/data/data/com.termux/files/usr/bin/sh

# An example hook script to validate a patch (and/or patch series) before
# sending it via email.
#
# The hook should exit with non-zero status after issuing an appropriate
# message if it wants to prevent the email(s) from being sent.
#
# To enable this hook, rename this file to "sendemail-validate".
#
# By default, it will only check that the patch(es) can be applied on top of
# the default upstream branch without conflicts in a secondary worktree. After
# validation (successful or not) of the last patch of a series, the worktree
# will be deleted.
#
# The following config variables can be set to change the default remote and
# remote ref that are used to apply the patches against:
#
#   sendemail.validateRemote (default: origin)
#   sendemail.validateRemoteRef (default: HEAD)
#
# Replace the TODO placeholders with appropriate checks according to your
# needs.

validate_cover_letter () {
	file="$1"
	# TODO: Replace with appropriate checks (e.g. spell checking).
	true
}

validate_patch () {
	file="$1"
	# Ensure that the patch applies without conflicts.
	git am -3 "$file" || return
	# TODO: Replace with appropriate checks for this patch
	# (e.g. checkpatch.pl).
	true
}

validate_series () {
	# TODO: Replace with appropriate checks for the whole series
	# (e.g. quick build, coding style checks, etc.).
	true
}

# main -------------------------------------------------------------------------

if test "$GIT_SENDEMAIL_FILE_COUNTER" = 1
then
	remote=$(git config --default origin --get sendemail.validateRemote) &&
	ref=$(git config --default HEAD --get sendemail.validateRemoteRef) &&
	worktree=$(mktemp --tmpdir -d sendemail-validate.XXXXXXX) &&
	git worktree add -fd --checkout "$worktree" "refs/remotes/$remote/$ref" &&
	git config --replace-all sendemail.validateWorktree "$worktree"
else
	worktree=$(git config --get sendemail.validateWorktree)
fi || {
	echo "sendemail-validate: error: failed to prepare worktree" >&2
	exit 1
}

unset GIT_DIR GIT_WORK_TREE
cd "$worktree" &&

if grep -q "^diff --git " "$1"
then
	validate_patch "$1"
else
	validate_cover_letter "$1"
fi &&

if test "$GIT_SENDEMAIL_FILE_COUNTER" = "$GIT_SENDEMAIL_FILE_TOTAL"
then
	git config --unset-all sendemail.validateWorktree &&
	trap 'git worktree remove -ff "$worktree"' EXIT &&
	validate_series
fi

```

---

## Arquivo: `./.git/hooks/update.sample`

```text
#!/data/data/com.termux/files/usr/bin/sh
#
# An example hook script to block unannotated tags from entering.
# Called by "git receive-pack" with arguments: refname sha1-old sha1-new
#
# To enable this hook, rename this file to "update".
#
# Config
# ------
# hooks.allowunannotated
#   This boolean sets whether unannotated tags will be allowed into the
#   repository.  By default they won't be.
# hooks.allowdeletetag
#   This boolean sets whether deleting tags will be allowed in the
#   repository.  By default they won't be.
# hooks.allowmodifytag
#   This boolean sets whether a tag may be modified after creation. By default
#   it won't be.
# hooks.allowdeletebranch
#   This boolean sets whether deleting branches will be allowed in the
#   repository.  By default they won't be.
# hooks.denycreatebranch
#   This boolean sets whether remotely creating branches will be denied
#   in the repository.  By default this is allowed.
#

# --- Command line
refname="$1"
oldrev="$2"
newrev="$3"

# --- Safety check
if [ -z "$GIT_DIR" ]; then
	echo "Don't run this script from the command line." >&2
	echo " (if you want, you could supply GIT_DIR then run" >&2
	echo "  $0 <ref> <oldrev> <newrev>)" >&2
	exit 1
fi

if [ -z "$refname" -o -z "$oldrev" -o -z "$newrev" ]; then
	echo "usage: $0 <ref> <oldrev> <newrev>" >&2
	exit 1
fi

# --- Config
allowunannotated=$(git config --type=bool hooks.allowunannotated)
allowdeletebranch=$(git config --type=bool hooks.allowdeletebranch)
denycreatebranch=$(git config --type=bool hooks.denycreatebranch)
allowdeletetag=$(git config --type=bool hooks.allowdeletetag)
allowmodifytag=$(git config --type=bool hooks.allowmodifytag)

# check for no description
projectdesc=$(sed -e '1q' "$GIT_DIR/description")
case "$projectdesc" in
"Unnamed repository"* | "")
	echo "*** Project description file hasn't been set" >&2
	exit 1
	;;
esac

# --- Check types
# if $newrev is 0000...0000, it's a commit to delete a ref.
zero=$(git hash-object --stdin </dev/null | tr '[0-9a-f]' '0')
if [ "$newrev" = "$zero" ]; then
	newrev_type=delete
else
	newrev_type=$(git cat-file -t $newrev)
fi

case "$refname","$newrev_type" in
	refs/tags/*,commit)
		# un-annotated tag
		short_refname=${refname##refs/tags/}
		if [ "$allowunannotated" != "true" ]; then
			echo "*** The un-annotated tag, $short_refname, is not allowed in this repository" >&2
			echo "*** Use 'git tag [ -a | -s ]' for tags you want to propagate." >&2
			exit 1
		fi
		;;
	refs/tags/*,delete)
		# delete tag
		if [ "$allowdeletetag" != "true" ]; then
			echo "*** Deleting a tag is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/tags/*,tag)
		# annotated tag
		if [ "$allowmodifytag" != "true" ] && git rev-parse $refname > /dev/null 2>&1
		then
			echo "*** Tag '$refname' already exists." >&2
			echo "*** Modifying a tag is not allowed in this repository." >&2
			exit 1
		fi
		;;
	refs/heads/*,commit)
		# branch
		if [ "$oldrev" = "$zero" -a "$denycreatebranch" = "true" ]; then
			echo "*** Creating a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/heads/*,delete)
		# delete branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	refs/remotes/*,commit)
		# tracking branch
		;;
	refs/remotes/*,delete)
		# delete tracking branch
		if [ "$allowdeletebranch" != "true" ]; then
			echo "*** Deleting a tracking branch is not allowed in this repository" >&2
			exit 1
		fi
		;;
	*)
		# Anything else (is there anything else?)
		echo "*** Update hook: unknown type of update to ref $refname of type $newrev_type" >&2
		exit 1
		;;
esac

# --- Finished
exit 0

```

---

## Arquivo: `./.git/info/exclude`

```text
# git ls-files --others --exclude-from=.git/info/exclude
# Lines that start with '#' are comments.
# For a project mostly in C, the following would be a good set of
# exclude patterns (uncomment them if you want to use them):
# *.[oa]
# *~

```

---

## Arquivo: `./.git/refs/heads/main`

```text
8d046d6e00cfe57c3ebce5fc5feb6a27a9d5530e

```

---

## Arquivo: `./.git/refs/remotes/origin/HEAD`

```text
ref: refs/remotes/origin/main

```

---

## Arquivo: `./.git/refs/remotes/origin/main`

```text
c650d325f4b616f6e450052fc3fffa932e1380c6

```

---

## Arquivo: `./.git/objects/37/c90ae6fc487fb86a57de8e2a7089b62a561aeb`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVTC0tGQwNDAwMzFRSErMS87XSy6oLMnIz9M1NjTRK6hMZhA98q71o/YL4YvyHjtLhE/Wm9ZZPYJqSEksSUxKLE7F0KP+w6r/3OuZq05luCqFchdEbV6nyQfVk5uYmYeh3mkTz+13y1/+djVy9V6qfNCjrztjFlR9UX5pSWoxho47JdUTI5Ywbd8Vo/Z3+e0Nk5QE7kUBAKc1Tuc=
```

---

## Arquivo: `./.git/objects/37/eaa058ab02790a4d07b4d7ffd2c4d921770a6a`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFLyslPUrAwZQjwDwqxNTUwMOZycYr3c/R1tU1OLEpJLMjMj09LLC4BMuJTkkByocGuQbalBvGJxsYGIL6Hf3CIbU5+cmJORn5xCUgEYpSJsREXADi+HFU=
```

---

## Arquivo: `./.git/objects/15/c4ee85f12be813d11f48b97413c97f357e3ae2`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGNVM9vE0cUfrO/4uAfCSSuZZKQDa6oXFCMU4dAWqicxBJIkKRrU4oIrNa7Q7LI3lnNbFrMCVU9cOZC1UtzbKUecuqhx/IPRBiJakhPVKp6SxUfqvbSWdubHJNZ6c177/tm5ts3T1NvkLpenJmbg/Op5AkQo/zF+iNPBngXBtGQ+s7+JeE8hQdgoBsQ9GYUIBFLN6TrciBPwn15Ckp9+iQYcgYCxUA5yCt/hdnlPOLxBrEc0yEB9r60+9TuFAoQR8P+Lyg8ZgzWDtDVSMJBBmAKDCgJZjh8+Bw+6LngZADGYU3ph7CqRd7hPCX40drckdwjdSBDKvUVHsmVDeXYXNXQjs0dMGLH5g4aJyKuEZ9Te3XJgQ5rsahGGjjvhXX00Vo8yhmJGkrAjBRVbhJqaAMZSR99ilzkwsfyBLgon+KJpXKtvFCuVszbxk0+sLRgLpdvVfiQbVHH8l1i+pSYTr2L3K5WDB7zCQvWKWY8Lsir5Wr1zoqxxKHLuL5SrT0ZFG06fVF8xW5udcWocWW29NFMXuWaU/esJubKJsNU7GUx9hWhDlc2xK5c8QkNnrxfoZToFtFt4mE7sGjo1y3PJrqDdcdyCJvXl/Malwjj2joOu1NsxVo28ddn+IBYFq7jg5XHNvYDl3hc9anrBXmJJxwrsOoWw+YmbXCEWdgLus7vFUKgZ2zSnA4wbW4+Ljx0G5gVNkgTF+yGi70AM/OgMq7HAqHKtVjhEcEN86ElYt81m8TZbFi00JU87bd4LPoROiFOC++N/STMU9iTTqrDu5nsi9bz1taZdubis8Sf8cwfI2NvRnKvRnJbN9sjxZ1EsaPB6HgvFZGzOxeutjPXdtOZF3ef3/229cOH7fTsbnbs++x32a2r22fb2dlD7Hw7fekwOtdOFztxbTS1B1oy9U8nBYl0ByQhJJbcGS5tf7a9uJO6/Dp25bfU0LOB//ZUAf3LzgrBX08szMNWWpifF2Rhf52PL56WX6rDi2n5ZVoVfl6lo4JIRT+CuOvuw0HDh6L75z/CvnCBjodo7JNunfA1OiXC8HFgp4XZkxFCb2HwLQz9Dmf+1gAlvkl2lFNomOoC/h+v0hFC
```

---

## Arquivo: `./.git/objects/27/f83a8fceeb99aaca684522550b705ab3ae290e`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGdVd9vE0cQ3kv824lJBAKqVOJoS4OBEhqCqJqq0sW+CBPnbJ0vFITB2txtzFHba3bXaUhVyZFQo8IDfeSxUp/6X1TiGalqKjU6UgmpT5X6gAp/QGfP9iVOa6BdyXM7M9/sznyz3l2u0WV1eubiOXQ6NZpAMH5sVW8/iSD0u1R6I9SdvPgTJm10E5lKDonOVxEK6EO5oUvDYvgYuoGKsV7Y7vc4MofN0MxQxyLCA1FhMxKgIgNRUTMWoKIDUfE9qNhAVMJMBmvFzZEjSCTMUZBJU3kXpVN/yJSNtOKlTIJrWdcWmRbjlHnR7FzlUqFkefEatXHtFuXCtxnaou4lbcwc3HRpxVn2rUsl3fRiTQBVGeFeEoKLWqn0WcHM+v5iwbS80IWZ89P2LmsIxUEZht+LBog2Kge+YpfKwACT46jcaxQqQws7oxy0o+w3WFrLI10nKqd6MxNd7MY00RUEpSvpiBfyy4o5WOBlzIkXanHCoA7M+ReUOV6oSZnwUrZPSWUF24Kyu+kYIPhdmzar017Upo0GsQWTqTG5A5MJMZkLS0oh6wN+QxLIFVBU7+aU3LEjbFo/Kwirt9amVtwa4VO3aJ1M2TWXNAThlYBot8EFbtgu5lO3KalBMqA33UqdOq0aZv5isoazzbtepEoEdIYdhd1kDvw0iDbaSR78NTnxc3JiZ/TQzvhRX74t5ZETL0ejI5F29vkYGhlrL7wAOOprlCzCb9Q7UAE0Stbhj5nuV5JalIh9I/ArV5RieJ8TVBPNdNc6hgYglNcihl6LGN6DQMXoP/Po5elnIY/lvrHHj4qv9JshOFzh9ccJtTsypq5Zumppc3ldzc2rRsFS9au5klVS4UysuNUWwzam6skgQga6jgr/qZyWV4tmblEzr6kL+rUzfZAGnJQK/N0EhhXgtKhXNDNzSTNPfnjuXNrfxljK5/tj7rQA6TrYIZU64ZirOcMKoMHq6Vl/iiehN4HxFXU0GZxCQfn/q+FN8nYIt5krabL0q1Z/TU1GbKoaS4vAVwaKPzM9qHobC1KlzMXBlhcGMoXZnZa7ih2qzhUKeV0z1Kw+ry3lLXVey5f0gJYuV+snsmahuNvlboebxHEdICajlTJaVp9tfT6Q0h70P58D2ci+PvbT4wrS4D5tQaP7AYIKXHsj/lYoq+NKE1dxHa4nGrB4HljssTNpPP6eqm7Dxzp4sn8vOKyixf89sEgajrz19oVA36ELFVJXrdyiXrK0xWKwWWbJNHXDqgSe/W0x0mH/GvQinUvci5I1YrcEAQOt113hhe0a5SQ9xA7DX55NgODy8VFVdgQ+XtRtuP5legw0CeEtEPIyHX/wUTu7PTr+8Po31x/caM8/CyU2jQ3jOYocir1EkXAcbtNwsmOKS1McTEe7pp8OfvxLaDYISUh/ouOPby5sLNxb3Ibl8hv5e8Z2KLZ5eePy13n2FuycHvGGKGeHYOod6D1DZ8maYJj7b41/+5PG6uAXST4LTJbzA/KX7BQa+8R/Ssin7D1wyUuZ3wLxfFhRlKco/hQd+A2depYYeZi+n/429+jLrcTpdnQ70L/aSnywV1/fSpwCPTX20L3vPhr9bn0rNd1O7uJXtxLvt6N/heLK2MvDJ5VxP5O/AUquCdc=
```

---

## Arquivo: `./.git/objects/42/b20cdbeea7e9fb4532454ba523c1488e8b689a`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAHFVs1vG0UUn7E3/sjajmM3OE2M4jb9wBRilEZNKjWuEKiyEaTuFioBTa3JeuJuau+6s+PSVkJyBaI9NhJSr+XW/AfcEfdEsZSyomoRcOitJUi98t6unYQGKrCKGMlvZt6bN+8372u9ULMWMpPHj82QI7FoP4Hx/dXq0t0+Qn7GTXcEO4vNJT8hLXKBaLRIClTSgk/6xnDvK/oLilTctb/YVwjIgLtWisFCSIbcdV8xXOiX/QVVqoWIjBSiMlqIyVhhQA4U4jJeGJSDY2Se7iNaQAtqoWmfZ1Um5hOlw10o27MWng/A2X5NnaYeF9aRaUCIA25KlLLeeifVolPd07EUmeqI5BCcfnPnOW8931+a2M3t3uDa+CsttSetSE9a0Z60Yj1pDfSkFe9Ja/DFWpBzA5CDu/JvXoGciG/nhByGyB7dHUNtsBtFLZEiWjJFavGtbBjR9qSIHN1910u0OgRWX3nOagp4w8iTI9recZIdeYzAsz4neIrZ8u1S0Qlq/HKT2zJLnYH3DHOJTX7I640ak9wGlnpWMmnop4wat1eoEzRMQ5YrC9mQE9Etc9GoNgXTmeWEdCYqrGFYTvCyKOtWhTvBBq8YFct2gnrN4KbkTljwqmFLgTxmspphcyewwPRLzUYzCrDegTu++wYuyZSEdd0/OfEWAO2ThqzBbVe4sA3LvB7M2S4kJ+DNADJcMQTXpSWuwUYxWR2Og1DIZkPfGScsfyzmzREgLXK+U7Zkq2jHiEbASXROYH9aIZtAifNJrsIk84hu1SckF/Xm1dwi+iR30arzXOeBdrnrhbJhAgBTN5idW7J4rbwI3gb3lOtWpVljIldnhjnRuOZEOzjL/Aq4SIyCPRV+NtpvkV8U9aui2AvrFSoUmJyw7AbHoTkdH9B9xNbjDriq58gF38yXhFTgwWlyhl6kGj0PEm/k6DhZ8T1GHScovAQQadiBAwOLlqgzaePF+wW6yomUy8w0LfA7L5cFGngVfptJIC3yjFCaf4rk68/cyQXsYgO5OxSgruOx9YHjPS7QEnKfG+cgCFOdTg0o6XW1Ac7itYmLsl5b8Qk07cS7Sapxu2GZNgcH7QeBi/qQhxrSjVXKwrKkOAIifN7mEBDwq7pnQz24ph68W733+bo6u6rMeqBBujW2HIpfsRaA0ii6DWunzm2bVXkTyxtqKNOppUzFyvwphzPCqjATuJA2mZJly6rgZ8+8v08Mg6JHMLgeXMVFmoP9GPzsGJAWuR8ZWk19sKrOrSpz237tOeYiA7d2Ai3G0cx2lN24uuR1PHQQCaJ7WZEU+MUVryFBAzsi5YbHJfh5FW8g2bL8H7/VNfa/vBUt214+/vg3+TiXTTvBTusQWCpeE0h0WNCJ3E5tmFUBf7CIk+wKoKtA13Y7lAigJIQtbIHZXIRwGxRWE9qYLcJ4KSa4wLYjIkiwFQtMPzGAJA7E8bNGw+mrW01TOiHL3NGunJhh6rVmhUOl4Z1OwJu9OvVXuVd9AhP7+ZQPnXD7Ic+LkyDFSNsfA33ip5Q+JAcekIkH5MgDkn5I2AZh64T9FIjePn3vo3bgaMv/iPhvhm+Eb2WXP7030x6a+namFW6Tdx9R5Wb6RvqWsU6Hn/oojW36iW/vE1w9CRCqbJDEGkncPrGRPLSWPNQmh+8Tf4c3c+fk8sk2Gd/mTN/JL+fbZP+/4xzfSI6vJcfb5MCL9I7dmV2ebZN9v5JReOgPkdG7l9qRyVYYH5C6kbqV/CL9O6DOI/4Y4s//plB6mj4NkWi6c/af6z4D3bxbVX8AscQoHw==
```

---

## Arquivo: `./.git/objects/dc/747b9158a402b7ba5c26fda7dbb0922210de5a`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/objects/dc/94c4788409c7f4229a0438bc1950add5d63f8d`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGlFE1v3FTwPXvttfczTVMlykfXTZS0K1BcSlBAQAX50gbasJjVQkQSy2u/JA679mJ7RRJAWj4EjVqUC5V64JArEgd+ARLhkuOiRmJrqQqIXnJbSCSQ4MC83XVSBYkLT3rzZubNm683M4WiXZCeGr/6HHoiEY8gWGRude2AQehXSgQr1EaOPgOkipaQgmdRBns4w3hMitLMLJsJeaEmzs5yGd7jU2gRX0JKSOHGceu9F14MAYdXwiccYTGcPR+YOT0VYaz9RhG7kRLpRsWOsfa1F1GiQygdO6R0mvHFl7Ozil3xiOOHFfJuhbheGvvJV0xrTbuWI6VyUfOICyx+hXiqUdjkZc0omRbllB2ybK77oveYmGiYDtE929nYTMrvu8XKyodymRimYbs6dartGKJJYWEfXQVQRXm0xDz7KUIG8PrR63gVK3gBblpLYRYgqa0lM+A+e0hpP+y0PPZD1FCacahWn3U9h7q3bDslzXOpxUGfyIbmaS2g26VRCLhUWZeXzSJx5VW7RGS9aBILYlV1zTG0smmrpuV6mqWbmiuv2aSoLmtAl021ZBuVoubITjNvbhDfaHnDj6mqZlm2B0lTVeccmBZhuxcBVNEfKImnmN+a8Kv3Gs3zG71FH4EE0k+iBIIW1Cewj76ECAZRChQsBNlDwXeWmTyTpXk8s07u2SVcDvWhPJvlzogAqeA8fhqPta2mqFT431Inurg8d7l9bYB3/SjPLaEne09flEM5Nhs9pQMs0JBCOea/7xdiwZtsMsBOzxy0isICDOWwwuVCMqvw4+3oh5CEFoRAlkcG1EI/ZG0A3XjVRM+zA8jEEvq//gWanmFNnA4f0v/YlN+YvjE9mZNMQ5pRXrspQQtpBVIkulmCgrJd6c3MtDIt0RKVXpSG3c1YuyFGV71S0aERO3EAvtB8qZoG9GXI0krED+s2lOS6lxYcnkrwesVxbWhVsk50aFpfWCaevmpbxBen13VS9kzb8jm9aLvEocnwO4IeVohbti2XpPnHLDJGwelpKgbTYNhn4XSpqZERCZbTQS+jbX9VGAHOJeBQze53AA6hKB+Jyds91Yl6PLk9vzV/++3qTD2eqM40GJE7XxcS24mtRK07sze2d3lfUOqJrm17y76fSN1iD6KJ+oWee+fu5m/NNAQkJrdjW7E7iboQ2Ra2hDuRR9Gun6LDP0aHd1a+ndubr72l1rSVmlmq2RsNhD7AEwwcN/EkU4sOQ/vEpijNTTF/HsdR7MIxwlz8gRBrsHD+1eDP6v8i8rdL6/LjgUkB74xNdKLvu64DutsZnZDY3QFmYgjtpjDFJZbiQ4OTHPsDx4LMXDrqh9vTwKH11xo8nW0WDJfm3DStFYd2nS/Q2VPQ4E9av9gaHK0PYoOkfo2cTqqqmXLhheaQIdedK8CjZea+BACCwfgAjTxEow9R3y9i570r++JQlX8Q69t5Zz92rSr+jMOf937UW4sN3McXjxk6cI5YxKR+b6JNC/8A+211SQ==
```

---

## Arquivo: `./.git/objects/de/012091e2517b9e4861c2741b0294f87e77fddf`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFlkc9Kw0AQxj3nKYb1kkCIaUWFQMEiHuqptN5EyjQ7rSub3XR3U9DSh/FZfDE3f6s1h5Cd75vfTL5dS72G2/H1xcboAjZoHZYCRFFq42A6ny105cjEsKBdRdYFv22Jo6KU6ITa9h1PQr3j+Lmtkw0C0/TD5MQKo6DrI+vrZx0hF4Zyp83HhA02FgXBfUtKtuRCdlUSF1xbL3DawJ7MqquEpl006zeOsgD8cwkzZYVBwF0lAMFWCLlWtpIOwRBKQA1rVLkGTsDRw8ESKMrJ2u8vI3SD6aasuF615gm8NEI948AEZxmM0lEMLJeClCN/Zg9opMcthdwj85LP2FW2VuakeOPyVacdyrp4l8Zpyo7xf+74L3eqEJa6+jyDPhZQGirR6HrYgB3fNNiG+tq8DbnKKBhiTvp7W5AtfTYUsu5/kzdXSE87DDuxLme/cPcVw0nsryeD88AazzEKfgBqTMlm
```

---

## Arquivo: `./.git/objects/de/0fdc591adc65e1de0eb22f4ec481b100846f8a`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/objects/de/e3ac308dd08e8ef396d2515c78fb5eafc05ced`

```text
x]OJ@u=_q7	T@.u%ѝHIoLs#U~?fmqϙnW*ӴO8>:
mPZ%h/OA)9݊b5(E"R<mѦcKiMZb*$Mn`#g8Sп25<wE#BK!֦UcI:vp.)Ys.	|١S[t3J$΋zqFK}
```

---

## Arquivo: `./.git/objects/1a/806857cc77bf0a020f04cb4c87b3f607bb5391`

```text
x]N09)pICJฝP-AiR	M{*dwm\
7۫λ:=3?+|E
,~
a4+qO˜~aw28
Za?v,w˥'Vr4-Zs(-Y)`[Vd{<5<:0ASc>{F۸[8)*
LFpWRe>QM7N
```

---

## Arquivo: `./.git/objects/1a/f6aef7350663b688e6645c888d9ea6a341a769`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAG1Vcty0zAUZZ2vuOPSabtonFc7xXHCZIDOsIEOMOxlS4lFZclIcptOyZI138CqG7bMsM+f8AP8AleWnTalZWg7eOHYinV17tE5R4lQCXQPBvuPzjeBzS2T1ECQEMPamc1FAJuLFv6TCJUeQ6okfmDdWJz1xi/xxcBEfyz5CaHKxCEOtmLKT8DYM8FGQU70jMvdRFmr8gh6nWI+DMYtwCsmkGk2HQUhoTmXYUo0JQVXQTO3IJRyOYvgoJhDdw9nQkLS45lWpaQRbPS6T/YP+0MEJZSO4DTjlg3BYg+7lKVKE8uVjEAqicOJ0pTpXU0oL00EgwrHz2+ff/34Au+VsEQDUfAMMSy/IgiYWH6i4pBgOyH2M261YksSwRpwp5zaLOp2Opur2ohDkMKwyCGqnoZQ929VEUH3avNWN5XWemKsaYEIPkP0gk1tw1jFms2aiVf5aUDgKkiWUYJT2KCU4tRXKmdxaDPP+v1qHGm2vEA6HlLF70zdVooqYhrRTZYXy+8MldOUxiftoaLqpkoD7moOXLpfFBsqz7dQf+Rf6B05OT+vyrYlcgOLBa5Jr9Jz13JvHgNWDDbbvWnwCTHnxG472O1CoxB3HrzCzdRVRLj+3RW7ZYGkTvN/WCqkzBDvUh02vaNCFosAcmYzRUfB0eu371bWo9wUgpxFXAru3FPLWPNZZiNwVqxN7Bf39zgp0eUS7FmBzjdlknO7qrim8sGzyeFe57pzvUUbw67Ujat561z3cN8lQlpq49xfKF4r6vllr3HoIV3ubUVV6Li6NvZX+tg8FSW/F3UBKOmpGAWa2VJLF6JTrvPtLUTKPhAM3ao6UDblkmPukNy5A5jBm5PR062dh/E9HQz6/f3/xPcLD//fuL502prPmTDsVmtjmpqCoKr7KzWtxOGPhSrz15OlFstNechkVmKiuFipTUFV+zZgkqIyqvMurPJ/7A5DPCP9eYhp9Bs/Mk/1
```

---

## Arquivo: `./.git/objects/16/bd5d75ec635a942665dafa3bce209fca683784`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/objects/16/f27232d7b8fe20fb5621ad3156a01cd7e1235e`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGdVt1u2zYU3rWf4kxdITnw5KS9KVzbW5Zkf2jroHHbizYLaImy2UqiSlL5aZC9woBhlwN2sRcYsJvd9032Atsj7CMpxXKa3swIIok8PDz8zne+w0UuF3Tvwc79T0RRSWVI6gEp3lswzWmCr7hiZhXz84qVaa25ioIfh4dKvuZG6uEeUymrhMTAyfN7Qb/Xu0O7Me2amuXiHVOkpGH6pGJLVvDSyLi66LmhjuvXUpSR3W5AwYfm8HkmzIpkxcvITVuzoE9MUzaiRKY2zCxWnKVRv1fKU3aS1WXCJIaDIPiSVVWsZG14FA4rJROuNVPriIZjUZpRWRccRyi4ZtPhOJOqYNNwQAU3K5nqycvwm4M5vsPD2dE8PO73Up7RLc6ijp8BOTf9UY/wy5QsKMuZfkMNzoq/rbk2bjaRZYlw8eCJYQrnsGuSWvnBMsarlnbcTdyhr2qdMJJ0ynKpyADkHEnDv1RSxVOBh5YFMiaRQRKGl7p1iVTyxMIRHB08Otib09Gzx5GIK8UT2aevn84ee/uTxo+o6PvZd0/8IAma4bWK4bI4ESniEzEezsIv0FQ1Nv7bW2FFSi++PXh6QFVsYcbKu3o0Mvzc0O6TfYxqw0ytMR4m8p0oVywMBrSBaN/jori1AiRxxk2yAmgNYA6NE4/GBHjol9vHJDL7RsCiHeE5qL3dQnnEbaIoxY5cKDkAfss1tKlYCsMAYyldPmOCffn+d9gxrcGazSTEDmUfB0hvOZjlkpmoyXZsOREvuYnCtRGI1Ym83/chO3YAKstAmgAVxz13DkcsN7bfRB2SO5Tfq+vMxWNAextKwc6j7XYzF97nTXjdJdckO2L5KQO5UlAIfylguIVFzw73d+fIqmOdpqODOa0zmYnSCUEqcUgX9rryENBdaE1n62akDdfOpsygnhsvvqifzF5E/YZLtzFpvXuXR27zjd0G5DYaUKdoG4ZZbl2XSXNAu9XN4+XiVPGwicW7cWf4CHFtmceJLAph1iUeJ7nUYPBDW/6Y9l+enYqbWpWUBePVzvSwFVHiBV2681wRRwnUlp9wS0e1VTf56XgI8/Hq/nTuhAGzhy47I3r6GV12AB/F97IrWN+31kjbRc4nqD5oymipOC8fhtO54w6jlJ/K/JQr78Mh11m9UNMxo5Xi2QQq2wYaTp/LHHpGFVPMCvZji+F4yKZBD9Lca8Rb8VjXi0g5rX7lxfrVR9Q63gK2HZEfuA4AbuVsqSfwtD+b7z56dFvTOLtuGll8piBgkd3ftayvui2L2UToGoHborfto7rwJxBlktdCEaOF018A64DowQh5b3tlt6H55RtNDEMbLQzfJzfbWGesfUWHq3KWrHXbEvIGoW9U2C3l4/S9qVUg2faA/+OrqR/fMlqXXeD9QT+EvT2Rg34PilovtBHGIispF+Ub0uiROUQbvT1cSxyuJ1QXlDBcVKA3almXxrc4LyI9EO8jaUC3AniGa3vma37GK1PkG7nB1EZurAFcXl8vmu+WsWFL+uDlD8Hx1rCNFZ/T461pvPWFJXs4cCpsW7r/qdBdMYglRshyEtx6L7m8xPUDffLqau22uZBMAtsLgqZgg4KppShHtLNdndP2w2A6ztmC59N/f/v5D2pDomgvF7iCcTpEX6pdGY+H3hBXoKo2ZC4qPgkgYwuurHNeTYLteHsnoBK3t0nghQMQyQCt9C3yxdM2hjORmtWIHiAEG8CiNkaWjUcUNxQvcAKmxkM/N+2Ph5au9pplUe0Sx2fhQ+J4u16lcGWLglfl37/+8s9fP9He+z/RplGqza2zUUPdqCHNwCecpoAELSWEKGF5Uue2x7vqje219T8fQKft
```

---

## Arquivo: `./.git/objects/6d/2385f2c11aeead6d4e7ba630de09017bf4c21f`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/objects/e6/9de29bb2d1d6434b8b29ae775ad8c2e48c5391`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFLyslPUjBgAAAJsAHw
```

---

## Arquivo: `./.git/objects/69/392601ee0dcdae3ea7df4b83270c3d156e1d7a`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVTC3ZDA0MDAzMVEoSi0uyM8rzixL1UsuLmY4GNo/XWNrtsYEv6g23wdzl/VaHrgAVVlcUpkDUTTDwmvN1T2+P5ovT/KPY96m6P+96SYAd2IjKA==
```

---

## Arquivo: `./.git/objects/69/94e6e569c7279e96818583f8b2974e0c1dd911`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGlU91u0zAU5jpPccg0KZWqaJsEQkhcoCkTk7pV6jq4QChyE6c1JD7VsQ2DiYdBXCAueIq+GMdO3aUUrrCUixzb3znfjxctLuD05Nnpo4awg7UwplWLfCXMClS3RrKwXnyom7PSrMTZk6dJOLYQusK4X6GWlRUEcARXQlupawQBvny3+Y6MWRNq9UXUAnhnTfheWkySWjZAcqmMJUGlM06QwswZSVp0chxm+YRUj/mUscKRxy5VPXqeAK8jmO6PBpuf4DyFmnzbWoKRS39r80NAw0w2v4xRHYbbnmDp2foO8GIfKdDP4u4o2fY774mCRggChDLT1Hw/ipCN+qqjvqjzypFBeqjn8k5Wzsosvby+KWZzuLyeT2FL38BfBCj9sAcqwOuXk9viBrJjM4b+G6Xj0N3LE9cAb4/zAd52cKaTV9h1yg5Grlo0Mv6HE4PCmpS2WZPeGrf5xhbCffTw685f9p1BB4Y8TllWn4CPklSjKk5Ai0ulB+NG/UtOlOXwbH3/D8FviklxPt8FK+gKF7Pp1YP8b14Vs4J/+xCyh8cmHQ9MGfUycSJdy0Ohd9lR3khbrTgerFH0P/+naOGE8uGPIELXfyQwyPJ5l8GoQXCt7/z25N1WEW91b0I68RqCcBbJPzj0MsckkLSONMzJyVCTrZH9UzoAQMdW6ZUAxe+c+CKa/BDpQjBCkvwGevVkmw==
```

---

## Arquivo: `./.git/objects/a0/acf158ded96dd83d795aa24753be1945658aa8`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/objects/52/a7058cebbd0d5ddf8957461bf9b3c902ef61c1`

```text
x]O1N0+Vq(H@
z6^#ӽ'1L[fgvfzm{<aSfg=mg#÷oZC8;-IiU)"31as%*VtO!@l+ƮfBkt	2 |ٮyAԊb(d)<>(Ң>'5vQz
4k&ٺyYvǔ0p<l}_o=
```

---

## Arquivo: `./.git/objects/b9/6de7ff9de8161921041e108a5b7f7fd04a436a`

```text
x-A
0E]c[Fxo dliR0;ŜZorAz]K17H6uN@Fh6mlBvE!|\S.+9&&M}z/'+Fd	`"w~YA>Ai1d;p_
D
```

---

## Arquivo: `./.git/objects/b9/e943fa2e516366a29e990e197504980e5b98d6`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAHt2sFKwzAYB/BkHYqCq3jZafBdxjYcgkzFo1WjDOecs4I7jazLpLC1W9s9gPgMPoDPIp58FcFXMN2srDuI5/H/aJu0TdLm19NX0hv6Pdo/qh0fsLvbhhspGvjBSEZUY9uMc3ZCxBjL/uy6mEVGH+NrSfCk8keZZXsvH1u6gZG7Y2Y+964LBAQgAAEIQAACEIAABCAAAQishsDYWM8XCvypFsneUDky6Mux6ydl9qwtLFuQbZ02BCVXqez2qd60xaVoU6tdv7baHboSHbLu7Zt6U/e5Fk27Sp4/UmSLB10dB8rxSQ/WqLQya/ndXd6ZPTCcDHVG2w3VZKo8Ry2dGqnHL90se3Kkqrpn5WnA1/PFIn8255PwvYH7OA2kI31noZ5JjbZ4h8qbtBD/ml2qx2Qqvcjty77qjlQow1+dc3Fh3TdsOqym2scy3UCFkdSv6emUPlaipHHpTH+Gt1f9HagV+KXfnpU4N+fmJ9MbAgIQgAAEIAABCEAAAhCAAAQgAIEVENjhWcZLRupXwDz//2Lm1wpMEFOAAAQgAAEIQAACEIAABCAAAQhAIBYwuVHcWFynEOf/etE/AgIQgAAEIAABCEAAAhCAAAQgAIEVFvgG01Kcgg==
```

---

## Arquivo: `./.git/objects/dd/0429d66bf5d14d6ae16035da6c733a0e620dda`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGNksFu1DAQhjn7KUbhkpWqFV1ArSr1sKVBHICtNq04RhN7khqythk7CxXqwwCPsi+GvbuladgDk0PG9nwzvz1Td7aG05PTZ3rlLAewXuw95++kde1MNGxXoGwgs4b9WWdRVbstIZ7DG2SmFgE9rJH15ueatI8IIH/t9drCNLEKQRsfNr+M1CgGKfKJEIoakNaQDMj55ExAtMB3OyctFAas0VPVcwfnUee0pSQpzy7n1/OLeVlUN8v3WUyVopPp5gn0mCodRtG7atB7NEkqRDxKWLmOAibxW9F5S4xRuaPOgpesXQBFIOOeD2wnf6ulpEyhZwMPLzeNF0o3yofaHwnqPI1FvcWuq1F+AYeKN79tLOQtmOTd4meE4V2jjkYbrfC/NDwJSmJVbXBF58OHvKg+zj8U2RFkElmh07ZybCtVZ5Ojf/jeE4/om7JYJtpZH1omfwhz6P03y2qEXs3L8tNieZnwQ9htTDlC3i3K6xR+PDuZvojf8SEuDfWIu1ost9zrVy9ncV7SWzzYbkXfJcU2F9uftibN9aBTjrUJeZMVzHFsYov2Y5v8Go20aUAUKuvP4AfdD0owak9AQog/FyEB+g==
```

---

## Arquivo: `./.git/objects/f2/0d61bd4c429d62b511294af8b818b84bbe1c8b`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/objects/f2/611c0a9bcda47d6e45bebe448780189bd78b06`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFtUU1rGzEQzXl/xaBe1rC4xrg5GAwpvTQFgzG9hWLG2rEts6tZz2gLTfCPCf0XufqPRdZ6nX5EByFm3rz39GZd8RpuJ7c3G+EaNqgBGweublgCfF7cL7kNJAUs6dCShuxP2DBQ3VQYnN/2E9+c3+P4e1cnzTJJ8zB748oH2WWONNb/mchLJ2QDy6+ZucLMIMvuOqbhlkJuPlqUMhrl2ClpAz9JVn0pl87qtPc8mGYQzwe49+oEAQ+tAwRtESx7bauAIIQVIMMavWUoCUosWUEJPFlSPT2L40TjAnldlbzqoDN4SOWzwpPxXJOZgvmK9fr0ItuWBL5Up2dVZ9kUYEpSK84in1GL028uIPr2BAQxX7dPoCYmkADjT8VoZI7FOwoL9/iIMEfZ7khcwP/I51ztInvdqqJQhVGhRr+PYBtlz/CrzKSTSSo/0i0UWvFwXcCw3+iStImZUW76uIe7UFeR7ulq0lwWEL94eRXw1kz5xdbfOab+cZC9AiyJ15I=
```

---

## Arquivo: `./.git/objects/f2/7ca221647210e1bbcfff3d16eaf5e97b6513cb`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFdj0FOxDAMRVnnFFbYtFLVkWADlUaCJaxQYY/SjluC0iQ4DhIazak4AhejJO0M4JX1v5/93RnXweX11dlAboJBBVZeg568I4bbh7vWRUaqoMW3iIHF77GacfJGsbbjStxr+6ounrKOQQhKPGxPu4pSLByGWf9HFDtN2LOjj608jslSiJu8qR6RC7npnR30OOs7HOAd6TkLBeWYzZq3bATMld1Iqnfp6P4A5/AYu8CaowKPRkGYG/P1OepebTple5dIQo5k4RilXn9rMXhnAxYyL69feDKygn3Cfo7KJYxsYOkqOJnLB83fbMk/lOIb3BmKZw==
```

---

## Arquivo: `./.git/objects/f2/b19ddca96254b2aca677658344e87c926b7e32`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFlUlGL1DAQ9rm/YggctFC6pz4oCwVFKneiKPXAB5ElTad7kTapyRR2Oe6/O0na20P70mHm+775ZibdaDt48/rti8HZCQbpSc4a9DRbR/D+221rF0JXQot/FvSUPYdVhNM8StLmuDE+afNbvrpLefQJ3kuSnfS4gY5Ih77LMhe1ob70yWeHgz7VYif7SRtRZGsL9Az7RzzvtUNF1p1r8QRjSvYuCVfcJxe7Bz8ux8edw6P25CwDpD8bBT0OsCUPAerSiPtt1hICcw/MKvYZ8Nd37CK5z4uYUYvz1nG276oUrwXe1UH3XHgZceTOSSLIJGCFJ1S83Fx8bz43H+6A4R/br1+AqbLDEZWe0JD18OOmaZtohvWuvCghD87KInkIkszh2io8IKl7a3C1Eup6CJCLhZWTLHLl5/Wv6BNPCmeCJv60NRfGLL2PkEEbOY7/j6NG65+3DBtZU5HnkBZn4OlS1fZKWvSzNcxdD1CCkRPWYjtOdU/TyEMrawhPVD9wJT5GsecDxqgEETbCibgYEHGHPB1nOOTgscj+AgC/7/8=
```

---

## Arquivo: `./.git/objects/9f/ba0e25984948008963514410bcda9ce992b9f0`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/objects/6b/f8cb84e78abe758e0dbb0efd54d3899116f888`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGlVMtu2zAQ7NlfsVAPsYEgyBMFGuSg2Api1JYNSW6Tk7AWaZeAJCoklTbf00/pj3Wpl+NHgLT1wZB2Z5c7s0MtU7mEs0+XZx9EVkhlQOpe81Tol0QW6/PeSskM2rcT/tMo1NCAAo7pSCRmWCotVa83uo3vZ2EEN9ToZM0Nz5/7ThN0jsFJZYLpd6mNM7BY3516e1gbtNgEFcNCyJgta/Qi9II9tA1adEFN14rrGjp3w/DbLBjtwdvEgZJZsD/3nIIWenV5cU6de4yvgGjRSP3B5x7QL5F5Tqd0+th3nph+lbQAy/amkeC4izI0uETNbcYS3mRKzZWNWmKbaIFa/5CK2UzL4VWWVldlaNxNNKmWEq8wMVK93Ozsys42qOZR3JQqr5jUDEUuDlBsede0q95E3PI9qU/q1+1e5cktPCkN7zuO01EfBp4beRC5txMPxnfgzyLwHsZhFNpmK7EuFSYoYSOhHVUwIEHG7gTmwXjqBo/wxXvccLWQXGY8JgsYpA654fDVDYb3btA/Oz0dVMf4i8lku+apJKRgyHiccU3GHvtRB+1GHlxXj8TivykWSrLSSP1v9N5DiXGdKGEVjLyHV3awEhWKJxL8xZSkHJIux+dvCZOg4WupBHZHXr0pIqqnUjwjk3A7m00814eRd+cuJhHcuZPQOyhjFfwIIyULBAS6DTxFYBwKzgQjfQpUCGv6o/0oeCo50OxKcDJJRgWJTMscYSVVhnGBa8x4biSFFdkZq+61KzceHAWz+cZ2jeXa44ZuOHRH3rW95Vap3eK3DNzW/7Vbrd223LZtTEHfTl1tsLPjNsBIg+m7VrmrUXstLmih7aKO/N+/JIi8wjI82j6LrpQpdeeErcI5zxlJz3dKaFVkiJhnEI2nXhi503l32HARBJ4fxV3moEPsFupVVJ8YmWXCNJ+YZjlJKjVvQxWoCfwB8PXYIg==
```

---

## Arquivo: `./.git/objects/b8/48793e4b9cd213ade9a06517e582e0a04cec79`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAF1VV2O40QQ5tmnKHkfNpGCk0FCQNBIQDYrjTRaVjOLhLRatcrtSqah3d10t6OEUQ6DeOAAHGEuRrUdO4kBv8Sp//rqq3KpbQk3X335zWeqdtZHiB4llSh/zU6CcAj9qx3enMa4sb7uNU8xun228baGEo20cHKW1pCM6LNstX734eH7e/HTwz3cgg3FliKZ3SS/UOQzyFOk5XyurUT9ZENcfr1YLPJptrq/4whrcfdm5D7Ik3eN0avf2TyTGkOAOxMcResfVYhU4zIDfr4LEaOSNcUnW7WSijZQKdwaTqgkeoF1qchEmkw7l+SWvJoguv5uIX9D4dReZfM2TLKK/nB2SQK2MVxyj8RkOpi22sZ3SlPIxgfr/60vaE+y4Vryx/X9evUBbr7lBpNz/7BnIbUNXO61nFP/p2Lcyo9GK0NA8IhN9fLHjvS5IdpLchHW7Y+yBjAAXbc4CrfJ195bMBZ+SFxYwnOIfkLTY54N5XmKjTfwPAhSL3noxiSsI6YhJ0OdL6EnW8FU5ClOprNrrx35gFa4A8/TsD2bFUnG/kVwWsXJ9OPi08ipHaOosLIhuVzMdmTYU0FE8nWzZ+Nc2ro4/QNlLsn8/mH99u7nxMSLER2zLBFMouOemVzE6DAcHYZ5nq86BSAkrF/+evnTAlMN9QzSjmHEhKXDyicNMaM9lw2ONMKKWepR8+h4mRQWHK4F54qGHFbEg6NZSiB2qJvTayyZfAmuJFdmY5lAA7av4D1tEdIgawJOWL/8XTXagm0A/W+N2nENXhmpHBdgTUVgpfWeGvZJPQ6RYik0T5ZzDdeFM6b3KGI5acsrz9StbUojrFdbqtmJj4XD+FSUGMhgTZNTvI+f33wqNkq3wimoDfSJSAdKx0CZwh0uWPcK3p4A7SrkrawtD5+72KYNTXAzknu1VSOAh15qMgG5rnaKXNwmf+7hLYRI5QmRSumF0Nbyet2vz+tjvw/9KK72wuFBW6w48Gg1pG4PklAVM/B8DEdkTbCz/qrIkUmHbjK6hHlk1JOezUYntPifOzkAxGzv71LjdYfQxY0/zkOTPjQ0fz53cZx7SkL057vTflIKxxd5wnFm8Euw5vYEzwyiqsk28faLYtERh/G+OlPnC+X4Q5Bl/wDi6RvP
```

---

## Arquivo: `./.git/objects/b8/56e63c26398d329d116ab9764acc7546c48e89`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAHdVl1v0zAU5Xm/4qowaZOWrE3XfbRhEgLtDQSI98mJndTCsY3tso6xH8Mjv2N/jOs4SbM1BQneyEM/nPiec8+99ziZUBkks9OLZ3f7wNaOSWphlBHL4qWrxAj27/f28FYmVP4ZHHeC4dIr+fBDcMvgiksic8YNgQheE0Mffmiu4L1RPpykYdujGLmSiOJ84JTyr5ALYu3LUY6bR5d7gFe6TC47BMrgDbOs0kwuFfQQVXqMz4UNGqy7FezlqCKm5DLKlHOqmsMknhlWLSBXQpk5PD89OTs5zxajy7cPP53hObFQMkO4BaqgIG5lSIXcPE6hTIW3EV6TslldOS74N0KJjdNjfbkXwH0SDTzlVgtyO4fScLqoPyOH3AVxLEISq0raORimGXEHZOVUVHB3BBWXFVkfJMlYr49gUpjDQ9xMNCZQ03+SVeIXG61qvXoMMpJ/Lo1aSYrpFucFKfIFZMpQhvlP9BqsEpzC8zyjMzZpb0WGUL5Caud6vcCEKeWy9PIlQT+HnRERwUs5hxwFYqaPX3OwmshWhgJLHFn+jc1hHF8MVQA6peoOWcCTFMfxNCR51SvKJ+WISI89Uqi7B/ZXap1RshyAf9oAk1MyPSFI/uMLuLuD0X6cFKPvda3dgWF2Vam41wfXzkMewv09wtYYG+D0GGXv/f2Pi1AL70fhPaOcKvtvNUC3mTI/hFiARvJa5msdov9J7Ub4xiqmg1UfnJuw2HrBdHoymc2QRr/FtDJw5Se/zrYdfHSaaag0uhovQCoH+OT1xhnQzEIrYjN2ZtQida7zDj1sVQEl3m1a51QoQsmxu/wq4ZKSYC4+njdRgTbbD9/rM/WVmUKom2g9B+8mW0PpSIZ+3ZjTDaduiUM9Hu93c48UBdEWB7X9tYD+sAtWuAV6YX+ea0vo2U+XuFsyQjcT0a7779SZlsZjh5oUs+Kio9P6drJlVAN4bfzULdvYnXON47OG5lA13XKYZWD6u2gfHI03U/D3ccJEvTKG5XicUDzLdsXCO2abrX9+UOzUZYrebm/wqWE3odOBBi53t2+ratBiU7X6CNkcrJsCsYSdF+Onrfc4DN1ZoNBbN4yXSzeH2dgHQl/Qce3JvQnzFux2dFfguhukCfnF0dpb/jbMY66nyLV7sfjtuaLj3jGyC3y4zj6z8CblK9ezgVZf3LZdcFz0g7/pgt5ZFaKhifn3r3CEhaXuVe0XvGP0CQ==
```

---

## Arquivo: `./.git/objects/0b/02867b4dad4f97153cd5464146b324a11ba5bb`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVTAzZzAxAAKF5OJiBvGC1XePnbNNmX62OGtnxLdgbym+m4YGBmYmJgrFJZU5qXogRdz/ChdXPyhf7be4YFn6taurBL5KLQIAHr4e2w==
```

---

## Arquivo: `./.git/objects/0b/5f1f0b9c29a24ede9bf5c9fac39e1772a56769`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAHlVMFq3DAQ7dlfMdXJC8ZNQ04LhpZAoCGHbdL7IltjV6ktKdI4UEo/pt/SH+t4LRlvDoYUeqpP1szTk2beG9W9reH91dXFm9bbAVoZSDoNenDWE9zw8uPhUwH3+DRioGwNKgkH10vSpkv4W20e5eWXOY7hHM7MpJtW9xgS/uEUuplCM1ZJkrUMmADaaDqqek56OxL6ZXNjTau70ctG2gIa6RXfnP+e/LGxCgtwqLSygXO9RkMc8djpQH6KSSN7HThWy+bb6LJMOgdVqjgnTT1W4ppZf/9iWjh4Kwp45vO1NZW4LC/E7rSpHOxoKBfv5voYtKoqV9pjQ9Z/r0TM7wowcmDutM6yD3x2ac0Rn/ma+ZTwNDrmV9hCXMXkbp8Bf7EvebyCNk0/KjzOHcrXnSnn2G6qr3yJiz3bwsRubkFin7cgUYEtyKLNFiiqtgWZ9VwQZx5MtvpLO0fDs38reGH1tdALbHLISdsOJ4NEQT1KxUpZyv08Vfs0XlFcjzR6AwtNmQbqHoOzJmDaWIBwUhvsy6809Il+Yj5n+iEGDEF2KPYgeJ6Ty0FZOHM4eKuk4WjDb8HBBuo8Pny+eyt+Zlm23OcV1a/fi/+i+f9O2z/I4Qho
```

---

## Arquivo: `./.git/objects/0b/f3b0b584f3d4e364b23d06bea2fdb3b1b690f4`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFdUctuwjAQ7DlfsfIpqVCQOHBAitQWqNoKRBW49BQ58Sa4cuJ07UhUiH+vIZhHfbLHs7szs7nSOYxH44eSdA0lN5a3EmTdarLw/Pme6s4iDSDFnw6NDW5pMaFpdWPQ+IK3zXKRnsF7qsW6VdzKpvLcD9l889Gmx9H0dMEtz7lBT6rQZiIPAjrJgOQqKWwJS7lL2JCLWjYsCs4jnJoE/jUPhSQsrKbfhF1oriR46hvHbk7IhnujuuowJKyksaQNG4C3mBWKG5PcGowCgSUoR+WUXWpC6pOa+MiiSQDuiNzJ6u2E0QkpOjKaHCryuL/ffcS4w8KFH7L1fDGfbuARXtPVEloUUmgDq3Q2T+HlCwqSXOgMa5jN11Pn6jjOEm8ML/Qpjb57XKIttlyp+zGF0gbP0FHJzfPUidB21MAlttivzC/aOx4Au6QQb22tXHx7dhXCJjeqDlHwB/Q02bk=
```

---

## Arquivo: `./.git/objects/0b/fe71a37be077ab4ea370a667d6d5aa10f51aa2`

```text
x1@@P"РvٝL
aň=?GSgeV6[uDb,"͞{E^:tLZTߙ%
/ 
```

---

## Arquivo: `./.git/objects/03/d83500e1cfa7ba5b20b30f012c11f56349f1e3`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFdkMtqwzAQRbvWVwzqxgbjQh8bQ6BZtnRRTPdFicaOgi2po3GhhHxVP6E/VtUPuUQrMXPP1UG7zu3g/uHuqiHXQ6MCK2/A9N4Rw/b1qXYDIxVQ48eAgcX/WMnY+06xse1CPBt7VLdv0xyDEDTysFm7slzMHIY4vyAybQj37OhrI1NM5kI8Tk1li5zJG69a1aNlF1caG/hEek+zjCbZarHOKwHxXMPLz3dr9go0QkqDdhBwAE/uiOzGpFbahbUwap5k/BkegqxAbttBkVY2gqlFnkeQkAeykMzL5StqDN7ZgJlMSHngvpMFnEbyT1DO4vGR+VbAukxgXF8IjqFzLn4BghqdnA==
```

---

## Arquivo: `./.git/objects/80/baca0b33cef08a029b5ec790683968de8a898b`

```text
x]J0=)xItAAG=I.i3F$;
Sv9
oojjh):Z}pPrp?`b{`l}ֿ髗Y$M<lϷT&Ө#
Ӛ̄/=5lu15oV
hҲ3zp	C!Ӑ}}vћZ&L !ᔤX_0*9;;0a?r"KXOi|7
```

---

## Arquivo: `./.git/objects/72/bc43973d066923f9860d95d4c850ff693de5c1`

```text
x]J0=)xitQTXXiD$Nk$Md"T>/fLesfof}ՑSըA#}#P{@\V2Qm?;mG/%6]Y.ؿ &lF.26=r&WL;@zYzMa9u^	DDd!45#>׭Z5ʶ.oяz_`d_w}cUp>̘D߹
```

---

## Arquivo: `./.git/objects/32/4a0d1920d12ea81b363a7e701f31f3aa9f4352`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAF9VM1P3EYUH3u9Xpvd5XMLFbTFbUrEphGbRjT0UFVKKHRBfGwNrIQCsQZ7Fky9thl7VYJ6MBISTXNIe2lz6CHX/hf9ExqB1K0lVKrmkhstkXrtG68NJCoZyW/ex/j35r15761Zzpry4a2xW+iD9nwbgvVLY31TEhD6iwnJSsfM6Q/ABOgeUrkpVOZ8rsz7/CCT+alUWfCFiE9NpcuiL0a8MJUpS740iFa5d5GaVsUxroXly6siaDKqdKZpW5UrfYnL812VVwW1bYxvadRsH1JzfcjqHI2P+Dk1fwUV258zuciH8u3KlOo0fELDjEq2GsTzi1yYKy/OzqjEcx3bIyB3TJv2Jr65SOquhX3igUpcJ75mrO2IJWzUTZtpXEpq5nYo+xeOyYZJie479P6OVMI2tswIsJ3G4JpuYc/TWZxxrIjdPQXf6ftAAlRF9/iP9xAyQPcW+oLb4FRuBSytVeIgGv45+yfM0CQAKoDMrlRzaB37HoN+LyQlA/u4RXSnPgJB1xvbpZppEa+04dRJSbdMYkN8mo6pgV3T0Uzb87Gtm9grbTrE0moYZNfU6o7RsDAt0Sh3XhLaiHs/zGkatm3Hh0RpGu0C16xWvB4gAfoX9XLi34z89FW0nYIaRfEzhi0Jvij+G3DtAK0keUHJG7pclauwE6+sMztf5StJFV44o6LRGGsQwYnMBVPMniGkLkHgXkKQX4MgAEL2cjvcgHu9fSWX/F3pSLjzvQpdpKaqKVWoCiV+NM4G1EJ65+7CxMzE+KIyPn97ZmJhfGJ4YWl22If3sIrXlRtFBXtKDfsNiuvw1o4WWa7D6aW5xeFrkTlSaS4xTMPxlEl1flaJhR0nBo8KS3PxeguF/X+pt//xsOUbL+Eqn6vzSxXlzrLyCvBOLm6akQ2/boUi9E2j7oR516Hn3osSZY8ZinqDeg50MtkmOvR0KNWIr284dsJhywrTuuV4hLK3CzuTjj7r9TRtZwbeWKO9wNACI28A8VhBXVVg0U7gwi5KYBQ4FHokviF9G/QM1vsWSICeyR0P3wzuNPMdj5YfLD+8G0yeiCid3Z/bnfu1xz0Utpr5nkfaA+0g/84F0wlChQn+BULpSb5Z6P9x/vv5g8JQMHsstO3P7M7szTUFcb+8W96bfpYt/JYdepodakodTan3OFf4rtbMDTxePUmn5LbTTCYnnqBMWqTdcJ25Yj7MxM1LWbVEIyLsilUjyTzyKIsz7E708Swz7XUqMoPERsgahgS2Mt7q/1Y2UzASoyT8jCKfrURJn0SzgnxKhwCANaD3GZCTFMdxf6CrR+jaERo5QgN/yt2Phw/lK4H4e27gyZeHuZuBfMxl9vt3+7+ZfvJ10H/Ajb7gYXCcphD/0T+Mi7z8B17FiQg=
```

---

## Arquivo: `./.git/objects/c7/95a31d404d3a90aa124e86de85f40e2907e000`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGdU8GOmzAQ7ZmvGCGtBBVim0bqIRJqVy2rpkp2K0J7RQaGrCvArMdIW1X99xqME0gubTnB8ObNm/fsvBY5rFbrd68qKRqoGCnWceBNJ6SCu6/bRPQKZQAJPvdIKoB7IRtnDg4lUidaQrJtn9P9LpmKQ2fJJRbKVpbNCpuuZoq3R9v9hbc/2NvU1JEMvGSK5YzQgo6osjJ3HDnKg+gs1eskVvwlcm9Z2fDW9Z1phNYXwQW5Z6QJ+TNyTzDd4nwwxKGe47m3hWgrfuwlKwSSG4DdOCtqRhTN9/WdEiswDdnQLY1xG+ugv3FAP2Wu1ZgtPH+sFL0kIXW1zEPzvvgR4gsWOgvPPcS7+GMKr+E+edxPowZtTMBuu9+msNIbDDOMCs1o6MIKVfEkWlzyFrUgWxpGzz5HFomqly2c7AltNDZQu2IA7tkoJsIn1dTarF9T1d1Mgn7P/O0EXRu88HBEtKLBTLuumF60VbgBUoNVw2H0wjD0A3ju9Q9eshKzBonRBnir5pB/N34Wy9n9T9r9NL723no+pniCjxRDFu724RAnKWwf0sdlZt7lcte7+PD9bvctPoB3QwHckO8GJ+K/aR/B5kwMCYum4eq/DsHlXfZ6Wdubtrwl76kvkEhESvaoT4GOTvWUFaLEaP1m7Tt/AOvQegM=
```

---

## Arquivo: `./.git/objects/c7/b58cee40b45127f786f012a1d7e1b34ff8306d`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGNVM1v1EYUH3u99jr7FRIgNLTNtnyoy0cMNGqQ+qEChW5QCKlBK6ESrFnbmzh4bXc8K4WVaBwJiUYcwpFDpebY/gc99tjjVonUrSUEVXvhFhqkXvvGH5sUlYqRPH7z3ps383vz3q9hu43KmVOnT6PjpeIAgvFTe35xTEDoD7ZIRzYRtn8GIUC3kMpNoRpHuRpP+TG25qcyNYEKtSzNRuvMlFiTqBTJwlSuJlN5DM1x7yA1q4qTXByPDsxJoJHUXF+TnxuYfSM9duevynOCOjDJxxo1P4LUwgiyBycSF1p8xb7iRHKWWhpBfe+SWj6EqoPP2O4qH8rnZqdUt01NEkqq+VXb9CloC7XrV6ZV0/dcxzfDwuVrV2fSVZULy5ctZxGfuW62PBtT0weVOG9SzWh0RAUbLcthGo+YTWsplOkuN9mwiKlTl9zpSEoD67fbHriWSHKSptvY93V27eTqiMHOwLd9GKYA1dEt/uw9hAzQvYm+4BY4lbsJlngoHEDjn7E9oUQSNBwRYM1u1HRJC1OfhX43NBQDUxxPutsahwy02ktK07JNX1lwW6ai25bpADxNx8TAnuVqluNT7OgW9pVF17S1Joa1Z2kt12jbmCgkSqSfIBv37oQFTcOO41JIk6aRITiZVZq/H6YA/Y047jz3PJq/nYz/22BBUQaYwAYrwCgDp0AI0A7aWaZ9adSRihQ0kVggG1wnH+d5fIG27CpP2PnhYPp2O69KymCIcnOU7GE+RQ9bDoCMtxN2ZZm5jMAUoD/ze3/NH/klf2R9/vu7PzY28ue6wjkyDLbOYIJfMZc8l1BMdND2hwhSBGcR3gHgpA/dr1APHvm/oKUV7HF1bjbtyn5YBMDTeh9D4CHtMiViPwL/igjca0fIvCIC/9oRBIjA8vnSSO8IGND/29VMnVeFekbN1gUl42Vv5tNQdeAZVVI44JaENaAQ5M7otYvTFy9crxyrXFKvXqnortO05tsE69jt7P+3zSNQ0dT1O/te0puGZbh+WNi9Ocyl7qHkxQ6d4QsutI5DT35mAYn4FrVcp3MSU4r1hRboP6ywRnNwy/w4rq+dJoNg44u+6wANSXAMixJKCyY2TOJXRZIDlKGot4nvAmWZS6YO5BXmmibVF7Bth1nddn2TsDKriiFvNMhb8Y4ILmEES0aZpmBggJKUt8/8K9GIq7+UFq8WuZHDYC/C538HE5S/XH5wIDjfK5bXbqzeePBlcOmpMHB/ZmWmO6xsCqd6xeE1bVXbKL69y3B8UzjRK+9bW15d3ihXglp/x7FN4XivtHfNXXU3SmPB58wwvTJ9b6YniPdrK7V7l7dEJI88Enu5oYe1Xm7Pw8ktSdgrBtMvCqhwYL3QnZzuztztfvD1Zn65KyxHbThTLYdSQlCENVxEg+GeRDWecq5PWC9F+QqHUmPC2ZYzT1gfhTnGlQ0MeY3THxNdzCUZoP6IHaIc/YCi0+Mk5j6KmNH8hJyAKKzT/SZMWxmO456go0/Q2cdo/DE6+Ls89Oi9TflQIP5WOLh+e7NwJpCfctL90ZXRb6bW7WB0g3v/Bc/IcjuD+ImtSISc8Dnm0i28vcGNPef3c5/yzF75KxKje/wDPTLH7A==
```

---

## Arquivo: `./.git/objects/c8/c6253d3093a99b4ad8a9c5196a7b9809485681`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/objects/99/6451d46298649357c5a9c29bdcde4f2b96cdc5`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFdUctKxDAUdZ2vuGTVQsmADAiFggMuVFSkzL6kzW0n0jxMUkHEfzdOm041y8t5px1NC/ub/VXvjIKe+8CtBKmscQEOrw+1mQK6Amp8n9CHAu7QohaebPHMobdGe/SJeX98fqqX419oQGVHHqQeEvZR6jd+fZzvuCgLHnjLPSbQgKERLSHunAeqS7YsJ4tmtK/gn1ompMMuGPdZ0RVGNxSG+oN1vDthJL8YjYTcziYsemZ0x4WSemf5wBXqYGgBqW3Tjdz7ats1JwJ7WMHNr4SbpysvG4o2ei1DZnOzPC8JxOcwTE7DGpWlXdKaSa4AutqwU1BjDPZFFy9aRqHzh33n5AcpyKzc
```

---

## Arquivo: `./.git/objects/99/da355cf31d0f3484bcb3380e3819a2958d25a8`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/objects/9c/d628a5fe5aba93e47b0eed579318068bbd394e`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGFVc1vE0cUn/3wx8Z24gAtNAGyQNPGbWrTEAna0lZ8JLJpEsLGONAmrDbrTbKp7TUz4yr45EiRIsSBaw89cOiBqv8Ehx5a9WKUSA0rIajKhZ4CQaXHvpndNQHSMNK+nXnvzZt5M7/fm5mSM6MODB4dQB+2J9oQtDu1uYWqjNBfbBC0kN/ZfAqdBrqCNCGHsgIVsiIVsxKVephOzMnZEA1lwzTMx1Iuko3SKO/LOSXbRtt60LRwCGkhLXxc8GLS2HQUNBEt2tLEp2Pj3cHSL/6aMh3S2o6LnkaL7UVafC8qJQd9F9oO83pe+Ac9TRn015qWYKXE9qNjotYOETtYxJLQipnUkkdQqvMxC5aSXOXUeE5zatTCbkSzrtYsQl152MHllOjGs/nREc0iVadCLDepWUUbWyYNNCnB7ThnVxaMgbxVrpYMahFQhecsqhdn6uGMUSzbFaapYmvWXnQVusVN8WI5+Fq9PWM6lVl7roYN0+Ex2rG/qG6WDEJMlq2fMWKnJcG3+S6IBiqgK+KJZYSKoNuPLgjzgiZMgcVrGQFyFR+zOW4Ee+mlBCzDmG1sFvI0KGGhD7sLmaJBDU+YTjkNR1KuLWZm7ZJFMvNO2cqYJduqQJa6aeCiUbUd3a4QalRM2yCZBccq6bMGjKu2XnaKtZKBM5ifLNmSoOGkq9fcuK4blYpD4cx0He+G9RlUydsgGug5igqXhCdc/hDx/ptgQfwcWIe1MHz8HP6GTgNNBeeDgpuuCgVhnHm80lp2sSCOBzzY4qOhAE89CDwiW0x+txVBArvy/3aYL+xsn+IMZRHGE6/HKQArNbEgZYRBPw+4Tal+eGJoZOhMXv1AHdbOj6ovwGM46khuNJdXP653btWm52m55IY9VSqC2ZZhWMPEAdRbi5YJ+HejsxY1552K5YbMkkMsHGNuyQDbLdTLOMkMYnEG74UOZpdGGKLeU1UV72K2Nm8pHaiAD4CCLUi+BtFAj5SOG/sap9cTHTcvX79845vG8LrctjK2NNbcfXxNPrGe2H1Tv66vJg56hpGlkeWxdTm8kl3KLp97FNvzR6z3bqz31lwzc/rOpV+/a54trMYmm/Ik3gPh0y8xhe2JI+QoX3lnpmjilF+HEMqI7JxxB0xzkxVAvg58pAbwE9DvJq/W4G8XjaKlly1iEKgUEqHYlewKBXJ1wjSPUvwwOLq5eIsZDvK9PEcJQOcTLn88ssH/v0x4Y56J2doM+DOQ8kT+5ZO3gTqD8k5QlwrSG6G+vYcwKRwTB/3dvIkQYJd2BvybCDPFQMebJmqSJgePA1xIqL7vLAA/P/Q67OujubGJIS2v5sby518mRN+r99evvnZ/auHUyMWhCbWvl/SrvSRVP+TV7i1lC+ryl6RmWoQ4n1Ncs+wM1Bt28TVccmMADlqDsugUrVSY08ujxj7IhPGuXLYp7oIBZtUkJWP2qGGVif1MMB55FAIOeRSK+RSqOgCt98HO8E1mQGzHoYcBhz5ak9M+odajk+vKO81o/7OQFApvRFEospJbyi1/xeyv8qq7qZ5pXsivxS425YscgWOpTjfi13PMsMVfDcyw6Hb6+nTwThHMyjHPzt0VGP3nzq7M4SibFWXvy4wBlcUrQN7j4JUZKSgVrtzK+CfEN+KdR/Qkf1OsLzBjMyv2ZBHEhiQIwgPUfxf1P0An76P0fdT9p7Lr+7415UgjfC/efevbtfhAQ3koRFa6lrqa8f23pxpdq8Knz0T2yGxKSPxsg3c39iAxutK91N1MHFgVDt7r67898bPy22BzfOL3T/7hDGXePU9FRl2+s/8AB5QFTA==
```

---

## Arquivo: `./.git/objects/9c/fd47bad5123a67e8356c4bd0ac341cc6bfbe6a`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVTAxM2cwMQAChfj4gsrkxOSM1Ph4hrgDbXHrtA6HRLyzmekoNePtk+f6WoYGBmYmJgqJeYk5mcWpegWVDBwLmeVNvWNbTR0NtyrsfZwm8LS9EKoqKTE5u7QApCjnK0ffSz7Td/9aTuRebdl+QFChyASqKDmxKCWxIDMfpOzgx33B3kFqk3g15d/d+zxZ8YT2syswZTmZqXklYBsVC72NdMU3XQuLaTzwzVcvceGaODeYqvy8tMz00qLE5ESwgf+0Ppm+Ki2/r6uV7izW7C9j/uJRM1RpSmpOZllqUSXYeS/0NQ+fbhHcfqjV2fRRtcPEaW/joMoKEtMTc4E2g40rfcA/zanwZ8LJ5ZH5d1+cyppxu30TTF1qSmZKfjHItHrexJ06Gw5XlRnc/iE8uyuz8rKFMlRVYVF8cn4K2Bd1Ca2J9z735cpuNo7+/H7VUT/7FxehqopS0zOLS4rAVn7aOPfOyqSQTWuWlac2u7yomZRdZ4SmDGwp9+cNW1s+X3mcssmWbd+iv5s3bpvwBQBKi8L8
```

---

## Arquivo: `./.git/objects/60/8d978c36be5b6b41da5de63f9eacd05f23a097`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFdU81P1EAUf9Oy2y27y5dGlI8AfqCryVaRBI3EaGLirlEDDXIwLk23HaDYbdeZwYgXS2LCwX/BA0eMFw/+AR6NJ4gmSBOiRi/cVBK9OtMPIL5k3ryPeTPv935t3fXrgxfOX74A59qKrcDlbf/swiYC+C6cVDKJsfuBGwHMgI6qUEEMVSQmVWQmD4iYVG2pZFgmsuVqtqIwJbJbqrmKytQBqKEhGE2uYq01ZQj0jJ4d468JYXldqeUnjsbeQe0VU6/WOtGf2vu7nqtldHVMiiM1eQhq6mhy60Wkt3aDnu8Gt8NFe6+368oJKBV2RElJDtXrE1XdX2SYhIqOHy1iykLlBm5iz6YlFBYqU3du65g2fY9i7rffcrwFc2QKN5quybA4kp3DzLDrocoOBFXbIdhiPlm6+7RdM+2G42k2dp3HmCzxmjaSXGlYrkmpJVpO2gYBRuZr9yRXAUzDjHTpOYDNY30wieaRjh7wTCwa4mCkHVETKiTuv4RIC/dFa7M+aZiMiquPh5OabTIzVpbfKHPMjcUn2qzjYqrN+w2sWa6DPY7KsExim03HNxyPMtOzHJNqJJoS3YNRbi6FBcMwPc9nfBSGQTr5M3m+6BGuAvgLCE2jX5F+eTred3kGrIQvYUOWrwiuYCiAfWgTIvqfTIPOv8Bp0NBokhXwnxbT0ZbnWcMlbbyqJBGVb2FHStUeiVKUDyW7TkUfw8OkQxwspHcYnE8iEIi/gvZxFcCP/OHN/KmN/KnVubVn7469v7l+bepj/t56yz3SxQ+UOkJl1uSTajpE9BXNn4h/J+xM4uWUcUoE4rArjSdfjePNEUUkcoKkukkxyQk3G489BiNj73GYsUxrHody2uYriHqIUeTGG7696OKrZJBXC97pfa5+ygihL6BtgLYNZ7ehvA2939SuF71BdqvQu/rwU2EkUD8f6QnUleJy8RMc+oqUlZ7lnvVC/5ob9HxEV7bOaG+yr9v/RGzuyiCN/5YEvdHb/wAYKAGB
```

---

## Arquivo: `./.git/objects/fb/0ded58fb7701a8ba7ea33dfdd7a56086546b29`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGdVsuSozYUzbq/4hadrulZ2Pjdboxdlep1Jk7P7KcEErYyQqKQ6Gf8MamssshX9I/lCgEGm56kwsIPkO7jnHOPiISKYLKcL394vQL2ZJikGryIaDbcm1R4cHW4uMBHkVDxNzDcCIa3toxyqjRQAnfqhcs9gQHckZy+/ZFxBdtc2WiSul2dELGSmMTYuCHlDxALovXai3Gzt7kAvML9ZLMlXDIBlEGd6rpO5MNnIt7+VB9DHxe6HRlo8yzY2ktJvuNyECljVBrAeDjPWbqCWAmVB3C5mN3MltHK2/wUqzQjcs+ApWBYminIGRGAPWVVb/Y/fyG2TWJy8vD2F/aLf369x3CU2eY1pEwTPQz9bHNRVoJt8wSkMk0Y7NM2Za+wKfOsnk9M7ou02oSl7LjGnFRhKEhVioApl8XGsdgKbXk4hrZQVhhQrjNBngNIBHtalZ8DynMWG65kYLEoUrmCHckQIAtPhbsNbS8Mn6gcMuCyrwu7pGSuSheR+NsuV4WkCHCyTEgSryBSOWWI+Dh7Aq0Ep3AZR3TOxvWjAXbHCx3AMsMaM0IplztL2MQxdtLEb4U2PHkeVOoJQGckZoOImUfGsBmkaicHHJnEkDHCxfKq88fc9mk/v9Ny3ZOTk/3XvsL9tMa2Jm4yX0xZtIITvY2GUwfoz6gLeH2FbGgVAocDhFixrMMkOAQDzV9YAKPh0nVc3ntkfLc3AdKep0T0CPfazQNclsER18MBB8HG3uA8TN9poBFeJ/FtdzjGbHI7xZ4e94jjoAQ4gCxnA4Gz2NNqudvbuEJwpjXWUk5CG7v691H7nT4Xo9GxyfGCTGcE5fhFGSICuP/RQuhdDSeJ9ztKMiXmOhsa+/Djf4K0I002YcsEszVaGw2t+pGAWekRTrKNLmdWlzXd0+lsPJ83GAiWIEcjZy4emtWOlCMaOMrLUr9m9d0Slooh9IkakfZ3qJFtUaujzno7I9NoiXjc11aEblXliHOO9vAV67egl9vPQ4c+2sL57bMS2uN8Mni9g/WuddQ9tQO28LZAW8H34b2weJ9roytYt7FlOM5vs6E2xBQa1mv4sMVzxxrAB/THy4Ql0/jmSCS9vbkZLValg6JRdzfmLCM5kVSVW2nESIK6r9moRv5ovpc0TmLWCl7p166QFKNfHU6ctYbHfpdjU5V9OBp5e0lF3xlddk1oRQak9PS15xOaculXR5fvwvpHi/DwoDJ7Rdfe9pfPX7xaaCdcl7RWqq6cDVV+ejx0KtRM4LkCEvW/9lzaJvoJ8RW7J673yKnZB0AKo76XqGxZZfYEgwciCsxW8+zZA+uMy5YIXI2MtnjZ1JtD3wU9H5JOmyeZG6H0524eWx31Zm9W/K/8d0rGonj7m6re/MfH7+U/rvj3/GguJcfvIxRGBb5tSTDPmRVBEaXcvCeCZvo7c+1OQHwrM0X5zpWHvovZnzT0rfjPn/XYXc8tJwOM0Hl/OjplSyYX1XZ3q3mZ/QcFb06L
```

---

## Arquivo: `./.git/objects/fb/44ded2bb654c6d65aea3713497b5eecf3b6df1`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/objects/d8/dc30ee0e8fa7937eb7c18822427e032feffbeb`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFdU81r1EAUf5N0N5vubrtWqdJaa/0orMLGj2IVqiJ42BWVGuoK4hpmk2kbzcc6MxUrHiIIPfgvePCoePHgH+BRPLW0oAaKil68qQW9OpNk2+LAvHkfM2/e7/1m2l7Y3n/82JlTcLSv3AtivBmZvRMjgG/S6I5cpmy8F0oEt8FEDagjjuoKV+oqV0elT2n01HM8l+hqI1/XuJboPY1CXef6KLTQGExkqXhvSxsDM2fmJ8VtcvCiqbWK03tSa7sMyl2r1Ts90tW3VrPQypn6pJJ6WuoYtPSJLOtJZPbuBrO4G7yKhzZv7ze1g1At/ZBHqmqsX5humOECJzTWTHJvgTAeaxdJhwQOq6K4VJ+5ctkkrBMGjAi7/5Ib3MEnZojf8TAnckt+jnDLacc63+bUHZcSm4d08erDioEd3w2MDp7DPgl4KA710SynZXuYMVvWnNUNEo0q5sYhISJowm3l9BMAR/j2wjU0j0x0S0TSYSCBRvkhz8QaTQFUEe0RtqxtNqQ+5kymPhCbhoM5ToUd+jUB2l94YMy6HmHGfOgTw/ZcUSBhlo2pgztuaLkB4ziwXcwMmrSJbeGodRbjkmXhIAi5aIZl0R3inqKYbFCICP4CQjfQr0Q+m0zXDREBO2NM6pAXM8ErOYpgC9u09P43mmCKN9gEA01kUYn/Yd9mc2vz3PdonzhWVagulrjSZWuTRyWJx4rTZrKQ8XFakRvLm0kswSmVGOTPYPLhRfC9uOtD8fBK8fDzuWXj/NvquxvLF66vFpvLPU06IHZUK7E2i0W3Oi6VpSUcUPmB4h2Zv9ZlnVEJOh7o+rOn4wZzVJOBgiSqjRmhBWnm09ancFQS3I9zNrbnSax263wJSQ0pjsKUHzoLHjlH94vTknt2U4ifKkLoMxgrYKzDkXWorcPwV33g6XCU/1Qafn53rXQi0j8ODkX6UvlxeQ12fkHa0tDjoeXSvhePoqFVNPWpeuz14KvRPwmhGyooZ38rkuHk7n8BdANz
```

---

## Arquivo: `./.git/objects/aa/b03e02ec302b8230dad4cbd7e6fc53e89fa6f0`

```text
xMJ1@a9E`u"xꤢ
!v+}+6GzCbF#K3X5aTׂTymBm":^SK-scXɢODǒM9u]G\o-;
6Xk6_ȼRX
|\/;O9k=w/W=N
```

---

## Arquivo: `./.git/objects/aa/cbabc741ba21308a7cb3667241dc83292ee17c`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGFlc1v3EQUwGdsZz+yyWbzAa2SQgxpgIUQV2mq9hCQmu2muyVNt25ISZvUcmwncfGul/GslC4gbaRIoeqhVw499MAFceHIMX8B2ioRpJaqgsilnAJBcOXN2N4WKOlIOzsz781782Z+73nJcZfksbFTZ9A76c52BG2rtnLzexGhX9gkam3h4GAPBg10A6m4iAqY4oJAhYJIxUG2JhSlQhttK8RojM/FYryQoAk+lorJQjttH0SL+DWktqmx0ziwSVOLCViJq4nWSsdiqjQQuX76ryYX29T200KwoqaOILXjCHIy46EKTcO+waf60UjtHA99LYrgKR3NTmK1C2xkmA0Ht6xk1O4hlO15wrZnRT95tlRU3Rq1iB9XrU9qlkd9acol5azgdxRmL06rlld1K57lZ1TLtIll0Ggli/2uC3blpj42a5Wrjk4tD5ZiKxbVzKV6TNHNsl1hK1ViLdtrfpI+o5YMbLnkVj2hVMGy6bLdaRK60wxH9zyDRRZGh9jNwMuhg+PQNdAcuiGc2UDIhLVj6DJexSpeAEnQFAxRCk/YHj9OgsCymEgwZ0dahgh16jHTr/uWYupUDzrDLY/CZZRra8qy7ViesuqWLcVwbKsC8WmGTky9aruaXfGoXjFs3VNuupajLeswr9pa2TVrjk4Uwu/Ui0Ibrd7yOzRNr1RcChelaaQXXDMivZeha6C/UAJfx7/x/t754P8AJIhfARuwFoMfv4JfYdBAC9HVoOh5q3gOl5jGv1pLLswJpQj3Z3RUFGEziEAj/owoHLYsiCBP/r8c9uPD5Qs8EZmFUud/7cxB8qnCnKjg8TAOeEix/u6V/HQ+Nyu/LU+ply7KITHyJfVcXpUn52WD2LrpalZZPpe/kqv3hAoah3B0lZYdPx5hFifs/H7MqBHPBe6tNcuADPATyxY1VnXH8dsMx/UskmJqmYjuFvcSyTCBYC6RIzAg7AU9RtYbsiyTHiZLOzbwQLTQJXkFFplT7zp0DbSX7LpztDG529l1d/72/J3rjaldqX1zZn2m2Tu5I+V203133dvudnqwcZ4JptenN2Z2pdhmYb2wcWEv1fdjavhBavj+SlPJbdnNyx818/PbqWtN6RrpA/v1vgg7BQ5Ba57yqW1+PvqPZGLH5SSd4Ac6PJlUYSEsSwgpAnsP0gXbfME2/VjgAsqFaFeoL3qUQJ51gzjILn4fnHbevcQEr3KfDPkcRz6H7/Xu89lXBkM/h3kcRssp6DNo+YF/4Jufgz5D+zD0xTnx+ehfzZwUxkNfL8If5OLheL8oPRYYVbwx0FUxqvhwrVJ95MPSubOz+RbfV/KzcnDB8nvysCdfLeTVvGybfFZPBzU2em1bgXrAHqJGHD8VbNMM17SyMU58QOtR8A3su+WyTUk/TAjL9qxE2LeFyKw7xjqGdkA1YB1QnQGYdMeuA9iBdfImKDHkvBnoDuX67NbU1sSOVGIYF9eLGx88D+yBpnziO2MnNdmUJjkCM9luPx7WVsIel1dwwmDwu8P10eib4RFWH3k4fk8kDD86dmWFJNiuBKv1Szpkd1AEgkIdpLoI3y6eqr5UdQFkFt3XiB8kuIDEBK/v1vuEpQ2rvl4Vun0RY/wYjTxAI4/RxCM0+ggN/Jzs+fKtneRQI/awY+D+xzsdY43kTzi+2b/e/8WF+581+rfx+B8CK/oHIhJO7fPhfh8SEpsD6wPNzqFtfPzhyIlve78p/slTgqkN/w5qYXb8De4h3wQ=
```

---

## Arquivo: `./.git/objects/aa/dc5f8c48c83fdc57064bf2fe779106ba35132a`

```text
x%10#q$("*|윔uv0A[pNs8tb	
r3d/0B&kq8ZO,0Xk6mIz{bpkJl957
```

---

## Arquivo: `./.git/objects/97/29b36c6985ed1755f3f1ef1bd72ec99e5b044f`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAHdV81u5EQQ5pynKBxF2ZV2PLYnk2T+IqFlBUICdtm9R213e6ZZ2+3tbieTjXLkjMQNhIQQB54AiROXvMm+ADwC1d22Z+yZwJ444EQ9GXe3u/zV931ViTMRw+gkij64PQK21qygCryYKOavdJ55cHR3cIBTcSaS16C5zhjeeiqKlC8rSe5/vf+NKRjAUyLp/c8lF/BcCvOogrotnf2JKPAEbR46p/wKlL7J2MLLyXpwzaleTeEsCMr1DHIil7yYQgCk0mLmXRwAXnbAh/MUJHtTMaV9HOXNZUkkyZW/ZPrRsaoSppQ4fgyLBRxrWbFjc57Zv31mTJLXSymqgg4SkQk5BbmMyaPw9AmE52McoskTCPxw/HgGsZCU4YqwXIMSGaf7145waf2sw9EJHU0mMygJpbxY4l7Jcgj9aIyfzRMHklBeKZyMNi89iIXWIsebvltLuSozcjOFNGMIDcn4shhwzXLcmCCaTM5gSUoEyz9zO1KEeXDN+HKlpzAOggY/i4EqSXHx7sdv5kP7F/RzqUh2RRQwILrCs94Sit8SkUMNLBQCYlIkAigDSqhQHzpwh5hRlyeXf8ySSf6/A38YhuF5dNagso3zYZhGk1E7tQHs1ADWghvVUMViPVArjOnaUCdEKkE0xmFgBpvfAJPqfn3MbM2rfojvjbhJakPWNm/RdobbZLbUaV+pjr7dh+QwO7di6sf1AGejE8PX8TkOoeUs8rCFpiWFI/EGQUs5yxTF37IN3R4ge/+QyKD37ofv//z92/km8yZicxmlOS64726cr6JG8p2Da1G0ot/IKJ2kJI1n0GH0qWV0n7dUwDOlScwylvAcdSHmw1W0J4iyiaE9zx8h8EgY/KmPcpAE/sTmshH1JCEjkuJ7f8IkKxKOGlHAi1TIvHHCUnKcKAlHBa15zI14UDCKVZC0Fkn5kmuSocZypojy58OyG2cP0fqrlZJF15wIJNFcFAtvSGjOiyF6q/PkRDDl4ZP1StCF9/zLl6/+gVIOgy0OWgfpbbBnZgZaTIRceIXI2aVE+yVYAtCAvAbRVjjW+3tpM0ZUG3t7XlALt0GYhnRMm3x3kuBdfIGnwr4s28i6ANqIeVFWGvRNiSVGY23zgCMgu8EXJMcVu/evSFbhxO0t2p/B1u8vMYXITQHLFIPjThU8hrs7D9C6E7YSGRaQhfdsPYVPSR5Xcol1ixPzOp8JhmXW1DMuGW2QrMthGARHHTGfm/zYYoJ2uVPCDoNRcBZGe510dHYSjsNmauMDtt42+Hf01uLvqoqodMYLdIpCFGwGGlOvuKHgtC6QrpBiGYrUjos5i2gZbPPT6QBMvW9psc8I+yR8UyH1UF+UXVoV/TckfNGeCq+E0TAWwc+NiOfD96FhUeUxk46Iuy/giLh7H+W98ELUNFkvPJSRBzvU7G/qU3Nsyfg/Z5mliMpJljUyanhdOzf0Daq2Py1s+3Ri3X6rNAW+1Ruy+WOWIvfBwiwUvPgK+yaKnS+m37IPHV7e/yJgybCnwwWmbc2J5gl6CzokWryNq+tSfV/vq6KN1nV+X1dK8/QGZWa7aNcQDrDT7qvNPieusI0savtTVZxzNMC64d7jHOl4wgJ03gaxxkl2Ku92a1G7UdN3Nq2DM4h+w+GMppLKNNul4K5z3bYRkzjrHmgo243cCTZPoRlsC9fvREzb3cnZ5KEaZnD566fv/oCXpseV8FGGzXNduTvWZAEcOgT3pswsMNd8aEqxW1Jns/7o/Q/0NyPYMUM=
```

---

## Arquivo: `./.git/objects/97/a9c75d753da2d99940f072650c4f68d5e14dbe`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGFVM1P3EYUn7F3vbuslwWWfJEUtiUhpUQ4IFpyqFqlUeguAbJx0EppAWuwh8XJru2MvVWCqspIkZIoh+ylVQ49cEz+gx5zqNoeQUTJdlTUVK1U5ZYU1F4747UBoUp9kmfee7+Z9/zem/cWq/ZifuTcyCgYas+0AUZP65XrP4gA/M6FiOIhs/0NY3ywAFRYBAXowYLgCX1cFopiIebFAl4sxguSJwV8rJgoJL1kH5iHbwM1rkrjsGXLS81LTJNQk7uatvlU6Ujkcm9XU/MxtW1caGnU9BGgykdAtWMsPOLJaqYfDLa/4vKgQFPnS0XVrnuY0ISKb9ax6w1CKhdmp6dU7Dq25WImZydN6zoancU1p4o87DKVVMGeZiyuSAoyaqbFNQ7BS+YtmvL2HUsZJsG6Z5PbK0nlJtFtI7jdTkLjml5FrqvzOMNYAf93llOwfZItPiiDBeHcHQAMpjsBrsBlqMI5hrRIgSwa4RW/QxMkCoDEmMx/ackmNeS53PQ7FCsG8lBr0e3aMAu6Vr+lLJlV7CrLdg0retXEFotP0xExkGPammm5HrJ0E7nKdRtXtSXEZMfUarZRryKikCB3LgtN47ENO7eprGnIsmyPJUrTSCdzzd+Ke5gtPvgHdMMr8E2wfjve2rcZAoIUcIZTin1BCr5nf+6DuSg1ICqjA8uwxE8coF1cKAul6CHuO6OCsdBWH2AnEvugkN21IDKc/8cBinB2H/4PLp4O7xosASdAWVThmZ49c9NwATixuXSkKYOSHPF7e/S/peyeLuJUIUKd+DBwpDme7IAWYDm2AM9EItvHwpboABNvAeAkylIptw8OWVUsJ9RYOS6z9isnZDAqKrs++sClPl6aXjDXHd38rxYsA1VSmX0FjoUVYk80uTJy9eLUxQuz+Zt1ZHmmgQys1bCL3PyEenk6r9vWklmpE6QjOz9VnC7O5kdox8GzFCpUsuo1TGwq1kmVdR+3oazIYWsNL3u1Ko0HhgdlwutLJb1OXJv1N76FddbpNLmEPX3ZtjCN61XbxVR0PUKTi8jFGjNKJcJk06FxgqwKphJyHGwZhD8G2hHNgN3pkCTtHBCMRXKs5S4IhaY91gLVVoyklyHkKIeh6SbZPpBvEengykwFE0S0MAjC3w335v7IFh/8kco+OOp/0sxkH167f+3B5/5EM9Z2d2Z1Zj038Sz2aTOTe6jd1zYzvS1ganXqzkwzJt0trBbuTP559oPGwPqxoeddZ74771/akUBHrjH+Ite/kevfzJ58kR3ayA49vrCZPesXXsrt/sVfMl2NkcaNtfNf288zA/dgM5l5KN+Xm3J3AzXlzsZy47NHX6yhtavrucHXcfFw299ATKXfiKD99I4M5EMv0qc20qfWKo+/epr46dD6x5c306X1WIl0sVhmBjM0EY4Qwh9HMKhoZ6gajqaiS3jv0q5IH05U06oQiQNJPsh4vcIKt6ZQq0IiG8xBBp+AwGcrw8kPg4mFPyIKM8BngDvBltcihPBXMLAF3tsCw1vg+G+prkfvPkv1+9LP8vG1G8/kUT/1Eibu9qz23Jtc+9Lv2YRjOwKfYdsiEN7/K2ADP/8CdC+diA==
```

---

## Arquivo: `./.git/objects/ed/90979c34133e75fc7474973ec0a8881d36ee6b`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFdU81P1EAUf9Oy2y27y5cGlI8gKuhqQgVJ0EiMJibuGjXQAAfj0nTbAYrddp0ZjHCxJCYc/Bc8cMR48eAf4NF4gkCCNCFq9MJNJdGrM20XiC+ZN+9j3pv3m19bcf3KmaEr14fgclO+Ebi875ld2EEA34VTl1RiHHziRgAzoKMSFBFDRYlJRZnJvSImlRqKKZaKbLmULipMieyGUqaoMrUXyqgPRpJWrLGs9IGe0tOj/DYhLKsr5ez4qdg7rr183Ss3jvfU7aNdz5RTujoqxZGy3AdldSTpehXpjR2gZzvAbXHR4e3NunIOCrl9UVKQQ/X2eEn3FxkmoaLjp4uYslC5g2vYs2kBhbni5IP7OqY136OY+833HG/BHJ7E1ZprMiyOpOcwM+xKqLJjQdV2CLaYT5YeLjdrpl11PI3gOYcy4vOaJpK0NCzXpNQSIydjgwAj83VwnqsApmFGuvYSwOaxbphA80hHj3kmFg1xMNK+qAkVEs9fQKSB+2K0WZ9UTUZF67PhhGabzIyV5VcHOebq4nNt1nEx1eb9KtYs18EeR2VYJrHNmuMbjkeZ6VmOSTUSvRLfExiDtaUwZxim5/mMP4VhkFZ+TZYv2s5VAH8BoWn0K9KvL8T7Ac+AlfAlbEjzFcEVDAVwBG1cRP+TadD5FzgNGhpJsgL+cv5wpnlWdUkTrypIROVb2FKn6pBEKcqHkl2hYo6BAdIiDubqPQzOJxEIxF9Bu7kK4Ef25E62fzPbvza3/uLD6Y93N25NbmWnNhqmSBs/UGgJlVmTv1TNIWKu6P2J+HfC1iQ+WGecEoE4bKvHk6/G8eaIIhIZQVLFpJhkhJuOnz0GI2PvWZiyTGseh3J9zDcQzRCjyIxVfXvRxTfJGV4teKePuPopI4S+gLYJ2h5c2oPBPej6pra96grSu7mutSfbueFA/dzeGair+ZX8Npz4ipTVzpXOjVzPuht0bqEbuxe1d+m3zX8iNg9kkMZ+S4Le6O5/bJkBrQ==
```

---

## Arquivo: `./.git/objects/e0/4e3c6c01bca1ec9a56e65f84a277cd3b051359`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAF9U81vG0UUn1lv1l5/5ItCUFLJS0MrUsAr2oj0gEBNmsiO3NRsI0shdlfr3bGz6XrXzIylNKeNFCmgHhAX4MChR/gv+icYJRJhpQgQvZQTECSuvFl/NALBk/bt+5h5M783v9fwgob2zs1bN9Gb47k0Annabe0+lBD6RThDGRsY51+AEaIHyMAlVMQcFyUu5YUvlRJFmcuxnSiNFRWuxLZcShZTPJVHdfwaMsYMZQn3a3G1rkAkaaRGkXRdrcwMj3zxN9S6bKSX4E5CjMwMMrIzyJtc7AcQzxq5ebQw/lz4C1Kk3q6UjKDLCY2SBvm4SxhfwFG2uHm3bBDWCXxGwJ9Yd/1d68YmaXc8ixMGIaVFuOk09hXdctquLyIdSpruXqTyC8tUx6XE5gF9tJ/WKWm5jNNA7B+ng/Km7VmM2QLpAC0St0/Ad/46qBBV0QPp1iFCDsQuow/xDjZwDTJ90THgkZ6LPVGSDiFQGXxxqWZA2xZnovSVqKU7Frf6yg7aBYDd7u7pTdcjTN8J2kS3PZf4gNC0LepYHTcwXZ9xy7ddi+m7AfHMpgV+xzXbgdP1LKrTuHvsBbhC51GUNU3L9wMOzTJNOgWHC76wV0CF6C+UwnX8e6y/bvX/55BBcROEIUSBL27Cr2CEqDZsDho+ZQdXcUWs+IeM8lJVqgzJeGGNgRYHtfIIViQvpAbmqEIC8up/52E//v98LR4TUaGS+3edKoyGIVUTOl4c4ICnTOy/fX+1vLqyqV3X1ox7d7UOcVwnYNo9486qoS1vaTZ1LScwSVu7s3p/ZR+YNKBVYYe3vSjNqeUzyw6Ap0kq4EWK3aUsAIqTPWID2aNUk3B7x/K8aMz2AkaoQBlNDgk+or5Mx0VCchr0ZTDoJVBMUOuapml0UuQmPeC0Rc3RLegchEU9tg0qRM/UicevhsunuYnPtj7derwdrp3K6aONg43eS8sn8srp1MyX+c/zx1NXwnWRKB+UDzdOZeWoeFA8XH+WufR95up3matPWj39g6dv9Sof9W5vH2dqPblGp6H+xkIuSg44SUUXY+ZHU4NQYThmjAoqRNPD+GBIXb9FBdOilJiMhgWt6HesT+t+XxIw6zGqb1F8Zh946r14BMj7dB4KCEqxNVC/JTDGP6JrZ+j6GSqcobmf1emv3jhR50Plh+zck4cn2Ruh+hNOHs0ezH5S/uZyOHuM3/1TEiNxnkDS0h+xGZ/zN2NKQM4=
```

---

## Arquivo: `./.git/objects/e0/ec3da760ded475ff87d0a37c06f99e5941ff5d`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVbAwsGAwNDAwMzFRSMxLzMksTtXLKMnNYfi7O+hwn+fVGn6GgNzjx6VYtGyW2EDVJSUmZ5cWQJRNTNX/voVfuLfKLfbNxwQPJo6luivgymBmdRy9e2Kj0aSdQWwRHbsPLfge+ofzJVRRcmJRSmJBZj7EtNqrk16u/v+HRef3lQkuk90nqbtHbUZTGJ+YkpuZB1F+j/9OpNSd1If3+Dbp+x1p3MjQkt+FobyosDSzLDElvxiiR+rbuu+mbMnbOp6lxHT0zlu22HF5Jrqe5JzM1LwSaEB8f7l8v/+ytqmz1VhFrpXMW9Bsl3EbXUNKZnpmSWIOxIZ5hTUxGtZLjhtatPGfsj/I/+HhnR8wDfl5aZnppUWJyYlQH1dNYFt66c6L7r3bYr+bV3kf+ph/2Q+qOCU1J7MstagSYurHGy8yWjiqKrrjzubWXTu6RCpxeipUYWZeSmoFRNXO3Of/574Qk1RkkRPoiq6vv+DlnAVVVZCYnpgL9BbU4pMbJ6oznfLwisr+YOh3dkLLj91tTXCVmXmpUM/Y3dt14N/EXX+l++e3ZG2fpfv9xY1SmLLUlEx4sCpdk50fpF7U9fCygJt3g8mV9/EqEqjqkCPuSpb30rmfX0/1nqZucE+puD3At2YHVHVhUXxyfgo07NkPlf5vM+DwuBr7771mSPSTd7OWesLVgZRBI9WLsa7m27M7C2O0pN4t1L/8Reb74mVQdUWp6ZnFJUVQX6+QPrJW2HHSmx9razb58Wwx1HfYo4KmEGpkwFKBna/Lpk7kOxxgeJTvq734CpcAABG8TQM=
```

---

## Arquivo: `./.git/objects/a3/fbab417347e109f9efc296191b3d69acc1ea64`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAF9U02Pm0AM7ZlfYdELVIhut7dIkbqN0i8l3VU+KvWEDGOyUwFDZgZpq6r/vWYYSFi15WTsZ/s925NXKoc3N29vX5Ra1VCisdhKkHWrtIW7h8871VnSCezo3JGxwTUs1WRa1RgyY8Knw3az88451FLdVmhlcxqxX2TzA28Pg5/MABdoMUdDI+hENhN5EGhHA5YXSlGrqZRPy/A1ilo2YRz4FsxmCc+KR0JqKqzSP5fhBOOU4N1QOOU+EVdqsJKGwgRGZVlRoTHLa11xIKhkAKtRWqrMJ0V6mNBiHFW8CIA/kTOdQUYUO0/RaaM0e0WeDrYPuOhLOCiLFa/CdhqFAoJzh42VAgWBdTE2WhJSKHNVMKUnKnhZUbhfb9arA6zu7zbr/Wod7Y/byCXGCdzEgMYXr6mxKnORhNHHr4folQs7V+ZbwIfd/XbsxzPrRfF4ulqxhIF/WpItHlVDcyHfqBHcDE+6a7G3+KigVLpG6BXgCR2D/2lw6GyC9jT/KeovQs5WzOjDx9398QHefx9oXAp7XUzw4nsmD6vqWp5XXlTKjLL7fV79+knxGhuYji4dD358JpGDDUN1TyyByRP620ofbV3xVU6BX5PVJ4bDOsKF30syj85EMWj2P0F/OysO/gDV5E21
```

---

## Arquivo: `./.git/objects/5b/58eb29a001a57d431ba9334cf7bf478b4e4da6`

```text
xTj0_!trbHISڐ4ew3ƻJmɕdز;)hf޼ytaޟiYàc=֌m{DҢvz@ЁWzWJ]ȣ%xhaڴG_&,UOb_, m<ʢ6d灸>9_7 ~/X8W-\e[6`&yd~=6,Ӱɢ,L?=G9%qyl, Xf)bXʦXXTK<Ŏe_7LݪhAd!EtlыtIk荋)|%JE&$Pta>qgsaiNN>gl/S=7,-ըa57hYңRTN"}Q:ԝ =!?Vu*ܺZ05i,i0]C
```

---

## Arquivo: `./.git/objects/4c/628295d5537337d647351c163a37b99ecdee85`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAHFU2Fr2zAQ3Wf/ikNQsIdxtnUwFjAsWx3akSbFcTf2yciSnGrYlivJo6P0v0+2LNfpYIP1wwIJ0Z3u7t17T0UlCnj99v27F6UUNZRYadxy4HUrpIbV1UUqOs1kCCm77ZjSIayFrL355Ugy1YpGMeXKzrPLTToG+0rKJSPaRY6LNavbCmveHFz1Z958x28yG2fKXqdY4wIr5i4dmM5p4XlygAfxI1S/lazkdzFaYFrzBgXeOMLgi+FJc99CE/JnjKZrpsT7YBtHZo6PFgRLamgRKAS3bE4qrFQ8XzXwKCuh4oZCmbsSX1rilo7BYOmB+dDCoLFb+MEQIZ1UQpooLSL7/ygRsTtGjBY+2ieb5FMGL2Gd7i6hlYJ2WijYpWdJCh+/AcGaHYTkOIRG1Mys0w+c7sVgu0cl0+QGV9XxGFIJxcZQj2R2HPpIpjvZwMRW5JRy+rqNQ0COhHyQIrrRdWUovEcOC1pOsB5mpLdCzVk3QnLCRYOlWaWneDrnYyN/QNYvuwSlew57l/pRFAXhkKJMEckJFkd5hMa0sQwxqbISWP9ePPF5VNw3954t5oCulwddbPdJmsHFNttNpIDf7xTCBD80KQM1nGuM5W3Hf2AqAviy2lwne/BPVAjz73q12ScBslz00/7e15rG/vY2EHXN9T855en79ztZudc5f1nm2ehO5URQFp++Ov2TH+zGcnHP6YPzxBibLMHpEnijn60Qur46W2XJoyb7JIOJc+OW7W5+/nqepAlwahInypjd5zQM/iuNvwBHAOQm
```

---

## Arquivo: `./.git/objects/21/714b322d17b2d6565c81c0f64d2e61a1ac5e46`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGlVP9q1EAQ9u88xRCQSySkrRWEw6C1pvTkri25UxGRYy+ZXCNJNt3diFr6MD6LL+ZsNsnl7toieJAjmf3m1zff7CrnKzh6efTiSSp4ASmTilUZZEXFhYKTq0nEa4XCgwhvapTKgzMuCmsI9gXKipcSZed2vphNo9aoPZNMYKw6y7azwqLKmcrKdef9Piu/secLY0dp4AlTbMUkdqA1qmWysizRlAfBplTHtdqYVFAAO9EcUwsXPwO7h9muZb0xkXwK7NgHBUp2cFvWBQq+1B93tgddn8s4Z1IGwy5dK8EUYiYSYs94OMIwNt5QN4g3hqxU7tgC+iUrqtM0RMVrS1wLyQVZk5Vv3tuDwamPPzCm2Tj2PJyGpwsoeYFLqlGxWrBSIZxFlzOIeZlma7LEjMN0Mpss4Ij6bbI0R5TFpPBTVPE1L7HNtRePgI3Hl9Hu0egrZNS+iYc5jWl0Slz8+U1kwJXgoybfY8U/M9VWgie14hI+nYdRCEzc1Nl3lnAq8uxkOg/hMnoXRvD2M3GtcM1Fxrym8bal3n+7KZbn9xAY51x2zWqiB59NqQJVLUroZeJ3muyU7DQwTWU7a6832L0W4jxDmoZ/rYrc3gBue6j2t7XG7DEMFLKBNoBdyjV4Z+A7Hh0XhOxe+5x3zdtA9hWX9+v+oNLrS/RqgafsF4qltiTcND8ouJG0qSFTWMoWNwaptJT1veH4vu8aiOKK5WNIc87U/mlKYLas2JoVRB7fi2G1q0OqK7mCYT6gxWmCw6sADs2GaQbbae7eRk4t8iB9YONpl1QtlzFPMDg+PDZro4M19P3n3vbDsCcX8zBawORicQmGXAmOVoRnOvNMQx7s0OIRtbpAFz6eTD+Ec3CeSg+Gz+gKy0TLb+QOtOcMptamaIf1UCbTufnXq8KLIlNbl9XW+jyyTf/O/2tZxyglD5Soka7fvWH8BdfDJJ4=
```

---

## Arquivo: `./.git/objects/1f/41da8914a8115c5f33138778f733e76deb8665`

```text
x]QOK0OȩBa)y"mRqm;[Ml$
#xؔv$t5q@<[C?XGzZP~$im>v㬬$ZzRj)lIf`_ZÆ;@sl c	_IkR# Nz_,La[	i<c2JӜAxitAE\%n2EBo>[<~'e"
```

---

## Arquivo: `./.git/objects/ae/1f606f8fc55eebc21b65b36feca00453afb758`

```text
xmTao0s~(l*U`
Pi;I7HU%ݽ{R9ɮWJjR2cY#-f:zJVv`|da|4J0/UX|jn*fܞr
]u0Q tU6L!
fY
`7EEk$Qo2JZI!4p2
rwߔ(*$*˪M
'eS^xXXF5.~8k&mǤ+&WWN3YeH#K@,*Wʜ/W2Ya5NK"MpO{%&f*QK\`6
&fE-& b4_㎃S`Z5=Fݒd5lZ]3eOwS^lv9`n	xgmHӃC=.G>ѻk 8jh&dSrf.dag+5<Gwǔ3]Ī ƥ;":$v
7vjFawӏ)Wu\pG3,lnB3֝(}HVeWV˃VcW>'q?NOU`Sѝ+4.VA4*07\
```

---

## Arquivo: `./.git/objects/ae/94f251639d059e049e4b38aa19b25ee4d13748`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVTAzNmIwNDAwMzFRSMxLzMksTtVLLqgsycjP0zU2NNErqExmqEmd4xn5jEXr9eW9u9JMfH89L9z/AaolKTE5u7QAQ8fxrT3vHLYEqn9v+yC08PrDzf4/DHKhOpITi1ISCzLzMfT8vfBgi6qKjdS80FOLNXYc2ey1J38bTE9OZmpeCabDZt4yjfksy2/SsmezBZ+F5KKpvaorYFry89Iy00uLEpMTMa2ac01j6b+oXZOfVPO9DZ8swda919IPqi8lNSezLLWoEsN5zR/1z3/a8KvipCLDBoGQ6ZekzpsoQ/Wkpxal5iVnJhbFFxYl56dguvO3y71Lu1N9clPXLS40mb713Xnr3I9QvQWJ6Ym5QM9hOvIC31pmO5XW1uYzxyq3h8/Z+UHKfB9MU2pKZkp+MYYbV51efdxxl6JBV83mtCLHO82aeg9roFoKi+KxOu3cA62upidrfh8RatznphnCkq9XsweqpSg1PbO4pAjTZfOefe99fWlB5MEP9pk6Lh3lLSuWTEXTg+m2B342OYx7Fr6ZFfYsvmVR+VlrVuFIAG+J/Jo=
```

---

## Arquivo: `./.git/objects/56/750b9d435fd664b0c122d48ea615c4f9646496`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGlU19rnTAU37Of4iAM4pDcsQ7GBGFdr6UbLS1ex9iTRBPbjGhcEqFb6Xfv0ZjO28fNFz0n55zfnxwbpRv4+OH9q87oHjpmHRslyH7UxsHpzZdST06YFErxaxLWpXCuTR9ti6kRdtSDFTa0XVRXl+WanDu5NKJ1IXPc7EQ/KubkcBu6v8rhJ3tX+bywvpwzxxpmRSi6Fa7mTRSZhR7kf6mS0YhO3ufxjvFeDnESrRDIL4cXw4mnps3vPH4uw5bokx9MEYfEuxElcG3jFILWulXM2nyrNIm46EBJdNDUawcx3rYs+JdkEeDDG+TiNZBkybSTsdpgljfUfx8dUHEvWrwJEh+Ky+KsgjdwXl5fwYoD1+W+KOHzD2iNZFzXood9cThDKTNcqMrBj6adcO0dU+oYo1XaijU109iEyxgj3GQGeDaKhksKVxvkphCvkPVyCfTO9QrdewjpOAucHjdmj9pu3N6hkW6yuwfJH1HHbC7GTMk/6K8/I5JnIAfcSh9n+J49nHeUUEqT/7f7283+tCoCWzgU1YqFMK8tfL8oygIkXyJUSDyRFFOJ9342Uve9dP/k9cufh0xGhdXerKVHrVvNRX7y9iSJngAfvkVT
```

---

## Arquivo: `./.git/objects/56/7afb65d82d592fab791ce2d487b02602ac3310`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAHNVN1u2jAU3nWewmIXJVJVtXRI66ZepMGoaCGw/GztVWRswywlcWY7bH2evcVu+2KzTQgEWqmVNmm5cs6fz/edz2eR8wW4uLp6/4YVFRcKcOk0p0o+YF6tBs5S8AJs/87oTyWQBE1QRFE+Ylj5tZBcOM7oJrudxQm4Br2cY5R/41L1jDX0ptBYMRIEVYxnZGHtaQwjY6904EpQaY1zL46/zqLRsWMW2drDd5eDnuMQugQrqnStvvvBAfrDvCx1Vtut+adY9a3TBJiGrpsuT1srQQotkKTGYzrdeWpJhbGaPnfWCkn5gwtiPNtm97yaSOvR3e6s2FKULRFWXDxcHzBnenNtP4KqWpQWyQYhK9kTELe4N7BtbQ3c4D3b3NTflLP+tyBBC5ojQCiAUmOlOcWsoKXiEvQTWqJSSVdnFyDO6xV4/F0yzPdK67FTXCva7/V61mz69SPoJRAk3k0AwWQMwlkC4N0kTmJAjy5ps0wmI0DzOfECMI8mUy+6B5/g/Y4qE1LygoIvXuTfelH/4vzcteXDNAi6cdL024lLw8nnFD4T/r3WUBlBhGYFlVrIkzBpQ8EIjr00SMDFefcSLBgiPKMFSCZTGCfedN7G+mkUwTDJWk+L1P1oj5oy17Gn/THMBSe1oX/NSlzniCCA+CFvNmszztdOoNrW32n/hcwfzC7TwzIkRXAMNVAfHk+3z4gLZqGmJIBaEL4X+95o7xG9Zp6ESs021lwk8G7v+ZgalaCYgzCdau34WhSng+dUgZGiK66n1kpj+KyCllzxNmwwHLrd2a+ZZGuag5vZLICeAbnRSBKlBxCR+F6ztRbKUezYC2L4Ql1Qwsg/lEVT/j9RhXmDnSfY5Z4pWkorhPaNdgMUVyh/kSKWXBQoq9AK2bXXDvxS62I70pPw8RcHrLSxBJ1079IrTdXy6cQ5LYnepvQg5S/tjc1W50XBVLPVm52Acy7p1mRXf2P4A6qAHS0=
```

---

## Arquivo: `./.git/objects/91/35305e5c3f4515aec966b5044cecdce8a958d0`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFdU8GO2jAQ7TlfMUoPBBWF0sNKRUJqVW1VKlC3lNtqhYZ4Am4TO4wdaSu0X9NDP2R/rBMHU9gckvh55r034/G2slt4f3PzqmRbQ4nOY6NB141lDx/v5ivbeuIRrOjQkvPJZVjO5BprHLmY8GW9XKxO4HWop7qp0Guzi7FftfmJ79Y9Tq4PV+hxi45i0I78Rm2ThIMNmP23lDVMpX6cpWNUtTbpMDlJiJsZvCDPlGYqvOXfs/QcJinJh544F50sHR+4sIpcOoJY2aao0LnZZV3DRFEJO2LkzSkh474709im4TQBedRWrPQlZMOAFC07y4Kqbd7/X23k9EiFNDxLf9wubj+t4dCi8Vqhok1NDh18Xn1bQmFNqXctY4EWFvPlfA0TqaaT7LdEoGfPS/LF3hq6likq6yLUOblYBhZvPVYnRaEKcveDl2YGD6DLqEiVnNrbkB1er+GOdggW9tZ5QN9iBQqlsYdWO/389/mPhQYZobbGI0tgpc0vYWMmb0FZ+L6SlaLA1s3EpuVKCnOeY7/zCA9zFlg32WA86PsQsvqWzeD+ISxL6bzMtgFGs6NsMoLLOt/A5HRsXR9Dao5NQ0Zlx5Dewd2TmrYmtukU9Oh6QwwKWqbH6Otp3PGMj/opPUc+9QY7poBJuS0bOI9lHq9EvEix2hGkp3nL976uZEqPabApmuErzP8AoBY8wA==
```

---

## Arquivo: `./.git/objects/91/652ff7b40f138d7a465decf160480208a52da8`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFtk0tu2zAQhrv2KQYKArRAZcWJ85IUL9IX0EVbICcYkSObDUWyJJU4KXqYrnKCnsAX69CSkyaoQBASHzP/P9+o0baB89P5q5/7QOtIRgbIGgw0XcVOZ7D/azLhrUZbcQ1RRU28dIniuncgLVypEKlDyOEdern57ZSFb96mYEYOl55FENZwjpjC1lLdgNAYwkUm+HK2mAA/9epwMcYnuKJl79FsHpCTBXiPPNcFnxiOOgjxTtNF1qFfKpM3NkbblTCbHnvqKhBWW1/C3sn8dH7WVNniI6ZQloPdGm1RJgvof/TqhtcIwlO6QShvRysxAA9eaVWSs3nY/KHwFpy3so8si8CRVEmgQD4cfZI5rQu3mAw6k9NRacOlW3rbG8m62rMWW1FBY70kFjpzawhWKwl7opHHNNtt5RxS9aGEM7euwKGUyiyffEoVnMa7ElpNvP+9D1G1d/lY7BKCQ0F5Q/GWyFSAWi1NrhgcRxSMg3y1vZrfenQlpLmCZXqdpTqOZLZ02MpQ/PSVnno133nblXtGh+dHTQUvqBxMD4doH9bO+ogeLtGIbeG3YOH156uvX94w3/mLFI+cW26fPKh7KuFgev5/xp/II/TdI1dhO6cpWgbYJZqMiYdMjBL+MHYwxh71AG0wxtaKZ25rhJWn9iIrUHbKFAll7woa3WS7Zm6iyXYleYZ7doJHc6wg8o+WSxLWY1TWlGCsoX+wHkxP2Bp38VivS1TrbbVSvrrAsfsHdaPIF3/cX6jPPwU=
```

---

## Arquivo: `./.git/objects/fc/4b85eafcab5b6f45f6948c3ac5b596b9c6a9c2`

```text
x]AK0=WZ(YA(<H{Ii7&u2Dƶ٭SyKݻ_\^*Oj4Cwo0%|L)0՞myGg=y.`{Ev}2]]9Zu@9/Nْgj6
9*	S69@X~u]LdLNBg<VM/LCp).?5֘,wixhBˏAel%v2.<ЇXa2ȃ_1
```

---

## Arquivo: `./.git/objects/fc/7c03a61b2d8d225065155e8660af440e0fc0ca`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGlFE1vG0V0Zte7XttrO01TJcpHvU2UtBYQtyUoSEAF+ZID/TCLZYhIslrvTpINttedXYskgGQ+BI1alAuVeuCQKxIHfgES4ZKjUSPhrlS1iF5yMyQSSHDgje1NqiBxYaR5896bN+9r3nv5gp1XLo1fuoieiUXDCNbOjZXVxxxCvzLCX4E2cvA5IFW0iFQ8i9LYxWnO5RKM5mb5dMANNHF+VkiLrphAC/gcUgOqMI5b793gQgA4oho84kgLwcxp38zxqUpj7TdqqBup4W5U6BhrX7thNTKEkvI+o5OcF3otM6vaFZdQL6iSmxXiuEnsxV+3Sqv65Swplgu6SxxgicvE1cz8hpjSzaJVYpwyJUvWmhdynxILmRYlhmvT9Y2O1AdOobL8Ueomfc6wTeIYzKu2Z4hlhYd9cBFAFeXQIvfiZwiZwOtHb+IVrOJ5uGktlZuHrLZWigP/+X1Ge0HactkLMEtJjjKtHu+4lPm3ZNOi7jrM4qBHUqbu6i1g2MVRiLhYWUstWQXipFbsIkkZBYuUIFjN0Kmply1bs0qOq5cMS3dSqzYpaEs60GVLK9pmpaDTFG0mzoEANRbgaHndkzVNL5VsF7KmafQUmA7Bds4CqKI/UBxPcb814dfvN5rnt0aLPgAJZBxFCQSrqE9hH3wFEQyiBCiY97OH/P8sczkuw/J4Yh3d84u4HOhDOT4jnBABUsU5/Dwea1tNMKngv6WOdAk54Xz72gTv+lFOWETP9h6/KAeyfCZyTPuYryGBstx/38/L/ptM3MeOzyz0isoDDGSxKmQDKV4Vx9vRDyEFzUu+rIhMqIV+yNoAuvqGhV7iB5CFFfR//fM1vcBbOBncZ/+xkXpr+ur0ZFaxTGVGvXFNgR7S86RADKsIBWU7ytvpaXVaYSWqvKIMOxuyXzArbrFAWcQ0CsCTmi81y4TGDJT0IvGChg0lueYmJSoyCdGoUMeGXiVrxICu9aQl4hordol4oek1g5Rdyy55glGwHUJZMrwOv4lV4pTtkkOS4lMWOTNPe5qKwTQY9ng4HWZqZESBRTvYZaTtrwYzgJ4DDtPsfA9gH4rySSh+u6c6UY/Gt+Y2526/W52pR2PVmQYXEk7XpdhWbDNW607vju2e35PUeqxry96078cSt/hHkVj9TM+9U3dzt2YaEgrFt+RN+U6sLoW3pE3pTvhJpOvnyPBPkeHt5e+u787V3tFq+nLNKtbs9QZCH+IJDo5reJKrRYahfeQpRgtT3J+HUSSfOURYiD6Q5AYP518N8aT+L8N/O6wuPxmYlPD22EQn+qHrCqA7nZEJhd8Z4CaG0E4CM1zhGT40OCnwPwo8yFxPRrxgexpQVn+twdPZZsFwaQ5Oq7RMWdd5Eps9eR3+pPWLrcHR+iDeT+o3iHYyVc2USy83hwy5Qi8Aj5WZ8yoACAbjR2jkIRp9iPp+CXXeu7AXGqqKD+S+7ff25MvV0GMc/KL3496afPY+ThxybOAc8IhTfm+iTQv/AExfdbk=
```

---

## Arquivo: `./.git/objects/c3/24f6b38dd045d556f639b05b277ec9e4d36ccd`

```text
x]QAN0W|JP
HTAZpx%qX;RIdgwgfRepwsUFE_	$բ6ޘF+xٮ	YM֟v{g\#Ф"<d@t7<DlE%kxVMBFw-ơ)NjCJ	8oi^rX@iҡƧ>*y`ȬއtHޒVdQ#6ume<5<'4(P"Nr\+Xěsgך窋h=/1y4ѳDhZa+trv'½J;a> 
```

---

## Arquivo: `./.git/objects/2c/a8e03704063c472e989540f1dbdfd9ec819248`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAHtWetu2zYU3m8/BSGgiNRpitNiw+bBw7LEaVMkcWY7G4ZiEGiJdrhKpEbRXdqiT7NH2Yvt8KIrk8YJmm4D5j+xSR7yXL7znUNmmfEl+urJ1998thI8RytcSlxQRPOCC4n2z49nfCOJCNGM/L4hpQzR88XifHKVkEJSzkJ0xEU+aMtGgpQFZyUpq12eL05PZnZQbZRSQRJZjXSFJcmLDEvK1pX0C8p+w08WZpyUZnmKJV7iklSL1kTG6TJOOGOwNSg2GAitOBo3RvjBwG4Puo1Rb2PfqMXFm7FXL/OCweB7s1MEZ/jerheiysA4yXBZjtvmBQNcvmEJSskKUZaSK18Yv40qBwajAYKPIHIjmOMMfyOysbcLdqzoeiNwwkkJJ0JQ5KYE81Iyfjp86ijVX7+lhh2xmzRVPgVvOR4GbypDzB6w4IwzokfoSg0yY6deshElF7BEDUeJ/mWl1bQUb5q1zfqIXJEEsOd788nJ5GCBHqOj2fTUHmh9g6azw8kM/fALoik6nMwP0Mnx6fEC7UHg1FbVp9bSnB6tiEwuQeGWGkRjGtXQ7upUQKTrHVeU4Sy7Xusk42V7W6WBsbs1YaNfwyyq4F0lRRWMEHlGdWtvdCnzDADxzg57I+uP9y1MFLxUSO0Igj8aZJY4e42FypYGZdWJNVBDxHhORoA9FTqV5n4URUGIclLicgTwltX43jCwsFaWwuhNYHkoaBxML84W/uPgGoQ4QNhovR0cvBz+WsdXxUyrqtZ+h4ZdKOiIahA3EL04P9xfTHrYnE8W2ocx8CZekowkNCdMcnDQI5XVvnJwGHSRSrKS3H7e8dl8Mlug47PFtHeo3rR/YoB+2j+5mMyR/6gMbjq5Y771T52Dh5CDYKDOQA2Anl9XkOBQNhgSmK2JvxcqfPh6ZYA+R3sWH8p31ad/RNsmLQgO2uRE8Ir/2laEaCejrwXZ0eYARn0aKFd2jdB8w/Ocyq0TXSE4EjzLljh51ZL6WDnfL3+W8QuoiinfhutxmlO2m2CRQqHmEMwtyV7LxZWck+7bJXAheLqRXJXPlyZfHiqlLdtTSVjZsHyCJVlzQbFhpx4IW9q18xu4uhXIfyvPd+PTEH1lFFB99bVN9qYraeCzJRqswD1hYNLzwTFAUwhzhwJaBNSAwiwZjYBxyJqIHigqXf97iLAxaqCgTQEc6L8uCAwzYOhNaEnuQAxG4J5QWEFnKrCua7HkEmdADUPNwg/FDPOLU59GBdwhuC341lGoQC+mx2dIc0ZsBhEt0PQMFRH0h2P4EZnhGH42a6FywRqYBMlcTcFKJfDz88lsArKm/YZqi/ydAq/5DlQfXQ/oW5xyKEHdEg4pCDu08dbtNFUBBOeoZZil6i80H27Nv86zq4xjCZFSEs2hn4rSdFjv0rtaLDYIdmwCNDtjLrIFWVOo8bo+gvH6ennL7asWuSeuL+FAKDSJ6tZsqXMUhakHgrrndRoZhRh7Cyoilf0hoBJarhzHgEeTfSHqJAYukU5HtRI8l0AXVUTq2hxXyE2wHqOpc5Tu8uqkcqabxLk1yT4ge0PSORLbJqEj+Gw2vThXV8MPuOzuvqkvnJpS1JWzc7Dn9cigjaM2JZimpCNrp+ue20a8E9ZuaFocdmsoWmtvcP3/fNe7quvo3IXvatJpGK+OPzBd/R2u9Q6ZbMeEdbpvX99rkXsyoe42YrjACgmkUrPhRy/vt3NeJxPaBKdUrPs/BDPQEsZcpCTvJJii0W4COdP/KLeN0U7C31J2iXccxXps5szXvHS96Q4v9aPqcpPylvp8qu5CnXWXZKtx3SRbx6iqUa6g67YVcIHeNb3dF+kSeLv1QmYeXNOlv929GJKBcakf+ppGTmDow7vv5X77JffL4TCEl2KJKbz5ToTg8ENtQa7++pPDlxxxdA5veWtB5j+e2Lpi4qT6S+cx9Yb6AcMCnp3i6s3cD761e8GLOYPmQW1m3rOaZ9HqOcxOtF81zcHua+Y7zxgHfvc4yyhTdxBviVnCY7gk4Awm7ImK/9Sl4Q8uXqnlR/BvB/hfAzqF14UMC+/9AD5/A4uzZjQ=
```

---

## Arquivo: `./.git/objects/c1/558f9728b56b28904e5a864de09da68d39c0d0`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGVU1tPwjAU9nm/4vhgAsbqRryQ+SLGmSyiI4743q0FatZ26YqAhv9uC4jTFS97WLKd853v0tOskBkEwUV37+QQEEIQpcO4n6RwE8FjlA6ShzR+im965nPwmNzGaRonD70+tO6T67gfHcGwd92PhhAZQHo3TAbt1ZTDE8+74pQwDC2O52jGiJ6EEPid03LehjcPzHNcMUIzrDaf9temr9PxyznsM15KpbHQl6v+5RrFMRMol0JToWtQjtXYFAo60iG4B1iGmpocF3kr8P0DQGtAu0FpESUmhImxGeoWtXRavTjvfjrNJFnUpI4KOkeEKZprJkUIuSymXDTIN36bKZWyYmukogXW7IU2sFb4NnTj8HuWtj6hbDwxYeGpls6GTGot+Q8NWpY7ql+1I07FtBYAYVVZ4EUINgkn9feIlJzt7pspbHTYt7NnbKtm75zF7ekGrtO1MT1PK81Gi4+VM8dlFo+qxjSXZVwzvWUyiwFBZ4eekVlsVLFXGoJ/3D1TlP9GlCksiIsnONvB8U9Hf7lwfkOlja522Vb3zLWF21iccpfe0nsHTgBYEg==
```

---

## Arquivo: `./.git/objects/c1/f1be534b5226920d291feedef39321c82be6d4`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAHdV+1u2zYU3W89BSEgqDwIStfkVwCh82YFyeA6gS2vGIZBoCTKYSqJKkmlCYI8TR9lL7bLD3257eAWGNAsQAzpkry8vOfcc6m0ZCk6PXn10w+0ahiXiAnHPombVtLSKTirUIGFxA1Fdmh+fblmrSTcR2vyviVC+uic8cpH26ZkOD+nJQGL/r2I4+voPiONpKyeeAs4EQ2rBRGd34v4zXJtjcp1TjnJZGeZLpakakosab3rVv9G61v8KjZ2Isz0HEucYkG6STsikzx1HK7jRyHqz+I1nBT0PnSPcV7R2p05dguIL0R7zj0TGuMPodtPgyXO9np5NV8ki8s1LHIha5Jmx63OinAdJoIKv1PnEt4w00fkngqZsHdhzFsCXnJSIJZCghPILU5JSTJakVqyBEBKRNnuvKzlggEA6uUMCclnZw6CP2MPyD3JACHP3UTL6NcY0Rydr6/eoD1/Ar29iNaR9gIBHwnXR55y6c9m2h3MB7t1WhCZ3bCaeGaMFqhmUrk0W6vtOaaQ7AnonspCK5KM5SQ8fXnqo5xITMvQjaaHQ/XfHxkidcZqyXHOIJ/aJZEtr9U2f76g+Yu/HOdng14AYHru8aOK9+k4wzwHjjI4QUesJCuxEOGYVjOd2xLSjXnSLdEn1klUazWhzwZmAwB6TAEKcN4x4dpc5ynYDKNsSkyiwJqngXm2A10yEwAi/BpsTQ70csg3xIJCFQd/39I7yJFwh9x/AfofDfINZ3krWYc4pHNCLB3XkUDz1QL13iHUeL2N0NV6Ea3RL3+gDEuyY5xiH6CviGILOIJD9XwpBfkPIvLGIZ3PlxsV0yjOyw1abZfL2YGR6nT2CZnyG5flBMwgK5noKK9gHb2O+dnLQNBJUCdcnuWUj9yOcYnWmOBGViXk8NHtYnHPUPcIswEhMMAvPCuSw4vmOihEVwINE5+pAZAwmoHeYg41hMVDnUHNFai3JnYTTx9A+TTs168K2I7wStW9IAhmvh7Kicg4zTCbjLuuHQYFzWCogB6gVGNvcc+dyeLBecFA31peToZ733rUsAC2GPqM2gcajbcCXZo5tjD15ILWuIThzm8AIkmbQbvGHhGuczPRbhEU4LTGkAl9cKVDypI0WN6ATxBy9RTcMlpPlHzstPdhalj5+EBhOWtI7fXeANsPqTtDWKC0LQrChx3VCtOGg4w1D2oJS2+9T/bw7cphHz2lTwBoZL/dk9sfyEB6uIaZSlenP7w1jeRrT576MNzL1SZax+hyFV/17Ne6sidQRnNU+7As9GE6MM4fy5I6uT8og4/uqKB3pJyh3+fLbbRB3pHwodF9+q9lxdeCN3MN3xUAncBpwTtg80Sn3Zzb/CrRYFVF5UG6ovPCTc/bvwJ5UB5hYW8o+43vNQhFaBsU3AtGTffk5ckBkmFaCj9+pPkTyIYWDGvr9WKQCrhRnCFay69vhd9Ooz0GudvrxTyOBs5sonhAHniqe5e54Izb2xdan2pm0MjURQMamr3/PA/soCJsg5zANzI/UwRNq39GEA73sm8oQcl2O+gxSrFSWtIc52RcjZ8ZHt9cv9OCtPoL5bi6ijs1tp8d/++qJPdZ2dJJRVrTd1qNC/hWBD3VH4rdNfQ5IfWvxfcPU/qGZA==
```

---

## Arquivo: `./.git/objects/98/384aacd5bc4df883d3924f5e03b6214ff782d9`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGdVttu1DAQ5Xm/whJCvWiTJmm7bZcXEA/AGyrwAXY8SQyOHTnObgvqvzO+JNndQqm6VauNx56cy8y4TGpGiiJfvVobrS35vSD4SZLOiJaa+6TUUps1eV1crs6BvT2INnoDLprzC+DXY7QfyhL6fjqbr+j5BR2jnKoazBTkZbEqVmNwS40Sqp6jN1dX2RRlc6C6rmhVjsdKanjCakRS+c+4buHOTrlyKG7OJwpMG74Do2T8EvK3i4fF4jSKwPRd0otfCGdN4m5cCqlRm1qoNcnCY0c59/vic6WVTSraCnm/JkdfodZAvn8+WpJbzbTVS/IJ5AasKOmSvDeCyiXpqeqTHoyoPAim+f2Ig5Y/a6MHxUcqG2qOE+Qbnk8ChuhUiM3EY5SLvpMU0VQSIgf3LeHCQGmFRi6YYGhV5CdU0oCoG7smeZZtGg+qAYqa/QdW9CK+dxLOWt1iru6O9FoKTiKHHRfiiUnL3EBLCvwTIP2FwY+ht6JyRaosKITad7SEhIHdAkQmVIpaJcJC2yNF3AUm5PP2NpTrLdrogZ0jOFMzepwt/U+aXSImrIjIu8kjdW8vlgYgobS4nCDuWbDXQSFP6oBSoSYNW3qXbAW3DSYqsqyLzoxLWfYm2hHLzalB6GB1WJ6kQvwTCGcrpvPAU2fGC/x6llHRWkO5GFDb6xH9hCpPZ2n21b5ApVf4m7h6eCy5G0GhwxJsl1A4MZdzo4iMDrfMErj2G/2ZMezZs9chmLXSpo15/1JpT/VKTTvUy78c80jKQO7WyTa20SrbHQ4BXZbejOeE6gaLYwAk9mM8PymZpVczjaD7SyxCyUPh7BbwpNpe1SETNqD0aklSZlUExP4xig5r3RkY1d422HuH5RroYPM8ZqW0itsP6utp8J7RI6nLwfTu+uq0mBvfO8+h1IaGwTe/0of8xNifFVNFCCWxfRMmdfkzkLIGB7cIiQ7lIVla9GGcey3X/r4Miobvz9TVnwsz5OyU3ELfaXzpRnCcx+QjXuFUko4aSj6AHCQ1S/KNMgmWAPnygZyeLd61wAUlxzsD52qFHXsSAexNdufeVHrzYHHLT/WBi/teyHZsdYv/UvXB/zfxaCi6I+P96u+AeeA94DT+A92vmdU=
```

---

## Arquivo: `./.git/objects/d0/0ead033e24858583ccc679b7579cb9f01a37be`

```text
x]SkA٤l>eVR
/TKM/4$[#LiA{У=VZ^zS#xM+>޼~ov6/XZDrXlo}N_bm WP\V2-}('E2*iT×4JpFIRHגVR"Ȍ##;xTKj𺂲 e']Eڽr
]"kDPX.Mk;D?ְfi 56.{DP>
eB
~Ht](2'H~,	,1.$Ru)BNw[oZ6zs^-(rNXt,ϴ\.[׷<jM~2ѵ	Y?k	rI\@ia\σ_:7ۃ
IVH^RE<*B2^lfyH+(,
`?ó96$Ol0/яا^k_a}Aq
R1]L%bp&`r[LQى~!PxIThf8zMB6gckGM}}PϹɽǇy_S'NXy;O?M//9Yq
```

---

## Arquivo: `./.git/objects/d0/dc988e624f44b58caac590c22c30e5a98348d3`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAG1lUtu2zAQhrvOKVgWAVqgsmzUaR6WDDROsq0bpIsuR+TEJkKRCknbdYocJqueoCfwxToUoyZBC3hTayGJr/n/4eNjpW3FBofD/qvi9dnnydW36Tmbh1qP94r4YRrMrORNyE4veaxDkOM9Rk9RYwAm5uA8hpJ/vbrIjqjHU5OBGku+VLhqrAucCWsCGuq6UjLMS4lLJTBrC++ZMioo0JkXoLEc9PpdqKCCxvGPfVZpK25YW2T79xNwcvPQKMumzlIrGpk67N8XeRqTrGhlbphDXXIf1hr9HJG8zB1elzz3AYISufCefqm1R38xyzylWVRWrh9TijXoUqHNcT4YvzDBMjYFZVAzadk5Ra5Qo1A1pWwp4ODZUANL1uqVXCrfaFifsGuN30dsBs0J6/cOHNajtipbuVgV36PHKYnq8SmgSwNkrUxO83utZgsHwqKn6dbgfcmrYHgn1oCUysyiwpAU6HOUhGhlMq/uMLYct1UViJuZswsjM2G1dSfszfDw4ODjMbmYdEKbn5tf6IscnnL7l7FbJ6zcraUvl2wSNbZ6EbRvgLbNTuen25tb3TQolbQ7XaxpkthqxeFM+eB2a+ayE9lqBwxo5XGXy/TJbB6ixlYv8Swsml1aOW0V/jbiGzD//yAfD+FDdTRitgGhArGn3zscMbFwPp5zY0MGWtsVyhFPvC35BRLoiWtEckLt7QIIanx8hlot0a3Z2/OaVQ6X+K7Io+cnHhQ5wS4VE1UjQxOZpVp2ucWrIbLTPUPcH+Q/3hsE/ZecT1FyChOJnVBNGu3d9Rv/1yCL
```

---

## Arquivo: `./.git/objects/7d/8245515ce2d9b927289d967e90e25857215082`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVTA0MLRgMDQwMDMxUdBLzStjMH+1IGI1UyWXL/uW6/8vHbmpWM6VZWIABArx8QWVyYnJGanx8QzXVZ2//FHZaCTSYd7Grm9h/P+wlTfUlMSc1KKSxPjc1OJEvYJKhnuP1xj0Xujr+zztUmBMxe+49Qdi3sJU5iXmZBanglRJNWSEnynfz8XEz3Lap33zN/bdwRNhqgpyMpMTi+JLivKT80FqxT4VGV3f8U/hd5jiWsOwBTLXHyrHwdUWgFRoveSdHG90aquUPFvuNEG5qqUzz7DBVJSW5OcmJifmxxel5iSW5Bdlgs1csOZjxL2buTdsK6MWuQfvk3RN7VoB1ZGUmJxdCjY2aDlrz+u9vLH3O8PdpH9uPsn0PvEgXFEexHF3WTSvZX+96Jv1MMH0Vk6xFV8S7y2oGqAnUhILIPZ9SpThmn12SW2e6759Lu0NErOvd8NcmJyfl5aZDvLGp5pFiilFAg93n/9vK/bq68vqVOHTMLPy84DhkZMaX5xZXJKaCw7p+bv4VGd4ejB0Jge6COy5NeflpJ0foMpTEksSkxIhQR1W9Tv1hm6k/upKmUdX2jeoMa0xFoAqy8wrLkgFhgnI8h0elXbecy4Jr325IFX8adODBT5vKqHKcjPTi0ARkpqXmFcCUtt7XnFmiIHQxVL98M/HJKUvd3vuOwpVW5CYnpibmlcCDmXmG6YMD88v3xWtsJmfUUfwa7Lnx8cwdakpmSn5xSDT7jEqTHwUWD3PI/FQiTTTlB915X/vQ1UVFiXnp4ATTMOuU9zG5z50Mc2OOz4hwzLjXldnN1RRUWo6MFCKIIYV7XGebsuWqfyzjXfqlRMB/zNtn8LirCi/JLE4PjElNzMPpD6xJLMsEeyAZ3Mfzd508Zqzd7fmuvKoG4ee9ARPhGSBovzSktSiYoY5f913XRWySn9hmuN9YY2JzLH9+7KAtpubmioUlebpFWcwmJ64OfFG+T/NTuXbMXP/P3ucPHejMsSM4hKgTckM3Ext1b5r/aeL2lx1c3TbrLJQeuluiAJgfBYAk2ZqMYOveqjLvVdW8306v/SFBxhKblV4dwaiprQkM6eYYa7s+Vsfl7XWxDffUWecU8bw8P/6H9BAACuIRwl9bN4CAM9UoV8=
```

---

## Arquivo: `./.git/objects/7d/d592e9abfffc042cfbd4904493479227475ab3`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGlVUlu2zAU7dqn+GBiIFnE8pCkiSwbSFu06KYN0qJ7SqQtIhKpklQGpD5FD1B005ygJ/CFeoR+ipKHxEmHeGHLlPT5/n8D40zF0Ds+3H920wZ+ZblkBkhMDe+kNs8ItGctvBNnKjmHREl8wLq1KO2P33DNZSJojmsKmIKXVLP590KoKMDbrYiJCzD2OuMjklM9FXIvVtaqPIR+t7gaknEL8BNRSDWfjEhAWS5kkGAVikUCqj+X4oIyZUhTpqCMCTkN4ai4gt4BFoGYJudTrUrJQtg67D5/dfRiiEgzpUO4TIXlQ7DY2B7jidLUCiVDkEricqw043pPUyZKE8J+BenXt68/4BPX8BZbNXCywBAFFFsKsKdxqxVNlM4h5zZVbERO33/4uID4WKdCFqUFe13gRBwoAhKnNyJS5ZxAkdGEpypDUCPyDpfcTAvErIKYx4JRAprjSDRnd+eB4xjCpWA2DfsHq7Nd3VGWecy1A8qLEel2ur1m/0LjcO4AONV8fqtg52x796/27a1xGpdItKxbNWWcC2y21kJD4vEmDrf6qMbXg4bCmkFPVbiJN0cbJKU2SHihBCpUo7JOmEiQalrxmEeBx+MIdMw5BtPBuKbYigtlUBNL/YYo4AE+bGmc8Qa2H2+v220vpIMyy2hheOgEV10NoebfqiKE3ioVVjeV1iTLeaNQmokpijPjE9t4o/KHTZsXm8k5+TcgcBeco1GZYLDFGMNXnXaiwKbeX/9Xw9P/tCreeHVbCaaEp2Z+O//JzbI0XmkPFZMG6QE0bQ5Cul+0IKaNb6F+yP+5Z4E/zOTmpirbcVaD2Qz3ZKvj+ddyZ9uAFUm705+QL05S1O442J3KSrtP3mHz6KpBuP7dx2cQTVykPRieOmgaR3nMZmRzZjFhMHyuQyEzgclYB7Pfxn9Hjxl6Tc+TyfFRt9v4t4ng2sB18i50jAnuTXI3jAcrroYVW/s41ktDr4Gszd2sLUlekxjPDH9QVWhkU1Ac6OBeXtUHTnWarIu6Rr/JilymJYrZKRoPnwsFCWXUWDx0VOchfJI5F7hTNqgSaOyOYDyZ/SmM678BIqF8Zg==
```

---

## Arquivo: `./.git/objects/78/888db6d4a470faf56a15d0e5f9d998132ad4ad`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGtVmtu20YQ7m+fYkrHSAKU1MOyYkuUgMRtggBFasS9wJK7lLYhd9ndpWPX1WGC/MgJegJfrLNLrkjKsusCkQA+9jEz37cz3zDJZQLHw9Hkh9sjYNeGCaohSIhm0doUeQBHm4MDnEpymX4Cw03OcOgdU0yknCg4J4refSm5hLDzfKGkNSdova1nI5UCvRhrOKb8CrS5ydkioFyXObmZwUpxOnfX0LACxwwLU5lXhdAzGGUKxpnCeVLOYKxYMQeS85UIOS7GBdoQZebB8gDw5y7xj2EIb6Uqqvzui8JAKcNIKdFGYdBhvdJFkuZE60WQIqTGgDUSr8fLD/JKwnv0EA/wzZl1UxmaBZIaLsUiGBBacDGw2wkSgq88xQmiAiiYWUu6CC5+u/y9Y9rZQA5ai3bE/uKcJCwHtL8IhCxYgCEUDKiEC0WMHLxhCadkFg/cuj37uSgrA+amRGoNnmsAHP07UyBIgaP1M/KbsrXMKUNPv1zP4A0x+Ie3iuM1lQWcrxmlFoRif1ZcMdr3Fg/uAbBk9hftQkrxUFdScRIsz/3j/wbTGmkQdQbuwbqQ6u7b3T9M/wQ1d/hwKRNMIKaJ/q7gSsVSGSwvFLv7JuHFx2cvnwhNVEXCkGhtWLkIhtFwVJ9abbAB2bz0AOLS4XeFQJlOFU8JwvjZPSJ3X+UTYbTp1pppgu8M9AC8FytMLI6ywDRgmjND8jXTURTtVsuebEsqY6Rocl1XScGNTStX4ahQqEW0MjIe1OvaxIwHtnzr9yaLW8H4laOSWKlotmuvGYRK/VTZQMUQ2hbtViX7+oEayTMQ0kBZB6mtKjoBaC5x6fURJVCqGRxOJ68mpwkq3Acm1lXhd0LaAEZvhAtKonhQtlitGufaSnff/D4BznJ2PQd7DSnWu1O3GUqBleBGeEdWeHeOxkaMbpBTKIELH9g9SHZdV/gTkn5aKVkJiuiy04xk6RwSqVCRUO/La9Ay5xQO04SesJGfChXKa4WCPy0x2JJQysUK17uOsO0lNZQ/Km14doNdxHUebBIlil6YMPOZMYTUayCpTUJsMPXZlBFRqHpXeOrIncR93GCPGkbTuaVUUDy/o80eJjzK9gjsSPcXryf+bDMMLNT8L4YAohqCP+4RG58d2+O+vYUyspoNmw3EiEDs2T2MTh0BPU7ZmJ1mww5Jw8g2TgRxUi92XG8JnVhCvfvJq5OT6Zl3vxVYjCEe2BiWmNCTRzBu07cDcRidOb/eR5PRUBC14iI0Ejt7HaL3u5UNwOR6fomx1yNOlZ67YDq53iXZPrc15IL4zPhqbTBxhsiJj2E0JccTMt+JYWLjDJYfnwGyHxxF4yz422oGMS/KyAnxy8ec72mNPrb9LXI7a508+F1h5GqVs4FLCCyMzWbn+8LnRc0ncokQelXv3fh7vE9BvZU2lexXmJWgfZVxWBNoa6KWmUOajqfjaadIeglomcVDrrO1lxunLin/I2Ib+b4wXhssVdVG8bouXjfS1OrjTNxrEp4jf+82DT/m7w+c9wPDNTVWLndFud/jOhS62H2rau719PY7+1/axFxK
```

---

## Arquivo: `./.git/objects/f7/e9a7bf4fa686959b260514d6749ea0833e68db`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/objects/9e/717c5c283ba4c73138860fca3fc10ff0e1dcf8`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFlj7ENwjAQRakzxWEpbSJSUKCQhgXYAJ3tI7Ewvig2UiTEMIiCHWi9GLaggvbf+//ppGUJzWq9uJZAcyCnPQiJnqohnK0Ac4QAyy0I4zTNAtDpb6Bw0jgaPmjTm4CJJesJhIDyVqQ1aVmdQLFLoyFn7dB0+3jvjcMN/LbbOl2Ldux2uRBfmkEjeIrP+OA/OgcT9ZgoxWfwF0Xec9XWY5fV6YuPPVnf4h5NTw==
```

---

## Arquivo: `./.git/objects/9e/e6f78debd2a059c1f03f692c44887784a8a495`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFdU81rE0EUn9mku9km6ZfFYluoWluNQhZLtRVEFA8mflGXNCfTZZtMkq37EWcm0PbiCoLSv8CDhx7rf+HRY6UFcaGo6KU3NYJX3+xHKz6Yt+/93ryZ935vdtX2Vk9fW7yMLg3k+xHIfrG9toUR+iacRPpio7cFho9WkI7LqIQ5LklcmhK+VE6V0jwd2qlyX0nm8hSq4TNIT+t9C3CeEK7UZEBkXTlCMjVl6UQU/VfrmVpaVxekCNP7x5CeHUP20Hy8iffruWlUyB8KvyAF6q2lsu51OaGBopOnXcJ4AQe5UuXBfZ2wjucyAv7gXctdM+cqxOnYJidsU9bMhmO5EJI7lDSt9UDlSRBAtWFRUuce3dhUNUpaFuPUA3yAxmcaddtkrC7ai1tEouQUrN45UD6qohVp8QVCDcAm0SPcxjp+DJFINAxNSIciJ1BoUjdNgy9qanrUMTkTR58NmlrD5Gak6p5ThF6d7rrWtGzCtLbnEK1uW8SFtoy6SRtmx/IMy2XcdOuWybQ1j9hG0wS/YxmO1+jaJtVoSBk76q3Y2QhyhmG6rseBIMOgQ3C3CoudBOWjPwjjKv4Z6jfno28PIijkQBhCZFghB2JcPjrud0mg/0kV6fCcqkjD83FUcLKZT/gutrlj0zxkFSSagU8wlAzweLRhPCRqlg6KPbkk3WgRTkcBEqlsEpSPvmdHP2ZnPmRntls7z96den9n92ZlL7u8m16mw7DhYSEbKDFVVNQUDiQYjqFiMn1GxX8RjCR4/HQst0UFA4Ec0RsVnUrqeIvCS6IyM9fDUZAbdAIyxKDZbVA/Uhjjz2j2AF08QMWv6sjrC/vqtC9/yk1sP9nPzfnqF6y8HH8+/ureTs4f38NXfktiML0Ukq7+Cs3wkr8s1+1x
```

---

## Arquivo: `./.git/objects/b2/2c50ab601e474e94e8839865dcbff317f8c342`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVTAxM2cwMQAChfj4gsrkxOSM1Ph4BkcOpzp3r+S9Sh+dQptmBWsfTr+oYWhgYGZiopCYl5iTWZyqV1DJ8CouJKDlwbqW3/Jy157f0Iwwv7ghEqoqKTE5u7QApCjnK0ffSz7Td/9aTuRebdl+QFChyASqKDmxKCWxIDMfpOzgx33B3kFqk3g15d/d+zxZ8YT2syswZTmZqXklYBsVC72NdMU3XQuLaTzwzVcvceGaODeYqvy8tMz00qLE5ESwgf+0Ppm+Ki2/r6uV7izW7C9j/uJRM1RpSmpOZllqUSXYeS/0NQ+fbhHcfqjV2fRRtcPEaW/joMoKEtMTc4E2g40rfcA/zanwZ8LJ5ZH5d1+cyppxu30TTF1qSmZKfjHItHrexJ06Gw5XlRnc/iE8uyuz8rKFMlRVYVF8cn4K2Bd1Ca2J9z735cpuNo7+/H7VUT/7FxehqopS0zOLS4rAVn7aOPfOyqSQTWuWlac2u7yomZRdZ4SmDGwp9+cNW1s+X3mcssmWbd+iv5s3bpvwBQAiIcRS
```

---

## Arquivo: `./.git/objects/b2/fa4fa712f8693f8a88770d132894a9371e33d3`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGNUktOw0AMZd1TWJYQK5oCqoRQkk3FEiiCPZpkXDpiPu3MpCqqehhWnIAT9GI4H4FIJNTZzbPfs/3sQrsCrqdXJ7tToG0kKwNgIQKNl9FohNP9aMShQrvyDaKKmhiaObtQr5UXh8/DFwU4h5nw8vCxUg7m3tVSVraUP/zSWa4Qa9FUqg2UWoSQYclkzEfAL11e5n116eA2RFGQplIZ5rs04bQ2f+G8AVFG5WyGiZBG2YTLtO2VjgKCobh0MsP5w9NzV6YpxR20IvWvfqmuiwBLZmidoRdPXJfH5K4xv2cEhr3cpElD60kpu6oixPcVZRjZWATFLQxUwQrDGUN8I3TFgd0O2mnG/RRQiy4EpAPB2Z8VnMF+j+BpXSlP8re3NGmmbrxrRv7XhHXFoyspJL0YCiJg/viDgCS4q8EjDLCVKci3Fgw0OwuGOK8ywwven9hmOJ1MEAam9El9U6bH2lBUMTrb7StUhVER8yehN8JD7x7TpE3uDjCpLzAfdcb2Tv8bz2UZgw==
```

---

## Arquivo: `./.git/objects/75/e00f964271f960c9a7596fdde8ca6a98db87b2`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFlUmGL1DAQ9XN/xRAQWihdTwRhoXAiFRVFqQd+EFnSdLoXaZOaTGGX4/67k6TbPbz90vDmvTdvZrYbbQdv39y8GJydYJCe5KxBT7N1BO++f2rtQuhKaPHvgp6yp7SKcJpHSdocL4rP2vyRr+8Sjj7Re0mykx4vpCPSoe+yzEVvqK998tnhoE+12Ml+0kYU2doCPdP+M8977VCRdedabDSWZLfJuOI+udg9+HE5Pu5meZQTGrLMkP5sFPQ4wIYeAtmlIfeXaUsI2j14csU+A/71HedI+fMiImpx3jpG+65K77XA2zrongs3kUfunCyCTSJWeELF683Fj+ZL8/4OmP6h/fYVWCo7HFHpmNjDz49N28Qw7PfSixLykKwsUoZgyRqurcYDkrq3Btcooa6HQLlGWDUpIld+vfodc+JJ4UzQxI+25qqYpfeRMmgjx/H5OGq0/mnLsJEVijqHtDgD262qy/+kRT9bw9r1ACUYvlUttutU9zSNPLWyhvBE9YNYmWIPm0aElTAQNwMiLpHHY4Sf/Hgssn+7PvDg
```

---

## Arquivo: `./.git/objects/75/fe95e15e9793a7c43a92502f1ff042d986b144`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAEtjkEOgjAQRV1zirEJWyAsDbLxAt7ATNsRGktLaDUY42GMC+/gthdziOwm/7/8N9J6CXVVbR450BzJ6QBCYqCij4MVYM4QYbsHYZymWQA6vQYKJ42j8SdtOhORWbKBQAjInxmvSevVBZR3PBqXrOnr9phenXG4A03W3Gi6NyWnWTO2hwVMX+1BIwRKn/Tmc6WAZRN1yK3yA4SrohB80ZRju6j467+NLT8WVUcQ
```

---

## Arquivo: `./.git/objects/c9/3e151fa98f28028a84dad978cf002580edce60`

```text
x]PMK0_1BzXo eKv;ͺSxy'oבu0`lpiH6adqI	c.b̂c{Rm57dָW}[pB7yWr;k,&%*gPtȞ><ӒDz@.p0
rq1OҲ@(DΉu(WSτ̳&̿R|=
```

---

## Arquivo: `./.git/objects/c9/b1912702ca484a5a6bf0314ecd9084f8bb8682`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFFjkEKwjAQRV33FGOgWytdSuzGC3gDmSZjGmwzoYlQEA8jLryD217MKQpu/3/899ueW6i39epWAk2Zgk2gWky06fLQK/BnyLDeg/LB0qQAg/0FBkeL0fPJeuczCkt9IlAKynsha23P5gKGg4zmJdNd3Rznh/MBdxDR4SAF60riQsfmsJDz2zJYhETza37yHwPRjeRQasMDpKuhlHijq9gsMvn99YnnA6VZR8I=
```

---

## Arquivo: `./.git/objects/f1/ce58788a8b681cf940f80825102a22a1bc4c94`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/objects/f1/d8e86884087a788b5ecd6d7ed6c5a41a619765`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAF9VFtum0AU7XdWceUoUiMZAvhFsBupaqX+VdnChbnGowBDh7HjtOpK+lFV/egKsgJvqEvoHR7GJlFBDDCPe84998zEmYrBnyyCN9+ugPaGClHBKMaK3I3JsxFcfb+44KE4U8kDGGky4q6PlMkd6Sdw4ANqcfhVSgX3WtkYhWjmni1MVMGhjY22EnIHlXnK6N0ox73zKIXZRBB6XrlfQo46lUUEHuDWqCXEmDykWm0L4SQqUzqCS2/tLwLkIaUFcYdf7qFSmRSg0xjfBrPZuHs81wuvu5mORiG3FS+YW6QShZBFGkHgzjTldtbeqTYo1KOF95kOBDNuHNvUob1xfbvT6+Xo7gL4Ok1GyKrM8CmCdUYcHzOZFo40lDNkwsmTXkKKJePXcE2mTqyMUTl3HlnYrPru/yY35+TaPPoVblDn0zIcsuwFjVq9prMx+LOQG38Mnuv3MVkHN+zEqWkdJQyshGuuqlPJrzSkz/8D3gOQwCr49+eP59UN26HRsmPa/9U9m6BzyxlcUIvYeWIdrnGdtIweSaYbE8Hc804MxYD3KAvKQBB0Bl7dbIIBXtnBHa3oThiLLcH3Wc5HcToWt1OcxCEDfSJNRSIJVAUlCSn4TWBwj5VFZzNoSrHeb7pAEAqoMhhTRonMeVS5q5uy53UiUvv5wnynZb30Fh76k873L4txvkOsiZq91O+Qurz9Dqm1Nnw8OLWrj34+9dhRt4Eapy7x3NvGTgPze435R3efqdhs81YzK5XoTho0cqegUJCr1xSqSiy6wnUE5tPFNIxfLdno7n3FwXZcD3t0JNLg4c/hmc7KgyVqSkgffqv6NMqZQ4IWnQC/bCUXycI2dWoL074GB+E/vf6t4w==
```

---

## Arquivo: `./.git/objects/22/d61d9f5227728ae1d310464b8034d4ef5f2418`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAE1jkEKwjAQRV33FGOg2xZdqcRuvIA3kCQztsE2E5oIBfEw4sI7uM3FTFG3bx7/je5Zw2q7WdxKoCmSwwBCq0BVF4degD1DhOUehHVIkwDl8AeMGlF5yye0rY0qu9QHAiGgvBd5TfdsLmDY5dE4M9mtm2N6tNapHXhCixxknWEhfXOYvfRGBlQQKL3Sk/8S5NRIrcpHwwOEq6EQuJK1b+ZQ/vnbyo0PhSVGKA==
```

---

## Arquivo: `./.git/objects/07/c275ff86300848d55dfeef29545be4ee9aa549`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGVlW1u4zYQhvs7pxhoESABIlm2k6zXsg0sFv3Xot1eYEGJI4k1RaokXTtNc5iiR9mLdUh9xHa8RSsbsk1a5LzvPDPMpc5hunicfvd8DXhwqLiFKGcWk9o1MoLrl6srmsqlLrbghJNIQ59/gU+aowXOLPyIlu4xfGKGf/2rFRp+Ntqvpnj31MkShVa0ifPrrrj4HQrJrF1HBT0cba6ArjBs3ZPEdcSFbSV7WkIp8ZDBrzvrRPkU94sswbaswDhHt0dUGTApKhULh41dQkHboMmgYaYSKs61c7pZwjR5MNhk/WZhw3q2GRUh/CDU9kjZakLTIbDwXwa1wXIdTRhvhJpQJKWodoYVGm00qMmdiqCXkLNiWxm9U5zCltos4d3j/fv7RZ5BSV7EVvyBS0iTDz4qaBnnQlV+wIcJ0y7Wj5KkMAOfd0w5wRlHoHdwfjVhvW8T8rP72vnYDiFcdgDOwok231tHObVf/9agLZAlRUhyRVtzGmA7MpA5UbDGW0uzDXhSQFH+V9YZrarN8zM0AYg/QaKqXA0vL6tJP9lPjaYRPgn8ZMk24Ve0gLZgCgVryAjDgOVGGNDg6ejQ4qISjslkNWk3V9/GpTKCZ+DvMcFACDn07u8aRWAYbJG5Gy8nLoWUd0CZbNjhZjZL28MdTEtze0tPs/YSLUR2qU1QAkL1iohmT4e/jvF9zT1lvVyUrCwyyLXhSBhM2wNYLQWHd0XOH3A6TMVkt9hRoIuWmB+JmCazQC44qtM4oP4Kea4Psa0pTXtCJyw9o+VNlbOb9C68kvTh9pj6EGs9/wYjafK+22yAZIqzD/OcFvDQQZ/lRO0aNDqkuJ6/Vsm/+bCvqT6PZHWgZzCWulBSKCpq33HeWPLoLbngIM5wUaZvin2QcVTtPjZ/rURTgTXFOhrE/Ga+eOBJTUSdxK2jvimEOnsreazwveCupnzOiZ4MahRV7cafo6xOz1kgq9ea7aI65WdPqMS5QbZdQvigtMv/JXJoV4NGsnYbBDrqikgav+SSqe2o5aQlLU4RmD08zpHaVuCPY6ENNQOtlqC0QiLjbI+xMY3KLoj9z/H158RxZ70U61gtaXLv+2eaLEJfHXKUptcU6cfQV8YD6yTSs5R0B5mv+L7G+/n+4+yc+wf4MEvR
```

---

## Arquivo: `./.git/objects/4a/017e7cf6e6dca15c2a1aeea12fd3f41cf7a3a6`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFtUUFOwzAQ5NxXrFz12AZaVUKJEwlxhQN8AG1sJ7Hi2MFOIVXVv7NOaMsBR7Kj2dHszk5pXAn77f7utAI1DsrKAKzEoDbN0BkGq/OCKqVxogXhLBGGiPFmW7y9w7OTKoDEAK8qYOAJwQsu9ReE4WhUzqQOvcFjCpVRYzbd62+PfQrxzqCOv9v7fsxYsQA61KxyHjqSA22nN8SGsRbPX/HSeal8Cg/9CMEZLWEphMigRym1ramwJ2GYaWuPUh9CCo8RG8jrGo2ubQqCPClPPBRt7d3ByhSWFcbvMtXcm7o3uyI6hdNpGm1jD53yDs5nsr6bHVy5uqsheJGzC/nTE5EBmiFntLz/hX73cFXpC47QeFXddIy27aQ0oK8ViX2UBm3LiqfSaw8vVOYJFjzpbxPxhFK5rphijluOQc54TN/KOWZCfwA2gKMU
```

---

## Arquivo: `./.git/objects/a8/1bc4ad134192ecf8ad7cb24e0cb4312f40bc24`

```text
x=M
0]c۶t)/
$?cL3P#.\)7{hOڦJ%aV!^;C*_`ld]b}D{kړiv]P;w1$kN9uoK`D̯?,⫡`TzV{G&
```

---

## Arquivo: `./.git/objects/a8/59f615ee70af67793d96d5322c40a4890f0260`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGlFE1vG0V0Ztdr79prO01TJcpHvU2UtBYoS9ugIAEVJDhKoB9msYwikpj1ehxvsHfN7FpKgyqZD0GjFuUCUo859ILEgV+ARLjkaNRIuCtV5aOX3AyJBBIceGN7kypIXBhp3rz35s37mvdevmznlYvTFy+jZ2LRMIK1fa209guH0K+M8Fegixx8CkgdrSANL6B57OJ5zuUSjOYW+PmAG2jj/IIwH3SDCbSMzyEtoAnTuPPeDS0HgBPUQkcccTmUPu2bOT41car7RpP6kRbuR+Weqe61G9YiYygp7zM6yXnSq+kFza65hHohjbxfI46bxF78ddNa0y9lSKVa1l3iACu4StxcIb8RVPVCxbQYp0pJ0Vz3JPcpMalgUmK4Nr250aN+4JRrq7dUSlZNx6W2wbzqeoZYVnjYB88BqKMsWuFe+AShAvCG0Zu4hDW8BDedpXFLkNXOUjnwn99ntBeiHZe9ALOU5CjT6vFgjPlXtGlFdx1mcdQrqgXd1TvAsCuTEHGltq4WzTJx1JJdIapRNokFweYMnRb0qmnnTMtxdcswdUdds0k5V9SBrpq5il2olXWq0nbinKMAJ6s3PTmX0y3LdiFtuRw9BbYl2M5ZAHX0B4rjFPdbG94Ptdrn106HPgAJZByFCQQrqY9hH3wBIYyiBChY8tOH/A+tclkuzRJ5Yh3d8yu4GhhCWT4tnBABUsNZfBlPda0mmFTo31JHuoSscL57XQDvhlFWWEHPDh6/qAYyfDpyTPuYryGBMtx/3y/J/pt03MeOzww0i8YDDGSwJmQCKq8Fp7vRjyEFLYm+bBAVoBiGIWsj6OobJnqRH0EmVtD/9c/X9Dxv4mRon/3HhvpW6mpqNqOYBWVOu3FNgSbS86RMDLMCFWU7ytvzKS2lsBpVXlbGnY2o3xKTJbdSpixkGgXgie2nObMArRmw9ArxQoYNRbnuJkUaZBJBo0YdG7qVrBMD+tYTi8Q1SrZFPCm1bpCqa9qWJxhl2yGUZcPr8dtYI07VthySDD5lkSvk6UBbMZgGwx4Pp8NMTUwosGgPu5R9h3MwBug5YDHVzrcA9qEsn0jxOwP1mWY0vrW4uXjnnfpcMxqrz7U4STjdFGNbsc1Yo39+d2r3/J6oNWN9W/am/SCWuM0/jsSaZwbunfoye3uuJSIpviVvyndjTTG8JW6Kd8NPIn0/RsZ/iIxvr35zY9dsLL7byJcaa1ajutFC6Bae5eC4jl/jGpFxaCA5xWghxf15GEXymUOEhehDUW7xcP7VCp7U/3n4b4dV5kcjsyLenprpRd/1XQF0pzcyo/A7I9zMGNpJYIYrPMPHRmcF/nuBB5nryYgX6g4EyiqwM3t6uyyYL+3ZaVqrlPWdJ7Lxk9fhUzrf2JkdnR/i/aR+hWgvU9XOufhSe86QK/QC8FihOa8AgGAwfowmHqHJR2joZ6n33oU9aawefCgPbb+3J1+qSz/h0GeDHw425LMPcOKQYyPngEec8nsbbVv4Bzz5d3E=
```

---

## Arquivo: `./.git/objects/50/a510b9eb7695910ec35031c50ef53f17a84450`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGtVs1O20AQ7jlPMTJFag/5bYCQmFzgAIdWiKJe0do7jlesvdbuhEApD9NTH6DqE+TFOmvnBxLIoe4qipz1zjffzHyzk0ibCHrd/uDd4z7gPWEuHQSRcNhKKdMB7D81Gvwq0ia+BVKkkbeucKIcWQMS4RubCAdNOBVWzn8WysClNR4tl5XVC4jY5OyEPG4o1R3EWjh3EsRsHIwbwCtMe+Nzhp//tiouXSzdOUC4tiJ3Yv5r/gdd2OajlU0Bjh40ngSZsBOVNyNDZLIhdFsHFrMRxEYbO4S9w/5RfxCNgvGpyd1UEwIZT58/pkC7AGY/BUoljYPCmhidE/45N4CORIQaY5VxFKYVtotxo6TAEauEjxBQSTE26HyUPiS/whXFLS5fME+nGdhlVjH3WbLss8L35j6h2vnkrxF9/hZhmzu0iTaz5v0QxJQMR7g6V3pn2ly6xemZkpRycjqd/RFExkq0TWalReFw6HNVPo2AWBFNodUkH4LGhEaQMLGmU9/5WKd1XOZ2w1PlLUUhXzLw+36FZJc0IhHfTqyZ5pIrk3STg+R4RWdZwF5xD85oJWEvjuQBdjcjq1Cr75DSJXYhpFT5xNM8WtC8OAvblL7OqmK2y/ozOlHH/oJlz4r9dwLXhoSuA3ApJqJUbR2QryRoWiuOM0GifW7sjmwyQbtdJ0/7VVmFFBn5sG3gi8p9kxgLBCp/ozEr6VTfz8VZtcVSh921DrGHg6SzW4dyhw73Hh+BWqzopycO6Y028XxC2gXjBQklVOaf6oDBLFWETVeImBu7sNjUKsfNbvcXaTCuyHsx13NZ3iQzVJOUhnDY6azv6O6h+NQX7OrqvY8v2G/1kuAHVzET9IFa5PvgYy3niyhKyJti2Rb/A5LHA7dHLaTNWfXyzh0sLrOyDLFVPCRuMNvp8PVu8gKrprTvj2djxb/wi82224o3/SBZ91rY5ilU/azQeAj62V5tV1urvwF/AR/oTrc=
```

---

## Arquivo: `./.git/objects/92/333af78bd89a3d6430cdced833e93142edbb64`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVTAzNmIwNDAwMzFRSMxLzMksTtVLLqgsycjP0zU2NNErqExmMPLilVS4qLdC2syqrkDe8POq+c5BUC1JicnZpQUYOo5v7XnnsCVQ/XvbB6GF1x9u9v9hkAvVkZxYlJJYkJmPoefEMVVbg8krZ3vdWHlUMqt6BqdHWCNMT05mal4JpsNm3jKN+SzLb9KyZ7MFn4Xkoqm9qitgWvLz0jLTS4sSkxMxrZpzTWPpv6hdk59U870NnyzB1r3X0g+qLyU1J7MstagSw3kJvdN7zPZFZzvein1mP2/NhXjlBdOhetJTi1LzkjMTi+ILi5LzUzDd+dvl3qXdqT65qesWF5pM3/ruvHXuR6jegsT0xFyg5zAdeeOOwTu+/uWT67Yf7FByqmPWf//7NUxTakpmSn4xhhtXnV593HGXokFXzea0Isc7zZp6D2ugWgqL4rE6bfrK47GltotuznT4UJTK459x9aHvPqiWotT0zOKSIkyXvZ0wfY6JsF3pn5KS6XYHVnTImr3LRtOD6bYHfjY5jHsWvpkV9iy+ZVH5WWtW4UgAJI/2jA==
```

---

## Arquivo: `./.git/objects/8d/046d6e00cfe57c3ebce5fc5feb6a27a9d5530e`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGVjstNxTAQRVm7imkA5G+chxACCmBDBWN7DIY4jvyJRD0sEHWkMUIJLO/RPdLxJefUQVp11SsRkIsieDsrh45LnK0yk/AmkCCtVDSI00Vj0GzDSmsHQWIiJ6INznM9G2cvXLtZaKOllU4aGVHGSTIc/a1UeKEBzyUT3O3F0wNlTMuNL/kehJ2NlIYbBddccc5OeqZ1+pfEntB/jA1OeVuol1t4fB+tU4M9tYGpQSgNNkzr8fM36HyuMb2Oisf38VWATrakneon+wWE+1p4
```

---

## Arquivo: `./.git/objects/8d/a345cd61ebb3ce42d31bff7045641de7cf3ef4`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVTA1NGEwMQAChfj4gsrkxOSM1Ph4hknGVt+7b8yyTTE4e+6G8UtDp7e7UwwNDMxMTBQS8xJzMotT9QoqGRb/Xu1Y7P6Q8+f7Q9MkpW0z1xx8BVOVlJicXVoAUhQd8VpzAePSWmfplcY+3/e7d/v5LoMalZxYlJJYkJkPUuaT1DT1anCx+TV3UxkxK/Od886+a4Upy8lMzSsB26hY6G2kK77pWlhM44FvvnqJC9fEucFU5eelZaaXFiUmJ4INPD51sayDr9WEVUJ+bfdav/Bpsj9ggCpNSc3JLEstqgTZK+94q1NkhWBMvLFwe8V34+e5r9tSocrSU4tS85IzE4viC4uS81PADlgnn5DffzTu9SHp1M35bxawBK/fHgFVXpCYnpgLdCjY9pkpgVeSZqRMDj+68tDsO/f8taedPQpTl5qSmZJfDLI8rJR7rnP8tZQNB5Wu9C0TPfIzJWUaVFVhUTzMzommBnEx9q6i606mbWXxeXPnxcqIC1BVRanpmcUlRWAr/3i3vvqzOjrf9duUHqujW6ftPLbyEJoysKWHVb5t7r3gejXsm+WGaPW6k08u55wFADXG08w=
```

---

## Arquivo: `./.git/objects/8d/cf2199543012d1752f57f3c6191bd38b49bec5`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGtVcFum0AQ7dlfMSWOAMm1GuVQyZEPjr1JXTm4MjitFEVoDWtnI2DdXZCiRvmYqoee+hX+sc6yEGOcY5EQywwz82bmzbBKxArOPp2fv1tLkUJMc7qiigFPt0LmsGF5GK96wDOuD51OzNaQ8o2k0nEHHcCrUjlu+RaJLINhZVfLCqmERKlW9qPyrVKVNidwTSXNcgY/CgZU4XdJkeEzZiBZQiMuMpqyLBfAnrjKWQpai0hRqQAt+Yaq0tUa4xg54oI7eytFXORC2T2wtyzmMR7vDW6N3WDpsycWFTlz1pZllW60Tl+TOXS7cCC6JNdT71Ckv5xegTcPgHyf+oEPjk9mZBzAGVwt5jcIBXGlNMc8QhU9sJT2dYpppuDbZ7IgGnLCQp3k0H42+F9sTCwuS5FmlYqpUsciXlYj5LHtQvCZeAcINRx9jWYBWUAwupwRqJ3CaDKB8Xy2vPHg2BtMvQAW5AoheWPit79QDo9dmHswwewCAuORPx5NyMVRdOJNsCCHci3rdvcyLLVhTGltmCHSlOeHzLhlkq95RAE5+bj7VREAirQNDrY0lrvfwrgrOfbaV6tqB49NP1qZ111QSbFBltqPgiUfVoXcFEzaFxVMtNEMNo7XLI8eRMaaWPkaMpFrWHt+bSXPcscaS469RPYe9q+GPIAvGBEuMSKT4GgYA2iCcPv9fgVDN7bF2oPyW1PPJ4tAd3LejqfAyUTKeqAj9HDY9OTENGZhyhRVLtyOZktsu3OqemBuF+kQLBfe1LsGHl9YvYNgjtUAbvXAaoLG97OPpsUa9P6EVUDmvlXMOxsZff8a4pgULFFsX91XR3homZrCry3ydsWbVIpw7U0nA3g27l6atDyBUV7QhP+kuIg2uHqkqPYNPvWyQhv2SFNk5xEhMcc3ubj8Ohnh8NSbCXwStBtlynNa8xKD6FXXGHuY+uAtZzNsCDgGd8+tFnCL+nU4s/z+dzSTYbnWm8NbMTRKhKpnxDSzIahm40b/THZ/cHL17yFKit3fmOIRa1pETCnxHhvSweEKyyUYhjAcghWGKeVZGFqGDfUfqfMPSc4N5g==
```

---

## Arquivo: `./.git/objects/cc/c506dc856051a3659eff2a58172efaa430f5f2`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVTAzZzAxAAKF5OJihkxLNcZ3vGfX2S2/792szmMrmidbZWhgYGZiolBcUpmTqgdSxP2vcHH1g/LVfosLlqVfu7pK4KvUIgCYFBwL
```

---

## Arquivo: `./.git/objects/44/78facbb8af323ed88fbc3c1f5a8d4dcbf50da3`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVbAwsGAwNDAwMzFRSMxLzMksTtXLKMnNYdgR9sxGzbLXaK5g1s4yrzOlbkf6OqHqkhKTs0sLIMompup/38Iv3FvlFvvmY4IHE8dS3RVwZTCzLtyZ0Zfk77K1Z9XRCYd0DJ6ubPa4DFWUnFiUkliQmQ8xrfbqpJer//9h0fl9ZYLLZPdJ6u5Rm9EUxiem5GbmQZRXdPRuu7Kk4NfXLNELT3/enCGsdWUthvKiwtLMssSU/GKIHqlv676bsiVv63iWEtPRO2/ZYsflmeh6knMyU/NKoAHx/eXy/f7L2qbOVmMVuVYyb0GzXcZtdA0pmemZJYk5EBvmFdbEaFgvOW5o0cZ/yv4g/4eHd37ANOTnpWWmlxYlJidCfbzpl/9yoR+Z9l0d5bzCGlNWmssZw4ImJTUnsyy1qBJiaum/qQ/jpk9efsRqUoC+/Aenm20bXaCmZualpFZAVO3Mff5/7gsxSUUWOYGu6Pr6C17OWVBVBYnpiblAb0EtPrlxojrTKQ+vqOwPhn5nJ7T82N3WBFeZmZcK9czHcxEVXd0ZMj8dfnCoCmgpLdzjMwWmLDUlEx6sStdk5wepF3U9vCzg5t1gcuV9vIoEqjrkiPvN+zbidznjil11i23/Xl+a0BaSrQlVXVgUn5yfAg179kOl/9sMODyuxv57rxkS/eTdrKWecHUgZdBI9WKsq/n27M7CGC2pdwv1L3+R+b54GVRdUWp6ZnFJEdTXK6SPrBV2nPTmx9qaTX48Wwz1HfaooCmEGhmwVGDn67KpE/kOBxge5ftqL77CJQAAOQxJZA==
```

---

## Arquivo: `./.git/objects/9d/1dcfdaf1a6857c5f83dc27019c7600e1ffaff8`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVTC2ZDA0MDAzMVGIj8/MyyyJj9crqGR4NvfR7E0Xrzl7d2uuK4+6cehJT/BEAIvFE9s=
```

---

## Arquivo: `./.git/objects/c2/5787c89ebf5480290bb665cf4dacf6f98810c6`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVTA0srRgMDQwMDMxUdBLzStjMH+1IGI1UyWXL/uW6/8vHbmpWM6VZWIABArx8QWVyYnJGanx8QzmJ7me/fGo35EVfq9Pq6Bzm1aY1GuoKYk5qUUlifG5qcWJegWVDPcerzHovdDX93napcCYit9x6w/EvIWpzEvMySxOBamSasgIP1O+n4uJn+W0T/vmb+y7gyfCVBXkZCYnFsWXFOUn54PUin0qMrq+45/C7zDFtYZhC2SuP1SOg6stAKnIVW79dFDq3dpcv+plBvc4Gau/HJKHqSgtyQApeTb30exNF685e3drriuPunHoSQ/CQqCSSpCazCnPnmYeV583rbG1+cem6X48sjcFEcbk5yYmJ+bHF6XmJJbkF2WCnbZgzceIezdzb9hWRi1yD94n6ZratQKqIykxObsU7Lqg5aw9r/fyxt7vDHeT/rn5JNP7xINwRXlAP6YkMex86fxLLzA5bdG8mXySpSwz+KJnXENRA3TeXRbNa9lfL/pmPUwwvZVTbMWXxHsLqgYYXimJBRA3fUqU4Zp9dkltnuu+fS7tDRKzr3ezwZTl56VlpoO8+qlmkWJKkcDD3ef/24q9+vqyOlX4NEIRMOhzUuOLM4tLUnPBkTp/F5/qDE8Phs7kQBeBPbfmvJy08wNUeUpiSWJSIiRWs3+cbnneta+0j3c339+Qy50TxX50QJVl5hUXpALDDWT5Do9KO+85l4TXvlyQKv606cECnzeVUGW5iZl5ICXc8fLcczQX+d2b/fXkr8PzxIuWpmdClRQkpifmpuaVgCOA+YYpw8Pzy3dFK2zmZ9QR/Jrs+fExTF1qSmZKfjHItHuMChMfBVbP80g8VCLNNOVHXfnf+1BVhUXJ+SngJNmw6xS38bkPXUyz445PyLDMuNfV2Q1VVJSaDgyLIohhRXucp9uyZSr/bOOdeuVEwP9M26ew6CzKL0ksjk9Myc3MA6lPLMksSwQ7AE/qg+hB8RTxquNLC4DhD3Y+Nk2QfFyUX1qSWlTM0LvY9Wzi683nnC5L/y9wTZF9ft7uC8yDICVgl+qseGDOwmbjrjdjqsPH2/dvvmmc5IGiKB45rWGzFKja3NRUoag0T684g2HVnfgejxP2d8LZvD/9K5/ItstUWAvirOISYPgkM5w5ynanNSFwceq8/1oR4nq/lhh8/QRRAEx8BcC8llrM4FLx6/SO9UZ2N/r32MhH9fqe/sq7GKKmtCQzp5hhruz5Wx+XtdbEN99RZ5xTxvDw//ofUEeDFcQTDF4APeQiug==
```

---

## Arquivo: `./.git/objects/c2/b906e4d7e888977be31f42b40f7ea5ad4b37f6`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVbAwsGAwNDAwMzFRSMxLzMksTtXLKMnNYfi7O+hwn+fVGn6GgNzjx6VYtGyW2EDVJSUmZ5cWQJRNTNX/voVfuLfKLfbNxwQPJo6luivgymBmdRy9e2Kj0aSdQWwRHbsPLfge+ofzJVRRcmJRSmJBZj7EtNqrk16u/v+HRef3lQkuk90nqbtHbUZTGJ+YkpuZB1F+j/9OpNSd1If3+Dbp+x1p3MjQkt+FobyosDSzLDElvxiiR+rbuu+mbMnbOp6lxHT0zlu22HF5Jrqe5JzM1LwSaEB8f7l8v/+ytqmz1VhFrpXMW9Bsl3EbXUNKZnpmSWIOxIZ5hTUxGtZLjhtatPGfsj/I/+HhnR8wDfl5aZnppUWJyYlQH1dNYFt66c6L7r3bYr+bV3kf+ph/2Q+qOCU1J7MstagSYmrLux7Lyum+H8p8ZHurt/6+ybXzcDFUYWZeSmoFRNXO3Of/574Qk1RkkRPoiq6vv+DlnAVVVZCYnpgL9BbU4pMbJ6oznfLwisr+YOh3dkLLj91tTXCVmXmpUM/Y3dt14N/EXX+l++e3ZG2fpfv9xY1SmLLUlEx4sCpdk50fpF7U9fCygJt3g8mV9/EqEqjqkCPuSpb30rmfX0/1nqZucE+puD3At2YHVHVhUXxyfgo07NkPlf5vM+DwuBr7771mSPSTd7OWesLVgZRBI9WLsa7m27M7C2O0pN4t1L/8Reb74mVQdUWp6ZnFJUVQX6+QPrJW2HHSmx9razb58Wwx1HfYo4KmEGpkwFKBna/Lpk7kOxxgeJTvq734CpcAAAYgTQI=
```

---

## Arquivo: `./.git/objects/bf/98b844c1f085b2c2044536f72b90ab01975bf4`

```text
x}SM0_a@Su6^*E"VI&!ӱ*TL>y3y&eM
iSUmбߗk8[á4`k-XqTU]J~U|q}z.L NKI
kBɼRO$x+1xB039X>cmVJk˾AJBYxѓ$o!vH֠5Hh~}pç
;4R;XiG]]2
A_]ಽpMzU2vqبLG42yflRKtt6XB'<<HI4i;Ns[}4;ŃR_]'V'9Gmμ+9Yנ4m4|:@}:DH"^Z@*zA:;];x{@nBr_= 5'Zw0b朗ć%Ê:	WYXC
```

---

## Arquivo: `./.git/objects/bf/e22a2c3867eebb0a24edf14ae8d832a43dbace`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGVjcsNwjAQBTmnii0gIDsk/iCEqAAJqMDZrIUhZo2xqZ8caIDbaKR5DznGUKCTalUyEWA3aKPRWBr90BvRWTGOSg3o+8mhV94aIwWqxtVy4wxXqnDiSLD/MNKRogvzBjkeQGozSKWt7mEttkI0i12uCv0VNTVNrtAOUuY7FYZlJc0/gOTCk+YWzpfFT9TC6PBRExBketXwDoXfzRemP0b6
```

---

## Arquivo: `./.git/objects/fd/40315965f5e6ea5d019c59e416a45d8d44e563`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/objects/fd/bb52c38e49d57c0f00506dc7c71a042a3ca43c`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGtVm1vnEYQ7uf7FdNzrZylcK++2r3DlpJW+dYoiap8tRZ2gVWApctytuv6x1T9KfljndkFDjBx06ggIdhdntmZeeaZDVIVwPrHy+V3D6cg7ozIeQnTgJVinpgsncLp42SCU0Gqwk8QqhxXGBr0uTxAmLKyvJqGTPMplOY+FVfTjOlY5l6gjFHZDtbL4m4/vZ4AXn6yaVaFKlV6BwemZ55XaIl/3Xt28GwPA4itRfhV5BVwAa/yz3+lshQg4A0zlWYZ7kj5i2RTGykGNk7Yku4nsCvChQhd8kr5h9jBcv6TFhlu9oMoq0xBLDRLgSuIjnbQ6gFjxEpgsa4KRm+F0gijM0bbK1jsdjT3F8X1xF9gnK4nE/97z4OfMU4lLaoNHGTOFQ4oeM3yUNHML4xGPA//pADXMeWyLFJ2v4NYS763T8+IDMeMoKhVWV7uQItCMDNjlVFeJM1LyGSesbvZmnLwElaRPsPgxqzYgfN9EOdeqjrWAxZ+irWqcr6Dk/WW7j0ESnOBGVwVd1CqVHI42Ww2e/Sfc5nHOHFJ4XXLPM24rHCL3bFURGYH5+3/o1yomWPZUxYsbyJS86fNbS+Nly6NHXrAb8qw1F8QhKOJ4+N6iBdFUUsUozBSQ5Ks5uc1SX6AhweYns7X0fRPm34z05Y48w5fbgwZBmTI8gweH5Gm6479MY8uLi4GrLzYOotorjZgQW8KwSWxhcARG9z3rDzDZbEsDQZd4VfX65qOLSv/pYhtBHq0+LYKXjkR+Ogqh+rlTVMv75p66VRwh3vIXy8RMk6QKpstwYA6CB2l6tbDeiCuN+piM2pYkIomqbeSmwSZuFyetkxE4qSsKLHcm7c9GBQ+j6UyzndArMTFXcqvGN1dM85UIhg/JpPG6PKNbuz3UPqFc9THlv+ufmpijxZDX6wua1pYaXW2j0/fJM0ujhWJ4YPV2qrpWPxN8tQb59HzWO8rlhvJGRf+4lsxbH3CK61FiJrKUc/HkHBU9/dI656kwTeB4vf9heQI9jEZkVzftCpNrewYteMbLsWaBokqCzL/un+6mbfq2CZ5KJJ9tXouj7Qj3/Bnckk8plZ6wjm2Bot8WxdMoFKOtEXdID/mVqQ6rqN/L95+/luBKAsRykhi6NULq1JmhNhNcL5yO3XXPZr/Hd0gBfwfsM9DFm2xo495+2FEl637QyX+0j6ekqzxnI5IOSdejLCGJlM8loxMuSQOmNuAuklOaaR2cDXdtEepri6FeMoRet9m27aJtrRrjX4r8qTKGvm3B4oj0wUeMXLbFCBXqHD4iWeU/xYFFwEsooGXiNMvORwgJXY12O86DsMdKBHmH/CrGVA=
```

---

## Arquivo: `./.git/objects/fd/d0e0b425243c1a9e55caa328b8c4b34abc6fb6`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/objects/3e/debac0fe91bafd1b8f9f846ab79a2df7e8d875`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/objects/34/e0ed34c42fd730ed075492a6edd3de40fbd95b`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVbAwsGAwNDAwMzFRSMxLzMksTtXLKMnNYfi7O+hwn+fVGn6GgNzjx6VYtGyW2EDVJSUmZ5cWQJRNTNX/voVfuLfKLfbNxwQPJo6luivgymBmXbgzoy/J32Vrz6qjEw7pGDxd2exxGaooObEoJbEgMx9iWu3VSS9X///DovP7ygSXye6T1N2jNqMpjE9Myc3Mgyiv6OjddmVJwa+vWaIXnv68OUNY68paDOVFhaWZZYkp+cUQPVLf1n03ZUve1vEsJaajd96yxY7LM9H1JOdkpuaVQAPi+8vl+/2XtU2drcYqcq1k3oJmu4zb6BpSMtMzSxJzIDbMK6yJ0bBectzQoo3/lP1B/g8P7/yAacjPS8tMLy1KTE6E+njTL//lQj8y7bs6ynmFNaasNJczhgVNSmpOZllqUSXE1NJ/Ux/GTZ+8/IjVpAB9+Q9ON9s2ukBNzcxLSa2AqNqZ+/z/3BdikooscgJd0fX1F7ycs6CqChLTE3OB3oJafHLjRHWmUx5eUdkfDP3OTmj5sbutCa4yMy8V6hm7e7sO/Ju46690//yWrO2zdL+/uFEKU5aakgkPVqVrsvOD1Iu6Hl4WcPNuMLnyPl5FAlUdcsT95n0b8bucccWuusW2f68vTWgLydaEqi4sik/OT4GGPfuh0v9tBhweV2P/vdcMiX7ybtZST7g6kDJopHox1tV8e3ZnYYyW1LuF+pe/yHxfvAyqrig1PbO4pAjq6xXSR9YKO05682NtzSY/ni2G+g57VNAUQo0MWCqw83XZ1Il8hwMMj/J9tRdf4RIAAD1pTHQ=
```

---

## Arquivo: `./.git/objects/12/90976485dd1e9a5beea1ffcbb7d539f4f4fca3`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVTA0srRgMDQwMDMxUdBLzStjMH+1IGI1UyWXL/uW6/8vHbmpWM6VZWIABArx8QWVyYnJGanx8QzmJ7me/fGo35EVfq9Pq6Bzm1aY1GuoKYk5qUUlifG5qcWJegWVDPcerzHovdDX93napcCYit9x6w/EvIWpzEvMySxOBamSasgIP1O+n4uJn+W0T/vmb+y7gyfCVBXkZCYnFsWXFOUn54PUin0qMrq+45/C7zDFtYZhC2SuP1SOg6stAKnIVW79dFDq3dpcv+plBvc4Gau/HJKHqSgtyQApeTb30exNF685e3drriuPunHoSQ/CQqCSSpCazCnPnmYeV583rbG1+cem6X48sjcFEcbk5yYmJ+bHF6XmJJbkF2WCnbZgzceIezdzb9hWRi1yD94n6ZratQKqIykxObsU7Lqg5aw9r/fyxt7vDHeT/rn5JNP7xINwRXlAP6YkMex86fxLLzA5bdG8mXySpSwz+KJnXENRA3TeXRbNa9lfL/pmPUwwvZVTbMWXxHsLqgYYXimJBRA3fUqU4Zp9dkltnuu+fS7tDRKzr3ezwZTl56VlpoO8+qlmkWJKkcDD3ef/24q9+vqyOlX4NEIRMOhzUuOLM4tLUnPBkTp/F5/qDE8Phs7kQBeBPbfmvJy08wNUeUpiSWJSIiRWs3+cbnneta+0j3c339+Qy50TxX50QJVl5hUXpALDDWT5Do9KO+85l4TXvlyQKv606cECnzeVUGW5iZl5ICXc8fLcczQX+d2b/fXkr8PzxIuWpmdClRQkpifmpuaVgCOA+YYpw8Pzy3dFK2zmZ9QR/Jrs+fExTF1qSmZKfjHItHuMChMfBVbP80g8VCLNNOVHXfnf+1BVhUXJ+SngJNmw6xS38bkPXUyz445PyLDMuNfV2Q1VVJSaDgyLIohhRXucp9uyZSr/bOOdeuVEwP9M26ew6CzKL0ksjk9Myc3MA6lPLMksSwQ7AE/qg+hB8RTxquNLC4DhD3Y+Nk2QfFyUX1qSWlTM0LvY9Wzi683nnC5L/y9wTZF9ft7uC8yDICVgl+qseGDOwmbjrjdjqsPH2/dvvmmc5IGiKB45rWGzFKja3NRUoag0T684g2HVnfgejxP2d8LZvD/9K5/ItstUWAvirOISYPgkM5w5ynanNSFwceq8/1oR4nq/lhh8/QRRAEx8BcC8llrMYPLgrckR/esGb9lDJi17e/mew++b0RA1pSWZOcUMc2XP3/q4rLUmvvmOOuOcMoaH/9f/gDoarCCeYPACAKMdI/w=
```

---

## Arquivo: `./.git/objects/00/8da9f0f6cc24f35569d738d2e9571db12df7c2`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGVjltqAzEUQ/vtVdwNpPgZeyCUhvwX2q7g2papYTwOE0/WX9MdFAmOEAiUemt1kHbmZewAKb3IxZ9tcDkrLOwiwKqUFKPPzizFTiU24s47tkGxQGvWyYSzB2KUrC1yUZYRcjCarcmREwQf46fv9I2DPnoDXZ494R2N6/qaensj5YNT3ijn6SSNlGK289rAv0bimmuqfWMqx/YX1po5g6Y/v+jWJ9Fo7WOSarvveDy4i1/vxFIq
```

---

## Arquivo: `./.git/objects/0c/e02c718a53a34283932a4ede1ce68e15a7b779`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAG1VVtPG0cUngXfzbUhQEtVtoqq4CbiFlAbtWq12IviYNbuek0ThcYadgdYtPY4M2MKb0aKiqo89Efkqb+jUh9bqS9FGyJV6lPfUOEH9MyCV7FTWpSqI+03Z86cmTnnfDN7Njy6oc4v3L2Lbg30pxC0559v7/wUR+h3OWi3ngvhdAmEFnqMTCWPxHmvCAXGPfmee72idxKZvSJiRkTUjIoYfHEzJhJmfAyJpJkATJnKDZRJ/iE3NDKKP2AS7OVcW2SbjFPmJz1qY2+bcuGnbcwc3HBp1dnwEw1QbTHC/cjiwp15+8KhoEsC9sJ3WgdoofVAKaHU9jvUIPQ+Wo+0h+uxUEqEUpAFOVrvC3UDbclEH12saaA1BJEomZgfCdxNOFjgDcyJH2lywsBjzPnXlDl+pEGZ8AfsIMLqJrYFZfuZBFjwfZs2tub9uE3rdWILP55bqt4rlq1AMLRVPRAqZd300zBV0srlL4tmLtCWiqbFZNyQxojcgCswUP3HM9KTc7BpbVoQVmvuzWy6HuEz27RGZmzPJXVBeDXMsFvnAtdtF/OZHUo8cBLGDbdao07TwyzYTMY23dj3Y1tEACVsHE5Lw8dvAbTQcfrar+mJX9ITx/0jx8PjAb4rceyDs/54X6yVOxlCfUOtlVMwRx0EyiACAhFEAATKOIK2cNHLZJekRVcL55U1pRTtmoShiRYu9ppEl1go/2rR84oFKsHT6G5tL4Iz5GXsaq/Mo9I/zpu9cKUieBacTqkXLWvqmqWrlrZU0NX8smoULVV/kC9bZZUASRvEI7ZbAz4pV6fCVXKx66hwcfJaQS2Z+VXNfKiu6A9vd5jU4Tqoa5qZvaeZU3Ozs5lge6NSKHTaca+51WlXMfJfVPRLzJ80cV24DnZItUY45mresEJTNacva5WCpc7Ndh5iMxc7tEpqqpVf1cuWtloKbbMV09QNqxrOhGFkPglE/OMVk9ZgcKffKFld6a5CfmVcpr6sg29Z/XVCplwnoxYNiKKgA4dZrZzVcnpn1FelwCEcEmRjqlr6A6tzjwYjNlWNyirQnQUeb89fRqSNBdmikOiQzcVLSd+kgoZm84uLmc5Dd13u7hJPXSoWC7omgzyn1TIrXSFi9qTp7gK3r9kua4Wy3k1l8+erUkkc13mTa///MCmvesdN78yXK0idB+SFT6HTQFCBvSuxuElZDVcbeAsHDz8k6Q5w2abhpvHDc6q69cDWwTc7z4I/h2jyv19YInVH1oeuJf/peRqZaFAw/Nh5GfTjZI/YTUFAQWs1V/hR26OcZHrYKPw+2QQAl+VbVdkYdH7crbtB2ZmEkTThOwCy7Aw/+7iVO+of/u7Rt4+efdVaPomhaPrQODBOUGIkcYYS0eTJaKjqk6o+UL0XqtJSlQbVOyiaPFw5WHm6ehRJHRYOCk+No0ji8P7B/W8K7G04LpP2eyhngyD6g+3qPU32BMM8KMVsGKbYWxKuSRiRcF2CrJZM+v49CrY6jyrxaVBhyWfsBkzJWsXnAE56FUV5gZIv0OBL9OFvqeut+FFqTMIIwMB4K32UGmrF/4wklaGz0WllONjyL7bkNpQ=
```

---

## Arquivo: `./.git/objects/53/2b844b9bb1682d6c1a28909a27e06afac7be06`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAHFVt1vE0cQn7Uv/og/4tikDomrGMJHXdq4ChEJEjGqWiG7aoM5WqS2BOtib5wL9p3ZW1NAqmTUqvBIpEq80jfyH/SdfyARlkJPRVC1feANmkq8dubOTlLSotai6kqe3Z3Z2fntfJ0XauZCevL4sRk4Eo30A44rsLR8pw/gZ9p0h7+z2Fz2ArTgAqisAHkmWd4jPWO09xS8eUUqztpb6Mv7pM9ZKwV/PiADzrqvEMz3y/58SIbyYRnOR2QkH5XR/IAcyMdkLD8oB8dgnu0D1af61cC0x7Uq4/Px4uEulO1ZDc778Gy/GppmLhfX4WlESANvihcz7nonVSNT3dPRJEx1RHIIT7+985y7nu8vTuzmdm9wbPyVVqgnrXBPWpGetKI9aQ30pBXrSWvw5VqYcwOYg7vyb17BnIht54Qcxsge3R1DdbAbRTWeBDWRhFpsKxtG1D1JkKO773qFVofQ6msvWE0ib5h4ckTdOw6ZkScEPOOx/ac0S75bLNh+lV9qcktmmD3wgW4sa5Mf83qjpkluISt0VmpSL5/Sa9xaZbZfN3RZqixkAna4bBqLerUptLJm2oGyJipaQzdt/yVRKpsVbvsbvKJXTMv2l2s6NyS3g4JXdUsK4mmGVtMtbvsWtPLFZqMZQVjv4R33vsNL0kVhXvNOTryDQPukLmt422UuLN00rvmzlgPJ9rkzggxWdMHL0hRXcaMYWh2Po1DIZqO8M05U/lTMmyNIWnC+U7awVbRjoAI6ic0J6k+rsIkU7M+yFU1qLimb9QnJRb15JbtIPskumXWe7TzQKnW9UNINBGCUdc3KLpu8VlpEb6N7SnWz0qxpIlvXdGOicdWOdHCW+GV0kRhFeyH8WWS/Bb8ooW8KYi+uV5lQcLKDshscm2XL9IDuI7Yed8BRPQcXPDNfA1TwwSk4w5aYys6jxB1ZNg6rniekY/uFmwAihTt0oG/RFHVNWnTxfkGussOlkmYYJvqdl0qCDLyOv80EkhY8B8Zyz4h8+4UzOYAdbCh3hoLUcTy1PnS8y0VaJO4L4xwGYarTqREluxZqoLN4bWJJ1murHkGm7Vg3SVVuNUzD4uig/ShwUB9yUWO6aZWSME0pjqCInrc5hAT9GtqzETq4Hjp4p3r3y/uh2TVl1gWN0q2x5VD6irUQlMrIbVQ7dW5ZWpU3qbyxhtKdWkpXzPSfcjgtzIpmIBfTJl00LVkV/OyZD/eJYVR0CQXXhas4SLO4H8OfFUXSggfhobXkR2uhuTVlbtuvPcdcpPHWTqDFOJnZjrITV4e8SYcOEiF0ryqSgr644g0iZGBHpJzwOIQ+r+ItIluW/+O3Osb+l7eSZcvNxx//Jh/nMinb32kdgkrFbQLxDgs7kdOpdaMq8A8W2ImuALsKdm2nQwkfSQLUwhY0i4sAbf3CbGIbs0SQLqUEF9R2RJgItWJB6ScGiMSQ2F6t0bD76mbTkHbANHa0KzuqG+Vas8Kx0uhO2+fObp16q9ytPkGJ/WLKB044/ZDnxEmUUqStT5E+9TLGHsGBhzDxEI48hNQj0DZAuw/aT77IrdN3P2n7jra8j8F7I3g9eDOz8vndmfbQ1PczrWAb3n/MlBup66mb+n02/MzDWHTTC569T2n11AdM2YD4OsRvndhIHFpPHGrD4Qfg7fBmbp9cOdmG8W3O9O3cSq4N+/8d5/hGYnw9Md6GAy/TO3Z7dmW2Dft+hVF86A/h0TsX2+HJVpAekLyevJn4KvU7os4R/ijhz/2mMHaaPQtAJNU5+891n6NuzqmqPwDXcydb
```

---

## Arquivo: `./.git/objects/2a/e90d935f32cab51a1f066d96111e7aa599cc06`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGdVl9v2jAQ33M+xSl7IEg0dKu2h0qRNk2t1GnSGO17dCQG3AXbPTtt2bfZZ9kX2zlxCJQukwChxL6f73f/fMei0gt4f/Hu4xu5MZocaBstSW9gidahkRC2r3n5eXYzgbl4qIV1B6CUhDVaWWE7+FyUkkTh5kFwCGfNThZLWfUHbputa791iHViYyqGq1Wn+6tU9/j+rt1neBRMXKAqdLeQyhrhNEURGgMZBPsTJ10lsvgLUvnnt5EaZqSBHYMzmGnrViRuf3yLx82xdKNr5ZJ42tobT2DPyqR1UNM2i4N8PAGFG9beraNgPLuZwQuz98/vYJ74ExucbmRZVuIJSSTx2jnDArRbVUApltAL8xWnD6uE2qRcdtmZQIFVlSvx7MaXEfDH0bZ98YsuXWwVPqF0PbrTNG4OtVhXk9odafbFcyGMg6vmIbUCtCB69XIJoy7+I5AKWittMgZUJazRonOUdJAJjAo0zIKUCyI9CiZ7dv/pcOkBKhF7NqK0AkQUveUANHlhoxAQCOUvMEgImn3cSLXmp+aC4tLgFyJ+tgFfCZ9oDrMPsFSleE6CGYzxAXhZ0UlNVRZPsWSt03stqrNFTata0LTg2uKbo7lefCHUNi90KbKL8wvOrrdwJa3jqiu1BdK1E2SjXXqauxd200KrpVxxYArUXfW3Mh/xVpovTJMTXzVSFVVdirzFJDvAOAoZu2nu+BUHmdp0GbR8gf7BHvx4hTlIhrh7yGnshhPpIxQud+92EAxw94jTqFFh5QvqiDoIBqh7xGnUBlfcQRRX5xH5TjRAv485zQDqqvOIv5MM0O9BTmNfYPGzNse+t/sDzDvAabylqOSjoO0xcycZ4N6DnMb+QE2HOCYPggHuHnEadVFJrrZXSj0IBqh7xP+oeR7kuZ+MeQ5ZBqM836BUeT5qe1CotPpRckdWTTPz/0QwLyUfkgXymJI8h7VNhXqUpFXqu/Vo9n1+N5rAh3NurO0sCCpSqlUSc0O85B934TUP9iw+T5svr7327JBiwgOu0lhmd1TzYPkLlfYfXA==
```

---

## Arquivo: `./.git/objects/7c/43fc83a1a8a6a210b42e0ec822774aeb215617`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVTAxM2cwMQAChfj4gsrkxOSM1Ph4hnVTPgUmz2WdxzLP22KV5Ka4JxfNPQwNDMxMTBQS8xJzMotT9QoqGRb/Xu1Y7P6Q8+f7Q9MkpW0z1xx8lQJVlZSYnF1aAFIUHfFacwHj0lpn6ZXGPt/3u3f7+S6DKkpOLEpJLMjMByk7+HFfsHeQ2iReTfl39z5PVjyh/ewKTFlOZmpeCdhGxUJvI13xTdfCYhoPfPPVS1y4Js4Npio/Ly0zvbQoMTkRbODxqYtlHXytJqwS8mu71/qFT5P9AQNUaUpqTmZZalElyN6rUsK+l54dX9nOtOKnTY/E/IkfnJShygoS0xNzgTaDjRN59Wei8YkzH7+oXj6c+1Xi0CWjtXtg6lJTMlPyi0GmhZVyz3WOv5ay4aDSlb5lokd+pqRMg6oqLIpPzk8B+2L/jB0uBz+0bjrE4mr2XXvCasbp0V+gqopS0zOLS4rAVp60E5Vf2a/B1NVy62bFeQbVhrfnEtCUgS09rPJtc+8F16th3yw3RKvXnXxyOecsAPrdwH0=
```

---

## Arquivo: `./.git/objects/7c/659c4959e6042aebd3bdba66344dfae771bff0`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAF9VM1P3EYUH3u9Xpv18rmFCtriJiVi04hNIxp6qColFLogPrYGVkKBWMaeBVPv2oxnVYJ6MBISTXNIe2lz6CHX/jetQOrWEipVc8mNlEi99o3XBhKVjOQ372P8e/PevPfWHHdN/ej22G30YXuuDcHaRhubkoDQ30xIVjpmTn8EJkD3kcZNoRJHuRJP+UEm81OpkkCFiE9NpUsiFSNemMqUJCoNolXufaSlNXGMa2FReVUETUaTzjRtq3K5L3F5vmvyqqC1jfEtjZbtQ5rSh5zO0fgIVbTcVVRof87kAh/Kd8pTmtugmIQZDW81sE8LXKiUFmdnNOx7bt3HIHdM2/VN49YirnmOQbEPKnEdU91a2xGLhlWz60zjEVy1t0OZXjgmWzbBJnXJgx2paNQNx44A20kMrpuO4fsmizOOFbG7p+A7/QBIgCroPv/JHkIW6N5BX3IbnMatgKW1ihxEwz9n/4QZkgRABJDZlaouqRnUZ9BXQly0DGq0iOnWRiDoWmO7WLUd7Bc33Boumo6N6xCfbhrEMjzb1e26T426aRt+cdPFjl41QPZsveZaDccgRRLlzk9CG/EehIquG/W6SyFRuk66wDWrFb8HSID+Rb2c+IKRn7+OtlNQoyh+xrAlwRfFfxOuHaCVJC8oeUOPq3BlduK1dWbnK3w5qcILZzQ0GmMNIjiRuWCK2TOE1CUI3CsI8hsQBEDIXm6HG3Bvtq8oyd/ljoQ73yvQRVqqktKEilDkR+NsQC2kd+4tTMxMjC+q4/N3ZiYWxieGF5Zmhym8h1O4od4sqIavVg3aIEYN3trVI8sNOL00tzh8PTJHKt3Dlm25vjqpzc+qsbDjxuBRYemesd5CYf9f6u1/PGxR6xVc9Qttfqms3l1WXwPeUeKmGdmgNScUoW8aNTfMeS45916QCHvMUDQbxHehk/E2NqGnQ6mKqbnh1hPOcJwwbTqujwl7u7Az6eizXk+TdmbgrTXSCwzJM/IWEJ8V1DUVFukELuwiGEaBS6BH4huSd0HPYP3vgATomdzx6O3gbjPX8Xj54fKje8HkiYjS2f253blfe7xDYauZ63msP9QPcu9dMJ0glJ/gXyKUnuSb+f6f5n+YP8gPBbPHQtv+zO7M3lxTEPdLu6W96WfZ/O/Zod+yQ02poyn1Hiv576tNZeDJ6kk6JbedZjKKeIIyaZF0w3XmCrkwEzcvYdUSjYiwK1aNJPPIJyzOsDvRx7PMrq8TkRkkNkLWDEhgK+Ot/m9lMwUjMUrCLyjy2UqU9Gk0K/BnZAgAWAP6nwM5SXEc9ye6doSuH6GRIzTwl9z9ZPhQvhqIfygDT786VG4F8jGX2e/f7f92+uk3Qf8BN/qSh8FxmkL8x/8wLvLyH5X9iEw=
```

---

## Arquivo: `./.git/objects/83/b530df6846ceeb2dfb55707ca206efae3bd090`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGlFEtsG1XwvV3vetffJE2VKB+8SZS0FihLi1EqARUkteVAS81iGRWSWOvdjbOpvevurqUkFch8BI1alAtIPebAhTt3RLjkaNRIuCtVBVEOuRkSCSQ4MG/tdaogceFJb97MvHnzezNTqpgl4cLchUvo2Vg0hGDtXltb/5VC6BdC+CvQRY4+BaSBVpCEF1EWOzhLOVSC0NQinQ04AQ+nF5ks67AJtIwnkBSQmDncee8ElwPAYaVgj8MtB3NnfDMnp8Slum8kfghJoSFU6Ut1r52QFJ5CycghoZOUy7+WW5TMuqNZblDSbtU120liN/66bqzLF/NatVaRHc0GFlvWnKJa2mJFWa3qBuHULG1V33B55ykxXtUtTXFMa3OrX7xtV+rl98WaXJarmuGYCnGr6xoiaaFhHz0PoIEKaIW69AlCKvDG0Ft4DUt4CW46S6KWIK2dJVIQAH1IaDdodXx2A8RUkrKIVpe2HYs4uGpaVdmxicVJtyyqsiN3gGJWZyHkan1DXNUrmi2umVVNVCo6eKnZRUW2VLmmm0XdsB3ZUHTZFtdNrVJclYGu6cWqqdYrsiVaXubskwhna5tupFiUDcN0IHHFotUPxnnY9jMAGugPFMcZ6jcPfjXU9s5v6A59BBJI6cUJBCmqj2EffQExTKIEKFjy84f8L61RBSpHMnlq9e7pFVwLjKICnWNOiQAp4QJ+Aae6VhNEKvhvqZ4upsCc616r4N0YKjAr6LmRkxe1QJ7OhU9oH/M1JFCe+u/7pYj/Jhf3sZMzD+0i0QADeSwx+YBIS+xcN/opJKAlzpdlkQrVMAZZG0dX39DRS/Q40rGA/q9/vqYXaR0ng4fkP7bEt9NX0wt5QVeFjHT9mgBtJJe0iqboXuHbwjvZtJQWSJEKrwjT9las1xSza061YpGYrSgAl/PeFnUVujNgQOO4QcWEstxwkpzFEglWqVu2CQ2rbWgKtK7LrWqOsmYamsunNxSt5uim4TJKxbQ1i6TD7fM7WdLsmmnYWpJ9yiKllqxhTzGYBsMuDadNTM3MCLCsPnIZ7XlchFFgTQCP6La/BXAIhfmEj98dbsy3ovGdG9s37r7XyLSisUamTfHMmRYX24ltx5pD2f3U/rkDTmrFBnfMbfNBLHGHfhyOtc4O3+//snAn0+YQH9+JbEfuxVpcaIfb5u6FnoQHfwxP/xCe3i03U1f2N5vvyk1Fb940m7dutxH6AF+h4LiO01QzPA09FMkQmslQfx5HUeTsMcJM9CEXadNw/tVmTxv4PPS3TYrzo/EFDu+m5gfQd4OXAd0bCM8L9N44NT+F9hKY4AJN8KnJBYb+nqFB5s1k2A12h4JFirAzfwa6LJgx3gDVjbJFWs/lyAgqyfAtnY/szI/OH9F+Vr9G1gBR5WWde9mbNdpl6zzwSK3ZrwKAYDB+jGYeodlHaPRnfuD++QN+qsE+jIzu3jyIXGzwP+HgZyMfjjQjiQdYOKbI1DmiETXxu4d6Fv4BfHN4yg==
```

---

## Arquivo: `./.git/objects/83/f12fcff2b0fa78c92100b0105497d21acf3423`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFdU81PE1EQn7ct2y5t5UMiEUhQEbSadCNBwcQYjQdbv4Ib6MmyWdpXurgf9e2rAS6uiYmGv8CDB474X3j0iIHEuAlRoxduak28Om8/wDjJm535zZv3Zn7zdtlyl09dnbsEF48VegFlr9Ra3SQA34STSE9sdDfR8GEJNFKBMuGkLHFpXPhSJVVO83Ropyo9ZZnL41Ajp0FLaz2zeJ4QnqnJiMha5hDJ1jLzx6Pov1rL1tKaMitFmNY7DFpuGKz+mXgT79XyE1AsHAi/KAXKzfmK5nY4ZUFGo0861ONFEuTLC/fvadRru45H0e+7YzqrxvQCtduWwam3IatGwzYdDMltRpvmWqDwJIig0jAZrXOXrW8oaoNa5lPK1hE/xuIz9bpleF5dtBe3CKLkFK7uWVQ+VGFJmnsB0EBsDB6SFtHII4xEohJsQjoQOUGGJXWzNPqipqbLbIN74ugzQVNtGNyIVN21S9ir3VlTm6ZFPbXl2lStWyZ1sC29brCG0TZd3XQ8bjh10/DUVZdaetNAv23qttvoWAZTWUiZd9hbqb0e5HXdcByXI0G6zvrxbgWXdwKVD3+AkCr5Geo356JvFyMQciAMITKukAMxLh+O+p0X6H9SBQ2fUxVUMhNHBScbhYTvUovbFitgVlFiWfwE/ckAj0YbxkOiplif2JNP0vUVytkQQiLVG0Plw/fc0Mfc5Ifc5NbK9rN3J9/f3rmxsJtb3EkvsgHc8KCYCzIxVUzUFA4kGIihUjJ9j4n/IhhM8PjpmM4KEwwEckRvVHQqqeMthJdEZWavhaOg19koZohBe7dQ/UgRQj7D1D5c2IfSV2Xw9fk9ZcKXP+VHtx7v5ad95QvJvBx5PvLq7nbeH9kll39LYjDdFEhXfoVmeMlf4V3tRQ==
```

---

## Arquivo: `./.git/objects/ce/e02a8a82e4acfbc41281be462954046f2e7cbc`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGFFV1v01b0+iNO3DhNSAsdZaLZCmWlEBNUKIwBAkSXQNtlplhCpLVc+7Z1SWzn2kGlmqZUQgLEA3nZxMMe8sj+wR73uMegVjSzhsY0pAntBVa0ve5ex24rtmlH8r3n655zz8c9nitbc5nc6VM5MNKd6AIY1rOLS7tZAH4lRAiRANn8GiN1MAskqgDylEvlaZceIDRdYPKsy/o4U4jkOZfzcbYQzcfc2ACYoT4AUkTixqiOLZef4TAnKsW2OF0zfLEvdLm9S/wMK3WN0R2OFO8DktAHyqnRQMUVpMQgGO5+Rehh2uMvFAuSVXMh8qISrNag4w5TnpCfnpyQoGNbpgMxnbximEvq8WlYscuqCx3M4hagq+hzK5yo6hXDJBwbwXlj2ePdHWq8biCouRa6sxITq0izdP90NwqMK1pZdRyNxBnECsjdGfxtHsBLHchglj51FwAd894Hn1OLlESVsKQDIoWjoV+RM14UhQEgFtPkSvMWqqiuQ0x/6EFRV121s2hWJYuDrtSWxXmjDB1x0apAUSsb0MTxKZqKdNU2LMUwHVc1NUN1xCULlpV5FdO2oVQsvVZWkYj83Dk4NIXElrXveIKiqKZpuThRioJ2YdekV5w9eKmDv8BuClJv/PWbsc6+iSXATwFBCJADfgre4pvXQSlMDQjLaFMyVSQa78CWnJbpYtiIO3QkMBrYGgBYI7pDFKBbFhgs5/9bjs9T/yNnDgXH9b2kdDIjUUf6ty1uSXG0/5ROUrMRmy3FQ30ZFIUQ397DaIrJbV6ISXQotSNZYHMlUgofZimZnaWOhCTeR4MHkwLjBwCwo3JEABIjRwVwnLFjMlfs2aEcoBIrR6WIHJM4KSrHsCYtMqHHAXB1CAAe7Ael3vDkvz1XGUgxicdrl8yJ9GhQUdzS8ZXctcsTly9NZ6o11XQNXdWhUoGO6mTGpc8mM5plzhsLNaRqqpWZKEwWpjM5L/WurkeJ+IGSY6LHmbUKRJbH1FDZo6to5dyi69rOx6KI+zlbRQ5EtyHK4och3s6JGoK4f49W0VHS1uJ5x1iBZ3Mnji3jb4g8o7MrQvCcs4tupYy6cZhexL/hsIBIY3mcVkOOhQcLXIYaHjFebB662qJlQi+ilS0HeozjIi82pzpQIbfiEKYN24sg1VyAHqfaNjR1RLrQS4XDZ2ss8R2ftD6HSFdhd35OvLiL3165kyw0gCUItx/wKMPjy4Z5qyMgNocyAaAUUUgsQKQiJYgKDWMe0XJ+x0sdvOSTD9+rX2wnko9uPLjx8GZ9vM123ZtanWr1jK+zn7YTPY+UB8paYn9HMLE6cXeqzXL38qv5u1d+O3byu5Oti9MbZ66vn7neGGrtHXmWPtK6WapffZlMN8Y2egaf9gyuJQ9sJEeeJkeeXFpLHqvnXwjd9cs/JdKNXONW88JX1rPE0H2q3TfQWGpyzWpTa/Uevs+3Y4lHwgOhLfQ21Lawq3G6LaRavVLrWqklzbTSs6+j7J6uPwHLx99EQPehtykg7N6IH3waP9hcePLl9/wPY63pm62ZudZ5bS2ut1gdpXG8U8MJLxrMOkS60p+o3q6AlQ3Ht4PIkPHSIT8Y/Ya5gDgiiJFWIfUNOqIzLjsVZfAfxM/yt8D32alC7BN/tMJzKIcNkGHljOPlNUNR1M9g6Dk4/Bxkn4N9v/Dpxx+t84N17kdhX/PWunC8zr+govf6V/vvX2l+Ue9fo0bf0mTYbjKAPvGHj/p+/gajOc/p
```

---

## Arquivo: `./.git/objects/d5/1a134dd2e6c7a98702a8f93c8c189f91f04223`

```text
x]OK@=@HAX*
z/fR?g'b~ڰ۫^'рq1CFŷKYMb	S6O|+etj6~zcNQ~cH؛%sR̘1Q?@:*yyG:
reRtCn~4-)Fy :(̫_ٱ9J
`
```

---

## Arquivo: `./.git/objects/14/eafc9133c8ccf1f425d3c36df518c2d232adbc`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFdkE9LxDAQxT3nUww5tVC6oAexEFhvKgpS9r5kt9Maaf44mYIifnfjtqmrOQ7v/d7LO4z+AFc31xc9eQu9jqyDAWODJ4bb5/vWT4xUQYtvE0YW57KaMAbvIsZsuNs9PbbL8a+U0YZRs3FD1j4Y96ovd/MdoxB0igL1G1sEwt68K7nRnTVOlmLBpEQF/wBFZwiP7OlDyVWWLGI7g+sBuZCboAdt0bGXFeT+++OoY1Tn7UvRYQ+reP9jpnmDJo9RNgLSI+SJHKyZdf5TXiIbK5ArsH5hO6YKn3KhyiaBTht/leIbPZCSBg==
```

---

## Arquivo: `./.git/objects/35/c8d991d877fe298923db5c9dffe6e3639db123`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFLyslPUrAwYFBW1E/KzNNPSizO4EpNzshXUPLMy0zOTMxLyVdIVHAM8FQAMpwTi1IOLyzIzFcIKMpXyMtXCEktyi2t0NPTU+IqqCzJyM8zVkgsKNArqOQCAOL0HM4=
```

---

## Arquivo: `./.git/objects/ee/778e2241f8a9976477c0134ed7d1e2905bc109`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/objects/93/a354ef94a979ffa472b6e614aa5ce9af85073c`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/objects/d4/6a4ba59df3eb954b962730de227387504d7cb8`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGdV1tu4zYU7XdWcaE0mASIZD2sxLEVA4N8T5vOzP+AEilbHUkUJCqPmXoVXUBRFCjQj64iG+oSekmKsuRHpqiDKLFE3uc5h1dxzmMIrmfhd1/PgD0JVtIGrJg0zFmLIrfgbHNygo/inCefQWQiZ3jrntGM8gYogTv+JSvXBGy4IzV9+b3KONzXXForqd41MpHwEp0IaTei2QM04jlnt1ZBnuzHjIr1HDzXdaunBRSkXmXlHFwgreALiEnyeVXztqR2wnNez+HUTb1rn+AjXlOGN7zqCRqeZxTqVUzO/TC8NL+u484uzEq7JjRrG9xwJT1VhNKsXM3Br1kh1zzZzZpQ/iidexgM+CFebHlRht1L9eNMLxbW8gTwE619k0qKGdpN9oWheccPlUkTcDpLSZosQK15ZNlqLeZw5bomWzvmQvAC/TqB3Ggt//nt1z/hnmQly4EyMJU/N3WfwAeSv/zBL6LJ2u9iqUwouoS9Uc8ZR3MzJUE866LREbvOTK/RJd1ufbWyV1jZrojbHTr+twkvKlKuGbACBCsqDjUjOSB6qg5F8nv2BevdABE1eXj5C5GFX356DwmnTMKsgYI1pHGiSbWU5f5vH9UZdUE4ZimUXPROEX/GSNTXy7Tpano9ncU7hbnRCf3AynVbdHYwl1XWYNCUo3UoeIHY5ipM45fljaTM1tsA9TRrqpw8zyHNGeJQXm2a1SwRGUfkYzhtUS5gRSrEknbf25HRY1opr6GCrDyUmFwyJNmWQZI71y7xAsOIb3FHdriDRM8df8SdHus7Sf3cNiJLn5GzivhzaCqSMDtm4pExTA57vyrtDKGBfEywfKzuKvFYy7zl9ZUSmBw19OW34SdaB4YLprdpHKf+dNRbz3E16Hf40pPwHYIPvn6FypEwhM0GIsyiNKYHjEf+yD6NCV7yuiD5QvZTyVbHO2t5rukMp8o2ytZmgzyWppdI5+BITj1cR34VPHsXRmge11hZW5V8DlXN7ByV5IDaTDW6dBwo0A2GIsk2gpup7JYw+zpmcgymNLi5GZXZdToKfeSC5HN4/72sqXXm+Kn1C+K4IOK8coR8ePF6ja87jepPBMSzx/ybADnbi7nreHIZSqlKbhe+U4leE61Rwg4AOUtRl83GUZJTFGtreU9WRFF9rmGhov9UmbuqeF0bj9WwQUjkBkEmjoPC02Xb80qdqn0PBUeSuI46uqzle6OlKLddbEmdoTx9wkrIliq3+22NJihLy5O9dg/low9Aq9VB4h6Vqh47A/kbtCroWmU6qw70/phWp/SoDerMHOFf824ocVr0K6cRRLQN3N7Cm3scSqTEvEFF1iPCNLwEL5zhxbvEMnohCp3phpGKY+PFzt7gYiHHnhxPmrHTmlWkJiXlvdvwBh0G7iX406s9t1cuCdPjU83uXuNWHTMqKQ9tejOZmI9+dpIyxDyS1O7eznpJMauzTTftmGYO/yrp6Eq92R53wyXHQCbXRJJCQNTJd2tNCC2yctJNCBNtdqLVSaqkhfOAWHN6a93/+OGjZWi0g1AFRrcbevpx0oxsw8jM/1HDcjx9oUR231rabW99F6474rYPwFPP82b+9QBQ3fi3X/vTIJh6Ybh3yCrk81ZI2Z7jiIHi/UoPVCF5JacHeCB5izkYxFtyWNhD5oAOOnNGJYS7bi/N5miije7rhincIc897A/77h9LVhz03q/4X/7veJnk7cvflB/0v318zP92xbf9o7Aq5ByvUBS3ONqXIJ4rCa02LjLRQ2soW/1J1svQt1GzC00kfaekhzTygLgmbd3I2aTiWTeBybcY84YSqkPvrWjVoF5HE53L4WSjiaTy/rOO/SPE6FNneEvDDy2MZubtugE8TzqL+lb/rvkv7TJhxw==
```

---

## Arquivo: `./.git/objects/95/00b6f178af45ef0481246457e30bf382e34086`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/objects/3b/ceb000dcdaffa51e56354f634b18a6594d94d6`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVTCytGAwNDAwMzFRSCwo0EsuqCzJyM/TNTY00SuoTGaYyrDtY8V61/csjSop4Y+5Pzc9dmiDKk9KzEvOx9AgeuRd60ftF8IX5T12lgifrDets3oE1ZCSWJKYlFiciqGH54FOYVfwYqfmyVp+92Se9Yku314J1ZOZV1yQWpJfhKHnE2/iXh+nuUlbBTW9fuyQ2OG9T6Ybqic3MTMPQ32wdov37I0ZujlSGhNmqT/I+nV8HxtUfVF+aUlqMYaOOyXVEyOWMG3fFaP2d/ntDZOUBO5FAQAyFXLh
```

---

## Arquivo: `./.git/objects/17/70abddc6ce3d6497cd736ab958f6534b1a0ed9`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVTC3ZDA0MDAzMVEoSi0uyM8rzixL1UsuLmY4GNo/XWNrtsYEv6g23wdzl/VaHrgAVVlcUpkDUfSuvE/J8cfK6SnlB4T9rl98NCH6ICcAe50jRQ==
```

---

## Arquivo: `./.git/objects/68/15229f858bc3785f5dede1b69e6f882fe5d289`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVbAwsGAwNDAwMzFRSMxLzMksTtXLKMnNYfi7O+hwn+fVGn6GgNzjx6VYtGyW2EDVJSUmZ5cWQJRNTNX/voVfuLfKLfbNxwQPJo6luivgymBmTV4c8n7Kysr/S4q2PRNZFfNyfSs7zKzkxKKUxILMfIhptVcnvVz9/w+Lzu8rE1wmu09Sd4/aDDUNpjA+MSU3Mw+i/B7/nUipO6kP7/Ft0vc70riRoSW/C0N5UWFpZlliSn4xRI/Ut3XfTdmSt3U8S4np6J23bLHj8kx0Pck5mal5JdCA+P5y+X7/ZW1TZ6uxilwrmbeg2S7jNrqGlMz0zJLEHIgN8wprYjSslxw3tGjjP2V/kP/Dwzs/YBry89Iy00uLEpMToT6errk5J7P1rXjo54/vpa/rnZwXzeIPVZySmpNZllpUCTH1440XGS0cVRXdcWdz664dXSKVOD0VqjAzLyW1AqJqZ+7z/3NfiEkqssgJdEXX11/wcs6CqipITE/MBXoLavHJjRPVmU55eEVlfzD0Ozuh5cfutia4ysy8VKhn7O7tOvBv4q6/0v3zW7K2z9L9/uJGKUxZakomPFiVrsnOD1Iv6np4WcDNu8Hkyvt4FQlUdcgRdyXLe+ncz6+nek9TN7inVNwe4FuzA6q6sCg+OT8FGvbsh0r/txlweFyN/fdeMyT6ybtZSz3h6kDKoJHqxVhX8+3ZnYUxWlLvFupf/iLzffEyqLqi1PTM4pIiqK9XSB9ZK+w46c2PtTWb/Hi2GOo77FFBUwg1MmCpwM7XZVMn8h0OMDzK99VefIVLAAB1X0sA
```

---

## Arquivo: `./.git/objects/89/36687ad52251b84432c284f5d0493076d343b5`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVTA0MLRgMDQwMDMxUdBLzStjMH+1IGI1UyWXL/uW6/8vHbmpWM6VZWIABArx8QWVyYnJGanx8QzW5zYw3Ln1f6lcmKl/srfEskjfKdegpiTmpBaVJMbnphYn6hVUMtx7vMag90Jf3+dplwJjKn7HrT8Q8xamMi8xJ7M4FaRKqiEj/Ez5fi4mfpbTPu2bv7HvDp4IU1WQk5mcWBRfUpSfnA9SK/apyOj6jn8Kv8MU1xqGLZC5/lA5Dq62AKRC6yXv5HijU1ul5NlypwnKVS2deYYNpqK0JD83MTkxP74oNSexJL8oE2zmgjUfI+7dzL1hWxm1yD14n6RratcKqI6kxOTsUrCxQctZe17v5Y293xnuJv1z80mm94kH4YryII67y6J5LfvrRd+shwmmt3KKrfiSeG9B1QA9kZJYALHvU6IM1+yzS2rzXPftc2lvkJh9vRvmwuT8vLTMdJA3PtUsUkwpEni4+/x/W7FXX19WpwqfhpmVnwcMj5zU+OLM4pLUXHBIz9/FpzrD04OhMznQRWDPrTkvJ+38AFWekliSmJQICeqwqt+pN3Qj9VdXyjy60r5BjWmNsQBUWWZecUEqMExAlu/wqLTznnNJeO3LBaniT5seLPB5UwlVlpuZXgSKkNS8xLwSkNre84ozQwyELpbqh38+Jil9udtz31Go2oLE9MTc1LwScCgz3zBleHh++a5ohc38jDqCX5M9Pz6GqUtNyUzJLwaZdo9RYeKjwOp5HomHSqSZpvyoK/97H6qqsCg5PwWcYBp2neI2Pvehi2l23PEJGZYZ97o6u6GKilLTgYFSBDGsaI/zdFu2TOWfbbxTr5wI+J9p+xQWZ0X5JYnF8YkpuZl5IPWJJZlliWAHPJv7aPami9ecvbs115VH3Tj0pCd4IiQLFOWXlqQWFTPUOP9pXrhi2SKBLXp8J5TKvV4rhokDbTc3NVUoKs3TK85gMD1xc+KN8n+ancq3Y+b+f/Y4ee5GZYgZxSVAm5IZuJnaqn3X+k8Xtbnq5ui2WWWh9NLdEAXA+CwAJs3UYoYMUaX5rd2HK+Jj3z7cNi+/Q//ppU6ImtKSzJxihrmy5299XNZaE998R51xThnDw//rf0ADAawgHiX0sXkLACEbojs=
```

---

## Arquivo: `./.git/objects/df/8f461ab7f766f9af05a63b80627e541ae9f074`

```text
xm ᬩb(RA6`Cbí?/Zv.xѪ-1a0fiemfERLRBS.fCF֫)'4oZexğ\i?^S|Fk]:4`u)7cI|-}`بw̰	﫝$T
```

---

## Arquivo: `./.git/objects/df/d96d7b8d5d0fea836d4a7da442f8cdc1d39193`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/objects/e5/7059e4b6d3c81512de0bbd9b28538faae4abf4`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGlFF1vG0Vw9+5s3/kzSVNS5csmUVIsUA6CIUhQPlIlcqoC5rCMCk7M+W6TXDjfmb1zmwaBzIegUYsiVULqAw95BKk/AsJLHg2JhHtSVT76krdAIoEED8zavqQKEi+stLMzs7PztTNTNu1y6omnpybRo/FYGMH6Jbe88gOH0K+M8JfQQQ4+BaSOFpCC51AWuzjLuVyS0dwcnxVcoYXzc4Fs0A0m0Tx+GCmCEpjC7fduaF4ATlAJHXHE+VDulG/m+FTETOeNIvUhJdyHzK5M59oNK5FRlI7uMTrNedJLuTnFrrmEeiGFvFsjjpvGXuKCYa2ok3lSqZqqSxxgBZeIW9LLa0FZ1SuGxThVShaNVU9yHxCTdIMSzbXp1bWE/J5j1pbel1VLNQ2HaMypjmOIJYWHffA4gDoqoAXumU8Q0oE3iF7Dy1jBRbhpL4UrQlLbS+bAfX6P0V6Itj32BGYozVGm1eMdlzL3Fm1aUV2HWRzxiKyrrtoGml2ZgIArtVV50TCJIy/bFSJrpkEsiLWkqVRXq4ZdMizHVS3NUB15xSZmaVEFumqUKrZeM1Uq01beHD++iepVL1oqqZZlu5C0Uol2g2kJtjMMoI7+QAl8Bf/Wgl9e2W+dt7U2fQASSDuKEghWUB/DPrgJEYygJCgo+tlD/ndWuQKXY3k8sY7u+QVcFQZQgc8FTogAqeACfhJnOlaTTCr0b6kjXYFC4GznWgfvBlEhsIAe6z9+URXyfC5yTPuYryGJ8tx/3xej/ptcwseOzzy0isIDFPJYCeQFmc90Yh9FKVQUfckg0qESBiFnQ+jiBQM9yw8hA6fQ//XO1/QUb+B0cI/9xpr8+szFmfP5lKGnZpVXX05BA6llYhLNqEA52U7qjeyMMpNiBZo6lxpz1qKddphYdismZfHSGABPbL0sGXpapEHGCGo16tjQl2SVaNChnrhIXG3ZtognzaxqpOoatuUFNNN2CGWxe11+wyrEqdqWQ9LBBwxwepk+1FIMlsCOx8PpMFPj4ylYtItdRjrulaDfaRI4TLNzG8AeVOB9KXH9TH26GUtsXFq/dP2t+mwzFq/P7nNS4FRTjG/E1+ONvux2Zvvsrqg0470b9rq9E09e4+9F4s3TZ251f1G4NrsvIimxEV2P3og3xfCGuC7eCN+P9P4YGfs+Mra59NUH30jbU438m43i242y2bDcxgu1ncjlhnD5z8MYip4+RDgQuyNG93k4/9oPntT2efhvh5XcR0PnQ3gzM92Nvu09B+hWd2Q6yW8NctMjaGsYMzzJM3xk5LzAfyfwIPNKOuKFOo1OWXG1Z0pPhwVzozUSDWuJsobyRDZWyir8QPvP2jOh/R28n8KvEe1hqloJFp9rzQ/yPB0HHqsh50UAEAzG99D4XTRxFw38LPXcemRXGq0H70QHNt/ZjU7WpZ9w6LP+D/sb0aEdPHzIsVlywCMu+XsLbVn4B1CIbbs=
```

---

## Arquivo: `./.git/objects/51/8cc3bb8f07a65ee17760e950b5754d9370581b`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGlFF1v21T0Xjt27Hx2XadW/Vi8Vu0WgeoxOhUJmFijVil0ELwo00Tb4NhO486xg+1IWSek8CFYtaG+gLQHHvqKxAO/AIny0segVSKzmAZiL30LtBJI8MC5cdxOReKFK91zzzn33PN1zzklwyoJL8xevIyeS8QjCNb2tcr6TxRCvxIiWKEecvAJIE20iiS8iLLYxVnKpVKEphbpbMgNdXF6kcmyLptCK/gckkISM4v99254JQQcVgofcbiVcO50YOb4lLiZ3huJH0RSZBAZfTO9azciRSdQOrZP6DTl8Vdzi5JVdzXbC0vae3XNcdPYS76um+vypbxWrRmyqznAYtc0t6iWNlhRVqu6STg1WyvrDY93nxHjVd3WFNeyb28kxDuOUV97XyzJyq16TSE+9fxCJCc07IOLAJqogFaplz5GSAXeKHobV7CEl+HGXxK1DDn1l0iB9/Q+ob2w7TvshYidNGUTrR7tuDbxrmzZVdl1iMVxTxVV2ZV9oFjVaYi3Wm+IZd3QHLFiVTVRMXTNhFCLimyrck23irrpuLKp6LIjrluaUSzLQNf0YtVS64Zsi3Y3bU4vvOnabS9WLMqmabmQsmLRPgWWedjOWQBN9AdK4gz1Wxd+udbpnl9f9+kDkEDKUZBAkHL6CPbB5xDAOEqBguUgeSj4zBpVoHIkjSfW0T29imuhEVSgc8wJESAlXMAv4pme1RSRCv9b6kgXU2DO965V8G4UFZhV9Pzw8YtaKE/nosd0gAUaUihP/ff9cix4k0sG2PGZh0aRaIChPJaYfEikJXa2F/0EEtAyF8iySIVSGIWsjaGlN3T0Mj2GdCyg/+tfoOkyreN0eJ/8x4Z4fX5pPpMXdFVYkN66JkADySXN0BS9CvVkOcKN7Lw0L5AKFV4VJp2NqN8O0xW3atgkYDsOwOO6D4u6Ck0ZMuWq5oUVCwqy4aY5myUSrFK3HQv6VGtoCnSsx5U1V6lYpubx8w1Fq7m6ZXqMYliOZpNceH1BA0uaU7NMR0uzz1ik1JI91FUMpsGwR8PpEFNTUwIsu49cRnx3i9D+9jlgEMXOtwD2oSSf8sl7Q825djy5dXPz5r13mgvteKK50KF45nSbS2wlNhOtwezuzO75PU5qJwa2rE3rYSJ1l34STbTPDD049UXh7kKHQ3xyK7YZu59oc5EtbpO7H3kaHfgxOvlDdHJ77Ztru4utG6utd8utitEyGx2E7uCrFBxLeI5qRSeheWIZQjMZ6s/DOIqdOUSYiT/iYh0azr867En9n0X+dkhVfjiW4fD2zFw/+m7gCqA7/dE5gd4Zo+Ym0E4KE1ygCT4xnmHo7xkaZN5MR71wbxTYpPr8qdPfY8Fk6c5M3VyzSc95HBk8JRm+xP9Ef2r4/0MHSf0K2f1EVTfj3CvdCaNdsS8AjxSZ8xoACAbjJ2jqMZp+jEZ+4fsfXNjjJ5rso9jI9q292KUm/zMOfzr8wXArNvoQjx1SZNwc0Ig6+3sX7Vr4B56Gc2g=
```

---

## Arquivo: `./.git/objects/bc/a013aaee9bb6cec33e68481ddcfb2bdab2609a`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/objects/19/61b5e9a334036f05dcc1401d58dec2e38502d5`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGlFE1vG0V0Ztdrr+21naapEuWj3jZKWguUpW1QkIAKEhwl0A+zWEYRScx6dxxvsHfN7BolQZXMh6BRi3IBqcccuCBx4BcgES45GjUS7kpV+eglN0MigQQH3tjepAoSF0aaN++9efO+5r1XKNsF+dLUpSvoqXgsgmBtXy+t/sIh9Csj/BXoIgefAFJHy0jF82gOu3iOc7kko7l5fi7gBto4Py/MBd1gEi3hc0gNqMIU7rx3Q0sB4ATV0BFHXAplTvtmjk9VnOy+UcP9SI30o3LPZPfajajRUZSS9hmd4rzwy5l51a65hHohlbxbI46bwl7iVdNa1S5nSaVa1lziACu4Qty8UdgIKppRMS3GqVJSNNe8sPuEWNgwKdFdm65v9CjvO+Xayi3FIGXzPULXdeZV1zPEssLDPngGQB3l0DL33McIGcAbRq/jElbxItx0lsotQlY7S+HAf36f0V6Idlz2AsxSiqNMq8c7LmX+FW1a0VyHWTzvFRVDc7UO0O3KBERcqa0pRbNMHKVkV4iil01iQbB5XaOGVjXtvGk5rmbppuYoqzYp54sa0FUzX7GNWlmjCm0nzjkKcKK67kn5vGZZtgtpy+fpKbAdhu2cBVBHf6AETnO/teGXoVb7/Nrp0AcggfSjMIFgJfUR7IPPIYTzKAkKFv30If9Dq1yOy7BEnlhH9/wyrgaGUI7PCCdEgFRxDl/Bk12rSSYV+rfUkS4hJ1zoXhvg3TDKCcvo6cHjF9VAls9Ej2kf8zUkUZb77/tFyX+TSfjY8ZmFZlF5gIEsVoVsQOHV4FQ3+lEko0XRlw0iA4phGLI2gq69ZqLn+RFkYhn9X/98Tc/yJk6F9tl/bChvpK+lZ7Kyaciz6s3rMjSRViBlopsVqCjbkd+cS6tpmdWo/KI85mzE/JaYKLmVMmUh0xgAT2w/zZsGtGbA0irEC+k2FOWamxJpkEkE9Rp1bOhWskZ06FtPLBJXL9kW8cLpNZ1UXdO2PEEv2w6hLBtej9/GKnGqtuWQVPAJi5xRoANtxWAaDHs8nA4zNT4uw6I97FLyHc7DGKDngMVUO98C2IeyfBxO3BmoTzdjia2FzYU7b9Vnm7F4fbbFhYXTTTG+Fd+MN/rndid3L+yJajPet2Vv2vfjydv8o2i8eWbg3qkvcrdnWyIKJ7akTeluvClGtsRN8W7kcbTvx+jYD9Gx7ZVvbu6ajYW3G4VSY9VqVDdaCN3CMxwcN/ArXCM6Bg0kpRktpLk/D2NIOnOIsBB7IEotHs6/WsGT+j+L/O2wyvxwZEbE25PTvei7vquA7vRGp2V+Z4SbHkU7ScxwmWf46PkZgf9e4EHmRirqhboDgbIK7Mye3i4L5kt7dprWCmV954ls/BQ0+JTON3ZmR+eHeD+pXyHay1S1cy6+0J4z5Cq9CDxWaM5LACAYjB+h8Ydo4iEa+jnce+/iXni0HnwgDW2/syddrod/wqFPBz8YbEhn7+PkIcdGzgGPOPn3Ntq28A+cSndF
```

---

## Arquivo: `./.git/objects/ea/5e545084e0ae84fb1f1ed6e7d8295837d1b059`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFlUl1LxDAQ9Lm/YgkILZSe3otwcKBIRUVRquCDyJG22zPSJjVJ4Q7xv7v5uDvRviTMzszOblr3qoaz+fyo02qAjhvLRwFiGJW2cPF4U6nJos6hws8JjU1+0wqLw9hzK+R6p7gV8oPPnwOOJtBbbnnNDe5Ia7Srtk4S7b1heeiTjho7sVmyGW8HIVmWxBZoiPbHPG2FxsYqvV2yPY0kyXkwLqhPymZfpp/W3zMueS8MUp2brWygxQ4itnJEHQZc7CbNwekWYKzOFgnQ19aUIWRPM480kzZKE9rWRbjHAm1qJVoqnHqe1dtg4WwCscANNrTalD2Vd+XlMxD9qnq4B5LyGntsxIDSKgMv12VV+jDkd2xYDqlLlmchg7MkDdWicYe2eVcSYxRXF52jHCJETYhIldeTN58TNw2OFkp/CCUPipEb4ymdoD32/8dpemV+t3QbiZDXabSTlrB/p2L3j1RoRiVJGx8gBxafpXi3Q0/jfrFYYgs4kNwOCPCrAOa3RvMQQle6fGfJD9ln6SI=
```

---

## Arquivo: `./.git/objects/6c/e82f29c3cb8411b7c2854335e27b409196ed5e`

```text
xeR]0b-BA^AdIH$].;I݋JÙsΜtvW/_?`>YfK@WCxLkNA/63]q#1P.yC{SGujَIVkDǼʡ֝[vxSݽa'Q?DlH!R]qZCTWG"/yCkvuP
/s6	-d7-}Q	M.!Pdu3DKPm51;kpjkU#Rǳ)'Q\3>QFe#[ƍP93pfKz5]/'lv9]4
-	x
=[l	! -X!MGP
```

---

## Arquivo: `./.git/objects/6c/f5088ee90e35eefe84c86dd584b7c011207234`

```text
xeRj0쳿bl04}(ZCZZZ@J9dy}QkK;B+wZHή܍wo_
N0HOr֠:>v!t%gAOKZE8ͣ$m''m~O^i,sK|v8C-6E@ϴ^;TdݱgKɸ><q?o:~/3?=]44g	AOf_q</"ct_&EI
x|nn/RJOhzxk&a^de2Kpm5ԣ5F	u=%ªIg̉3AmE1K#eF-FV(_:!-֮P"=MH#+kT?&pZ@
l/Eң
```

---

## Arquivo: `./.git/objects/fe/2af235ea7577df2d2a674316834f1c37e8e283`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAG9VNtq3DAQ7bO/YjCE2MU4VyhdMG1oHbJlc2Hjtg+lGNkeb1RsayPJkBD6Nf2U/lhHlu2ut0lpXrpgWI00t3POTFaJDA5eHb5+weu1kBqEckopaiiZ0mzNoTefXM2XotUoA1jibYtKB3AqZB3AWZJcxXc5rjUXzcQ3lKjWolGohihnyfli2RtNoIJLzPVgmTprrNcV07xZDd4fePONHSbWjn2dBdMsYwqHRyvUaZE5juyqhQjGyr21xJLfRe4eK2reuL7Tp6D6ItgK7tnShLyP3PEZuTgFliAyAiIlDFiGFea8xkaLlOBLVdWuvLyVShBQ5jADpaU/c4B+1h7iHeaEpOdex4v4XQK8gNPl5TlsxVPw+Sxexl0Uqm9HuQF4JmTg+104ek/2PmiJOr8RDXr2jpfQCG1C2tQmvWScYJrQ5VELulVpLgqMjvePAyhQM15FbjxtDpqfPwRgk4tGS1YIQqILibqVjUnzZZcXu18d563FPSQaPHfvwdT7fY+8Sr5qJcsFmjYGXaR5xZSKNlXhdwBbh9QEGUE0bp3wZoMCe1iLjGCwtPfdW0zIWmSh/d9fUKEpwR09h0Hb6d8IfGn5+90lEz13lG8ikS73joLF/HyewIFh1JY0cGpjPElrT3ZeCTUwbVrsj5uUjJoNh3kZpszrYQzA3aw4vNF1RQU99FZ3Bvaa3hkO6NyRSSMwcLwW6kmSJzx2DzeIbESNKYlAM9JEo7EbEmraLBQvDEM/gNuWLnjBCkxrVEzNgDdG7uOT/0X+o8S/p8lN4ufS/gjd3aYYN0KXy8yVO7+4jpcJzC+Sy54GMz2kK6OXLUkFNOpTPP+Ez4dPJ4uP8TV4OyqgXWI+3w3GhIMM/yVU52SnwohP1DXXk8EbBWlaeUKf27vfa2UVlf1qfnRvvFFtjkqJSMsWCUrCYVxdR/tHvvML6yZF9g==
```

---

## Arquivo: `./.git/objects/7f/0d61b92cb0c37a7630dbf8139b8a6979d33823`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFlUl1r3DAQ7LN/xSIo2GB8/aAUDgwtxSEpLS1uoA+lHLK0vijYkivJcEfIf+/q4+5C4heJ2ZnZ2ZWHyQzw8f2HV6M1M4zceb4oUPNirIfPP296s3q0NfT4b0Xni6e0xuO8TNwrvT8pvip9z9/dJhxdokvu+cAdnkh79Ds5FIWN3tBe+pSLxVEdWrbhclaaVUVugY5oz8xLqSwKb+yxZWcaSYpPybihPiXbPLhp3T9uFpRKGkd17o5agMQRMrYLRJsG3J4mrSHotuC8rbYF0CcHypCyl1VExGqdsYTKoUn3XKBN7ZSkwtvI8/aYLIJNIjZ4QEGrLdmv7lv35RaIftX/+A4k5QNOKNSM2hsHv6+7vothyO+1YzWUIVldpQzBkjRUy8YjenFnNOYooa7GQLlEyJoUkSp/3vyNOfEgcPHQxUMZfVEs3LlIGZXm0/RyHDEZ97Rl2EiGos6iX62G8zs1p3+kR7cYTdr8ADVoPmPL8ts0d36eaGZhtMeDbx9Y5rEtnBUsLISAuBdgcYU0HCF0pctjVfwHO9buZw==
```

---

## Arquivo: `./.git/objects/7e/608561def38e6d1db3335bf3efaac54e3fe8d1`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFlUl2L1DAU9bm/4hIQWqgdP0BhoKBIRUVR6oIPiwxpcjsbaZNOksIMy/53bz5mZnH7knDuOeeee9NhMgO8e/P22WjNDCN3ni8K1LwY6+HDzy+9WT3aGno8rOh88ZjWeJyXiXul92fFV6X/8tc3CUeX6JJ7PnCHZ9Ie/U4ORWGjN7TXPuVicVTHlm24nJVmVZFboCPaf+alVBaFN/bUsguNJMX7ZNxQn5Jt7t207h82B/tCGImOCNydtACJIxzsLoC7wLRpwu151BqCcAvO22pbAH1yoBApfFlFRKzWGUuoHJp0zwVa1U5JKryKPG9PySLYJGKDRxS025L96r51H2+A6J/6H9+BpHzACYWaUXvj4Pfnru9iGPJ77lgNZUhWVylDsCQN1bLxiF7cGY05SqirMVCuEbImRaTK7cs/MSceBS4eungoo6+KhTsXKaPSfJqejiMm4x63DBvJUNRZ9KvVcHmo5vyT9OgWo0mbH6AGzWdsWX6b5s7PE80sjPZ49O09yzy2hYuChYUQEPcCLK6QhiOErnR5qIp/5tHuiA==
```

---

## Arquivo: `./.git/objects/1e/16eb1f7dbc0485b7904b81454272b252fa2f62`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGVj8tNBDEQRDk7ik5gkcdju70SQpAAFyLwpw1G4+mRx96EOBABEWxiOAWOVXpPqopca+mg0D70RgTRBn31MuEapTOZgl21sxqTscFFdA51XqRBcfhGe4cUTA7o8+LVik6ZRTq7OBmC1VLHaKYcNRIKP/onN3inAW9cCZ5uHOmFqi/bY+T6DAs6o5TW5goXuUopZjundfqXJF6/xtkJjsa5nGfh3W9AsJV6MCSGSvuANH/ynsvHaP7+c/+lcyKRW6OZvic3k5/CKf4Avx1bHQ==
```

---

## Arquivo: `./.git/objects/1e/ef69da3d061046bba67a3c18b377c468c7cee2`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/objects/d7/2543f4fc24b13214883786072f3833ffc33a4b`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVTCytGAwNDAwMzFRSCwo0EsuqCzJyM/TNTY00SuoTGYQ2xtb+iY5aopa6q1f1ucU5p/KMG+BKk9KzEvOx9AgeuRd60ftF8IX5T12lgifrDets3oE1ZCSWJKYlFiciqGH54FOYVfwYqfmyVp+92Se9Yku314J1ZOZV1yQWpJfhKHnE2/iXh+nuUlbBTW9fuyQ2OG9T6Ybqic3MTMPQ32wdov37I0ZujlSGhNmqT/I+nV8HxtUfVF+aUlqMYaOOyXVEyOWMG3fFaP2d/ntDZOUBO5FAQAgInLQ
```

---

## Arquivo: `./.git/objects/41/08427e474a63bd22f14255829a532bc367d128`

```text
x+)JMU036b040031QHK,NK.,564+LfxZdB_d=w/{X2`kiĢĂ|=oVj]'d`:lUfo;w.Co[fe%&'bZ02Ws"-uy՗YZT<ĭ/09 qVP=EyəEE)rTuMo}w:#ToAbzb.sljp?kߡ5ޯ0)5%3%Íwh<EiɀWBcuڟeҺJqm	]j)JM,.)tيo
֧WNj㰤)M0YfVسEgY#
```

---

## Arquivo: `./.git/objects/6f/0599094ec87af093d75835083f5a0f0e033c9b`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVbAwsGAwNDAwMzFRSMxLzMksTtXLKMnNYfi7O+hwn+fVGn6GgNzjx6VYtGyW2EDVJSUmZ5cWQJRNTNX/voVfuLfKLfbNxwQPJo6luivgymBmyb3PvGXLJuC2e1mVjcTm8iMZx889gipKTixKSSzIzIeYVnt10svV//+w6Py+MsFlsvskdfeozWgK4xNTcjPzIMrv8d+JlLqT+vAe3yZ9vyONGxla8rswlBcVlmaWJabkF0P0SH1b992ULXlbx7OUmI7eecsWOy7PRNeTnJOZmlcCDYjvL5fv91/WNnW2GqvItZJ5C5rtMm6ja0jJTM8sScyB2DCvsCZGw3rJcUOLNv5T9gf5Pzy88wOmIT8vLTO9tCgxORHq4+mam3MyW9+Kh37++F76ut7JedEs/lDFKak5mWWpRZUQUz/eeJHRwlFV0R13Nrfu2tElUonTU6EKM/NSUisgqnbmPv8/94WYpCKLnEBXdH39BS/nLKiqgsT0xFygt6AWn9w4UZ3plIdXVPYHQ7+zE1p+7G5rgqvMzEuFesbu3q4D/ybu+ivdP78la/ss3e8vbpTClKWmZMKDVema7Pwg9aKuh5cF3LwbTK68j1eRQFWHHHFXsryXzv38eqr3NHWDe0rF7QG+NTugqguL4pPzU6Bhz36o9H+bAYfH1dh/7zVDop+8m7XUE64OpAwaqV6MdTXfnt1ZGKMl9W6h/uUvMt8XL4OqK0pNzywuKYL6eoX0kbXCjpPe/Fhbs8mPZ4uhvsMeFTSFUCMDlgrsfF02dSLf4QDDo3xf7cVXuAQAAGB4SYs=
```

---

## Arquivo: `./.git/objects/49/6623f818805d8429ab6d9e3e2d764a7dbc68c6`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVTA0MLRgMDQwMDMxUdBLzStjMH+1IGI1UyWXL/uW6/8vHbmpWM6VZWIABArx8QWVyYnJGanx8QzXVZ2//FHZaCTSYd7Grm9h/P+wlTfUlMSc1KKSxPjc1OJEvYJKhnuP1xj0Xujr+zztUmBMxe+49Qdi3sJU5iXmZBanglRJNWSEnynfz8XEz3Lap33zN/bdwRNhqgpyMpMTi+JLivKT80FqxT4VGV3f8U/hd5jiWsOwBTLXHyrHwdUWgFRoveSdHG90aquUPFvuNEG5qqUzz7DBVJSW5OcmJifmxxel5iSW5Bdlgs1csOZjxL2buTdsK6MWuQfvk3RN7VoB1ZGUmJxdCjY2aDlrz+u9vLH3O8PdpH9uPsn0PvEgXFEexHF3WTSvZX+96Jv1MMH0Vk6xFV8S7y2oGqAnUhILIPZ9SpThmn12SW2e6759Lu0NErOvd8NcmJyfl5aZDvLGp5pFiilFAg93n/9vK/bq68vqVOHTMLPy84DhkZMaX5xZXJKaCw7p+bv4VGd4ejB0Jge6COy5NeflpJ0foMpTEksSkxIhQR1W9Tv1hm6k/upKmUdX2jeoMa0xFoAqy8wrLkgFhgnI8h0elXbecy4Jr325IFX8adODBT5vKqHKcjPTi0ARkpqXmFcCUtt7XnFmiIHQxVL98M/HJKUvd3vuOwpVW5CYnpibmlcCDmXmG6YMD88v3xWtsJmfUUfwa7Lnx8cwdakpmSn5xSDT7jEqTHwUWD3PI/FQiTTTlB915X/vQ1UVFiXnp4ATTMOuU9zG5z50Mc2OOz4hwzLjXldnN1RRUWo6MFCKIIYV7XGebsuWqfyzjXfqlRMB/zNtn8LirCi/JLE4PjElNzMPpD6xJLMsEeyAZ3Mfzd508Zqzd7fmuvKoG4ee9ARPhGSBovzSktSiYoZNOgGrE+Tc/aa8aJ6Remf/Z/Efh52AtpubmioUlebpFWcwmJ64OfFG+T/NTuXbMXP/P3ucPHejMsSM4hKgTckM3Ext1b5r/aeL2lx1c3TbrLJQeuluiAJgfBYAk2ZqMUM+60xOvxNVHyZfjzDlsI/i52O2mQ1RU1qSmVPMMFf2/K2Py1pr4pvvqDPOKWN4+H/9D2gggBXEo4Q+Nm8BABLSnxo=
```

---

## Arquivo: `./.git/objects/2d/0b7b7faf46ed747ba91c1277970c9a10cb0193`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGlFF1PHFX03vme3WH5aCu1C+4KgXaVMFoh1aiNhUDAVMXpZk0jMBlmLjB0dme9MxspRrN+REtaAy9NePChT0YT/4T40sc2JXE7SYNGX3hbhUQTffDc3R1oMPHFk9xzz8e993zcc86C5y9kn7/w0ih6NtWWQADWleWVXR6hXxgTg9Ai9j8HoormkYGn0RQO8RQXchnGc9P8lBAKDZqfFqekUMqgOfw0MgRDvICb90N5TgCJZMiHEmVOnjkRmznaDWWkdcdQu5GR6EZex0hLHSaMZD/KaXuMz3GRemlm2vArIaGRbJD3KiQIczhqf90trVjn86RY9qyQBCCSlkhoOgtrkm45RbfEJGVKFt3VSA0fO6Y6LiV26NPra+36B4FXWfpQt0qW5wbEZk61HEMsKZAotP8coCoqoHnuxc8QckDWg97Gy9jAs6BpgsHNcjGtc+A+v8f4SKZNjyOBGcpxlL0a8UFImXuLPi1aYcAs9kVEd6zQaiLbLw5DwMXKqr7oeiTQl/0i0W3PJSWI1bQt6lhl1zfdUhBaJdu1An3FJ565aAFfds2i71Q8i+q0kbcgjm+4fD3STNMqlfwQkmaatBNMq7CCM4Cq6A+UxvJvDH31fp1t39kNbh+0yD6MEBgN1qew9r8G7/tQBi7PxplD8VeWuQI3w3J4DA71/DwuC2lU4GfEY0eANXABv4BHWlYz7JT871OHb4kF8WxL7UCp96CCOI+GWFwtKAt5fiYZc0d7/EIG5bn/1hucwRsCtINo8DpflmZZFhow0x5TR3u+0QqAlTw21LxgJPKSLoy08tGPsmhWiU9LyIHK6IE89qLLeRe9zPciF2fR//U4fmmUd3Euucd+aE2/MnF5YjyfdZ3spPHWG1loKGuBeMR2i1BefpB9Z2rCmMiygs2+mh0Ios5FK6xQq6E1Qygdbyn2O2pr8GaZOK7jB5EWuvY1aMMi8P6a1uqr4eWw6FGWLNoGKFIaJk3XiSRKgkrRzylUYgrJrtDAh0Ynq8SGlo+URRLay36JROrEqk3KoeuXItH2/IBQlryoI54ABgnKfikgOfkxQ5yzQFkFRBJYZPZ42OmTIAlYKQ0OZhnQDnYk2XLWhDFC+0HC3g/uA9qD4v5Vbb95ujpWa2vfuLp+9ea71claW6o6WedU8URNSW2k1lP3uqfujtw9u6MYtdTJDX/df5DK3OB3k6naqdNbnbcLNybrClLbN7R17VaqpiQ2lHXlVoLJerau1JTurc6a8sQWX5eFlFSdPNCQdurH5MD95MCdpW8+qimdmxfA0KZQU7o2J2tKx+ZgXRVfw9I+EjW5jkRR/vMgDXcOEBbbHipanYf9r7p03OSXib+DUYjqk97xTnxnZCyNvj95SQZ6O50cy/Hbg9zYENo+hxmd4xk91Dee4n9I8XDmzVwykltThrJKbg60rpYIhlZjHrulJco6OlLYTFuw4Lea/9scSM2v4+NEf4toF3uq8Q3KK43hRS7SZ0DGCja4CAiiwXgXDT5Cw49Q+me1a+vcjtpflR5q6TvXdrTzVfUnLH9x5uMz97TeB/ipAw6G1z6PuMzvjGq8/w8tV40c
```

---

## Arquivo: `./.git/objects/08/a1031f354b5d85354131b520bde36610e58771`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAFlUm2L00AQ9nN+xRARUghpz29XKCha0UNRegd+ECmT3Um7mmTj7qa0HPdjxJ9yf8zZl16D9kum8zzzzDOzU7e6huvrq2eN0R00aB0OClQ3aOPg9ZcPGz06MiVs6NdI1mVTWuWoG1p0qt+dK25U/wNf3sU82UiX6LBGS2fSjtxW1llmgjasLn2KwVCjjqt8jrJTfT7LUguyTPtHvJDKkHDanFb5E41LsldRuOI+RT6/t+24e5hjj62yxDjaUy9AUgMpt/VEEwdcnictwdctwTozW2bAP1mzh+i9mIWMGI3VhrOyrmKcAN7UVkkGrgLPmVOU8DKRWNGRBK+2yG/XH9dv7oDp7zafPwGXYk0tCdVR77SFr+/Xm3Uww3ovbF5C4Z2Vs+jBS3INY0m4ISf2uqdkxeOq8ZSLhVQTLTLybfE9+KSjoMHBOnyU7i8VA1obKI3iPbb/jyNabact/UZSKtQ9h7dKsOTjb6M0Lx8M2bHTMKA0j3/81yDQQTk0QMbw3AKtBgShezu2zgd8bMTBgfo9ssSglYWDQri5DS2S4gruw18/ZN6gGw2GTW6ddtjmS1hUi/LCCNntQFJJbT06xZT4ybfaMahjYah7yFI/1u7h6fSq89lvyA7sms43VUKeLq3au67lF5w4THfH8ikq4WLOPzQj4b0n6XAj/HoMccjBxHPcQpDzC46GZ9lfngg1PQ==
```

---

## Arquivo: `./.git/objects/5e/c0865eae2ac35458ee3c99411a98ede4e72f2a`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVTAzNmIwNDAwMzFRSMxLzMksTtVLLqgsycjP0zU2NNErqExm0OWurl/v9rakeqWMUPl0nlkCpxknQ7UkJSZnlxZg6AjsOby7n31Z3MPyhJcBW0t9JxdESEN1JCcWpSQWZOZj6Ll/M7e6N5b/VXOuV+0Spx9nD16eCLMlOSczNa8E02F7Fgivejd727nDdhkesnd+a9/alDALZk1+XlpmemlRYnIiplV/HQwjU78+exXLOCfyidiS2F6Xp8lQfSmpOZllqUWVGM6TTNz6crEJcz7rnYMOshH3Dj1uZboK1ZOeWpSal5yZWBRfWJScn4Lpzt8u9y7tTvXJTV23uNBk+tZ3561zP0L1FiSmJ+YCPYfpyOatBvcz3M691v0dWlCziO39OusLE2CaUlMyU/KLMdx4Z8qRihbO41+UZrFY7JEMWHv1mn0vVEthUTxWp/2pYV4mrdurFJAqGteWsN6Fj//AKaiWotT0zOKSIkyXrYj8JvquYH16pe20q0Y6Dks6+ZkS0PRguu2Bn00O456Fb2aFPYtvWVR+1ppVOBIAzMv2dw==
```

---

## Arquivo: `./.git/objects/c5/4760b626e2d68a31c43efbdfb0c5614ba646e4`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVTA0MLRgMDQwMDMxUdBLzStjMH+1IGI1UyWXL/uW6/8vHbmpWM6VZWIABArx8QWVyYnJGanx8QzXVZ2//FHZaCTSYd7Grm9h/P+wlTfUlMSc1KKSxPjc1OJEvYJKhnuP1xj0Xujr+zztUmBMxe+49Qdi3sJU5iXmZBanglRJNWSEnynfz8XEz3Lap33zN/bdwRNhqgpyMpMTi+JLivKT80FqxT4VGV3f8U/hd5jiWsOwBTLXHyrHwdUWgFRoveSdHG90aquUPFvuNEG5qqUzz7DBVJSW5OcmJifmxxel5iSW5Bdlgs1csOZjxL2buTdsK6MWuQfvk3RN7VoB1ZGUmJxdCjY2aDlrz+u9vLH3O8PdpH9uPsn0PvEgXFEexHF3WTSvZX+96Jv1MMH0Vk6xFV8S7y2oGqAnUhILIPZ9SpThmn12SW2e6759Lu0NErOvd8NcmJyfl5aZDvLGp5pFiilFAg93n/9vK/bq68vqVOHTMLPy84DhkZMaX5xZXJKaCw7p+bv4VGd4ejB0Jge6COy5NeflpJ0foMpTEksSkxIhQR1W9Tv1hm6k/upKmUdX2jeoMa0xFoAqy8wrLkgFhgnI8h0elXbecy4Jr325IFX8adODBT5vKqHKcjPTi0ARkpqXmFcCUtt7XnFmiIHQxVL98M/HJKUvd3vuOwpVW5CYnpibmlcCDmXmG6YMD88v3xWtsJmfUUfwa7Lnx8cwdakpmSn5xSDT7jEqTHwUWD3PI/FQiTTTlB915X/vQ1UVFiXnp4ATTMOuU9zG5z50Mc2OOz4hwzLjXldnN1RRUWo6MFCKIIYV7XGebsuWqfyzjXfqlRMB/zNtn8LirCi/JLE4PjElNzMPpD6xJLMsEeyAZ3Mfzd508Zqzd7fmuvKoG4ee9ARPhGSBovzSktSiYoY5f913XRWySn9hmuN9YY2JzLH9+7KAtpubmioUlebpFWcwmJ64OfFG+T/NTuXbMXP/P3ucPHejMsSM4hKgTckM3Ext1b5r/aeL2lx1c3TbrLJQeuluiAJgfBYAk2ZqMUM+60xOvxNVHyZfjzDlsI/i52O2mQ1RU1qSmVPMMFf2/K2Py1pr4pvvqDPOKWN4+H/9D2gggBXEo4Q+Nm8BAAp0nv8=
```

---

## Arquivo: `./.git/objects/db/5fb7af1a2378251086180bb6404cc5486c47e7`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGVzk1KBTEQRWHHWUVtQKnOX/cDEcG5E1dQqdxooNORvHSv37cFpwc+ONpbq5OsX57mAEiDXyOnaCNsjpu4Rb1DSbkk1hAXnyT6CG9+ZeCYJJLYgS3UsU2bdZwle015RSwaHLZbkVjYyDl/+qAvnPTZG+j16op3NKn7i/b2Rsu6BWsthxs9s2M2j/pYm/gXMh99jPoNumRUubDTwP1snQ6h0adQBskhe73D/AFxOk1Q
```

---

## Arquivo: `./.git/objects/88/c5ddc8b13292b952065888bbc2a0f755fc09e9`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/objects/7a/9006a5d2dce88bbdb65df7377a4bc2f16fd34e`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAHtV81uGzcQ7tlPMVnDkASY0motJbZ+DKROWhTob5KeA+4uJbHhLjck15Zq+Nhzgd5aFCiKHvIEBXrqxW+SF2gfoTPclbRWbAe9Fl0Y1C45HA5nvvlmHCsdw9EwPP7g8gDE0ok8tRDE3IruwmUqgIOrPVyJlU5eQaJzFHA0N0nlOSSKWzsNMr5kF2ypIFsyXjoNxZINoFixfhSc7gE+fpg8YAzOeCyu33C10MBYtXhDVcyOwaEdLMGDhKn3k46mmMyVzAWbKbEE6URma3H4prROzlbrzwvWH8CCBqPLPBUpi9DMeM54FgvDhmHY64fVeZuZ6pPkshivEWuTClP/NPZFYcM2su/tTz/+9cf3/qbe3B56qLqg/1z01+7y1yP9Nhv59yN8n6FrGd7b8FirFPA3eSXzOXNyvnABWLdSYhokWmkzgnNu2oz5vRmX+SHsz/zTGQenZzqfyXlp+PWb69+FnfQW/YYVxQ0jbAaZY9F96ksnUtR/kvAjPiP9Hwsj8kQK0BZSnuJYGIkTBZc4oUFYhyFWIpEZRlAjZjKUwE97/ZvuTnpFHfTKPVtgPFbCOA6pgOdlIqzd4gPhJ2dgxOsSdXdxNKuXBTc8s925cO2WreRbHZhOoeVMKVqgDdTTBFYfAAKsTKeB09w6Vq8Ga39grB9CgfFeA6XCiciE4Sr1SInCHTA0Fwc1jNZzR2E9gT72sbUikz607wWtLXgi2JJFYBfo4Aum5g2oTXA5P33783eTnn/bAs5/PlaYNXXswXJ1zq0PQX3fB81dky1EKfnzFN2M3trG5CNtslJd/2qkBl4gQnlOEV4WSibScQqwAAoFcPj62adAtEERRJ5oYnCb6TNUCJlwC42B+PKL5y8C4ImTOp8GGxCm0haKr0ZAjhr7kaUSEURyI9Styiwfw5wXI4gGxRIxufHB5sWTRZ00/0bh8U19HjiK8LzOwCqW8lsxgrD7aGhEhiZS7l4IytQRPArDcUUhmMO5pRuPoCwKYRL0zhiUcBghRkHG/CYt4ZCU3J3acTyLBpR6n+sM3avh6c0Um/S8hVsveKtlXpQO3KpA2iCmCCDHgE2DHJW8NJSlyBEYvwDZRJW4cHm5m7vdXVnKw938Fgpj3t6Z9TvvlG5hql5dBVVVIGMbTx2zC5m6xQj6YXgwRoSlqfdVH8MN/YcYozUfG57K0qJg5CeRNOc+gdcciVSfcIMMZuYxb4eHUP91jzqd+3xe02l9DOrHg61WMq25t6oKzAetVh4Nh4ewHcJuf0hn3ADMSQUYXTqqXyPIdS6a+K0z8r8N4xfacUU08ZmwHAvU+9Cbl1Ss1/h9XSJqJVYe8TKj/ffhd1f2TkS+g1+v+k7x4f/4vR2/lMi+QN1Kl8eeLW8hup0mAzJu5jJnTiPFVwz/RMwwYbDMbEMKbo2jr57BmU6FhTmWPt+RUEnSVP6qnmOnUDZaD28wdQY179RUUx3tSaVRXbxwXDqn85pYbRlnctue3cFaFWE1uGl/NjwRYbwhoP3wKHzUj3YqyTFVktvooyafHe7zfWpNKZCUxlKnWGhJbTTx5ZJV7QSWHORV5LNoiAOjwZNjNED+6g+PcegjTyJDNpmJ7k7P37/88Cc8p77CQLPX2FAWCU16lZe2JalJbJMeFcXTvb315MQmRhaukrbCvcDWESmy3caO7hQuN6qxrbBY0qh/gykWwqSkDoSawKcK+67cfbj6JG23bjR4rc54sx+rV9svdhpKyV4/2fUQ6PqqLanXwDNamsq0W6E7hhYEFvDWVt3uzrUsbgt3xN65VHUi5oM+F+3OIeB/Ig1Dq4716hAGoZ/Hpq32UNWnVf+NYav2D1UkTlA=
```

---

## Arquivo: `./.git/objects/c6/50d325f4b616f6e450052fc3fffa932e1380c6`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAGVzl1OwzAQRWGevYrZANVkkvEPQgixAF66Ase+UQN1HMUO66db6OuRPumkWsraSabxpR8AuexlUh00QXKYgzjxIQfrEBiiXp0Myl7MHg9snXzmyWYL5rRAXRoxJ+iSdMFso7gYsurIMPHst3rQFSd91wJ6/6sJnyhxvV9SLR80OK8i1g1Mrzwym0d9rHU8hcxXTL/n/kbx52wdjbZKe1w33CmDduQ110agghab+Qf2fUxX
```

---

## Arquivo: `./.git/objects/c6/b49a0d73c085feb6348647d56b8c78874f1057`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVTA0MLRgMDQwMDMxUdBLzStjMH+1IGI1UyWXL/uW6/8vHbmpWM6VZWIABArx8QWVyYnJGanx8QzXVZ2//FHZaCTSYd7Grm9h/P+wlTfUlMSc1KKSxPjc1OJEvYJKhnuP1xj0Xujr+zztUmBMxe+49Qdi3sJU5iXmZBanglRJNWSEnynfz8XEz3Lap33zN/bdwRNhqgpyMpMTi+JLivKT80FqxT4VGV3f8U/hd5jiWsOwBTLXHyrHwdUWgFRoveSdHG90aquUPFvuNEG5qqUzz7DBVJSW5OcmJifmxxel5iSW5Bdlgs1csOZjxL2buTdsK6MWuQfvk3RN7VoB1ZGUmJxdCjY2aDlrz+u9vLH3O8PdpH9uPsn0PvEgXFEexHF3WTSvZX+96Jv1MMH0Vk6xFV8S7y2oGqAnUhILIPZ9SpThmn12SW2e6759Lu0NErOvd8NcmJyfl5aZDvLGp5pFiilFAg93n/9vK/bq68vqVOHTMLPy84DhkZMaX5xZXJKaCw7p+bv4VGd4ejB0Jge6COy5NeflpJ0foMpTEksSkxIhQR1W9Tv1hm6k/upKmUdX2jeoMa0xFoAqy8wrLkgFhgnI8h0elXbecy4Jr325IFX8adODBT5vKqHKcjPTi0ARkpqXmFcCUtt7XnFmiIHQxVL98M/HJKUvd3vuOwpVW5CYnpibmlcCDmXmG6YMD88v3xWtsJmfUUfwa7Lnx8cwdakpmSn5xSDT7jEqTHwUWD3PI/FQiTTTlB915X/vQ1UVFiXnp4ATTMOuU9zG5z50Mc2OOz4hwzLjXldnN1RRUWo6MFCKIIYV7XGebsuWqfyzjXfqlRMB/zNtn8LirCi/JLE4PjElNzMPpD6xJLMsEeyAZ3Mfzd508Zqzd7fmuvKoG4ee9ARPhGSBovzSktSiYoY5f913XRWySn9hmuN9YY2JzLH9+7KAtpubmioUlebpFWcwmJ64OfFG+T/NTuXbMXP/P3ucPHejMsSM4hKgTckM3Ext1b5r/aeL2lx1c3TbrLJQeuluiAJgfBYAk2ZqMcODN7bLE+5dKf3ffmFxDdvPeZGO/2MhakpLMnOKGebKnr/1cVlrTXzzHXXGOWUMD/+v/wENBLCCeJTQx+YtAM13pBk=
```

---

## Arquivo: `./.git/objects/84/ee8c3979974df0764c1d8d7bb5fbd90ab9c373`

```text
x}n09)EHTo-R	
N<qmSp}^;nUE·=3ٹ29WϾ<(Ǖj/LLqiBPܹ#;vf1zMfЬY:]]qX<g7\UԍȂe[qr&I%+HyN֊Gu^.kΠ
5PyɸѲ$9{ӇtN9
cnio~"DgT>YRw>%Q֖F	gq%yYV~ίFcƢeNEJЮgU'94h&zM|B|Du!D.4f4[sNBj5Y3:_Y<B2AH(h
v82!-^:#U9`2kh	WY#X*=򻉆A`4LhooۺͩKek"e˜'0I)uFI1GS
8bc6r(P0E=m)k΀6%8gqH큿C='411$ǲ^EQZ=`\
h><!1_GO(z:ISO
_Qze@8jiX|sÃNl6Jk+waİ=9M?S
```

---

## Arquivo: `./.git/objects/eb/f1dc783bab02a873561c5de1e433f5aa694ad4`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVTA0MLRgMDQwMDMxUdBLzStjMH+1IGI1UyWXL/uW6/8vHbmpWM6VZWIABArx8QWVyYnJGanx8QzXVZ2//FHZaCTSYd7Grm9h/P+wlTfUlMSc1KKSxPjc1OJEvYJKhnuP1xj0Xujr+zztUmBMxe+49Qdi3sJU5iXmZBanglRJNWSEnynfz8XEz3Lap33zN/bdwRNhqgpyMpMTi+JLivKT80FqxT4VGV3f8U/hd5jiWsOwBTLXHyrHwdUWgFRoveSdHG90aquUPFvuNEG5qqUzz7DBVJSW5OcmJifmxxel5iSW5Bdlgs1csOZjxL2buTdsK6MWuQfvk3RN7VoB1ZGUmJxdCjY2aDlrz+u9vLH3O8PdpH9uPsn0PvEgXFEexHF3WTSvZX+96Jv1MMH0Vk6xFV8S7y2oGqAnUhILIPZ9SpThmn12SW2e6759Lu0NErOvd8NcmJyfl5aZDvLGp5pFiilFAg93n/9vK/bq68vqVOHTMLPy84DhkZMaX5xZXJKaCw7p+bv4VGd4ejB0Jge6COy5NeflpJ0foMpTEksSkxIhQR1W9Tv1hm6k/upKmUdX2jeoMa0xFoAqy8wrLkgFhgnI8h0elXbecy4Jr325IFX8adODBT5vKqHKcjPTi0ARkpqXmFcCUtt7XnFmiIHQxVL98M/HJKUvd3vuOwpVW5CYnpibmlcCDmXmG6YMD88v3xWtsJmfUUfwa7Lnx8cwdakpmSn5xSDT7jEqTHwUWD3PI/FQiTTTlB915X/vQ1UVFiXnp4ATTMOuU9zG5z50Mc2OOz4hwzLjXldnN1RRUWo6MFCKIIYV7XGebsuWqfyzjXfqlRMB/zNtn8LirCi/JLE4PjElNzMPpD6xJLMsEeyAZ3Mfzd508Zqzd7fmuvKoG4ee9ARPhGSBovzSktSiYoY5f913XRWySn9hmuN9YY2JzLH9+7KAtpubmioUlebpFWcwmJ64OfFG+T/NTuXbMXP/P3ucPHejMsSM4hKgTckM3Ext1b5r/aeL2lx1c3TbrLJQeuluiAJgfBYAk2ZqMcOhnWxPrr/omF79WN5pC3/d0rXe5t8gakpLMnOKGebKnr/1cVlrTXzzHXXGOWUMD/+v/wENBLCCeJTQx+YtAGMJouc=
```

---

## Arquivo: `./.git/objects/c0/f24621842dffe3cda41dbfb3c0e1da4382bc71`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./.git/objects/4d/275544deea3a9f4c89f48e57503119b520eecc`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
eAErKUpNVbAwsGAwNDAwMzFRSMxLzMksTtXLKMnNYfi7O+hwn+fVGn6GgNzjx6VYtGyW2EDVJSUmZ5cWQJRNTNX/voVfuLfKLfbNxwQPJo6luivgymBmdRy9e2Kj0aSdQWwRHbsPLfge+ofzJVRRcmJRSmJBZj7EtNqrk16u/v+HRef3lQkuk90nqbtHbUZTGJ+YkpuZB1F+j/9OpNSd1If3+Dbp+x1p3MjQkt+FobyosDSzLDElvxiiR+rbuu+mbMnbOp6lxHT0zlu22HF5Jrqe5JzM1LwSaEB8f7l8v/+ytqmz1VhFrpXMW9Bsl3EbXUNKZnpmSWIOxIZ5hTUxGtZLjhtatPGfsj/I/+HhnR8wDfl5aZnppUWJyYlQH1dNYFt66c6L7r3bYr+bV3kf+ph/2Q+qOCU1J7MstagSYmrLux7Lyum+H8p8ZHurt/6+ybXzcDFUYWZeSmoFRNXO3Of/574Qk1RkkRPoiq6vv+DlnAVVVZCYnpgL9BbU4pMbJ6oznfLwisr+YOh3dkLLj91tTXCVmXmpUM/Y3dt14N/EXX+l++e3ZG2fpfv9xY1SmLLUlEx4sB745KbYovv/8dklsvs3H3h4y7lpTyGqOuSIu5LlvXTu59dTvaepG9xTKm4P8K3ZAVVdWBSfnJ8CDXv2Q6X/2ww4PK7G/nuvGRL95N2spZ5wdSBl0Ej1Yqyr+fbszsIYLal3C/Uvf5H5vngZVF1RanpmcUkR1NcrpI+sFXac9ObH2ppNfjxbDPUd9qigKYQaGbBUYOfrsqkT+Q4HGB7l+2ovvsIlAAAMB1CL
```

---

## Arquivo: `./.git/logs/HEAD`

```text
0000000000000000000000000000000000000000 bfe22a2c3867eebb0a24edf14ae8d832a43dbace Seu Nome <voce@email.com> 1785167974 -0300	commit (initial): update: projeto completo com painel, QR code, backup e requisitos
bfe22a2c3867eebb0a24edf14ae8d832a43dbace 0000000000000000000000000000000000000000 Seu Nome <voce@email.com> 1785167974 -0300	Branch: renamed refs/heads/master to refs/heads/main
0000000000000000000000000000000000000000 bfe22a2c3867eebb0a24edf14ae8d832a43dbace Seu Nome <voce@email.com> 1785167974 -0300	Branch: renamed refs/heads/master to refs/heads/main
bfe22a2c3867eebb0a24edf14ae8d832a43dbace 008da9f0f6cc24f35569d738d2e9571db12df7c2 Seu Nome <voce@email.com> 1785173157 -0300	commit: Adiciona funcionalidade de QR Code em lote e impressao
008da9f0f6cc24f35569d738d2e9571db12df7c2 008da9f0f6cc24f35569d738d2e9571db12df7c2 Seu Nome <voce@email.com> 1785199353 -0300	reset: moving to HEAD
008da9f0f6cc24f35569d738d2e9571db12df7c2 008da9f0f6cc24f35569d738d2e9571db12df7c2 Seu Nome <voce@email.com> 1785200760 -0300	reset: moving to origin/main
008da9f0f6cc24f35569d738d2e9571db12df7c2 df8f461ab7f766f9af05a63b80627e541ae9f074 Seu Nome <voce@email.com> 1785218291 -0300	commit: feat: implementado multi-tenant por slug e barra de menu responsiva
df8f461ab7f766f9af05a63b80627e541ae9f074 0000000000000000000000000000000000000000 Seu Nome <voce@email.com> 1785218354 -0300	Branch: renamed refs/heads/main to refs/heads/main
df8f461ab7f766f9af05a63b80627e541ae9f074 df8f461ab7f766f9af05a63b80627e541ae9f074 Seu Nome <voce@email.com> 1785218354 -0300	Branch: renamed refs/heads/main to refs/heads/main
df8f461ab7f766f9af05a63b80627e541ae9f074 aab03e02ec302b8230dad4cbd7e6fc53e89fa6f0 Seu Nome <voce@email.com> 1785221836 -0300	commit: Correcao de rotas, slug e templates modularizados
aab03e02ec302b8230dad4cbd7e6fc53e89fa6f0 db5fb7af1a2378251086180bb6404cc5486c47e7 Seu Nome <voce@email.com> 1785222059 -0300	commit: Corrige variavel resumo na rota de analise
db5fb7af1a2378251086180bb6404cc5486c47e7 1e16eb1f7dbc0485b7904b81454272b252fa2f62 Seu Nome <voce@email.com> 1785224459 -0300	commit: Ajuste profissional e limpo do menu de configurações e correção de campos
1e16eb1f7dbc0485b7904b81454272b252fa2f62 8d046d6e00cfe57c3ebce5fc5feb6a27a9d5530e Seu Nome <voce@email.com> 1785225053 -0300	commit: Backup completo: Ajustes visuais dos painéis de configuração e delivery
8d046d6e00cfe57c3ebce5fc5feb6a27a9d5530e c650d325f4b616f6e450052fc3fffa932e1380c6 Seu Nome <voce@email.com> 1785226710 -0300	commit: Backup: ajustes no painel de pedidos e mesas
c650d325f4b616f6e450052fc3fffa932e1380c6 c650d325f4b616f6e450052fc3fffa932e1380c6 Seu Nome <voce@email.com> 1785227400 -0300	reset: moving to origin/main
c650d325f4b616f6e450052fc3fffa932e1380c6 8d046d6e00cfe57c3ebce5fc5feb6a27a9d5530e Seu Nome <voce@email.com> 1785281976 -0300	reset: moving to HEAD~1

```

---

## Arquivo: `./.git/logs/refs/heads/main`

```text
0000000000000000000000000000000000000000 bfe22a2c3867eebb0a24edf14ae8d832a43dbace Seu Nome <voce@email.com> 1785167974 -0300	commit (initial): update: projeto completo com painel, QR code, backup e requisitos
bfe22a2c3867eebb0a24edf14ae8d832a43dbace bfe22a2c3867eebb0a24edf14ae8d832a43dbace Seu Nome <voce@email.com> 1785167974 -0300	Branch: renamed refs/heads/master to refs/heads/main
bfe22a2c3867eebb0a24edf14ae8d832a43dbace 008da9f0f6cc24f35569d738d2e9571db12df7c2 Seu Nome <voce@email.com> 1785173157 -0300	commit: Adiciona funcionalidade de QR Code em lote e impressao
008da9f0f6cc24f35569d738d2e9571db12df7c2 df8f461ab7f766f9af05a63b80627e541ae9f074 Seu Nome <voce@email.com> 1785218291 -0300	commit: feat: implementado multi-tenant por slug e barra de menu responsiva
df8f461ab7f766f9af05a63b80627e541ae9f074 df8f461ab7f766f9af05a63b80627e541ae9f074 Seu Nome <voce@email.com> 1785218354 -0300	Branch: renamed refs/heads/main to refs/heads/main
df8f461ab7f766f9af05a63b80627e541ae9f074 aab03e02ec302b8230dad4cbd7e6fc53e89fa6f0 Seu Nome <voce@email.com> 1785221836 -0300	commit: Correcao de rotas, slug e templates modularizados
aab03e02ec302b8230dad4cbd7e6fc53e89fa6f0 db5fb7af1a2378251086180bb6404cc5486c47e7 Seu Nome <voce@email.com> 1785222059 -0300	commit: Corrige variavel resumo na rota de analise
db5fb7af1a2378251086180bb6404cc5486c47e7 1e16eb1f7dbc0485b7904b81454272b252fa2f62 Seu Nome <voce@email.com> 1785224459 -0300	commit: Ajuste profissional e limpo do menu de configurações e correção de campos
1e16eb1f7dbc0485b7904b81454272b252fa2f62 8d046d6e00cfe57c3ebce5fc5feb6a27a9d5530e Seu Nome <voce@email.com> 1785225053 -0300	commit: Backup completo: Ajustes visuais dos painéis de configuração e delivery
8d046d6e00cfe57c3ebce5fc5feb6a27a9d5530e c650d325f4b616f6e450052fc3fffa932e1380c6 Seu Nome <voce@email.com> 1785226710 -0300	commit: Backup: ajustes no painel de pedidos e mesas
c650d325f4b616f6e450052fc3fffa932e1380c6 8d046d6e00cfe57c3ebce5fc5feb6a27a9d5530e Seu Nome <voce@email.com> 1785281976 -0300	reset: moving to HEAD~1

```

---

## Arquivo: `./.git/logs/refs/remotes/origin/HEAD`

```text
0000000000000000000000000000000000000000 008da9f0f6cc24f35569d738d2e9571db12df7c2 Seu Nome <voce@email.com> 1785200760 -0300	fetch

```

---

## Arquivo: `./.git/logs/refs/remotes/origin/main`

```text
0000000000000000000000000000000000000000 bfe22a2c3867eebb0a24edf14ae8d832a43dbace Seu Nome <voce@email.com> 1785167976 -0300	update by push
bfe22a2c3867eebb0a24edf14ae8d832a43dbace 008da9f0f6cc24f35569d738d2e9571db12df7c2 Seu Nome <voce@email.com> 1785173159 -0300	update by push
008da9f0f6cc24f35569d738d2e9571db12df7c2 df8f461ab7f766f9af05a63b80627e541ae9f074 Seu Nome <voce@email.com> 1785218356 -0300	update by push
df8f461ab7f766f9af05a63b80627e541ae9f074 aab03e02ec302b8230dad4cbd7e6fc53e89fa6f0 Seu Nome <voce@email.com> 1785221838 -0300	update by push
aab03e02ec302b8230dad4cbd7e6fc53e89fa6f0 db5fb7af1a2378251086180bb6404cc5486c47e7 Seu Nome <voce@email.com> 1785222061 -0300	update by push
db5fb7af1a2378251086180bb6404cc5486c47e7 1e16eb1f7dbc0485b7904b81454272b252fa2f62 Seu Nome <voce@email.com> 1785224462 -0300	update by push
1e16eb1f7dbc0485b7904b81454272b252fa2f62 8d046d6e00cfe57c3ebce5fc5feb6a27a9d5530e Seu Nome <voce@email.com> 1785225055 -0300	update by push
8d046d6e00cfe57c3ebce5fc5feb6a27a9d5530e c650d325f4b616f6e450052fc3fffa932e1380c6 Seu Nome <voce@email.com> 1785226712 -0300	update by push

```

---

## Arquivo: `./static/style.css`

```text
/* Estilos customizados adicionais, se necessário */
body {
    margin: 0;
    padding: 0;
}

```

---

## Arquivo: `./static/css/responsive.css`

```text
/* --- ESTILOS DE RESPONSIVIDADE PROFISSIONAL (MOBILE, TABLET E DESKTOP) --- */

@media (max-width: 1024px) {
    .sidebar {
        width: 220px !important;
    }
    .main-content {
        margin-left: 220px !important;
        max-width: calc(100% - 220px) !important;
        padding: 20px !important;
    }
}

@media (max-width: 768px) {
    body {
        flex-direction: column !important;
    }
    .sidebar {
        position: relative !important;
        width: 100% !important;
        height: auto !important;
        bottom: auto !important;
        top: auto !important;
    }
    .sidebar-menu {
        display: flex !important;
        flex-direction: row !important;
        flex-wrap: wrap !important;
        gap: 4px !important;
        padding: 10px !important;
        justify-content: center !important;
    }
    .sidebar-menu a {
        padding: 8px 12px !important;
        font-size: 0.85rem !important;
    }
    .sidebar-brand {
        padding: 15px !important;
        justify-content: center !important;
    }
    .main-content {
        margin-left: 0 !important;
        max-width: 100% !important;
        padding: 15px !important;
    }
}

```

---

## Arquivo: `./static/css/style.css`

```text
/* ==========================================================================
   CARDÁPIO PRO - DESIGN SYSTEM DE ALTO PADRÃO (SaaS Edition)
   ========================================================================== */

:root {
    --bg-base: #070a13;
    --bg-surface: #0f172a;
    --bg-card: #162032;
    --bg-card-hover: #1e293b;
    
    --border-subtle: #273548;
    --border-focus: #f59e0b;
    
    --text-primary: #f8fafc;
    --text-secondary: #94a3b8;
    --text-muted: #64748b;
    
    --accent-primary: #f59e0b;
    --accent-primary-hover: #d97706;
    --accent-success: #10b981;
    --accent-danger: #ef4444;
    --accent-info: #3b82f6;

    --radius-sm: 8px;
    --radius-md: 12px;
    --radius-lg: 16px;
    
    --shadow-card: 0 10px 25px -5px rgba(0, 0, 0, 0.4), 0 8px 10px -6px rgba(0, 0, 0, 0.4);
    --transition-smooth: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Reset Global */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    background-color: var(--bg-base);
    color: var(--text-primary);
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    line-height: 1.5;
    min-height: 100vh;
}

/* Tipografia refinada */
h1, h2, h3, h4, h5, h6 {
    color: var(--text-primary);
    font-weight: 600;
    letter-spacing: -0.025em;
}

p {
    color: var(--text-secondary);
}

/* Container Principal */
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2.5rem 1.5rem;
}

/* Cartões / Painéis de Alto Padrão */
.card, .metric-card, form, table {
    background-color: var(--bg-surface);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-md);
    box-shadow: var(--shadow-card);
    padding: 1.5rem;
    margin-bottom: 1.5rem;
}

/* Tabelas Sofisticadas */
table {
    width: 100%;
    border-collapse: collapse;
    overflow: hidden;
}

th, td {
    padding: 1rem;
    text-align: left;
    border-bottom: 1px solid var(--border-subtle);
    font-size: 0.95rem;
}

th {
    background-color: var(--bg-card);
    color: var(--text-primary);
    font-weight: 600;
    text-transform: uppercase;
    font-size: 0.75rem;
    letter-spacing: 0.05em;
}

tr:hover td {
    background-color: var(--bg-card-hover);
}

/* Formulários & Inputs Modernos */
input[type="text"],
input[type="number"],
input[type="password"],
input[type="email"],
select,
textarea {
    width: 100%;
    background-color: var(--bg-base);
    border: 1px solid var(--border-subtle);
    border-radius: var(--radius-sm);
    color: var(--text-primary);
    padding: 0.75rem 1rem;
    font-size: 0.95rem;
    transition: var(--transition-smooth);
    outline: none;
    margin-top: 0.35rem;
    margin-bottom: 1rem;
}

input:focus, select:focus, textarea:focus {
    border-color: var(--accent-primary);
    box-shadow: 0 0 0 3px rgba(245, 158, 11, 0.15);
}

label {
    display: block;
    font-size: 0.85rem;
    font-weight: 500;
    color: var(--text-secondary);
}

/* Botões de Alto Padrão */
.btn, button, input[type="submit"] {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    background-color: var(--accent-primary);
    color: #070a13;
    font-weight: 600;
    font-size: 0.9rem;
    padding: 0.7rem 1.25rem;
    border: none;
    border-radius: var(--radius-sm);
    cursor: pointer;
    text-decoration: none;
    transition: var(--transition-smooth);
    box-shadow: 0 4px 12px rgba(245, 158, 11, 0.2);
}

.btn:hover, button:hover, input[type="submit"]:hover {
    background-color: var(--accent-primary-hover);
    transform: translateY(-1px);
    box-shadow: 0 6px 16px rgba(245, 158, 11, 0.3);
}

.btn-secondary {
    background-color: var(--bg-card);
    color: var(--text-primary);
    border: 1px solid var(--border-subtle);
    box-shadow: none;
}

.btn-secondary:hover {
    background-color: var(--border-subtle);
    color: #fff;
}

/* Alertas e Badges de Status */
.badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 50px;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.02em;
}

.badge-success { background-color: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); }
.badge-warning { background-color: rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3); }
.badge-danger { background-color: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.3); }

```

---

## Arquivo: `./templates/analise.html`

```text
{% extends "base.html" %}

{% block content %}
<div class="card" style="margin-bottom: 20px;">
    <h3 style="color: var(--primary-color); margin-bottom: 5px;">Menu de Análise e Faturamento</h3>
    <p style="color: #a0a0a0; margin-bottom: 15px; font-size: 0.9rem;">Resumo geral do faturamento e vendas agrupadas por forma de pagamento.</p>
</div>

<!-- Cards de Resumo vindos do Banco de Dados -->
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 15px; margin-bottom: 20px;">
    <div style="background: #252525; border: 1px solid #333; padding: 18px; border-radius: 8px; border-left: 4px solid var(--primary-color);">
        <span style="color: #a0a0a0; font-size: 0.8rem;">Faturamento Total</span>
        <h2 style="color: #fff; margin-top: 5px; font-size: 1.4rem;">R$ {{ "%.2f"|format(resumo.faturamento_total or 0) }}</h2>
        <span style="color: #777; font-size: 0.75rem;">{{ resumo.total_pedidos or 0 }} pedido(s) registrado(s)</span>
    </div>
</div>

<div class="card" style="margin-top: 20px;">
    <h3 style="color: var(--primary-color); margin-bottom: 10px;">Vendas por Forma de Pagamento</h3>
    <div style="max-height: 350px; overflow-y: auto;">
        <table style="width: 100%; border-collapse: collapse; text-align: left; background: #1a1a1a;">
            <thead>
                <tr style="background: #252525; border-bottom: 2px solid #333; color: var(--primary-color); font-size: 0.85rem;">
                    <th style="padding: 10px 12px;">Forma de Pagamento</th>
                    <th style="padding: 10px 12px;">Quantidade</th>
                    <th style="padding: 10px 12px;">Total Arrecadado</th>
                </tr>
            </thead>
            <tbody>
                {% if por_pagamento %}
                    {% for item in por_pagamento %}
                    <tr style="border-bottom: 1px solid #333; font-size: 0.85rem;">
                        <td style="padding: 10px 12px; color: #ddd; font-weight: bold;">{{ item.forma_pagamento or 'Não especificado' }}</td>
                        <td style="padding: 10px 12px; color: #a0a0a0;">{{ item.qtd }}</td>
                        <td style="padding: 10px 12px; color: #4caf50; font-weight: bold;">R$ {{ "%.2f"|format(item.total or 0) }}</td>
                    </tr>
                    {% endfor %}
                {% else %}
                    <tr>
                        <td colspan="3" style="text-align: center; color: #777; padding: 20px;">Nenhum registro de pagamento encontrado no banco.</td>
                    </tr>
                {% endif %}
            </tbody>
        </table>
    </div>
</div>
{% endblock %}

```

---

## Arquivo: `./templates/backup.html`

```text
{% extends "base.html" %}

{% block title %}Backup do Sistema - Cardápio Pro{% endblock %}

{% block content %}
<div class="card">
    <h2>Backup e Segurança dos Dados</h2>
    <p style="margin-bottom: 1.5rem; color: #64748b;">Faça o download do arquivo de segurança contendo todas as configurações, produtos e pedidos cadastrados.</p>

    <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.5rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
        <div>
            <h4 style="color: #1e293b; margin-bottom: 0.2rem;">Exportar Banco de Dados (JSON)</h4>
            <p style="font-size: 0.9rem; color: #64748b;">Gera um arquivo completo com todos os dados do sistema atual.</p>
        </div>
        <a href="/admin/backup/exportar" class="btn" style="background: #16a34a; text-decoration: none; padding: 0.6rem 1.2rem;">Baixar Backup</a>
    </div>
</div>
{% endblock %}

```

---

## Arquivo: `./templates/base.html`

```text
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Cardápio Pro{% endblock %}</title>
    <style>
        /* 1. Midnight Blue (Padrão Sofisticado) */
        :root {
            --bg-main: #090d16;
            --bg-card: #111827;
            --nav-bg: #070a13;
            --border-color: rgba(255, 255, 255, 0.08);
            --text-main: #f9fafb;
            --text-muted: #9ca3af;
            --input-bg: #1f2937;
            --input-text: #f9fafb;
            --accent-grad: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
            --accent-color: #f59e0b;
            --accent-text: #ffffff;
            --shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.5);
        }

        /* 2. Clean Light Minimalista */
        [data-theme="light"] {
            --bg-main: #f8fafc;
            --bg-card: #ffffff;
            --nav-bg: #ffffff;
            --border-color: #e2e8f0;
            --text-main: #0f172a;
            --text-muted: #64748b;
            --input-bg: #f8fafc;
            --input-text: #0f172a;
            --accent-grad: linear-gradient(135deg, #3b82f6 0%, #1d4ed8 100%);
            --accent-color: #3b82f6;
            --accent-text: #ffffff;
            --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        }

        /* 3. Emerald Restô (Verde Gourmet) */
        [data-theme="emerald"] {
            --bg-main: #022c22;
            --bg-card: #064e3b;
            --nav-bg: #01211a;
            --border-color: rgba(255, 255, 255, 0.12);
            --text-main: #ecfdf5;
            --text-muted: #6ee7b7;
            --input-bg: #047857;
            --input-text: #ffffff;
            --accent-grad: linear-gradient(135deg, #34d399 0%, #059669 100%);
            --accent-color: #34d399;
            --accent-text: #022c22;
            --shadow: 0 10px 25px -5px rgba(0, 44, 34, 0.6);
        }

        /* 4. Warm Terracotta (Gastronomia Quente) */
        [data-theme="terracotta"] {
            --bg-main: #1c1512;
            --bg-card: #291e18;
            --nav-bg: #140f0c;
            --border-color: rgba(255, 255, 255, 0.09);
            --text-main: #fdf8f6;
            --text-muted: #d4b5a7;
            --input-bg: #382921;
            --input-text: #fdf8f6;
            --accent-grad: linear-gradient(135deg, #f97316 0%, #c2410c 100%);
            --accent-color: #f97316;
            --accent-text: #ffffff;
            --shadow: 0 10px 25px -5px rgba(28, 21, 18, 0.7);
        }

        body {
            margin: 0;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: var(--bg-main);
            color: var(--text-main);
            transition: background-color 0.3s ease, color 0.3s ease;
        }

        /* old header */
/*
            background-color: var(--nav-bg) !important;
            border-bottom: 1px solid var(--border-color);
            padding: 0.85rem 1.75rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1rem;
            box-shadow: 0 4px 20px rgba(0,0,0,0.2);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .nav-brand {
            font-size: 1.2rem;
            font-weight: 700;
            color: var(--text-main);
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 0.6rem;
            letter-spacing: -0.5px;
        }

        .nav-links {
            display: flex;
            gap: 0.6rem;
            align-items: center;
            overflow-x: auto;
            white-space: nowrap;
            max-width: 100%;
            padding: 6px 4px;
            scrollbar-width: thin;
            -webkit-overflow-scrolling: touch;
        }
        .nav-links::-webkit-scrollbar {
            height: 5px;
        }
        .nav-links::-webkit-scrollbar-thumb {
            background: var(--accent-color);
            border-radius: 10px;
        }
        .nav-link-item {
            color: var(--text-muted);
            text-decoration: none;
            font-size: 0.88rem;
            font-weight: 600;
            padding: 0.55rem 1rem;
            border-radius: 10px;
            border: 1px solid var(--border-color);
            background: var(--bg-card);
            transition: all 0.2s ease;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
        }
        .nav-link-item:hover, .nav-link-item:active {
            color: var(--text-main);
            border-color: var(--accent-color);
            background: var(--input-bg);
            transform: translateY(-1px);
        }

            color: var(--text-muted);
            text-decoration: none;
            font-size: 0.85rem;
            font-weight: 500;
            padding: 0.45rem 0.85rem;
            border-radius: 8px;
            border: 1px solid var(--border-color);
            background: var(--bg-card);
            transition: all 0.2s;
        }

            color: var(--text-main);
            border-color: var(--accent-color);
            background: var(--input-bg);
        }

        /* Menu Flutuante Discreto de Temas */
        .theme-dropdown-container {
            position: relative;
            display: inline-block;
        }
        .theme-toggle-btn {
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            color: var(--text-main);
            padding: 0.45rem 0.85rem;
            border-radius: 8px;
            cursor: pointer;
            font-size: 0.85rem;
            font-weight: 500;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            transition: all 0.2s;
        }
        .theme-toggle-btn:hover {
            border-color: var(--accent-color);
        }
        .theme-menu-content {
            display: none;
            position: absolute;
            right: 0;
            top: calc(100% + 8px);
            background: var(--bg-card);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            box-shadow: var(--shadow);
            min-width: 200px;
            z-index: 1000;
            padding: 0.5rem;
        }
        .theme-menu-content.show {
            display: block;
        }
        .theme-option {
            width: 100%;
            text-align: left;
            background: transparent;
            border: none;
            color: var(--text-main);
            padding: 0.55rem 0.75rem;
            font-size: 0.85rem;
            border-radius: 6px;
            cursor: pointer;
            transition: background 0.15s;
        }
        .theme-option:hover {
            background: var(--input-bg);
            color: var(--accent-color);
        }

        main {
            padding: 2rem 1.5rem;
            max-width: 1200px;
            margin: 0 auto;
        }
    
        @media (min-width: 992px) {
            .nav-links {
                overflow-x: visible !important;
                flex-wrap: wrap !important;
                white-space: normal !important;
            }
        }
        @media (max-width: 991px) {
            header {
                padding: 0.6rem 1rem !important;
            }
            .nav-links {
                width: 100%;
                overflow-x: auto;
                white-space: nowrap;
                padding-bottom: 6px;
                -webkit-overflow-scrolling: touch;
            }
        }
    
        header {
            background-color: var(--nav-bg) !important;
            border-bottom: 1px solid var(--border-color);
            padding: 0.75rem 1rem;
            display: flex;
            flex-direction: column;
            gap: 0.75rem;
            position: sticky;
            top: 0;
            z-index: 100;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }
        .header-top {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
        }
        .nav-brand {
            font-size: 1.1rem;
            font-weight: 700;
            color: var(--text-main);
            text-decoration: none;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .nav-links {
            display: flex;
            gap: 0.4rem;
            align-items: center;
            overflow-x: auto;
            width: 100%;
            padding-bottom: 4px;
            scrollbar-width: none; /* Firefox */
            -ms-overflow-style: none; /* IE/Edge */
        }
        .nav-links::-webkit-scrollbar {
            display: none; /* Chrome/Safari */
        }
        .nav-link-item {
            color: var(--text-muted);
            text-decoration: none;
            font-size: 0.8rem;
            font-weight: 600;
            padding: 0.45rem 0.75rem;
            border-radius: 8px;
            border: 1px solid var(--border-color);
            background: var(--bg-card);
            white-space: nowrap;
            flex-shrink: 0;
            transition: all 0.2s ease;
        }
        .nav-link-item:hover, .nav-link-item:active {
            color: var(--text-main);
            border-color: var(--accent-color);
            background: var(--input-bg);
        }
        @media (min-width: 992px) {
            header {
                flex-direction: row;
                justify-content: space-between;
                padding: 0.85rem 1.75rem;
            }
            .nav-links {
                width: auto;
                flex-wrap: wrap;
                overflow-x: visible;
            }
        }

</style>

    <script>
    (function() {
        const parts = window.location.pathname.split("/");
        if (parts.length >= 3 && parts[1] === "admin" && parts[2]) {
            const currentSlug = parts[2];
            window.APP_SLUG = currentSlug;

            document.addEventListener("DOMContentLoaded", () => {
                document.querySelectorAll("a[href^='/admin/'], form[action^='/admin/']").forEach(el => {
                    const attr = el.hasAttribute("href") ? "href" : "action";
                    let val = el.getAttribute(attr);
                    if (val.startsWith("/admin/") && !val.includes("/" + currentSlug + "/")) {
                        let cleanPath = val.replace(/^\/admin\/+/, "");
                        el.setAttribute(attr, `/admin/${currentSlug}/${cleanPath}`);
                    }
                });
            });
        }
    })();
    </script>
    <!-- corrige-painel-tema -->
    <style>
    /* Ajuste dinâmico para os painéis internos acompanharem o tema */
    .bg-card-color, .bg-card-color, .card-painel, .panel-content, div[class*="bg-"] {
        /* Se houver classes estáticas de azul escuro, substituímos por variáveis ou cores neutras do tema */
    }
    .min-h-screen, body {
        background-color: var(--bg-main, #0f172a);
    }
    </style>
    
    <script>
    document.addEventListener("DOMContentLoaded", () => {
        const themeSelector = document.querySelector("#theme-selector") || document.querySelector("select[name='theme']") || document.getElementById("temaSelect");
        
        // Monitora mudanças no seletor de temas ou cliques nos dropdowns de tema
        document.querySelectorAll("[data-theme-option], .theme-option, select").forEach(el => {
            el.addEventListener("change", (e) => {
                setTimeout(applyThemeStyles, 50);
            });
        });

        function applyThemeStyles() {
            // Verifica se o tema atual é claro ou escuro pelo estilo do body/header
            const isLight = document.body.classList.contains("light") || 
                            document.documentElement.classList.contains("light") ||
                            document.querySelector(".bg-white, .bg-gray-50");
            
            document.querySelectorAll(".bg-slate-900, .bg-gray-900, .card-painel").forEach(panel => {
                if (window.getComputedStyle(document.body).backgroundColor !== "rgb(15, 23, 42)") {
                    // Tema claro ativo
                    panel.style.backgroundColor = "#ffffff";
                    panel.style.color = "#1f2937";
                    panel.style.borderColor = "#e5e7eb";
                } else {
                    // Tema escuro ativo
                    panel.style.backgroundColor = "";
                    panel.style.color = "";
                    panel.style.borderColor = "";
                }
            });
        }
    });
    </script>
    
    <style>
    /* Força os painéis de configuração a acompanharem a cor de fundo do tema selecionado */
    body[data-theme*="light"] .bg-slate-900, 
    body[data-theme*="light"] .bg-gray-900,
    body:not(.dark) .bg-slate-900,
    body:not(.dark) .bg-gray-900 {
        background-color: #ffffff !important;
        color: #111827 !important;
        border-color: #e5e7eb !important;
    }
    </style>
    </head>
    
    
    
<body>

    <header>
        <a href="/admin/{{ slug }}/cardapio" class="nav-brand">
            🍽️ Cardápio Pro <span style="font-size: 0.75rem; font-weight: 400; color: var(--text-muted); border-left: 1px solid var(--border-color); padding-left: 0.75rem;">Painel de Gestão</span>
        </a>

        <div style="display: flex; align-items: center; gap: 1rem;">
            <div class="nav-links">
                <a href="/admin/{{ slug }}/configuracoes" class="nav-link-item">⚙️ Configurações</a>
                <a href="/admin/{{ slug }}/cardapio" class="nav-link-item">📖 Cardápio</a>
                <a href="/admin/{{ slug }}/pedidos" class="nav-link-item">📦 Pedidos</a>
                <a href="/admin/{{ slug }}/pagamento" class="nav-link-item">💳 Pagamentos</a>
                <a href="/admin/{{ slug }}/registro" class="nav-link-item">📋 Registro</a>
                <a href="/admin/{{ slug }}/analise" class="nav-link-item">📊 Análise</a>
                <a href="/admin/{{ slug }}/delivery" class="nav-link-item">🛵 Delivery</a>
                <a href="/admin/{{ slug }}/backup" class="nav-link-item">💾 Backup</a>
                <a href="/admin/{{ slug }}/qr-codes" class="nav-link-item">📱 QR Codes</a>
            </div>

            <!-- Botão Flutuante Discreto de Tema -->
            <div class="theme-dropdown-container">
                <button class="theme-toggle-btn" onclick="toggleThemeMenu()">
                    🎨 <span id="currentThemeLabel">Tema</span> ▾
                </button>
                <div id="themeMenu" class="theme-menu-content">
                    <button class="theme-option" onclick="mudarTema('dark', 'Midnight Blue')">🌌 Midnight Blue (Escuro)</button>
                    <button class="theme-option" onclick="mudarTema('light', 'Clean Light')">☀️ Clean Light (Claro)</button>
                    <button class="theme-option" onclick="mudarTema('emerald', 'Emerald Restô')">🌿 Emerald Restô (Verde)</button>
                    <button class="theme-option" onclick="mudarTema('terracotta', 'Warm Terracotta')">🏺 Warm Terracotta (Quente)</button>
                </div>
            </div>
        </div>
    </header>

    <main>
        {% block content %}{% endblock %}
    </main>

    <script>
        function toggleThemeMenu() {
            document.getElementById('themeMenu').classList.toggle('show');
        }

        window.addEventListener('click', function(e) {
            if (!e.target.closest('.theme-dropdown-container')) {
                const menu = document.getElementById('themeMenu');
                if (menu && menu.classList.contains('show')) {
                    menu.classList.remove('show');
                }
            }
        });

        function aplicarTemaGlobal(tema, nomeExibicao) {
            if (tema === 'dark') {
                document.documentElement.removeAttribute('data-theme');
            } else {
                document.documentElement.setAttribute('data-theme', tema);
            }
            if (nomeExibicao) {
                document.getElementById('currentThemeLabel').innerText = nomeExibicao;
            }
        }

        function mudarTema(tema, nomeExibicao) {
            aplicarTemaGlobal(tema, nomeExibicao);
            localStorage.setItem('cardapio_pro_theme', tema);
            localStorage.setItem('cardapio_pro_theme_name', nomeExibicao);
            document.getElementById('themeMenu').classList.remove('show');
        }

        window.addEventListener('DOMContentLoaded', () => {
            const temaSalvo = localStorage.getItem('cardapio_pro_theme') || 'dark';
            const nomeSalvo = localStorage.getItem('cardapio_pro_theme_name') || 'Midnight Blue';
            aplicarTemaGlobal(temaSalvo, nomeSalvo);
        });
    </script>

<script>
document.addEventListener("DOMContentLoaded", function() {
    const pathSegments = window.location.pathname.split("/");
    // Se estiver em /admin/slug/pagina, extrai o slug
    if (pathSegments.length >= 3 && pathSegments[1] === "admin" && pathSegments[2] !== "") {
        const currentSlug = pathSegments[2];
        document.querySelectorAll("nav a, .menu a, a[href*=\"/admin/\}").forEach(a => {
            let href = a.getAttribute("href");
            if (href && href.startsWith("/admin/") && !href.includes(currentSlug)) {
                // Substitui barras duplas ou links quebrados por /admin/slug/rota
                const cleanHref = href.replace(/\/admin\/+(\{\{\s*slug\s*\}\})?\/?/, "/admin/" + currentSlug + "/");
                a.setAttribute("href", cleanHref);
            }
        });
    }
});
</script>
</body>
</html>

```

---

## Arquivo: `./templates/cardapio.html`

```text
{% extends "base.html" %}
{% block content %}
<h2>Gerenciamento do Cardápio</h2>
<div style="margin-bottom: 20px;">
    <a href="/admin/cardapio/arquivados" style="padding: 8px 15px; background: #607D8B; color: white; text-decoration: none; border-radius: 4px;">📦 Ver Itens Arquivados</a>
</div>

<form method="POST" style="margin-bottom: 20px;">
    <input type="text" name="nome" placeholder="Nome do prato/bebida" required style="padding:8px; width:250px;">
    <input type="number" step="0.01" name="preco" placeholder="Preço (R$)" required style="padding:8px; width:120px;">
    <button type="submit" style="padding:9px 15px; background:#2196F3; color:white; border:none; border-radius:4px; cursor:pointer;">Adicionar Item</button>
</form>

<h3>Itens Ativos no Cardápio:</h3>
<table style="width:100%; border-collapse: collapse; margin-top: 10px;">
    <tr style="background: #eee; text-align: left;">
        <th style="padding: 8px; border: 1px solid #ddd;">Nome</th>
        <th style="padding: 8px; border: 1px solid #ddd;">Preço</th>
        <th style="padding: 8px; border: 1px solid #ddd; text-align: center;">Ações</th>
    </tr>
    {% for item in itens %}
    <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">{{ item.nome }}</td>
        <td style="padding: 8px; border: 1px solid #ddd;">R$ {{ "%.2f"|format(item.preco) }}</td>
        <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">
            <form action="/admin/cardapio/arquivar/{{ item.id }}" method="POST" style="display:inline;">
                <button type="submit" style="background: #ff9800; color: white; border: none; padding: 5px 10px; border-radius: 3px; cursor: pointer;">Arquivar</button>
            </form>
        </td>
    </tr>
    {% else %}
    <tr>
        <td colspan="3" style="padding: 15px; text-align: center; border: 1px solid #ddd;">Nenhum item ativo cadastrado.</td>
    </tr>
    {% endfor %}
</table>
{% endblock %}

```

---

## Arquivo: `./templates/cardapio_admin.html`

```text
{% extends "base.html" %}

{% block title %}Gerenciar Cardápio - Cardápio Pro{% endblock %}

{% block content %}
<style>
    .cardapio-grid {
        display: grid;
        grid-template-columns: 1fr 1.6fr;
        gap: 2rem;
        align-items: start;
    }
    @media (max-width: 960px) {
        .cardapio-grid {
            grid-template-columns: 1fr !important;
        }
    }
    
    .dynamic-card {
        background-color: var(--bg-card);
        border: 1px solid var(--border-color);
        border-radius: 16px;
        padding: 2rem;
        box-shadow: var(--shadow);
        transition: background-color 0.3s ease, border-color 0.3s ease;
    }

    .tab-container {
        display: flex;
        gap: 0.75rem;
        align-items: center;
        margin-bottom: 2rem;
    }

    .tab-btn {
        padding: 0.6rem 1.25rem;
        border-radius: 10px;
        font-size: 0.85rem;
        font-weight: 600;
        cursor: pointer;
        border: 1px solid var(--border-color);
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 0.5rem;
        transition: all 0.2s;
    }
    .tab-ativo {
        background: var(--accent-grad);
        color: var(--accent-text) !important;
        border-color: var(--accent-color);
        box-shadow: 0 4px 15px rgba(245, 158, 11, 0.25);
    }
    .tab-inativo {
        background: var(--bg-card);
        color: var(--text-muted);
    }
    .tab-inativo:hover {
        color: var(--text-main);
        border-color: var(--accent-color);
        background: var(--input-bg);
    }

    .form-group {
        margin-bottom: 1.25rem;
    }

    .form-label {
        display: block;
        font-size: 0.85rem;
        font-weight: 500;
        color: var(--text-muted);
        margin-bottom: 0.4rem;
    }

    .form-control-pro {
        width: 100%;
        padding: 0.8rem 1rem;
        background-color: var(--input-bg);
        border: 1px solid var(--border-color);
        border-radius: 10px;
        color: var(--input-text);
        font-size: 0.9rem;
        outline: none;
        box-sizing: border-box;
        transition: all 0.2s;
    }
    .form-control-pro:focus {
        border-color: var(--accent-color);
        box-shadow: 0 0 0 3px rgba(245, 158, 11, 0.15);
    }
</style>

<!-- Abas de Navegação Superior do Cardápio -->
<div class="tab-container">
    <a href="/admin/cardapio?tab=ativos" class="tab-btn {% if tab == 'ativos' %}tab-ativo{% else %}tab-inativo{% endif %}">
        🍽️ Produtos Ativos
    </a>
    <a href="/admin/cardapio?tab=arquivados" class="tab-btn {% if tab == 'arquivados' %}tab-ativo{% else %}tab-inativo{% endif %}">
        📦 Arquivados & Lixeira
    </a>
</div>

<div class="cardapio-grid">

    <!-- Formulário de Cadastro -->
    {% if tab == 'ativos' %}
    <div class="dynamic-card">
        <h2 style="font-size: 1.2rem; color: var(--text-main); font-weight: 700; margin-top: 0; margin-bottom: 1.5rem; border-bottom: 1px solid var(--border-color); padding-bottom: 0.85rem; display: flex; align-items: center; gap: 0.5rem;">
            ➕ Cadastrar Novo Item
        </h2>
        
        <form action="/admin/cardapio/adicionar" method="POST" enctype="multipart/form-data">
            <div class="form-group">
                <label for="nome" class="form-label">Nome do Prato/Bebida</label>
                <input type="text" id="nome" name="nome" placeholder="Ex: Batata Frita com Cheddar" required class="form-control-pro">
            </div>

            <div class="form-group">
                <label for="categoria" class="form-label">Categoria</label>
                <input type="text" id="categoria" name="categoria" placeholder="Ex: Porções, Bebidas" required class="form-control-pro">
            </div>

            <div class="form-group">
                <label for="preco" class="form-label">Preço (R$)</label>
                <input type="number" step="0.01" id="preco" name="preco" placeholder="0.00" required class="form-control-pro">
            </div>

            <div class="form-group">
                <label for="foto_arquivo" class="form-label">📁 Upload de Foto (Armazenamento)</label>
                <input type="file" id="foto_arquivo" name="foto_arquivo" accept="image/*" class="form-control-pro" style="padding: 0.55rem; color: var(--text-muted);">
            </div>

            <div class="form-group">
                <label for="foto_url" class="form-label">🔗 Ou Link da Foto (URL)</label>
                <input type="url" id="foto_url" name="foto_url" placeholder="https://exemplo.com/foto.jpg" class="form-control-pro">
            </div>

            <div class="form-group" style="margin-bottom: 1.75rem;">
                <label for="descricao" class="form-label">Descrição</label>
                <input type="text" id="descricao" name="descricao" placeholder="Ingredientes e detalhes..." class="form-control-pro">
            </div>

            <button type="submit" style="width: 100%; background: var(--accent-grad); color: var(--accent-text); font-weight: 600; padding: 0.85rem; border: none; border-radius: 10px; cursor: pointer; font-size: 0.95rem; box-shadow: 0 4px 15px rgba(245, 158, 11, 0.25); transition: opacity 0.2s;">
                Cadastrar Produto
            </button>
        </form>
    </div>
    {% endif %}

    <!-- Lista de Produtos -->
    <div class="dynamic-card" style="{% if tab == 'ativos' %}grid-column: span 1;{% else %}grid-column: span 2;{% endif %}">
        <h2 style="font-size: 1.2rem; color: var(--text-main); font-weight: 700; margin-top: 0; margin-bottom: 1.5rem; border-bottom: 1px solid var(--border-color); padding-bottom: 0.85rem;">
            {% if tab == 'ativos' %}📖 Itens Ativos no Cardápio{% else %}📦 Produtos Arquivados{% endif %}
        </h2>
        
        {% if not produtos %}
            <p style="color: var(--text-muted); font-size: 0.9rem;">Nenhum produto encontrado nesta categoria.</p>
        {% else %}
            <div style="display: flex; flex-direction: column; gap: 1rem;">
                {% for p in produtos %}
                <div style="background: var(--input-bg); border: 1px solid var(--border-color); border-radius: 12px; padding: 1.25rem; display: flex; flex-direction: column; gap: 1rem; transition: border-color 0.2s;">
                    
                    <div style="display: flex; align-items: flex-start; gap: 1rem;">
                        {% if p.foto %}
                            <img src="{{ p.foto }}" alt="{{ p.nome }}" style="width: 70px; height: 70px; border-radius: 10px; object-fit: cover; border: 1px solid var(--border-color); flex-shrink: 0;">
                        {% else %}
                            <div style="width: 70px; height: 70px; border-radius: 10px; background: var(--bg-card); display: flex; align-items: center; justify-content: center; font-size: 1.6rem; flex-shrink: 0; border: 1px solid var(--border-color);">🍽️</div>
                        {% endif %}
                        
                        <div style="flex-grow: 1; min-width: 0;">
                            <div style="display: flex; align-items: center; justify-content: space-between; gap: 0.5rem; flex-wrap: wrap;">
                                <h4 style="font-size: 1rem; color: var(--text-main); margin: 0; word-break: break-word; font-weight: 600;">{{ p.nome }}</h4>
                                <span style="font-size: 0.75rem; background: var(--bg-card); padding: 0.2rem 0.6rem; border-radius: 6px; color: var(--text-muted); font-weight: 500; border: 1px solid var(--border-color);">{{ p.categoria }}</span>
                            </div>
                            
                            <p style="font-size: 0.85rem; color: var(--text-muted); margin-top: 0.4rem; word-break: break-word; line-height: 1.4;">{{ p.descricao or 'Sem descrição' }}</p>
                            
                            <div style="display: flex; align-items: center; justify-content: space-between; margin-top: 0.75rem; flex-wrap: wrap; gap: 0.5rem;">
                                <span style="font-weight: 700; color: var(--accent-color); font-size: 1.05rem;">R$ {{ "%.2f"|format(p.preco) }}</span>
                                {% if tab == 'ativos' %}
                                    <span style="font-size: 0.75rem; padding: 0.2rem 0.6rem; border-radius: 6px; font-weight: 500; background: {% if p.visivel == False %}rgba(239, 68, 68, 0.15); color: #f87171;{% else %}rgba(16, 185, 129, 0.15); color: #34d399;{% endif %}">
                                        {% if p.visivel == False %}Oculto do Cliente{% else %}Visível para Cliente{% endif %}
                                    </span>
                                {% endif %}
                            </div>
                        </div>
                    </div>

                    <div style="display: flex; gap: 0.75rem; justify-content: flex-end; border-top: 1px solid var(--border-color); padding-top: 0.85rem;">
                        {% if tab == 'ativos' %}
                            <form action="/admin/cardapio/toggle_visibilidade/{{ p.id }}" method="POST" style="margin: 0; flex: 1;">
                                <button type="submit" style="width: 100%; background-color: var(--bg-card); color: var(--text-main); border: 1px solid var(--border-color); padding: 0.55rem; font-size: 0.8rem; border-radius: 8px; cursor: pointer; font-weight: 600; transition: background 0.15s;">
                                    {% if p.visivel == False %}👁️ Mostrar{% else %}🙈 Ocultar{% endif %}
                                </button>
                            </form>

                            <form action="/admin/cardapio/arquivar/{{ p.id }}" method="POST" style="margin: 0; flex: 1;">
                                <button type="submit" style="width: 100%; background-color: rgba(239, 68, 68, 0.15); color: #f87171; border: 1px solid rgba(239, 68, 68, 0.3); padding: 0.55rem; font-size: 0.8rem; border-radius: 8px; cursor: pointer; font-weight: 600;">
                                    📦 Arquivar
                                </button>
                            </form>
                        {% else %}
                            <form action="/admin/cardapio/desarquivar/{{ p.id }}" method="POST" style="margin: 0; flex: 1;">
                                <button type="submit" style="width: 100%; background-color: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); padding: 0.55rem; font-size: 0.8rem; border-radius: 8px; cursor: pointer; font-weight: 600;">
                                    📂 Desarquivar
                                </button>
                            </form>

                            <form action="/admin/cardapio/excluir/{{ p.id }}" method="POST" style="margin: 0; flex: 1;" onsubmit="return confirm('Deseja excluir definitivamente este cadastro?');">
                                <button type="submit" style="width: 100%; background-color: rgba(127, 29, 29, 0.4); color: #fca5a5; border: 1px solid rgba(127, 29, 29, 0.6); padding: 0.55rem; font-size: 0.8rem; border-radius: 8px; cursor: pointer; font-weight: 600;">
                                    🗑️ Excluir
                                </button>
                            </form>
                        {% endif %}
                    </div>

                </div>
                {% endfor %}
            </div>
        {% endif %}
    </div>

</div>
{% endblock %}

```

---

## Arquivo: `./templates/cardapio_arquivados.html`

```text
{% extends "base.html" %}
{% block content %}
<h2>Itens Arquivados</h2>
<div style="margin-bottom: 20px;">
    <a href="/admin/cardapio" style="padding: 8px 15px; background: #2196F3; color: white; text-decoration: none; border-radius: 4px;">⬅️ Voltar ao Cardápio Ativo</a>
</div>

<table style="width:100%; border-collapse: collapse; margin-top: 10px;">
    <tr style="background: #eee; text-align: left;">
        <th style="padding: 8px; border: 1px solid #ddd;">Nome</th>
        <th style="padding: 8px; border: 1px solid #ddd;">Preço</th>
        <th style="padding: 8px; border: 1px solid #ddd; text-align: center;">Ações</th>
    </tr>
    {% for item in itens %}
    <tr>
        <td style="padding: 8px; border: 1px solid #ddd;">{{ item.nome }}</td>
        <td style="padding: 8px; border: 1px solid #ddd;">R$ {{ "%.2f"|format(item.preco) }}</td>
        <td style="padding: 8px; border: 1px solid #ddd; text-align: center;">
            <form action="/admin/cardapio/desarquivar/{{ item.id }}" method="POST" style="display:inline; margin-right: 5px;">
                <button type="submit" style="background: #4CAF50; color: white; border: none; padding: 5px 10px; border-radius: 3px; cursor: pointer;">Desarquivar</button>
            </form>
            <form action="/admin/cardapio/excluir/{{ item.id }}" method="POST" style="display:inline;" onsubmit="return confirm('Deseja excluir definitivamente este item?');">
                <button type="submit" style="background: #f44336; color: white; border: none; padding: 5px 10px; border-radius: 3px; cursor: pointer;">Excluir</button>
            </form>
        </td>
    </tr>
    {% else %}
    <tr>
        <td colspan="3" style="padding: 15px; text-align: center; border: 1px solid #ddd;">Nenhum item arquivado.</td>
    </tr>
    {% endfor %}
</table>
{% endblock %}

```

---

## Arquivo: `./templates/cardapio_cliente.html`

```text
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cardápio - Mesa {{ mesa }} | {{ nome_restaurante }}</title>
    <link rel="stylesheet" href="/static/css/style.css">
</head>
<body>
    <header style="background: #1e293b; color: white; padding: 1rem; text-align: center;">
        <h1 style="font-size: 1.4rem; margin-bottom: 0.2rem;">{{ nome_restaurante }}</h1>
        <p style="font-size: 0.9rem; color: #cbd5e1;">Mesa Atendida: <strong>{{ mesa }}</strong></p>
    </header>

    <div class="container" style="max-width: 600px; padding-bottom: 120px;">
        
        {% if request.query_params.get('sucesso') %}
        <div style="background: #dcfce7; border: 1px solid #bbf7d0; color: #16a34a; padding: 1rem; border-radius: 8px; margin-bottom: 1.5rem; text-align: center;">
            Pedido realizado com sucesso! A cozinha já está preparando.
        </div>
        {% endif %}

        <h2 style="margin-bottom: 1rem; font-size: 1.2rem; color: #334155;">Nosso Cardápio</h2>

        {% if not produtos %}
            <p style="text-align: center; color: #64748b;">Nenhum produto disponível no momento.</p>
        {% else %}
            <form id="form-pedido" action="/mesa/{{ mesa }}/pedir" method="POST">
                <input type="hidden" id="itens_pedido" name="itens_pedido">
                <input type="hidden" id="total" name="total">

                <div style="display: flex; flex-direction: column; gap: 1rem;">
                    {% for p in produtos %}
                    <div style="background: white; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
                        <div style="flex: 1; padding-right: 1rem;">
                            <h4 style="font-size: 1.05rem; color: #1e293b;">{{ p.nome }}</h4>
                            <p style="font-size: 0.85rem; color: #64748b; margin: 0.2rem 0;">{{ p.descricao or '' }}</p>
                            <span style="font-weight: 600; color: #16a34a;">R$ {{ "%.2f"|format(p.preco) }}</span>
                        </div>
                        <div style="display: flex; align-items: center; gap: 0.5rem;">
                            <button type="button" onclick="alterarQtd('{{ p.id }}', -1)" style="padding: 0.3rem 0.6rem; background: #e2e8f0; color: #334155; border: none; border-radius: 4px; cursor: pointer;">-</button>
                            <span id="qtd-{{ p.id }}" style="font-weight: 600; min-width: 20px; text-align: center;">0</span>
                            <button type="button" onclick="alterarQtd('{{ p.id }}', 1)" style="padding: 0.3rem 0.6rem; background: #2563eb; color: white; border: none; border-radius: 4px; cursor: pointer;">+</button>
                        </div>
                    </div>
                    {% endfor %}
                </div>

                <!-- Seção de Forma de Pagamento -->
                <div style="background: white; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1rem; margin-top: 1.5rem; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
                    <label for="forma_pagamento" style="display: block; font-weight: 600; margin-bottom: 0.5rem; color: #1e293b;">Forma de Pagamento:</label>
                    <select id="forma_pagamento" name="forma_pagamento" style="width: 100%; padding: 0.6rem; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 1rem;">
                        <option value="PIX">PIX</option>
                        <option value="Cartão de Crédito">Cartão de Crédito</option>
                        <option value="Cartão de Débito">Cartão de Débito</option>
                        <option value="Dinheiro">Dinheiro</option>
                    </select>
                </div>

                <!-- Barra Fixa inferior -->
                <div style="position: fixed; bottom: 0; left: 0; right: 0; background: white; border-top: 1px solid #cbd5e1; padding: 1rem; display: flex; justify-content: space-between; align-items: center; box-shadow: 0 -4px 6px -1px rgba(0,0,0,0.05);">
                    <div>
                        <span style="font-size: 0.9rem; color: #64748b; display: block;">Total do Pedido:</span>
                        <strong id="span-total" style="font-size: 1.2rem; color: #1e293b;">R$ 0.00</strong>
                    </div>
                    <button type="submit" id="btn-enviar" style="background: #16a34a; color: white; border: none; padding: 0.75rem 1.5rem; border-radius: 6px; font-size: 1rem; opacity: 0.5; pointer-events: none; cursor: pointer;">Enviar Pedido</button>
                </div>
            </form>
        {% endif %}
    </div>

    <script>
        const carrinho = {};

        function alterarQtd(id, delta) {
            if (!carrinho[id]) carrinho[id] = 0;
            carrinho[id] += delta;
            if (carrinho[id] < 0) carrinho[id] = 0;

            document.getElementById(`qtd-${id}`).innerText = carrinho[id];
            recalcularTotal();
        }

        function recalcularTotal() {
            let total = 0;
            let textoPedidos = "";
            
            {% for p in produtos %}
            {
                let q = carrinho['{{ p.id }}'] || 0;
                if (q > 0) {
                    let sub = q * {{ p.preco }};
                    total += sub;
                    textoPedidos += `${q}x {{ p.nome }} (R$ {{ "%.2f"|format(p.preco) }})\n`;
                }
            }
            {% endfor %}

            document.getElementById('span-total').innerText = `R$ ${total.toFixed(2)}`;
            document.getElementById('total').value = total.toFixed(2);
            document.getElementById('itens_pedido').value = textoPedidos;

            const btnEnviar = document.getElementById('btn-enviar');
            if (total > 0) {
                btnEnviar.style.opacity = '1';
                btnEnviar.style.pointerEvents = 'auto';
            } else {
                btnEnviar.style.opacity = '0.5';
                btnEnviar.style.pointerEvents = 'none';
            }
        }
    </script>
</body>
</html>

```

---

## Arquivo: `./templates/cardapio_digital.html`

```text
{% extends "base.html" if t != "index" and t != "cardapio_digital" else "" %}
{% block content %}
<h2>Página: cardapio_digital</h2>
<p>Conteúdo da seção cardapio_digital carregado com sucesso.</p>
{% endblock %}

```

---

## Arquivo: `./templates/configuracao.html`

```text
{% extends "base.html" %}
{% block content %}
<div class="max-w-xl mx-auto px-4 py-12">
    
    <!-- Cabeçalho -->
    <div class="mb-8 text-center">
        <div class="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-amber-500/10 text-amber-500 text-2xl mb-4 border border-amber-500/20">
            ⚙️
        </div>
        <h1 class="text-2xl sm:text-3xl font-extrabold tracking-tight" style="color: var(--text-main, #ffffff);">Configurações</h1>
        <p class="text-sm mt-2" style="color: var(--text-muted, #9ca3af);">Gerencie os dados principais do estabelecimento com precisão.</p>
    </div>

    <!-- Alerta de Sucesso -->
    {% if request.query_params.get('sucesso') == 'true' or sucesso %}
    <div id="toast-sucesso" class="mb-6 p-4 rounded-xl bg-emerald-500/20 border border-emerald-500/40 text-emerald-300 text-sm font-semibold flex items-center justify-center space-x-2 shadow-lg">
        <span>✅</span>
        <span>Alterações salvas com sucesso!</span>
    </div>
    {% endif %}

    <!-- Formulário apontando explicitamente para a URL base de configurações -->
    <form method="POST" action="" style="display: flex; flex-direction: column; gap: 24px;">
        
        <div style="display: flex; flex-direction: column; gap: 8px;">
            <label style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-main, #fbbf24);">Nome do Estabelecimento</label>
            <input type="text" name="nome_restaurante" value="{{ estabelecimento.nome_restaurante if estabelecimento else (estabelecimento.nome if estabelecimento else '') }}" 
                   style="width: 100%; padding: 14px 16px; border-radius: 12px; background: var(--bg-card, rgba(0, 0, 0, 0.3)); color: var(--text-main, #ffffff); border: 1px solid var(--border-color, rgba(255, 255, 255, 0.15)); font-size: 0.95rem; outline: none;">
        </div>

        <div style="display: flex; flex-direction: column; gap: 8px;">
            <label style="font-size: 0.75rem; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: var(--text-main, #fbbf24);">Total de Mesas</label>
            <input type="number" name="quantidade_mesas" value="{{ estabelecimento.quantidade_mesas if estabelecimento else (estabelecimento.mesas if estabelecimento else 5) }}" 
                   style="width: 100%; padding: 14px 16px; border-radius: 12px; background: var(--bg-card, rgba(0, 0, 0, 0.3)); color: var(--text-main, #ffffff); border: 1px solid var(--border-color, rgba(255, 255, 255, 0.15)); font-size: 0.95rem; outline: none;">
            <span style="font-size: 0.8rem; color: var(--text-muted, #9ca3af); margin-top: 4px;">Define a quantidade total de QR Codes gerados para o salão.</span>
        </div>

        <div style="padding-top: 12px;">
            <button type="submit" style="width: 100%; padding: 16px; background: #f59e0b; color: #030712; font-weight: 800; font-size: 0.95rem; border-radius: 12px; border: none; cursor: pointer; box-shadow: 0 10px 25px -5px rgba(245, 158, 11, 0.3);">
                💾 Salvar Alterações
            </button>
        </div>

    </form>

</div>

<script>
    setTimeout(() => {
        const toast = document.getElementById('toast-sucesso');
        if (toast) {
            toast.style.transition = 'opacity 0.5s ease';
            toast.style.opacity = '0';
            setTimeout(() => toast.remove(), 500);
        }
    }, 4000);
</script>
{% endblock %}

```

---

## Arquivo: `./templates/delivery.html`

```text
{% extends "base.html" %}
{% block content %}
<div class="max-w-4xl mx-auto px-4 py-12">
    
    <!-- Cabeçalho limpo sem o painel de fundo -->
    <div class="mb-10 text-center">
        <div class="inline-flex items-center justify-center w-14 h-14 rounded-2xl bg-amber-500/10 text-amber-500 text-2xl mb-4 border border-amber-500/20">
            🛵
        </div>
        <h1 class="text-2xl sm:text-3xl font-extrabold tracking-tight" style="color: var(--text-main, #ffffff);">Painel de Delivery</h1>
        <p class="text-sm mt-2" style="color: var(--text-muted, #9ca3af);">Gerencie os pedidos e taxas de entrega externa do estabelecimento.</p>
    </div>

    <!-- Conteúdo fluido -->
    <div style="display: flex; flex-direction: column; gap: 24px; align-items: center; justify-content: center; padding: 40px 20px; border-radius: 24px; background: var(--bg-card, rgba(0, 0, 0, 0.2)); border: 1px solid var(--border-color, rgba(255, 255, 255, 0.08)); text-align: center;">
        
        <div style="font-size: 3rem; margin-bottom: -10px;">📦</div>
        
        <div>
            <h3 style="font-size: 1.1rem; font-weight: 700; color: var(--text-main, #ffffff); margin-bottom: 6px;">Nenhum pedido de delivery ativo no momento.</h3>
            <p style="font-size: 0.85rem; color: var(--text-muted, #9ca3af); max-width: 320px; margin: 0 auto;">As novas solicitações de entrega aparecerão automaticamente aqui.</p>
        </div>

    </div>

</div>
{% endblock %}

```

---

## Arquivo: `./templates/index.html`

```text
{% extends "base.html" if t != "index" and t != "cardapio_digital" else "" %}
{% block content %}
<h2>Página: index</h2>
<p>Conteúdo da seção index carregado com sucesso.</p>
{% endblock %}

```

---

## Arquivo: `./templates/pagamento.html`

```text
{% extends "base.html" if t != "index" and t != "cardapio_digital" else "" %}
{% block content %}
<h2>Página: pagamento</h2>
<p>Conteúdo da seção pagamento carregado com sucesso.</p>
{% endblock %}

```

---

## Arquivo: `./templates/painel.html`

```text
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Painel - Cardápio Pro</title>
    <style>
        :root {
            --bg-color: #121212;
            --surface-color: #1e1e1e;
            --primary-color: #ff9800;
            --text-color: #e0e0e0;
            --sidebar-width: 260px;
            --sidebar-collapsed-width: 70px;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            display: flex;
            height: 100vh;
            overflow: hidden;
        }

        /* Sidebar Retrátil */
        aside {
            width: var(--sidebar-width);
            background-color: var(--surface-color);
            border-right: 1px solid #2c2c2c;
            display: flex;
            flex-direction: column;
            transition: width 0.3s ease;
            z-index: 100;
        }

        aside.collapsed {
            width: var(--sidebar-collapsed-width);
        }

        .sidebar-header {
            padding: 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            border-bottom: 1px solid #2c2c2c;
        }

        .sidebar-header h2 {
            font-size: 1.2rem;
            color: var(--primary-color);
            white-space: nowrap;
            overflow: hidden;
            transition: opacity 0.3s ease;
        }

        aside.collapsed .sidebar-header h2 {
            opacity: 0;
            pointer-events: none;
            width: 0;
        }

        .toggle-btn {
            background: none;
            border: none;
            color: var(--text-color);
            font-size: 1.5rem;
            cursor: pointer;
            padding: 5px;
        }

        /* Menus da Sidebar */
        .sidebar-menu {
            list-style: none;
            padding: 15px 0;
            flex-grow: 1;
            overflow-y: auto;
        }

        .sidebar-menu li {
            padding: 12px 20px;
            display: flex;
            align-items: center;
            cursor: pointer;
            transition: background 0.2s;
            white-space: nowrap;
        }

        .sidebar-menu li:hover {
            background-color: rgba(255, 152, 0, 0.1);
            color: var(--primary-color);
        }

        .sidebar-menu li span.icon {
            font-size: 1.3rem;
            min-width: 30px;
            text-align: center;
        }

        .sidebar-menu li span.text {
            margin-left: 10px;
            transition: opacity 0.3s ease;
        }

        aside.collapsed .sidebar-menu li span.text {
            opacity: 0;
            pointer-events: none;
            display: none;
        }

        /* Conteúdo Principal */
        main {
            flex-grow: 1;
            display: flex;
            flex-direction: column;
            overflow-y: auto;
        }

        header {
            background-color: var(--surface-color);
            padding: 15px 30px;
            border-bottom: 1px solid #2c2c2c;
            font-size: 1.1rem;
            font-weight: 600;
        }

        .content-area {
            padding: 30px;
        }

        .card {
            background-color: var(--surface-color);
            padding: 20px;
            border-radius: 8px;
            border: 1px solid #2c2c2c;
        }
    </style>
</head>
<body>

    <!-- Sidebar Retrátil -->
    <aside id="sidebar">
        <div class="sidebar-header">
            <h2>Cardápio Pro</h2>
            <button class="toggle-btn" onclick="toggleSidebar()">☰</button>
        </div>
        <ul class="sidebar-menu">
            <li onclick="carregarSecao('Configurações')">
                <span class="icon">⚙️</span>
                <span class="text">Configurações</span>
            </li>
            <li onclick="carregarSecao('Cardápio')">
                <span class="icon">📖</span>
                <span class="text">Cardápio</span>
            </li>
            <li onclick="carregarSecao('Pedido')">
                <span class="icon">🛒</span>
                <span class="text">Pedido</span>
            </li>
            <li onclick="carregarSecao('Pagamentos')">
                <span class="icon">💳</span>
                <span class="text">Pagamentos</span>
            </li>
            <li onclick="carregarSecao('Registro')">
                <span class="icon">📋</span>
                <span class="text">Registro</span>
            </li>
            <li onclick="carregarSecao('Analisar')">
                <span class="icon">📊</span>
                <span class="text">Analisar</span>
            </li>
            <li onclick="carregarSecao('QR Code')">
                <span class="icon">📷</span>
                <span class="text">QR Code</span>
            </li>
            <li onclick="carregarSecao('Backup')">
                <span class="icon">💾</span>
                <span class="text">Backup</span>
            </li>
        </ul>
    </aside>

    <!-- Área Principal -->
    <main>
        <header id="header-title">Painel de Controle</header>
        <div class="content-area">
            <div class="card">
                <h3 id="section-title">Bem-vindo ao sistema</h3>
                <p id="section-desc" style="margin-top: 10px; color: #a0a0a0;">Selecione um menu na barra lateral para começar.</p>
            </div>
        </div>
    </main>

                                <script>
        function toggleSidebar() {
            const sidebar = document.getElementById('sidebar');
            sidebar.classList.toggle('collapsed');
        }

        // Inicializa dados globais no localStorage se não existirem
        if (!localStorage.getItem('produtos')) {
            localStorage.setItem('produtos', JSON.stringify([]));
        }
        if (!localStorage.getItem('historico_pagamentos')) {
            localStorage.setItem('historico_pagamentos', JSON.stringify([]));
        }
        if (!localStorage.getItem('banco_memoria_backup')) {
            localStorage.setItem('banco_memoria_backup', JSON.stringify([]));
        }

        // Simulação de verificação automática de backup às 04:00 AM (ou verificação de 24h)
        verificarBackupAutomaticoDiario();

        function carregarSecao(nome) {
            document.getElementById('header-title').innerText = nome;
            const contentArea = document.querySelector('.content-area');

            if (nome === 'Configurações') {
                const nomeEstabelecimento = localStorage.getItem('nome_estabelecimento') || '';
                const qtdRemessas = localStorage.getItem('qtd_remessas') || '';

                contentArea.innerHTML = `
                    <div class="card">
                        <h3 style="color: var(--primary-color); margin-bottom: 15px;">Configurações do Estabelecimento</h3>
                        <form id="config-form" onsubmit="salvarConfiguracoes(event)" style="display: flex; flex-direction: column; gap: 15px; max-width: 400px;">
                            <div>
                                <label style="display: block; margin-bottom: 5px; color: #a0a0a0;">Nome do Estabelecimento:</label>
                                <input type="text" id="nome_est" value="${nomeEstabelecimento}" required style="width: 100%; padding: 10px; background: #2c2c2c; border: 1px solid #444; color: #fff; border-radius: 5px;">
                            </div>
                            <div>
                                <label style="display: block; margin-bottom: 5px; color: #a0a0a0;">Quantidade de Mesas / Remessas:</label>
                                <input type="number" id="qtd_rem" value="${qtdRemessas}" required min="1" style="width: 100%; padding: 10px; background: #2c2c2c; border: 1px solid #444; color: #fff; border-radius: 5px;">
                            </div>
                            <button type="submit" style="padding: 10px; background: var(--primary-color); border: none; color: #121212; font-weight: bold; border-radius: 5px; cursor: pointer;">Salvar Configurações</button>
                        </form>
                        <div id="msg-sucesso" style="margin-top: 10px; color: #4caf50; display: none;">Salvo com sucesso!</div>
                    </div>
                `;
            } else if (nome === 'Cardápio') {
                renderizarTelaCardapio('ativos');
            } else if (nome === 'Pedido') {
                const qtdRemessas = localStorage.getItem('qtd_remessas') || '0';
                const nomeEstabelecimento = localStorage.getItem('nome_estabelecimento') || 'Estabelecimento';
                const mesasPagas = JSON.parse(localStorage.getItem('mesas_pagas')) || [];

                let mesasHtml = '';
                for (let i = 1; i <= parseInt(qtdRemessas); i++) {
                    if (mesasPagas.includes(i)) continue;

                    mesasHtml += `
                        <div style="background: #252525; border: 1px solid #333; padding: 15px; border-radius: 8px; display: flex; flex-direction: column; justify-content: space-between; gap: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
                            <div style="display: flex; justify-content: space-between; align-items: center;">
                                <span style="font-weight: bold; color: var(--primary-color); font-size: 1.1rem;">Mesa / Remessa #${i}</span>
                                <span style="background: #333; padding: 3px 8px; border-radius: 12px; font-size: 0.8rem; color: #4caf50;">Ativa</span>
                            </div>
                            <p style="font-size: 0.85rem; color: #a0a0a0;">${nomeEstabelecimento}</p>
                            <button onclick="abrirExtrato(${i})" style="padding: 8px; background: #333; border: 1px solid var(--primary-color); color: var(--primary-color); border-radius: 5px; cursor: pointer; font-weight: bold; transition: 0.2s;" onmouseover="this.style.background='var(--primary-color)'; this.style.color='#121212'" onmouseout="this.style.background='#333'; this.style.color='var(--primary-color)'">Ver Extrato</button>
                        </div>
                    `;
                }

                contentArea.innerHTML = `
                    <div class="card" style="position: relative;">
                        <h3 style="color: var(--primary-color); margin-bottom: 5px;">Controle de Mesas e Pedidos</h3>
                        <p style="color: #a0a0a0; margin-bottom: 20px;">Clique em "Ver Extrato" em uma mesa para visualizar os itens e imprimir.</p>
                        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 15px; max-height: 450px; overflow-y: auto; padding-right: 5px;">
                            ${parseInt(qtdRemessas) > 0 && mesasHtml !== '' ? mesasHtml : '<p style="color: #777;">Nenhuma mesa com pedido pendente no momento.</p>'}
                        </div>
                    </div>

                    <!-- Modal do Extrato -->
                    <div id="modal-extrato" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); z-index: 1000; justify-content: center; align-items: center;">
                        <div style="background: #1e1e1e; border: 1px solid #333; width: 400px; padding: 25px; border-radius: 10px; box-shadow: 0 10px 25px rgba(0,0,0,0.5);">
                            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #333; padding-bottom: 10px; margin-bottom: 15px;">
                                <h3 id="modal-titulo" style="color: var(--primary-color);">Extrato da Mesa</h3>
                                <button onclick="fecharExtrato()" style="background: none; border: none; color: #fff; font-size: 1.2rem; cursor: pointer;">✕</button>
                            </div>
                            <div id="extrato-conteudo" style="background: #121212; padding: 15px; border-radius: 6px; margin-bottom: 20px; font-family: monospace; color: #ddd; max-height: 200px; overflow-y: auto;">
                                <p>1x Prato Executivo - R$ 25,00</p>
                                <p>2x Refrigerante Lata - R$ 10,00</p>
                                <hr style="border: 0; border-top: 1px dashed #444; margin: 10px 0;">
                                <p style="font-weight: bold; color: var(--primary-color);">Total: R$ 35,00</p>
                            </div>
                            <div style="display: flex; gap: 10px;">
                                <button onclick="imprimirExtrato()" style="flex: 1; padding: 10px; background: var(--primary-color); border: none; color: #121212; font-weight: bold; border-radius: 5px; cursor: pointer;">🖨️ Imprimir</button>
                                <button onclick="fecharExtrato()" style="padding: 10px; background: #333; border: none; color: #fff; border-radius: 5px; cursor: pointer;">Fechar</button>
                            </div>
                        </div>
                    </div>
                `;
            } else if (nome === 'Pagamentos') {
                renderizarTelaPagamentos();
            } else if (nome === 'Registro') {
                renderizarTelaRegistro();
            } else if (nome === 'Análise') {
                renderizarTelaAnalise();
            } else if (nome === 'Backup') {
                renderizarTelaBackup();
            } 
        else if (nome === 'QR Code') {
            const qtdRemessas = parseInt(localStorage.getItem('qtd_remessas') || '0');
            if (qtdRemessas <= 0) {
                contentArea.innerHTML = `<div class="card" style="padding: 20px; background: #1e1e1e; color: #fff; border-radius: 8px;"><h3>QR Code das Mesas</h3><p style="color: #ff5252; margin-top: 10px;">Nenhuma mesa configurada. Vá em Configurações e defina a quantidade de mesas.</p></div>`;
                return;
            }

            let cardsHtml = '';
            for (let i = 1; i <= qtdRemessas; i++) {
                const linkMesa = `${window.location.origin}/cardapio?mesa=${i}`;
                const qrServerApi = `https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=${encodeURIComponent(linkMesa)}`;
                cardsHtml += `
                    <div class="card-qr-item" style="background: #222; padding: 15px; border-radius: 8px; border: 1px solid #444; text-align: center; page-break-inside: avoid;">
                        <h3 style="color: #ff9800; margin-bottom: 10px; font-size: 1.1rem;">Mesa / Remessa #${i}</h3>
                        <div style="background: #fff; padding: 10px; display: inline-block; border-radius: 6px; margin-bottom: 10px;">
                            <img src="${qrServerApi}" alt="QR Code Mesa ${i}" style="width: 160px; height: 160px; display: block; margin: 0 auto;">
                        </div>
                        <p style="color: #aaa; font-size: 0.75rem; word-break: break-all; margin: 0;">${linkMesa}</p>
                    </div>
                `;
            }

            contentArea.innerHTML = `
                <div style="display: flex; flex-direction: column; gap: 20px; padding: 10px; color: #fff; max-width: 900px; margin: 0 auto;">
                    <div class="card" style="background: #1e1e1e; padding: 20px; border-radius: 8px; border: 1px solid #333; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px;">
                        <div>
                            <h3 style="color: #ff9800; margin-bottom: 5px;">QR Codes de Todas as Mesas</h3>
                            <p style="color: #aaa; font-size: 0.9rem; margin: 0;">Visualize e imprima os QR Codes individuais de todas as mesas configuradas.</p>
                        </div>
                        <button onclick="imprimirTodosQRCodes()" style="padding: 12px 20px; background: #ff9800; color: #121212; font-weight: bold; border: none; border-radius: 5px; cursor: pointer;">🖨️ Imprimir Todos</button>
                    </div>

                    <div id="grid-qr-codes" style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 15px;">
                        ${cardsHtml}
                    </div>
                </div>
            `;
        }

        else {
                contentArea.innerHTML = `
                    <div class="card">
                        <h3 id="section-title">Gerenciamento de ${nome}</h3>
                        <p id="section-desc" style="margin-top: 10px; color: #a0a0a0;">Aqui você poderá visualizar e gerenciar todas as informações referentes a ${nome.toLowerCase()}.</p>
                    </div>
                `;
            }
        }

        function renderizarTelaBackup() {
            const contentArea = document.querySelector('.content-area');
            const bancoMemoria = JSON.parse(localStorage.getItem('banco_memoria_backup')) || [];

            let listaMemoriaHtml = '';
            if (bancoMemoria.length === 0) {
                listaMemoriaHtml = '<p style="color: #777; padding: 10px;">Nenhum registro armazenado permanentemente no banco de memória ainda.</p>';
            } else {
                bancoMemoria.slice().reverse().forEach(item => {
                    listaMemoriaHtml += `
                        <div style="background: #252525; border: 1px solid #333; padding: 12px 15px; border-radius: 6px; margin-bottom: 8px; display: flex; justify-content: space-between; align-items: center;">
                            <div>
                                <span style="color: var(--primary-color); font-weight: bold; font-size: 0.95rem;">Data: ${item.data}</span>
                                <span style="color: #a0a0a0; font-size: 0.85rem; margin-left: 10px;">Ano: ${item.ano} | Mês: ${item.mes}</span>
                                <p style="color: #fff; font-size: 0.9rem; margin-top: 4px;">Mesa #${item.mesa} - Total: R$ ${item.valorTotal.toFixed(2)} (${item.formaPagamento})</p>
                            </div>
                            <span style="background: #1a1a1a; color: #4caf50; padding: 4px 8px; border-radius: 4px; font-size: 0.75rem; border: 1px solid #333;">Salvo Permanentemente</span>
                        </div>
                    `;
                });
            }

            contentArea.innerHTML = `
                <div style="display: grid; grid-template-columns: 1fr; gap: 20px;">
                    <div class="card">
                        <h3 style="color: var(--primary-color); margin-bottom: 5px;">Painel de Backup e Segurança</h3>
                        <p style="color: #a0a0a0; margin-bottom: 20px; font-size: 0.9rem;">Exporte os dados correntes em um arquivo compactado protegido por senha, limpe o histórico ativo e mantenha o registro permanente organizado.</p>
                        
                        <div style="background: #222; padding: 20px; border-radius: 8px; border: 1px solid #333; max-width: 500px; display: flex; flex-direction: column; gap: 15px;">
                            <div>
                                <label style="display: block; font-size: 0.85rem; color: #a0a0a0; margin-bottom: 5px;">Senha para Proteção do Arquivo ZIP:</label>
                                <input type="password" id="senha-backup" placeholder="Digite a senha de segurança" style="width: 100%; padding: 10px; background: #2c2c2c; border: 1px solid #444; color: #fff; border-radius: 5px;">
                            </div>
                            <button onclick="executarBackupManual()" style="padding: 12px; background: var(--primary-color); border: none; color: #121212; font-weight: bold; border-radius: 5px; cursor: pointer; display: flex; justify-content: center; align-items: center; gap: 8px;">
                                🔒 Realizar Backup, Baixar ZIP e Limpar Histórico
                            </button>
                            <p style="color: #777; font-size: 0.75rem; line-height: 1.4;">Nota: O sistema gera o arquivo compactado seguro para o computador, armazena permanentemente os dados no banco de memória interno e limpa os menus de Pagamento e Registro.</p>
                        </div>
                    </div>

                    <div class="card">
                        <h3 style="color: var(--primary-color); margin-bottom: 5px;">Banco de Memória Permanente</h3>
                        <p style="color: #a0a0a0; margin-bottom: 15px; font-size: 0.9rem;">Histórico consolidado organizado por dia, mês e ano que nunca é apagado.</p>
                        <div style="max-height: 350px; overflow-y: auto; padding-right: 5px;">
                            ${listaMemoriaHtml}
                        </div>
                    </div>
                </div>
            `;
        }

        function executarBackupManual() {
            const senha = document.getElementById('senha-backup').value;
            if (!senha) {
                alert('Por favor, informe uma senha para proteger o arquivo de backup.');
                return;
            }

            const historico = JSON.parse(localStorage.getItem('historico_pagamentos')) || [];
            if (historico.length === 0) {
                alert('Não há novos registros de pagamento ou transações para realizar o backup.');
                return;
            }

            // 1. Salva permanentemente no banco de memória (nunca apagado)
            let bancoMemoria = JSON.parse(localStorage.getItem('banco_memoria_backup')) || [];
            historico.forEach(item => {
                // item.data formato DD/MM/AAAA
                const partes = item.data.split('/');
                const dia = partes[0] || '01';
                const mes = partes[1] || '01';
                const ano = partes[2] || '2026';

                bancoMemoria.push({
                    ...item,
                    dia,
                    mes,
                    ano
                });
            });
            localStorage.setItem('banco_memoria_backup', JSON.stringify(bancoMemoria));

            // 2. Simula o download do arquivo ZIP compactado com senha
            const dadosStr = JSON.stringify(historico, null, 2);
            const blob = new Blob([dadosStr], { type: 'application/zip' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'backup_sistema_seguro_' + new Date().toISOString().slice(0,10) + '.zip';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
            URL.revokeObjectURL(url);

            // 3. Limpa o histórico de pagamentos e registro
            localStorage.setItem('historico_pagamentos', JSON.stringify([]));
            localStorage.setItem('mesas_pagas', JSON.stringify([]));

            alert('Backup executado com sucesso! Arquivo compactado baixado, dados salvos no banco de memória permanente e histórico ativo limpo.');
            renderizarTelaBackup();
        }

        function verificarBackupAutomaticoDiario() {
            // Simulação de verificação automática do agendamento das 04:00 da manhã
            const ultimoBackup = localStorage.getItem('ultimo_backup_auto');
            const hojeStr = new Date().toDateString();

            if (ultimoBackup !== hojeStr) {
                const historico = JSON.parse(localStorage.getItem('historico_pagamentos')) || [];
                if (historico.length > 0) {
                    let bancoMemoria = JSON.parse(localStorage.getItem('banco_memoria_backup')) || [];
                    historico.forEach(item => {
                        const partes = (item.data || '').split('/');
                        bancoMemoria.push({
                            ...item,
                            dia: partes[0] || '01',
                            mes: partes[1] || '01',
                            ano: partes[2] || '2026'
                        });
                    });
                    localStorage.setItem('banco_memoria_backup', JSON.stringify(bancoMemoria));
                    localStorage.setItem('historico_pagamentos', JSON.stringify([]));
                    localStorage.setItem('mesas_pagas', JSON.stringify([]));
                }
                localStorage.setItem('ultimo_backup_auto', hojeStr);
            }
        }

        function renderizarTelaAnalise() {
            const contentArea = document.querySelector('.content-area');
            const historico = JSON.parse(localStorage.getItem('historico_pagamentos')) || [];

            contentArea.innerHTML = `
                <div class="card" style="margin-bottom: 20px;">
                    <h3 style="color: var(--primary-color); margin-bottom: 5px;">Filtros de Análise</h3>
                    <p style="color: #a0a0a0; margin-bottom: 15px; font-size: 0.9rem;">Selecione o período desejado para filtrar o faturamento.</p>
                    
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)) 1fr auto; gap: 12px; align-items: end;">
                        <div>
                            <label style="display: block; font-size: 0.8rem; color: #a0a0a0; margin-bottom: 4px;">Ano:</label>
                            <select id="filtro-ano" style="width: 100%; padding: 8px; background: #2c2c2c; border: 1px solid #444; color: #fff; border-radius: 4px;">
                                <option value="">Todos os Anos</option>
                                <option value="2026">2026</option>
                                <option value="2025">2025</option>
                            </select>
                        </div>
                        <div>
                            <label style="display: block; font-size: 0.8rem; color: #a0a0a0; margin-bottom: 4px;">Mês:</label>
                            <select id="filtro-mes" style="width: 100%; padding: 8px; background: #2c2c2c; border: 1px solid #444; color: #fff; border-radius: 4px;">
                                <option value="">Todos os Meses</option>
                                <option value="01">Janeiro</option>
                                <option value="02">Fevereiro</option>
                                <option value="03">Março</option>
                                <option value="04">Abril</option>
                                <option value="05">Maio</option>
                                <option value="06">Junho</option>
                                <option value="07">Julho</option>
                                <option value="08">Agosto</option>
                                <option value="09">Setembro</option>
                                <option value="10">Outubro</option>
                                <option value="11">Novembro</option>
                                <option value="12">Dezembro</option>
                            </select>
                        </div>
                        <div>
                            <label style="display: block; font-size: 0.8rem; color: #a0a0a0; margin-bottom: 4px;">Dia (Início a Fim):</label>
                            <div style="display: flex; gap: 5px;">
                                <input type="number" id="filtro-dia-inicio" placeholder="De" min="1" max="31" style="width: 50%; padding: 8px; background: #2c2c2c; border: 1px solid #444; color: #fff; border-radius: 4px;">
                                <input type="number" id="filtro-dia-fim" placeholder="Até" min="1" max="31" style="width: 50%; padding: 8px; background: #2c2c2c; border: 1px solid #444; color: #fff; border-radius: 4px;">
                            </div>
                        </div>
                        <button onclick="aplicarFiltrosAnalise()" style="padding: 9px 15px; background: var(--primary-color); border: none; color: #121212; font-weight: bold; border-radius: 4px; cursor: pointer;">Filtrar</button>
                    </div>
                </div>

                <div id="cards-resultados-analise">
                    <!-- Cards inseridos dinamicamente -->
                </div>
            `;

            processarEExibirAnalise(historico);
        }

        function aplicarFiltrosAnalise() {
            const historico = JSON.parse(localStorage.getItem('historico_pagamentos')) || [];
            const anoSel = document.getElementById('filtro-ano').value;
            const mesSel = document.getElementById('filtro-mes').value;
            const diaIni = parseInt(document.getElementById('filtro-dia-inicio').value) || 0;
            const diaFim = parseInt(document.getElementById('filtro-dia-fim').value) || 0;

            const filtrado = historico.filter(item => {
                const partes = item.data.split('/');
                if (partes.length !== 3) return false;
                const d = parseInt(partes[0]);
                const m = partes[1];
                const a = partes[2];

                if (anoSel && a !== anoSel) return false;
                if (mesSel && m !== mesSel) return false;
                if (diaIni > 0 && d < diaIni) return false;
                if (diaFim > 0 && d > diaFim) return false;

                return true;
            });

            processarEExibirAnalise(filtrado);
        }

        function processarEExibirAnalise(dados) {
            let totalGeral = 0;
            let totalPix = 0;
            let totalCartao = 0;
            let totalDinheiro = 0;

            dados.forEach(item => {
                const val = parseFloat(item.valorTotal) || 0;
                totalGeral += val;
                if (item.formaPagamento.includes('Pix')) {
                    totalPix += val;
                } else if (item.formaPagamento.includes('Cartão')) {
                    totalCartao += val;
                } else if (item.formaPagamento.includes('Dinheiro')) {
                    totalDinheiro += val;
                }
            });

            const container = document.getElementById('cards-resultados-analise');
            container.innerHTML = `
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 15px; margin-bottom: 20px;">
                    <div style="background: #252525; border: 1px solid #333; padding: 20px; border-radius: 8px; border-left: 4px solid var(--primary-color);">
                        <span style="color: #a0a0a0; font-size: 0.85rem;">Faturamento Total</span>
                        <h2 style="color: #fff; margin-top: 5px; font-size: 1.5rem;">R$ ${totalGeral.toFixed(2)}</h2>
                        <span style="color: #777; font-size: 0.75rem;">${dados.length} transação(ões)</span>
                    </div>
                    <div style="background: #252525; border: 1px solid #333; padding: 20px; border-radius: 8px; border-left: 4px solid #4caf50;">
                        <span style="color: #a0a0a0; font-size: 0.85rem;">Total em PIX</span>
                        <h2 style="color: #4caf50; margin-top: 5px; font-size: 1.5rem;">R$ ${totalPix.toFixed(2)}</h2>
                    </div>
                    <div style="background: #252525; border: 1px solid #333; padding: 20px; border-radius: 8px; border-left: 4px solid #03a9f4;">
                        <span style="color: #a0a0a0; font-size: 0.85rem;">Total em Cartão</span>
                        <h2 style="color: #03a9f4; margin-top: 5px; font-size: 1.5rem;">R$ ${totalCartao.toFixed(2)}</h2>
                    </div>
                    <div style="background: #252525; border: 1px solid #333; padding: 20px; border-radius: 8px; border-left: 4px solid #ff9800;">
                        <span style="color: #a0a0a0; font-size: 0.85rem;">Total em Dinheiro</span>
                        <h2 style="color: #ff9800; margin-top: 5px; font-size: 1.5rem;">R$ ${totalDinheiro.toFixed(2)}</h2>
                    </div>
                </div>
            `;
        }

        function renderizarTelaRegistro() {
            const contentArea = document.querySelector('.content-area');
            const historico = JSON.parse(localStorage.getItem('historico_pagamentos')) || [];

            let linhasTabela = '';
            if (historico.length === 0) {
                linhasTabela = `<tr><td colspan="5" style="text-align: center; color: #777; padding: 20px;">Nenhuma transação registrada até o momento.</td></tr>`;
            } else {
                historico.slice().reverse().forEach(item => {
                    const trocoFormatado = item.troco > 0 ? `R$ ${item.troco.toFixed(2)}` : 'Nenhum';
                    linhasTabela += `
                        <tr style="border-bottom: 1px solid #333; transition: background 0.2s;" onmouseover="this.style.background='#222'" onmouseout="this.style.background='transparent'">
                            <td style="padding: 12px 15px; color: #ddd; font-size: 0.9rem;">${item.data} às ${item.hora}</td>
                            <td style="padding: 12px 15px; color: var(--primary-color); font-weight: bold; font-size: 0.9rem;">Mesa #${item.mesa}</td>
                            <td style="padding: 12px 15px; color: #4caf50; font-weight: bold; font-size: 0.9rem;">R$ ${item.valorTotal.toFixed(2)}</td>
                            <td style="padding: 12px 15px; color: #ddd; font-size: 0.9rem;">${item.formaPagamento} ${item.detalhes !== '1x' ? '(' + item.detalhes + ')' : ''}</td>
                            <td style="padding: 12px 15px; color: #ff9800; font-size: 0.9rem;">${trocoFormatado}</td>
                        </tr>
                    `;
                });
            }

            contentArea.innerHTML = `
                <div class="card">
                    <h3 style="color: var(--primary-color); margin-bottom: 5px;">Registro de Transações e Vendas</h3>
                    <p style="color: #a0a0a0; margin-bottom: 20px;">Histórico completo de pagamentos efetuados e fechamentos de comanda.</p>
                    <div style="max-height: 450px; overflow-y: auto; border: 1px solid #333; border-radius: 6px;">
                        <table style="width: 100%; border-collapse: collapse; text-align: left; background: #1a1a1a;">
                            <thead>
                                <tr style="background: #252525; border-bottom: 2px solid #333; color: var(--primary-color); font-size: 0.9rem;">
                                    <th style="padding: 12px 15px;">Data e Hora</th>
                                    <th style="padding: 12px 15px;">Mesa</th>
                                    <th style="padding: 12px 15px;">Valor Pago</th>
                                    <th style="padding: 12px 15px;">Forma de Pagamento</th>
                                    <th style="padding: 12px 15px;">Troco</th>
                                </tr>
                            </thead>
                            <tbody>
                                ${linhasTabela}
                            </tbody>
                        </table>
                    </div>
                </div>
            `;
        }

        function renderizarTelaPagamentos() {
            const contentArea = document.querySelector('.content-area');
            const qtdRemessas = parseInt(localStorage.getItem('qtd_remessas') || '0');
            const mesasPagas = JSON.parse(localStorage.getItem('mesas_pagas')) || [];

            let mesasPagamentosHtml = '';
            for (let i = 1; i <= qtdRemessas; i++) {
                if (mesasPagas.includes(i)) continue;

                mesasPagamentosHtml += `
                    <div style="background: #252525; border: 1px solid #333; padding: 15px; border-radius: 8px; display: flex; flex-direction: column; justify-content: space-between; gap: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.3);">
                        <div style="display: flex; justify-content: space-between; align-items: center;">
                            <span style="font-weight: bold; color: var(--primary-color); font-size: 1.1rem;">Mesa / Remessa #${i}</span>
                            <span style="background: #333; padding: 3px 8px; border-radius: 12px; font-size: 0.8rem; color: #ff9800;">Aguardando Pagamento</span>
                        </div>
                        <p style="font-size: 0.9rem; color: #ddd;">Valor Total: <strong>R$ 35,00</strong></p>
                        <button onclick="abrirModalPagamento(${i}, 35.00)" style="padding: 8px; background: var(--primary-color); border: none; color: #121212; border-radius: 5px; cursor: pointer; font-weight: bold;">Efetuar Pagamento</button>
                    </div>
                `;
            }

            contentArea.innerHTML = `
                <div class="card" style="position: relative;">
                    <h3 style="color: var(--primary-color); margin-bottom: 5px;">Painel de Pagamentos</h3>
                    <p style="color: #a0a0a0; margin-bottom: 20px;">Selecione a mesa ocupada para realizar a cobrança e fechar a comanda.</p>
                    <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(240px, 1fr)); gap: 15px; max-height: 450px; overflow-y: auto; padding-right: 5px;">
                        ${qtdRemessas > 0 && mesasPagamentosHtml !== '' ? mesasPagamentosHtml : '<p style="color: #777;">Nenhuma mesa com pedido pendente de pagamento no momento.</p>'}
                    </div>
                </div>

                <!-- Modal de Pagamento -->
                <div id="modal-pagamento" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.85); z-index: 1100; justify-content: center; align-items: center;">
                    <div style="background: #1e1e1e; border: 1px solid #333; width: 420px; padding: 25px; border-radius: 10px; box-shadow: 0 10px 25px rgba(0,0,0,0.5);">
                        <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #333; padding-bottom: 10px; margin-bottom: 15px;">
                            <h3 id="pag-titulo" style="color: var(--primary-color);">Pagamento</h3>
                            <button onclick="fecharModalPagamento()" style="background: none; border: none; color: #fff; font-size: 1.2rem; cursor: pointer;">✕</button>
                        </div>
                        
                        <div id="etapa-selecao-metodo">
                            <p id="pag-valor-total" style="margin-bottom: 15px; font-size: 1rem; color: #ddd;"></p>
                            <label style="display: block; margin-bottom: 8px; color: #a0a0a0; font-size: 0.9rem;">Escolha a forma de pagamento:</label>
                            <div style="display: flex; flex-direction: column; gap: 10px; margin-bottom: 20px;">
                                <button onclick="selecionarMetodo('Pix')" style="padding: 12px; background: #252525; border: 1px solid #4caf50; color: #4caf50; font-weight: bold; border-radius: 6px; cursor: pointer; text-align: left;">🟢 PIX (Pagamento Direto)</button>
                                <button onclick="selecionarMetodo('Dinheiro')" style="padding: 12px; background: #252525; border: 1px solid #ff9800; color: #ff9800; font-weight: bold; border-radius: 6px; cursor: pointer; text-align: left;">💵 Dinheiro (Com Calculadora de Troco)</button>
                                <button onclick="selecionarMetodo('Cartao')" style="padding: 12px; background: #252525; border: 1px solid #03a9f4; color: #03a9f4; font-weight: bold; border-radius: 6px; cursor: pointer; text-align: left;">💳 Cartão (Débito ou Crédito)</button>
                            </div>
                        </div>

                        <!-- Sub-etapa Dinheiro -->
                        <div id="etapa-dinheiro" style="display: none;">
                            <p style="color: #a0a0a0; font-size: 0.9rem; margin-bottom: 10px;">Valor do Pedido: <strong id="din-total" style="color:#fff;"></strong></p>
                            <label style="display: block; margin-bottom: 5px; color: #a0a0a0; font-size: 0.85rem;">Valor recebido em dinheiro:</label>
                            <input type="number" step="0.01" id="din-recebido" oninput="calcularTroco()" placeholder="0.00" style="width: 100%; padding: 10px; background: #2c2c2c; border: 1px solid #444; color: #fff; border-radius: 5px; margin-bottom: 15px;">
                            <p style="color: #4caf50; font-weight: bold; margin-bottom: 20px;" id="din-troco-txt">Troco: R$ 0,00</p>
                            <div style="display: flex; gap: 10px;">
                                <button onclick="confirmarPagamentoDinheiro()" style="flex: 1; padding: 10px; background: var(--primary-color); border: none; color: #121212; font-weight: bold; border-radius: 5px; cursor: pointer;">Confirmar Pagamento</button>
                                <button onclick="voltarSelecaoMetodo()" style="padding: 10px; background: #333; border: none; color: #fff; border-radius: 5px; cursor: pointer;">Voltar</button>
                            </div>
                        </div>

                        <!-- Sub-etapa Cartão -->
                        <div id="etapa-cartao" style="display: none;">
                            <label style="display: block; margin-bottom: 8px; color: #a0a0a0; font-size: 0.9rem;">Tipo de Cartão:</label>
                            <select id="cartao-tipo" onchange="mudarTipoCartao()" style="width: 100%; padding: 10px; background: #2c2c2c; border: 1px solid #444; color: #fff; border-radius: 5px; margin-bottom: 15px;">
                                <option value="Debito">Débito</option>
                                <option value="Credito">Crédito</option>
                            </select>
                            
                            <div id="bloco-parcelas" style="display: none; margin-bottom: 15px;">
                                <label style="display: block; margin-bottom: 5px; color: #a0a0a0; font-size: 0.85rem;">Quantidade de Parcelas (até 9x):</label>
                                <select id="cartao-parcelas" style="width: 100%; padding: 10px; background: #2c2c2c; border: 1px solid #444; color: #fff; border-radius: 5px;">
                                    <option value="1">1x (À vista)</option>
                                    <option value="2">2x</option>
                                    <option value="3">3x</option>
                                    <option value="4">4x</option>
                                    <option value="5">5x</option>
                                    <option value="6">6x</option>
                                    <option value="7">7x</option>
                                    <option value="8">8x</option>
                                    <option value="9">9x</option>
                                </select>
                            </div>

                            <div style="display: flex; gap: 10px;">
                                <button onclick="confirmarPagamentoCartao()" style="flex: 1; padding: 10px; background: var(--primary-color); border: none; color: #121212; font-weight: bold; border-radius: 5px; cursor: pointer;">Confirmar Pagamento</button>
                                <button onclick="voltarSelecaoMetodo()" style="padding: 10px; background: #333; border: none; color: #fff; border-radius: 5px; cursor: pointer;">Voltar</button>
                            </div>
                        </div>
                    </div>
                </div>
            `;
        }

        let mesaAtualPagamento = null;
        let valorAtualPagamento = 0;

        function abrirModalPagamento(mesa, valor) {
            mesaAtualPagamento = mesa;
            valorAtualPagamento = valor;
            document.getElementById('pag-titulo').innerText = 'Pagamento - Mesa / Remessa #' + mesa;
            document.getElementById('pag-valor-total').innerHTML = 'Valor Total do Pedido: <strong style="color: var(--primary-color);">R$ ' + valor.toFixed(2) + '</strong>';
            
            document.getElementById('etapa-selecao-metodo').style.display = 'block';
            document.getElementById('etapa-dinheiro').style.display = 'none';
            document.getElementById('etapa-cartao').style.display = 'none';
            document.getElementById('modal-pagamento').style.display = 'flex';
        }

        function fecharModalPagamento() {
            document.getElementById('modal-pagamento').style.display = 'none';
        }

        function voltarSelecaoMetodo() {
            document.getElementById('etapa-selecao-metodo').style.display = 'block';
            document.getElementById('etapa-dinheiro').style.display = 'none';
            document.getElementById('etapa-cartao').style.display = 'none';
        }

        function selecionarMetodo(metodo) {
            if (metodo === 'Pix') {
                salvarPagamentoBanco('Pix', valorAtualPagamento, 0, '1x');
            } else if (metodo === 'Dinheiro') {
                document.getElementById('din-total').innerText = 'R$ ' + valorAtualPagamento.toFixed(2);
                document.getElementById('din-recebido').value = '';
                document.getElementById('din-troco-txt').innerText = 'Troco: R$ 0.00';
                document.getElementById('etapa-selecao-metodo').style.display = 'none';
                document.getElementById('etapa-dinheiro').style.display = 'block';
            } else if (metodo === 'Cartao') {
                document.getElementById('etapa-selecao-metodo').style.display = 'none';
                document.getElementById('etapa-cartao').style.display = 'block';
                mudarTipoCartao();
            }
        }

        function calcularTroco() {
            const recebido = parseFloat(document.getElementById('din-recebido').value) || 0;
            const troco = recebido - valorAtualPagamento;
            if (troco >= 0) {
                document.getElementById('din-troco-txt').innerText = 'Troco: R$ ' + troco.toFixed(2);
                document.getElementById('din-troco-txt').style.color = '#4caf50';
            } else {
                document.getElementById('din-troco-txt').innerText = 'Valor insuficiente!';
                document.getElementById('din-troco-txt').style.color = '#c62828';
            }
        }

        function confirmarPagamentoDinheiro() {
            const recebido = parseFloat(document.getElementById('din-recebido').value) || 0;
            if (recebido < valorAtualPagamento) {
                alert('O valor recebido é menor que o total do pedido.');
                return;
            }
            const troco = recebido - valorAtualPagamento;
            salvarPagamentoBanco('Dinheiro', valorAtualPagamento, troco, '1x');
        }

        function mudarTipoCartao() {
            const tipo = document.getElementById('cartao-tipo').value;
            const blocoParcelas = document.getElementById('bloco-parcelas');
            if (tipo === 'Credito') {
                blocoParcelas.style.display = 'block';
            } else {
                blocoParcelas.style.display = 'none';
            }
        }

        function confirmarPagamentoCartao() {
            const tipo = document.getElementById('cartao-tipo').value;
            const parcelas = tipo === 'Credito' ? document.getElementById('cartao-parcelas').value + 'x' : '1x';
            salvarPagamentoBanco('Cartão (' + tipo + ')', valorAtualPagamento, 0, parcelas);
        }

        function salvarPagamentoBanco(forma, valor, troco, parcelas) {
            const agora = new Date();
            const dataStr = agora.toLocaleDateString('pt-BR');
            const horaStr = agora.toLocaleTimeString('pt-BR');

            const registroPagamento = {
                mesa: mesaAtualPagamento,
                data: dataStr,
                hora: horaStr,
                formaPagamento: forma,
                valorTotal: valor,
                troco: troco,
                detalhes: parcelas
            };

            const historico = JSON.parse(localStorage.getItem('historico_pagamentos')) || [];
            historico.push(registroPagamento);
            localStorage.setItem('historico_pagamentos', JSON.stringify(historico));

            let mesasPagas = JSON.parse(localStorage.getItem('mesas_pagas')) || [];
            if (!mesasPagas.includes(mesaAtualPagamento)) {
                mesasPagas.push(mesaAtualPagamento);
                localStorage.setItem('mesas_pagas', JSON.stringify(mesasPagas));
            }

            fecharModalPagamento();
            alert('Pagamento registrado e salvo com sucesso! Mesa #' + mesaAtualPagamento + ' liberada.');
            renderizarTelaPagamentos();
        }

        function renderizarTelaCardapio(abaAtiva) {
            const contentArea = document.querySelector('.content-area');
            const produtos = JSON.parse(localStorage.getItem('produtos')) || [];

            const produtosAtivos = produtos.filter(p => !p.arquivado);
            const produtosArquivados = produtos.filter(p => p.arquivado);

            let listaHtml = '';
            const itensExibir = abaAtiva === 'ativos' ? produtosAtivos : produtosArquivados;

            if (itensExibir.length === 0) {
                listaHtml = `<p style="color: #777; padding: 10px;">Nenhum produto cadastrado nesta aba.</p>`;
            } else {
                itensExibir.forEach(p => {
                    listaHtml += `
                        <div style="background: #252525; border: 1px solid #333; padding: 12px 15px; border-radius: 6px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                            <div>
                                <strong style="color: #fff; font-size: 1rem;">${p.nome}</strong>
                                <span style="background: #333; color: var(--primary-color); padding: 2px 6px; border-radius: 4px; font-size: 0.75rem; margin-left: 8px;">${p.categoria}</span>
                                <div style="color: #4caf50; font-size: 0.9rem; margin-top: 3px; font-weight: bold;">R$ ${parseFloat(p.valor).toFixed(2)}</div>
                            </div>
                            <div style="display: flex; gap: 8px; align-items: center;">
                                ${abaAtiva === 'ativos' ? `
                                    <button onclick="toggleVisibilidade(${p.id})" style="padding: 6px 10px; background: ${p.visivel ? '#2e7d32' : '#c62828'}; border: none; color: #fff; border-radius: 4px; cursor: pointer; font-size: 0.8rem;">
                                        ${p.visivel ? '👁️ Visível' : '🚫 Oculto'}
                                    </button>
                                    <button onclick="arquivarProduto(${p.id})" style="padding: 6px 10px; background: #444; border: none; color: #fff; border-radius: 4px; cursor: pointer; font-size: 0.8rem;">📁 Arquivar</button>
                                ` : `
                                    <button onclick="desarquivarProduto(${p.id})" style="padding: 6px 10px; background: #0277bd; border: none; color: #fff; border-radius: 4px; cursor: pointer; font-size: 0.8rem;">📂 Desarquivar</button>
                                    <button onclick="excluirProduto(${p.id})" style="padding: 6px 10px; background: #c62828; border: none; color: #fff; border-radius: 4px; cursor: pointer; font-size: 0.8rem;">🗑️ Excluir</button>
                                `}
                            </div>
                        </div>
                    `;
                });
            }

            contentArea.innerHTML = `
                <div class="card">
                    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                        <h3 style="color: var(--primary-color);">Gerenciamento de Cardápio</h3>
                        <div style="display: flex; gap: 10px;">
                            <button onclick="renderizarTelaCardapio('ativos')" style="padding: 6px 12px; background: ${abaAtiva === 'ativos' ? 'var(--primary-color)' : '#333'}; border: none; color: ${abaAtiva === 'ativos' ? '#121212' : '#fff'}; border-radius: 4px; cursor: pointer; font-weight: bold;">Ativos</button>
                            <button onclick="renderizarTelaCardapio('arquivados')" style="padding: 6px 12px; background: ${abaAtiva === 'arquivados' ? 'var(--primary-color)' : '#333'}; border: none; color: ${abaAtiva === 'arquivados' ? '#121212' : '#fff'}; border-radius: 4px; cursor: pointer; font-weight: bold;">Arquivados</button>
                        </div>
                    </div>

                    ${abaAtiva === 'ativos' ? `
                        <form onsubmit="cadastrarProduto(event)" style="background: #222; padding: 15px; border-radius: 6px; margin-bottom: 20px; display: grid; grid-template-columns: 2fr 1fr 1fr auto; gap: 10px; align-items: end;">
                            <div>
                                <label style="display: block; font-size: 0.8rem; color: #a0a0a0; margin-bottom: 3px;">Nome do Produto:</label>
                                <input type="text" id="prod_nome" required style="width: 100%; padding: 8px; background: #2c2c2c; border: 1px solid #444; color: #fff; border-radius: 4px;">
                            </div>
                            <div>
                                <label style="display: block; font-size: 0.8rem; color: #a0a0a0; margin-bottom: 3px;">Valor (R$):</label>
                                <input type="number" step="0.01" id="prod_valor" required style="width: 100%; padding: 8px; background: #2c2c2c; border: 1px solid #444; color: #fff; border-radius: 4px;">
                            </div>
                            <div>
                                <label style="display: block; font-size: 0.8rem; color: #a0a0a0; margin-bottom: 3px;">Categoria:</label>
                                <input type="text" id="prod_cat" required style="width: 100%; padding: 8px; background: #2c2c2c; border: 1px solid #444; color: #fff; border-radius: 4px;">
                            </div>
                            <button type="submit" style="padding: 9px 15px; background: var(--primary-color); border: none; color: #121212; font-weight: bold; border-radius: 4px; cursor: pointer;">Cadastrar</button>
                        </form>
                    ` : ''}

                    <div style="max-height: 350px; overflow-y: auto;">
                        ${listaHtml}
                    </div>
                </div>
            `;
        }

        function cadastrarProduto(event) {
            event.preventDefault();
            const nome = document.getElementById('prod_nome').value;
            const valor = document.getElementById('prod_valor').value;
            const categoria = document.getElementById('prod_cat').value;

            const produtos = JSON.parse(localStorage.getItem('produtos')) || [];
            const novoProd = {
                id: Date.now(),
                nome,
                valor,
                categoria,
                visivel: true,
                arquivado: false
            };

            produtos.push(novoProd);
            localStorage.setItem('produtos', JSON.stringify(produtos));
            renderizarTelaCardapio('ativos');
        }

        function toggleVisibilidade(id) {
            const produtos = JSON.parse(localStorage.getItem('produtos')) || [];
            const prod = produtos.find(p => p.id === id);
            if (prod) {
                prod.visivel = !prod.visivel;
                localStorage.setItem('produtos', JSON.stringify(produtos));
                renderizarTelaCardapio('ativos');
            }
        }

        function arquivarProduto(id) {
            const produtos = JSON.parse(localStorage.getItem('produtos')) || [];
            const prod = produtos.find(p => p.id === id);
            if (prod) {
                prod.arquivado = true;
                localStorage.setItem('produtos', JSON.stringify(produtos));
                renderizarTelaCardapio('ativos');
            }
        }

        function desarquivarProduto(id) {
            const produtos = JSON.parse(localStorage.getItem('produtos')) || [];
            const prod = produtos.find(p => p.id === id);
            if (prod) {
                prod.arquivado = false;
                localStorage.setItem('produtos', JSON.stringify(produtos));
                renderizarTelaCardapio('arquivados');
            }
        }

        function excluirProduto(id) {
            if (confirm('Deseja realmente excluir este produto? O histórico de pedidos passados não será afetado.')) {
                let produtos = JSON.parse(localStorage.getItem('produtos')) || [];
                produtos = produtos.filter(p => p.id !== id);
                localStorage.setItem('produtos', JSON.stringify(produtos));
                renderizarTelaCardapio('arquivados');
            }
        }

        function salvarConfiguracoes(event) {
            event.preventDefault();
            const nomeEst = document.getElementById('nome_est').value;
            const qtdRem = document.getElementById('qtd_rem').value;

            localStorage.setItem('nome_estabelecimento', nomeEst);
            localStorage.setItem('qtd_remessas', qtdRem);

            const msg = document.getElementById('msg-sucesso');
            msg.style.display = 'block';
            setTimeout(() => { msg.style.display = 'none'; }, 2500);
        }

        function abrirExtrato(numeroMesa) {
            document.getElementById('modal-titulo').innerText = 'Extrato - Mesa / Remessa #' + numeroMesa;
            document.getElementById('modal-extrato').style.display = 'flex';
        }

        function fecharExtrato() {
            document.getElementById('modal-extrato').style.display = 'none';
        }

        function imprimirExtrato() {
            const conteudo = document.getElementById('extrato-conteudo').innerHTML;
            const titulo = document.getElementById('modal-titulo').innerText;
            const janela = window.open('', '', 'height=500,width=400');
            janela.document.write('<html><head><title>Imprimir Extrato</title></head><body style="font-family:sans-serif; padding:20px;">');
            janela.document.write('<h2>' + titulo + '</h2>');
            janela.document.write(conteudo);
            janela.document.write('</body></html>');
            janela.document.close();
            janela.print();
        }
    </script>
```

---

## Arquivo: `./templates/pedidos.html`

```text
{% extends "base.html" if t != "index" and t != "cardapio_digital" else "" %}
{% block content %}
<h2>Página: pedidos</h2>
<p>Conteúdo da seção pedidos carregado com sucesso.</p>
{% endblock %}

```

---

## Arquivo: `./templates/pedidos_admin.html`

```text
{% extends "base.html" %}

{% block title %}Pedidos da Cozinha - Cardápio Pro{% endblock %}

{% block content %}
<div style="max-width: 1000px; margin: 0 auto; background-color: #0f172a; border: 1px solid rgba(255,255,255,0.08); border-radius: 16px; padding: 2rem; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.4);">
    <h2 style="font-size: 1.25rem; color: #f8fafc; font-weight: 600; margin-bottom: 0.3rem;">📦 Painel de Pedidos (Cozinha / Salão)</h2>
    <p style="margin-bottom: 1.5rem; color: #94a3b8; font-size: 0.85rem; border-bottom: 1px solid rgba(255,255,255,0.06); padding-bottom: 1rem;">Acompanhe em tempo real os pedidos realizados através dos QR codes das mesas.</p>                                          
    
    {% if not pedidos %}
        <p style="color: #64748b; font-size: 0.9rem;">Nenhum pedido registrado no momento.</p>
    {% else %}
        <div style="display: flex; flex-direction: column; gap: 1rem;">
            {% for p in pedidos %}
            <div style="background: #070a13; border: 1px solid rgba(255,255,255,0.06); border-radius: 12px; padding: 1.25rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem;">
                <div>
                    <h3 style="color: #fbbf24; font-size: 1.05rem; margin-bottom: 0.3rem;">Mesa {{ p.mesa }} <span style="font-size: 0.8rem; font-weight: normal; color: #94a3b8;">(Pedido #{{ p.id }})</span></h3>
                    <p style="font-size: 0.9rem; color: #f8fafc; white-space: pre-line; margin-bottom: 0.4rem;">{{ p.itens }}</p>
                    <p style="font-weight: 600; color: #34d399; font-size: 0.9rem;">Total: R$ {{ "%.2f"|format(p.total) }} <span style="font-size: 0.75rem; background: #1e293b; padding: 0.15rem 0.4rem; border-radius: 4px; color: #94a3b8; margin-left: 0.4rem; font-weight: 400;">Pagamento: {{ p.forma_pagamento }}</span></p>
                    <small style="color: #64748b; font-size: 0.75rem; display: block; margin-top: 0.2rem;">Realizado em: {{ p.criado_em }}</small>
                </div>

                <div style="display: flex; align-items: center; gap: 1rem;">
                    <div style="padding: 0.35rem 0.75rem; border-radius: 6px; font-weight: 600; font-size: 0.8rem; background: {% if p.status == 'Pendente' %}rgba(245, 158, 11, 0.15); color: #fbbf24; border: 1px solid rgba(245, 158, 11, 0.3);{% elif p.status == 'Preparando' %}rgba(59, 130, 246, 0.15); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.3);{% else %}rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3);{% endif %}">
                        {{ p.status }}
                    </div>

                    <form action="/admin/pedidos/status/{{ p.id }}" method="POST" style="display: flex; gap: 0.5rem; margin: 0;">
                        <select name="status" style="padding: 0.35rem; font-size: 0.8rem; background: #111827; color: #f8fafc; border: 1px solid #334155; border-radius: 6px; outline: none;">
                            <option value="Pendente" {% if p.status == 'Pendente' %}selected{% endif %}>Pendente</option>
                            <option value="Preparando" {% if p.status == 'Preparando' %}selected{% endif %}>Preparando</option>
                            <option value="Concluído" {% if p.status == 'Concluído' %}selected{% endif %}>Concluído</option>
                        </select>
                        <button type="submit" style="background: #1e293b; color: #f8fafc; border: 1px solid #334155; padding: 0.35rem 0.75rem; font-size: 0.8rem; border-radius: 6px; cursor: pointer; font-weight: 500;">Atualizar</button>
                    </form>
                </div>
            </div>
            {% endfor %}
        </div>
    {% endif %}
</div>
{% endblock %}

```

---

## Arquivo: `./templates/qr_code.html`

```text
{% extends "base.html" %}

{% block title %}QR Codes das Mesas - Cardápio Pro{% endblock %}

{% block content %}
<div class="card">
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1.5rem;">
        <h2>QR Codes e Links das Mesas</h2>
        <a href="/admin/configuracoes" class="btn" style="background-color: #64748b; font-size: 0.9rem; padding: 0.5rem 1rem;">Alterar Quantidade de Mesas</a>
    </div>
    
    <p style="margin-bottom: 1.5rem; color: #64748b;">Estes são os QR codes gerados automaticamente com base nas <strong>{{ mesas | length }}</strong> mesas configuradas. Os clientes escaneiam para abrir o cardápio digital.</p>

    <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 1.5rem;">
        {% for mesa in mesas %}
        <div style="background: #f8fafc; border: 1px solid #cbd5e1; border-radius: 8px; padding: 1.25rem; text-align: center; box-shadow: 0 1px 2px rgba(0,0,0,0.05);">
            <h3 style="margin-bottom: 0.75rem; color: #1e293b;">Mesa {{ mesa.numero }}</h3>
            <div style="background: white; padding: 0.5rem; display: inline-block; border-radius: 6px; border: 1px solid #e2e8f0; margin-bottom: 0.75rem;">
                <img src="{{ mesa.qr_code }}" alt="QR Code Mesa {{ mesa.numero }}" style="width: 130px; height: 130px; display: block;">
            </div>
            <div style="word-break: break-all; margin-bottom: 0.75rem;">
                <a href="{{ mesa.link }}" target="_blank" style="font-size: 0.85rem; color: #2563eb; text-decoration: none;">{{ mesa.link }}</a>
            </div>
            <a href="{{ mesa.link }}" target="_blank" class="btn" style="font-size: 0.85rem; padding: 0.4rem 0.8rem; width: 100%;">Abrir Cardápio</a>
        </div>
        {% endfor %}
    </div>
</div>
{% endblock %}

```

---

## Arquivo: `./templates/qrcodes.html`

```text
{% extends "base.html" %}
{% block content %}
<h2>QR Codes das Mesas</h2>
<div style="display: flex; flex-wrap: wrap; gap: 20px;">
    {% for mesa in mesas %}
        <div style="border: 1px solid #ccc; padding: 15px; border-radius: 8px; text-align: center; background: #fafafa;">
            <h3>Mesa {{ mesa.numero }}</h3>
            <img src="{{ mesa.qr }}" alt="QR Mesa {{ mesa.numero }}">
            <p><a href="{{ mesa.link }}" target="_blank">Abrir Link</a></p>
        </div>
    {% endfor %}
</div>
{% endblock %}

```

---

## Arquivo: `./templates/registro.html`

```text
{% extends "base.html" if t != "index" and t != "cardapio_digital" else "" %}
{% block content %}
<h2>Página: registro</h2>
<p>Conteúdo da seção registro carregado com sucesso.</p>
{% endblock %}

```

---

## Arquivo: `./templates/registros.html`

```text
{% extends "base.html" %}

{% block title %}Registro de Vendas - Cardápio Pro{% endblock %}

{% block content %}
<div class="card">
    <h2>Histórico de Registros e Transações</h2>
    <p style="margin-bottom: 1.5rem; color: #64748b;">Consulte todas as operações e pedidos processados no estabelecimento.</p>

    {% if not transacoes %}
        <p style="color: #64748b;">Nenhum registro encontrado.</p>
    {% else %}
        <div style="overflow-x: auto;">
            <table style="width: 100%; border-collapse: collapse; text-align: left; font-size: 0.95rem;">
                <thead>
                    <tr style="background: #f1f5f9; border-bottom: 2px solid #cbd5e1;">
                        <th style="padding: 0.75rem;">ID</th>
                        <th style="padding: 0.75rem;">Mesa</th>
                        <th style="padding: 0.75rem;">Itens</th>
                        <th style="padding: 0.75rem;">Total</th>
                        <th style="padding: 0.75rem;">Pagamento</th>
                        <th style="padding: 0.75rem;">Status</th>
                        <th style="padding: 0.75rem;">Data/Hora</th>
                    </tr>
                </thead>
                <tbody>
                    {% for t in transacoes %}
                    <tr style="border-bottom: 1px solid #e2e8f0;">
                        <td style="padding: 0.75rem;">#{{ t.id }}</td>
                        <td style="padding: 0.75rem;">Mesa {{ t.mesa }}</td>
                        <td style="padding: 0.75rem; white-space: pre-line; font-size: 0.9rem;">{{ t.itens }}</td>
                        <td style="padding: 0.75rem; font-weight: 600; color: #16a34a;">R$ {{ "%.2f"|format(t.total) }}</td>
                        <td style="padding: 0.75rem;">{{ t.forma_pagamento }}</td>
                        <td style="padding: 0.75rem;">{{ t.status }}</td>
                        <td style="padding: 0.75rem; color: #64748b; font-size: 0.85rem;">{{ t.criado_em }}</td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
    {% endif %}
</div>
{% endblock %}

```

---

## Arquivo: `./__pycache__/app.cpython-314.pyc`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./__pycache__/banco.cpython-314.pyc`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
Kw4NCgAAAABBWGdqbgMAAOMAAAAAAAAAAAAAAAACAAAAAAAAAPM2AAAAgABeAFIBSQB0AF4AUgFJAXQBXgBSAkkCSAN0Ax8AXQMhADQAAAAAAAAAHwBSAxcAdARSASMAKQTpAAAAAE4pAdoLbG9hZF9kb3RlbnZjAAAAAAAAAAAAAAAACgAAAAMAAADzugEAAIAAGwBcAAAAAAAAAAAAUAIAAAAAAAAAAAAAAAAAAAAAAAAhAFIANAEAAAAAAABwAFYAJwAAAAAAAABkFwAAHABcBAAAAAAAAAAAUAYAAAAAAAAAAAAAAAAAAAAAAAAhAFYANAEAAAAAAAAjAFwEAAAAAAAAAABQBgAAAAAAAAAAAAAAAAAAAAAAACEAXAAAAAAAAAAAAFACAAAAAAAAAAAAAAAAAAAAAAAAIQBSAVICNAIAAAAAAABcAAAAAAAAAAAAUAIAAAAAAAAAAAAAAAAAAAAAAAAhAFIDUgQ0AgAAAAAAAFwAAAAAAAAAAABQAgAAAAAAAAAAAAAAAAAAAAAAACEAUgVSBjQCAAAAAAAAXAAAAAAAAAAAAFACAAAAAAAAAAAAAAAAAAAAAAAAIQBSB1IINAIAAAAAAABcAAAAAAAAAAAAUAIAAAAAAAAAAAAAAAAAAAAAAAAhAFIJUgo0AgAAAAAAAFILNwUAAAAAAAAjACAAXAgAAAAAAAAAAAYAZBYAABwAcAFcCwAAAAAAAAAAUgxUAQwAMgI0AQAAAAAAAB8AVAFoAVINcAE/AWkBaQA7Ax0AaQEpDtoMREFUQUJBU0VfVVJM2gdEQl9OQU1F2g9jYXJkYXBpb19wcm9fZGLaB0RCX1VTRVLaCHBvc3RncmVz2gtEQl9QQVNTV09SRNoA2gdEQl9IT1NUegkxMjcuMC4wLjHaB0RCX1BPUlTaBDU0MzIpBdoGZGJuYW1l2gR1c2Vy2ghwYXNzd29yZNoEaG9zdNoEcG9ydHokRXJybyBhbyBjb25lY3RhciBhbyBiYW5jbyBkZSBkYWRvczogTikG2gJvc9oGZ2V0ZW522ghwc3ljb3BnMtoHY29ubmVjdNoJRXhjZXB0aW9u2gVwcmludCkC2gxkYXRhYmFzZV91cmzaAWVzAgAAACAg2lsvZGF0YS9kYXRhL2NvbS50ZXJtdXgvZmlsZXMvaG9tZS9jbGllbnRlc19jYXJkYXBpb19pbnN0YW5jaWFzL2pvZWxfZmFzdGFwaV9tb2R1bGFyL2JhbmNvLnB52ghjb25lY3RhcnIdAAAACAAAAHOsAAAAgADwAhEFENwXGZd5knmgHtMXMIgM5wsX5BMb1xMj0hMjoEzTEzHQDDH0BgAUHNcTI9ITI9wXGZd5knmgGdAsPdMXPtwVF5dZklmYeagq0xU13BkbnxmaGaA9sCLTGTXcFReXWZJZmHmoK9MVNtwVF5dZklmYeagm0xUx9AsGFA7wAAYNDvj0DgAMFfQAAgUQ3AgN0BA0sFGwQ9AOONQIOdgOD4gH+/AFAgUQ+nMiAAAAgh1COgCgFUI6ALZCA0I6AMI6C0MaA8MFEEMVA8MVBUMaAykFchQAAAByFgAAANoGZG90ZW52cgMAAAByHQAAAKkA8wAAAAByHAAAANoIPG1vZHVsZT5yIQAAAAEAAABzGgAAAPADAQEB2wAJ2wAP3QAe8QYAAQyEDfQEEgEQciAAAAA=
```

---

## Arquivo: `./__pycache__/database.cpython-314.pyc`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
Kw4NCgAAAAC4PWlqzgcAAOMAAAAAAAAAAAAAAAACAAAAAAAAAPNCAAAAgABeAFIBSQB0AF4AUgFJAXQBXgBSAkkCSAN0Ax8AUgN0BFIEdAVSBXQGUgV0B1IGdAhSBxcAdAlSCBcAdApSASMAKQnpAAAAAE4pAdoOUmVhbERpY3RDdXJzb3LaCWxvY2FsaG9zdNoLY2FyZGFwaW9fZGLaCHBvc3RncmVz2gQ1NDMyYwAAAAAAAAAAAAAAAAkAAAADAAAA824AAACAAFwAAAAAAAAAAABQAgAAAAAAAAAAAAAAAAAAAAAAACEAXAQAAAAAAAAAAFwGAAAAAAAAAABcCAAAAAAAAAAAXAoAAAAAAAAAAFwMAAAAAAAAAABcDgAAAAAAAAAAUgA3BgAAAAAAAHAAVgAjACkBKQbaBGhvc3TaCGRhdGFiYXNl2gR1c2Vy2ghwYXNzd29yZNoEcG9ydNoOY3Vyc29yX2ZhY3RvcnkpCNoIcHN5Y29wZzLaB2Nvbm5lY3TaB0RCX0hPU1TaB0RCX05BTUXaB0RCX1VTRVLaC0RCX1BBU1NXT1JE2gdEQl9QT1JUcgMAAAApAdoEY29ubnMBAAAAINpeL2RhdGEvZGF0YS9jb20udGVybXV4L2ZpbGVzL2hvbWUvY2xpZW50ZXNfY2FyZGFwaW9faW5zdGFuY2lhcy9qb2VsX2Zhc3RhcGlfbW9kdWxhci9kYXRhYmFzZS5wedoGZ2V0X2RichgAAAALAAAAcysAAACAANwLE9cLG9ILG9wNFNwRGNwNFNwRHNwNFNwXJfQNBwwGgETwEAAMEIBL8wAAAABjAAAAAAAAAAAAAAAAAwAAAAMAAADzAAEAAIAAXAEAAAAAAAAAADQAAAAAAAAAcABWAFADAAAAAAAAAAAAAAAAAAAAAAAANAAAAAAAAABwAVYBUAUAAAAAAAAAAAAAAAAAAAAAAABSADQBAAAAAAAAHwBWAVAFAAAAAAAAAAAAAAAAAAAAAAAAUgE0AQAAAAAAAB8AVgFQBQAAAAAAAAAAAAAAAAAAAAAAAFICNAEAAAAAAAAfAFYAUAcAAAAAAAAAAAAAAAAAAAAAAAA0AAAAAAAAAB8AVgFQCQAAAAAAAAAAAAAAAAAAAAAAADQAAAAAAAAAHwBWAFAJAAAAAAAAAAAAAAAAAAAAAAAANAAAAAAAAAAfAFIDIwApBGEwAQAACiAgICAgICAgQ1JFQVRFIFRBQkxFIElGIE5PVCBFWElTVFMgZXN0YWJlbGVjaW1lbnRvcyAoCiAgICAgICAgICAgIGlkIFNFUklBTCBQUklNQVJZIEtFWSwKICAgICAgICAgICAgbm9tZSBWQVJDSEFSKDEwMCkgTk9UIE5VTEwsCiAgICAgICAgICAgIHNsdWcgVkFSQ0hBUigxMDApIFVOSVFVRSBOT1QgTlVMTCwKICAgICAgICAgICAgcXVhbnRpZGFkZV9tZXNhcyBJTlQgTk9UIE5VTEwgREVGQVVMVCAxMCwKICAgICAgICAgICAgY3JpYWRvX2VtIFRJTUVTVEFNUCBERUZBVUxUIENVUlJFTlRfVElNRVNUQU1QCiAgICAgICAgKTsKICAgIGHGAQAACiAgICAgICAgQ1JFQVRFIFRBQkxFIElGIE5PVCBFWElTVFMgcHJvZHV0b3MgKAogICAgICAgICAgICBpZCBTRVJJQUwgUFJJTUFSWSBLRVksCiAgICAgICAgICAgIGVzdGFiZWxlY2ltZW50b19pZCBJTlQgUkVGRVJFTkNFUyBlc3RhYmVsZWNpbWVudG9zKGlkKSBPTiBERUxFVEUgQ0FTQ0FERSwKICAgICAgICAgICAgbm9tZSBWQVJDSEFSKDEwMCkgTk9UIE5VTEwsCiAgICAgICAgICAgIGRlc2NyaWNhbyBURVhULAogICAgICAgICAgICBwcmVjbyBOVU1FUklDKDEwLDIpIE5PVCBOVUxMLAogICAgICAgICAgICBjYXRlZ29yaWEgVkFSQ0hBUig1MCkgTk9UIE5VTEwsCiAgICAgICAgICAgIGZvdG8gVkFSQ0hBUigyNTUpLAogICAgICAgICAgICB2aXNpdmVsIEJPT0xFQU4gREVGQVVMVCBUUlVFLAogICAgICAgICAgICBhcnF1aXZhZG8gQk9PTEVBTiBERUZBVUxUIEZBTFNFCiAgICAgICAgKTsKICAgIHXPAQAACiAgICAgICAgQ1JFQVRFIFRBQkxFIElGIE5PVCBFWElTVFMgcGVkaWRvcyAoCiAgICAgICAgICAgIGlkIFNFUklBTCBQUklNQVJZIEtFWSwKICAgICAgICAgICAgZXN0YWJlbGVjaW1lbnRvX2lkIElOVCBSRUZFUkVOQ0VTIGVzdGFiZWxlY2ltZW50b3MoaWQpIE9OIERFTEVURSBDQVNDQURFLAogICAgICAgICAgICBtZXNhIElOVCBOT1QgTlVMTCwKICAgICAgICAgICAgaXRlbnMgVEVYVCBOT1QgTlVMTCwKICAgICAgICAgICAgdG90YWwgTlVNRVJJQygxMCwyKSBOT1QgTlVMTCwKICAgICAgICAgICAgZm9ybWFfcGFnYW1lbnRvIFZBUkNIQVIoMzApIERFRkFVTFQgJ07Do28gaW5mb3JtYWRhJywKICAgICAgICAgICAgc3RhdHVzIFZBUkNIQVIoMzApIERFRkFVTFQgJ1BlbmRlbnRlJywKICAgICAgICAgICAgY3JpYWRvX2VtIFRJTUVTVEFNUCBERUZBVUxUIENVUlJFTlRfVElNRVNUQU1QCiAgICAgICAgKTsKICAgIE4pBXIYAAAA2gZjdXJzb3LaB2V4ZWN1dGXaBmNvbW1pdNoFY2xvc2UpAnIWAAAAchsAAABzAgAAACAgchcAAADaB2luaXRfZGJyHwAAABYAAABzagAAAIAA3AsRiziARNgNEY9biVuLXYBG8AYABQuHToFO8AAIFAj0AAgFCfAWAAULh06BTvAADBQI9AAMBQnwHgAFC4dOgU7wAAsUCPQACwUJ8BoABQmHS4FLhE3YBAqHTIFMhE7YBAiHSoFKhkxyGQAAACkL2gJvc3IPAAAA2g9wc3ljb3BnMi5leHRyYXNyAwAAAHIRAAAAchIAAAByEwAAAHIUAAAAchUAAAByGAAAAHIfAAAAqQByGQAAAHIXAAAA2gg8bW9kdWxlPnIjAAAAAQAAAHMxAAAA8AMBAQHbAAnbAA/dACrgChWAB9gKF4AH2AoUgAfYDhiAC9gKEIAH8gQJARD0Fi4BEXIZAAAA
```

---

## Arquivo: `./__pycache__/inspetor.cpython-314.pyc`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./__pycache__/main.cpython-314.pyc`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./__pycache__/models.cpython-314.pyc`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
Kw4NCgAAAAAsaGhqswMAAOMAAAAAAAAAAAAAAAAFAAAAAAAAAPN8AAAAgABeAFIBSQBIAXQBSAJ0AkgDdANIBHQESAV0BR8AXgBSAkkGSAd0Bx8AXgBSA0kISAl0CR8AFQAhAFIEFwBSBV0JNAMAAAAAAAB0ChUAIQBSBhcAUgddCTQDAAAAAAAAdAsVACEAUggXAFIJXQk0AwAAAAAAAHQMUgojACkL6QAAAAApBdoGQ29sdW1u2gdJbnRlZ2Vy2gZTdHJpbmfaBUZsb2F02gpGb3JlaWduS2V5KQHaDHJlbGF0aW9uc2hpcCkB2gRCYXNlYwAAAAAAAAAAAAAAAAYAAAAAAAAA824AAACAAF0AdAFSAHQCXgV0A1IBdARdBSEAXQZSAlICUgM3AwAAAAAAAHQHXQUhAF0IUgJSAlIENwMAAAAAAAB0CV0FIQBdCFIFUgY3AgAAAAAAAHQKXQUhAF0GXgpSBzcCAAAAAAAAdAtSCHQMUgkjACkK2g9Fc3RhYmVsZWNpbWVudG/aEGVzdGFiZWxlY2ltZW50b3NUqQLaC3ByaW1hcnlfa2V52gVpbmRleCkC2gZ1bmlxdWVyDwAAAEapAdoIbnVsbGFibGUpAdoHZGVmYXVsdKkATikN2ghfX25hbWVfX9oKX19tb2R1bGVfX9oMX19xdWFsbmFtZV9f2g9fX2ZpcnN0bGluZW5vX1/aDV9fdGFibGVuYW1lX19yAwAAAHIEAAAA2gJpZHIFAAAA2gRzbHVn2gRub21l2hBxdWFudGlkYWRlX21lc2Fz2hVfX3N0YXRpY19hdHRyaWJ1dGVzX19yFAAAAPMAAAAA2lwvZGF0YS9kYXRhL2NvbS50ZXJtdXgvZmlsZXMvaG9tZS9jbGllbnRlc19jYXJkYXBpb19pbnN0YW5jaWFzL2pvZWxfZmFzdGFwaV9tb2R1bGFyL21vZGVscy5weXILAAAAcgsAAAAFAAAAczwAAACGANgUJoBN4QkPkAegVLAU1Ak2gELZCxGQJqAUqFTUCzKARNkLEZAmoDXUCymARNkXHZhnqHLUFzLUBBRyHwAAAHILAAAAYwAAAAAAAAAAAAAAAAYAAAAAAAAA82IAAACAAF0AdAFSAHQCXg10A1IBdARdBSEAXQZSAlICUgM3AwAAAAAAAHQHXQUhAF0IUgRSBTcCAAAAAAAAdAldBSEAXQZdCiEAUgY0AQAAAAAAADQCAAAAAAAAdAtSB3QMUggjACkJ2glDYXRlZ29yaWHaCmNhdGVnb3JpYXNUcg0AAABGchEAAAD6E2VzdGFiZWxlY2ltZW50b3MuaWRyFAAAAE4pDXIVAAAAchYAAAByFwAAAHIYAAAAchkAAAByAwAAAHIEAAAAchoAAAByBQAAAHIcAAAAcgcAAADaEmVzdGFiZWxlY2ltZW50b19pZHIeAAAAchQAAAByHwAAAHIgAAAAciIAAAByIgAAAA0AAABzNAAAAIYA2BQggE3hCQ+QB6BUsBTUCTaAQtkLEZAmoDXUCymARNkZH6AHqRrQNEnTKUrTGUvUBBZyHwAAAHIiAAAAYwAAAAAAAAAAAAAAAAYAAAAAAAAA84oAAACAAF0AdAFSAHQCXhR0A1IBdARdBSEAXQZSAlICUgM3AwAAAAAAAHQHXQUhAF0IUgRSBTcCAAAAAAAAdAldBSEAXQpSBFIFNwIAAAAAAAB0C10FIQBdCFICUgU3AgAAAAAAAHQMXQUhAF0GXQ0hAFIGNAEAAAAAAAA0AgAAAAAAAHQOUgd0D1IIIwApCdoHUHJvZHV0b9oIcHJvZHV0b3NUcg0AAABGchEAAAByJAAAAHIUAAAATikQchUAAAByFgAAAHIXAAAAchgAAAByGQAAAHIDAAAAcgQAAAByGgAAAHIFAAAAchwAAAByBgAAANoFcHJlY2/aCWRlc2NyaWNhb3IHAAAAciUAAAByHgAAAHIUAAAAch8AAAByIAAAAHInAAAAcicAAAAUAAAAc0wAAACGANgUHoBN4QkPkAegVLAU1Ak2gELZCxGQJqA11AspgETZDBKQNaA11AwpgEXZEBaQdqgE1BAtgEnZGR+gB6ka0DRJ0ylK0xlL1AQWch8AAAByJwAAAE4pDdoKc3FsYWxjaGVteXIDAAAAcgQAAAByBQAAAHIGAAAAcgcAAADaDnNxbGFsY2hlbXkub3JtcggAAADaCGRhdGFiYXNlcgkAAAByCwAAAHIiAAAAcicAAAByFAAAAHIfAAAAciAAAADaCDxtb2R1bGU+ci4AAAABAAAAczkAAADwAwEBAd8AQdUAQd0AJ90AGfQEBgEzkGT0AAYBM/QQBQFMAZAE9AAFAUwB9A4HAUwBiGT2AAcBTAFyHwAAAA==
```

---

## Arquivo: `./__pycache__/routes.cpython-314.pyc`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./utils/__init__.py`

```text

```

---

## Arquivo: `./routers/analise.py`

```text
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

@router.get("/{slug}/analise")
async def analise_get(request: Request, slug: str):
    db = get_db()
    cursor = db.cursor()
    est_id = 1
    try:
        cursor.execute("SELECT id FROM estabelecimentos WHERE slug = %s", (slug,))
        est = cursor.fetchone()
        if est:
            est_id = est[0]
    except Exception:
        pass
    finally:
        cursor.close()
        db.close()

    # Dicionário de resumo padrão para evitar erros caso a consulta completa venha depois via JS
    resumo = {
        "faturamento_total": 0.0,
        "total_pedidos": 0,
        "ticket_medio": 0.0
    }

    return templates.TemplateResponse(request, "analise.html", {
        "request": request, 
        "slug": slug, 
        "estab_id": est_id,
        "resumo": resumo
    })

```

---

## Arquivo: `./routers/backup.py`

```text
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

@router.get("/{slug}/backup")
async def backup_get(request: Request, slug: str):
    db = get_db()
    cursor = db.cursor()
    est_id = 1
    try:
        cursor.execute("SELECT id FROM estabelecimentos WHERE slug = %s", (slug,))
        est = cursor.fetchone()
        if est:
            est_id = est[0]
    except Exception:
        pass
    finally:
        cursor.close()
        db.close()

    return templates.TemplateResponse(request, name="backup.html", context={"request": request, "slug": slug, "estab_id": est_id})

```

---

## Arquivo: `./routers/cardapio.py`

```text
import os
import shutil
from fastapi import APIRouter, Request, Form, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

UPLOAD_DIR = "static/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def obter_estabelecimento_por_slug(cursor, slug: str):
    cursor.execute("SELECT id FROM estabelecimentos WHERE slug = %s", (slug,))
    est = cursor.fetchone()
    if not est:
        raise HTTPException(status_code=404, detail="Estabelecimento não encontrado")
    return est['id']

@router.get("/{slug}/cardapio", response_class=HTMLResponse)
def listar_cardapio(slug: str, request: Request, tab: str = "ativos"):
    db = get_db()
    cursor = db.cursor()
    
    est_id = obter_estabelecimento_por_slug(cursor, slug)
    
    if tab == "arquivados":
        cursor.execute("SELECT * FROM produtos WHERE estabelecimento_id = %s AND arquivado = TRUE ORDER BY categoria, nome", (est_id,))
    else:
        cursor.execute("SELECT * FROM produtos WHERE estabelecimento_id = %s AND (arquivado = FALSE OR arquivado IS NULL) ORDER BY categoria, nome", (est_id,))

    produtos = cursor.fetchall()
    cursor.close()
    db.close()
    
    return templates.TemplateResponse(request, "cardapio_admin.html", {"produtos": produtos, "tab": tab, "slug": slug})

@router.post("/{slug}/cardapio/adicionar")
async def adicionar_produto(
    slug: str,
    nome: str = Form(...),
    descricao: str = Form(""),
    preco: float = Form(...),
    categoria: str = Form(...),
    foto_url: str = Form(""),
    foto_arquivo: UploadFile = File(None)
):
    foto_final = foto_url.strip()
    if foto_arquivo and foto_arquivo.filename:
        file_path = os.path.join(UPLOAD_DIR, foto_arquivo.filename)
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(foto_arquivo.file, buffer)
        foto_final = f"/{file_path}"
        
    db = get_db()
    cursor = db.cursor()
    est_id = obter_estabelecimento_por_slug(cursor, slug)
    
    cursor.execute(
        "INSERT INTO produtos (estabelecimento_id, nome, descricao, preco, categoria, foto, arquivado, visivel) VALUES (%s, %s, %s, %s, %s, %s, FALSE, TRUE)",
        (est_id, nome, descricao, preco, categoria, foto_final)
    )
    db.commit()
    cursor.close()
    db.close()

    return RedirectResponse(url=f"/admin/{slug}/cardapio?tab=ativos", status_code=303)

@router.post("/{slug}/cardapio/arquivar/{id}")
def arquivar_produto(slug: str, id: int):
    db = get_db()
    cursor = db.cursor()
    est_id = obter_estabelecimento_por_slug(cursor, slug)
    cursor.execute("UPDATE produtos SET arquivado = TRUE WHERE id = %s AND estabelecimento_id = %s", (id, est_id))
    db.commit()
    cursor.close()
    db.close()

    return RedirectResponse(url=f"/admin/{slug}/cardapio?tab=ativos", status_code=303)

@router.post("/{slug}/cardapio/desarquivar/{id}")
def desarquivar_produto(slug: str, id: int):
    db = get_db()
    cursor = db.cursor()
    est_id = obter_estabelecimento_por_slug(cursor, slug)
    cursor.execute("UPDATE produtos SET arquivado = FALSE WHERE id = %s AND estabelecimento_id = %s", (id, est_id))
    db.commit()
    cursor.close()
    db.close()

    return RedirectResponse(url=f"/admin/{slug}/cardapio?tab=arquivados", status_code=303)

@router.post("/{slug}/cardapio/toggle_visibilidade/{id}")
def toggle_visibilidade(slug: str, id: int):
    db = get_db()
    cursor = db.cursor()
    est_id = obter_estabelecimento_por_slug(cursor, slug)
    cursor.execute("UPDATE produtos SET visivel = NOT visivel WHERE id = %s AND estabelecimento_id = %s", (id, est_id))
    db.commit()
    cursor.close()
    db.close()

    return RedirectResponse(url=f"/admin/{slug}/cardapio?tab=ativos", status_code=303)

@router.post("/{slug}/cardapio/excluir/{id}")
def excluir_produto(slug: str, id: int):
    db = get_db()
    cursor = db.cursor()
    est_id = obter_estabelecimento_por_slug(cursor, slug)
    cursor.execute("DELETE FROM produtos WHERE id = %s AND estabelecimento_id = %s", (id, est_id))
    db.commit()
    cursor.close()
    db.close()

    return RedirectResponse(url=f"/admin/{slug}/cardapio?tab=arquivados", status_code=303)

```

---

## Arquivo: `./routers/cardapiodigital.py`

```text
from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/{slug}", response_class=HTMLResponse)
def cardapio_digital_get(slug: str, request: Request, mesa: int = None):
    db = get_db()
    cursor = db.cursor()

    # Busca o estabelecimento
    cursor.execute("SELECT id, nome, quantidade_mesas FROM estabelecimentos WHERE slug = %s", (slug,))
    est = cursor.fetchone()
    if not est:
        cursor.close()
        db.close()
        raise HTTPException(status_code=404, detail="Estabelecimento não encontrado")

    est_id = est["id"] if isinstance(est, dict) else est[0]
    nome_estab = est["nome"] if isinstance(est, dict) else est[1]
    qtd_mesas = est["quantidade_mesas"] if isinstance(est, dict) else est[2]

    # Busca os produtos visíveis e não arquivados
    cursor.execute(
        "SELECT * FROM produtos WHERE estabelecimento_id = %s AND (visivel = TRUE OR visivel IS NULL) AND (arquivado = FALSE OR arquivado IS NULL) ORDER BY categoria, nome",
        (est_id,)
    )
    produtos = cursor.fetchall()

    cursor.close()
    db.close()

    return templates.TemplateResponse(
        request, 
        "cardapio_digital.html", 
        {
            "slug": slug,
            "nome_estabelecimento": nome_estab,
            "quantidade_mesas": qtd_mesas,
            "produtos": produtos
        }
    )

@router.post("/{slug}/fazer-pedido")
def fazer_pedido(
    slug: str,
    mesa: int = Form(...),
    itens: str = Form(...),
    total: float = Form(...)
):
    db = get_db()
    cursor = db.cursor()

    cursor.execute("SELECT id FROM estabelecimentos WHERE slug = %s", (slug,))
    est = cursor.fetchone()
    if not est:
        cursor.close()
        db.close()
        raise HTTPException(status_code=404, detail="Estabelecimento não encontrado")

    est_id = est["id"] if isinstance(est, dict) else est[0]

    # Salva o pedido na tabela pedidos do PostgreSQL
    cursor.execute(
        "INSERT INTO pedidos (estabelecimento_id, mesa, itens, total, status) VALUES (%s, %s, %s, %s, 'Pendente')",
        (est_id, mesa, itens, total)
    )
    db.commit()
    cursor.close()
    db.close()

    return RedirectResponse(url=f"/{slug}?pedido=enviado", status_code=303)

```

---

## Arquivo: `./routers/cliente.py`

```text
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/mesa/{numero_mesa}", response_class=HTMLResponse)
def cardapio_mesa(request: Request, numero_mesa: int):
    db = get_db()
    cursor = db.cursor()
    
    cursor.execute("SELECT nome_restaurante FROM configuracao LIMIT 1")
    config = cursor.fetchone()
    nome_restaurante = config['nome_restaurante'] if config else 'Cardápio Pro'
    
    cursor.execute("SELECT * FROM produtos WHERE arquivado = FALSE ORDER BY categoria, nome")
    produtos = cursor.fetchall()
    
    cursor.close()
    db.close()
    
    return templates.TemplateResponse(
        request,
        "cardapio_cliente.html",
        {
            "mesa": numero_mesa,
            "nome_restaurante": nome_restaurante,
            "produtos": produtos
        }
    )

@router.post("/mesa/{numero_mesa}/pedir")
def fazer_pedido(
    numero_mesa: int,
    itens_pedido: str = Form(...),
    total: float = Form(...),
    forma_pagamento: str = Form(...)
):
    if not itens_pedido or total <= 0:
        return RedirectResponse(url=f"/mesa/{numero_mesa}", status_code=303)
        
    db = get_db()
    cursor = db.cursor()
    
    cursor.execute(
        "INSERT INTO pedidos (mesa, itens, total, forma_pagamento, status) VALUES (%s, %s, %s, %s, 'Pendente')",
        (numero_mesa, itens_pedido, total, forma_pagamento)
    )
    db.commit()
    cursor.close()
    db.close()
    
    return RedirectResponse(url=f"/mesa/{numero_mesa}?sucesso=true", status_code=303)

```

---

## Arquivo: `./routers/configuracao.py`

```text
import os
from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

def obter_estabelecimento_por_slug(cursor, slug: str):
    cursor.execute("SELECT id FROM estabelecimentos WHERE slug = %s", (slug,))
    est = cursor.fetchone()
    if not est:
        raise HTTPException(status_code=404, detail="Estabelecimento não encontrado")
    return est['id']

@router.get("/{slug}/configuracoes", response_class=HTMLResponse)
def config_get(slug: str, request: Request):
    db = get_db()
    cursor = db.cursor()
    est_id = obter_estabelecimento_por_slug(cursor, slug)
    
    cursor.execute("SELECT * FROM configuracao WHERE estabelecimento_id = %s LIMIT 1", (est_id,))
    config = cursor.fetchone()
    cursor.close()
    db.close()

    return templates.TemplateResponse(request, "configuracao.html", {"config": config, "slug": slug})

@router.post("/{slug}/configuracoes")
def config_post(slug: str, nome_restaurante: str = Form(...), quantidade_mesas: int = Form(...)):
    db = get_db()
    cursor = db.cursor()
    est_id = obter_estabelecimento_por_slug(cursor, slug)

    cursor.execute("DELETE FROM configuracao WHERE estabelecimento_id = %s", (est_id,))
    cursor.execute(
        "INSERT INTO configuracao (estabelecimento_id, nome_restaurante, quantidade_mesas) VALUES (%s, %s, %s)",
        (est_id, nome_restaurante, quantidade_mesas)
    )
    db.commit()
    cursor.close()
    db.close()

    return RedirectResponse(url=f"/admin/{slug}/configuracoes?sucesso=true", status_code=303)

```

---

## Arquivo: `./routers/delivery.py`

```text
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

@router.get("/{slug}/delivery")
async def delivery_get(request: Request, slug: str):
    db = get_db()
    cursor = db.cursor()
    est_id = 1
    try:
        cursor.execute("SELECT id FROM estabelecimentos WHERE slug = %s", (slug,))
        est = cursor.fetchone()
        if est:
            est_id = est[0]
    except Exception:
        pass
    finally:
        cursor.close()
        db.close()

    return templates.TemplateResponse(request, name="delivery.html", context={"request": request, "slug": slug, "estab_id": est_id})

```

---

## Arquivo: `./routers/pagamento.py`

```text
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

@router.get("/{slug}/pagamento")
async def pagamento_get(request: Request, slug: str):
    db = get_db()
    cursor = db.cursor()
    est_id = 1
    try:
        cursor.execute("SELECT id FROM estabelecimentos WHERE slug = %s", (slug,))
        est = cursor.fetchone()
        if est:
            est_id = est[0]
    except Exception:
        pass
    finally:
        cursor.close()
        db.close()

    return templates.TemplateResponse(request, name="pagamento.html", context={"request": request, "slug": slug, "estab_id": est_id})

```

---

## Arquivo: `./routers/pedidos.py`

```text
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

@router.get("/{slug}/pedidos")
async def pedidos_get(request: Request, slug: str):
    db = get_db()
    cursor = db.cursor()
    est_id = 1
    try:
        cursor.execute("SELECT id FROM estabelecimentos WHERE slug = %s", (slug,))
        est = cursor.fetchone()
        if est:
            est_id = est[0]
    except Exception:
        pass
    finally:
        cursor.close()
        db.close()

    return templates.TemplateResponse(request, name="pedidos.html", context={"request": request, "slug": slug, "estab_id": est_id})

```

---

## Arquivo: `./routers/qr_code.py`

```text
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

@router.get("/{slug}/qr-codes")
async def qr_code_get(request: Request, slug: str):
    db = get_db()
    cursor = db.cursor()
    est_id = 1
    try:
        cursor.execute("SELECT id FROM estabelecimentos WHERE slug = %s", (slug,))
        est = cursor.fetchone()
        if est:
            est_id = est[0]
    except Exception:
        pass
    finally:
        cursor.close()
        db.close()

    return templates.TemplateResponse(request, name="qr_code.html", context={"request": request, "slug": slug, "estab_id": est_id})

```

---

## Arquivo: `./routers/registro.py`

```text
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

@router.get("/{slug}/registro")
async def registro_get(request: Request, slug: str):
    db = get_db()
    cursor = db.cursor()
    est_id = 1
    try:
        cursor.execute("SELECT id FROM estabelecimentos WHERE slug = %s", (slug,))
        est = cursor.fetchone()
        if est:
            est_id = est[0]
    except Exception:
        pass
    finally:
        cursor.close()
        db.close()

    return templates.TemplateResponse(request, name="registro.html", context={"request": request, "slug": slug, "estab_id": est_id})

```

---

## Arquivo: `./routers/registros.py`

```text
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from database import get_db

router = APIRouter(prefix="/admin")
templates = Jinja2Templates(directory="templates")

@router.get("/{slug}/registros", response_class=HTMLResponse)
def listar_registros(request: Request):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM pedidos ORDER BY criado_em DESC")
    transacoes = cursor.fetchall()
    cursor.close()
    db.close()
    
    return templates.TemplateResponse(request, "registros.html", {"transacoes": transacoes})

```

---

## Arquivo: `./routers/__pycache__/analise.cpython-314.pyc`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./routers/__pycache__/backup.cpython-314.pyc`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./routers/__pycache__/cardapio.cpython-314.pyc`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./routers/__pycache__/cardapiodigital.cpython-314.pyc`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./routers/__pycache__/cliente.cpython-314.pyc`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./routers/__pycache__/configuracao.cpython-314.pyc`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./routers/__pycache__/delivery.cpython-314.pyc`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./routers/__pycache__/gerenciar_qrcode.cpython-314.pyc`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./routers/__pycache__/pagamento.cpython-314.pyc`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./routers/__pycache__/pedidos.cpython-314.pyc`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
Kw4NCgAAAADTKmlq3wIAAOMAAAAAAAAAAAAAAAAEAAAAAAAAAPOGAAAAgABeAFIBSQBIAXQBSAJ0Ah8AXgBSAkkDSAR0BB8AXgBSA0kFSAZ0Bh8AXQEhAFIEUgU3AQAAAAAAAHQHXQQhAFIGUgc3AQAAAAAAAHQIXQdQEwAAAAAAAAAAAAAAAAAAAAAAAFIINAEAAAAAAABSCRcAUgoXAGwQNAAAAAAAAAB0ClILIwApDOkAAAAAKQLaCUFQSVJvdXRlctoHUmVxdWVzdCkB2g9KaW5qYTJUZW1wbGF0ZXMpAdoGZ2V0X2RiegYvYWRtaW4pAdoGcHJlZml42gl0ZW1wbGF0ZXMpAdoJZGlyZWN0b3J5eg8ve3NsdWd9L3BlZGlkb3NjAQAAAAEAAAAAAAAABAAAAAMAAADzMAAAAIAAVgBeAjiEAABkAwAAHABRAWgBUgFcAAAAAAAAAAAAUgJcAgAAAAAAAAAALwIjACkD6QIAAADaB3JlcXVlc3TaBHNsdWcpAnIEAAAA2gNzdHIpAdoGZm9ybWF0cwEAAAAi2mUvZGF0YS9kYXRhL2NvbS50ZXJtdXgvZmlsZXMvaG9tZS9jbGllbnRlc19jYXJkYXBpb19pbnN0YW5jaWFzL2pvZWxfZmFzdGFwaV9tb2R1bGFyL3JvdXRlcnMvcGVkaWRvcy5wedoMX19hbm5vdGF0ZV9fchEAAAAJAAAAcx4AAACAAPcADwFEAvEADwFEApx38AAPAUQCrGPxAA8BRALzAAAAAGMCAAAAAAAAAAAAAAAKAAAAgwAAAPOUAQAAIgAfAIAAXAEAAAAAAAAAADQAAAAAAAAAcAJWAlADAAAAAAAAAAAAAAAAAAAAAAAANAAAAAAAAABwA14BcAQbAFYDUAUAAAAAAAAAAAAAAAAAAAAAAABSAVYBMwE0AgAAAAAAAB8AVgNQBwAAAAAAAAAAAAAAAAAAAAAAADQAAAAAAAAAcAVWBScAAAAAAAAAZAoAABwAVgVeACwaAAAAAAAAAAAAAHAEVANQCwAAAAAAAAAAAAAAAAAAAAAAADQAAAAAAAAAHwBUAlALAAAAAAAAAAAAAAAAAAAAAAAANAAAAAAAAAAfAFwMAAAAAAAAAABQDwAAAAAAAAAAAAAAAAAAAAAAAFQAUgJSA1QAUgRUAVIFVAQvA1IGNwMAAAAAAAAjACAAXAgAAAAAAAAAAAYAZAQAABwAHwAdAExLaQA7Ax0AaQEgAFQDUAsAAAAAAAAAAAAAAAAAAAAAAAA0AAAAAAAAAB8AVAJQCwAAAAAAAAAAAAAAAAAAAAAAADQAAAAAAAAAHwBpADsDHQBpATUDaQEpB+kBAAAAei9TRUxFQ1QgaWQgRlJPTSBlc3RhYmVsZWNpbWVudG9zIFdIRVJFIHNsdWcgPSAlc3oMcGVkaWRvcy5odG1scgwAAAByDQAAANoIZXN0YWJfaWQpAtoEbmFtZdoHY29udGV4dCkIcgYAAADaBmN1cnNvctoHZXhlY3V0ZdoIZmV0Y2hvbmXaCUV4Y2VwdGlvbtoFY2xvc2VyCAAAANoQVGVtcGxhdGVSZXNwb25zZSkGcgwAAAByDQAAANoCZGJyGAAAANoGZXN0X2lk2gNlc3RzBgAAACYmICAgIHIQAAAA2gtwZWRpZG9zX2dldHIhAAAACAAAAHO+AAAA6QCAAOQJD4sYgELYDQ+PWYlZi1uARtgNDoBG8AIJBRPYCA6PDokO0BdIyDTIJ9QIUtgOFI9viW/TDh+IA98LDtgVGJgRlVaIRvAIAAkPjwyJDIwO2AgKjwiJCIwK5AsU1wsl0QsloGewTshZ0Fhf0GFn0Glt0G958AAAfAFCAvAAAE0BQwLQCyXzAAAMRALwAAAFRAL49A0ADBX0AAEFDdkIDPADAQUN+/AGAAkPjwyJDIwO2AgKjwiJCI0K/HM0AAAAgh1DCAGgNEISAMEUPkMIAcISC0IgA8IdAkIjAMIfAUIgA8IgA0IjAMIjIkMFA8MFA0MIAU4pC9oHZmFzdGFwaXIDAAAAcgQAAADaEmZhc3RhcGkudGVtcGxhdGluZ3IFAAAA2ghkYXRhYmFzZXIGAAAA2gZyb3V0ZXJyCAAAANoDZ2V0ciEAAACpAHISAAAAchAAAADaCDxtb2R1bGU+cigAAAABAAAAc0AAAADwAwEBAd8AJt0ALt0AG+EJEpgo1AkjgAbZDBuga9QMMoAJ4AEHhxqBGtAMHdMBHvQCDwFEAvMDAAIf8gIPAUQCchIAAAA=
```

---

## Arquivo: `./routers/__pycache__/qr_code.cpython-314.pyc`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./routers/__pycache__/registro.cpython-314.pyc`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
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
```

---

## Arquivo: `./routers/__pycache__/registros.cpython-314.pyc`

*Arquivo binário detectado. Conteúdo codificado em Base64 para integridade.*

```base64
Kw4NCgAAAADAdWdqawIAAOMAAAAAAAAAAAAAAAAFAAAAAAAAAPOWAAAAgABeAFIBSQBIAXQBSAJ0Ah8AXgBSAkkDSAR0BB8AXgBSA0kFSAZ0Bh8AXgBSBEkHSAh0CB8AXQEhAFIFUgY3AQAAAAAAAHQJXQYhAFIHUgg3AQAAAAAAAHQKXQlQFwAAAAAAAAAAAAAAAAAAAAAAAFIJXQRSCjcCAAAAAAAAUgsXAFIMFwBsEDQAAAAAAAAAdAxSDSMAKQ7pAAAAACkC2glBUElSb3V0ZXLaB1JlcXVlc3QpAdoMSFRNTFJlc3BvbnNlKQHaD0ppbmphMlRlbXBsYXRlcykB2gZnZXRfZGJ6Bi9hZG1pbikB2gZwcmVmaXjaCXRlbXBsYXRlcykB2glkaXJlY3Rvcnl6Ci9yZWdpc3Ryb3MpAdoOcmVzcG9uc2VfY2xhc3NjAQAAAAEAAAAAAAAAAgAAAAMAAADzJAAAAIAAVgBeAjiEAABkAwAAHABRAWgBUgFcAAAAAAAAAAAALwEjACkC6QIAAADaB3JlcXVlc3QpAXIEAAAAKQHaBmZvcm1hdHMBAAAAItpnL2RhdGEvZGF0YS9jb20udGVybXV4L2ZpbGVzL2hvbWUvY2xpZW50ZXNfY2FyZGFwaW9faW5zdGFuY2lhcy9qb2VsX2Zhc3RhcGlfbW9kdWxhci9yb3V0ZXJzL3JlZ2lzdHJvcy5wedoMX19hbm5vdGF0ZV9fchEAAAAKAAAAcxYAAACAAPcACAFdAfEACAFdAZxn8QAIAV0B8wAAAABjAQAAAAAAAAAAAAAABgAAAAMAAADz6gAAAIAAXAEAAAAAAAAAADQAAAAAAAAAcAFWAVADAAAAAAAAAAAAAAAAAAAAAAAANAAAAAAAAABwAlYCUAUAAAAAAAAAAAAAAAAAAAAAAABSADQBAAAAAAAAHwBWAlAHAAAAAAAAAAAAAAAAAAAAAAAANAAAAAAAAABwA1YCUAkAAAAAAAAAAAAAAAAAAAAAAAA0AAAAAAAAAB8AVgFQCQAAAAAAAAAAAAAAAAAAAAAAADQAAAAAAAAAHwBcCgAAAAAAAAAAUA0AAAAAAAAAAAAAAAAAAAAAAABWAFIBUgJWAy8BNAMAAAAAAAAjACkDei1TRUxFQ1QgKiBGUk9NIHBlZGlkb3MgT1JERVIgQlkgY3JpYWRvX2VtIERFU0N6DnJlZ2lzdHJvcy5odG1s2gp0cmFuc2Fjb2VzKQdyBwAAANoGY3Vyc29y2gdleGVjdXRl2ghmZXRjaGFsbNoFY2xvc2VyCQAAANoQVGVtcGxhdGVSZXNwb25zZSkEcg4AAADaAmRichUAAAByFAAAAHMEAAAAJiAgIHIQAAAA2hBsaXN0YXJfcmVnaXN0cm9zchsAAAAJAAAAc1sAAACAAOQJD4sYgELYDQ+PWYlZi1uARtgECodOgU7QE0LUBEPYEReXH5Ef0xEigErYBAqHTIFMhE7YBAaHSIFIhErkCxTXCyXRCyWgZ9AvP8As0FBa0EFb0wtc0ARcchIAAABOKQ3aB2Zhc3RhcGlyAwAAAHIEAAAA2hFmYXN0YXBpLnJlc3BvbnNlc3IFAAAA2hJmYXN0YXBpLnRlbXBsYXRpbmdyBgAAANoIZGF0YWJhc2VyBwAAANoGcm91dGVycgkAAADaA2dldHIbAAAAqQByEgAAAHIQAAAA2gg8bW9kdWxlPnIjAAAAAQAAAHNGAAAA8AMBAQHfACbdACrdAC7dABvhCRKYKNQJI4AG2QwboGvUDDKACeABB4cagRqITKgcgBrTATb0AggBXQHzAwACN/ICCAFdAXISAAAA
```

---

