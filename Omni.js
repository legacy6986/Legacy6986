trixie292206021957
Repository navigation
Code
Issues
2
 (2)
Pull requests
1
 (1)
Discussions
trixie292206021957/core
/Omni.js
rickyplambert-seed
rickyplambert-seed
3 days ago
94 lines (93 loc) · 12.5 KB

Code

Blame
‎Omni‎
Original file line number	Diff line number	Diff line change
@@ -0,0 +1,84 @@
grep -r omni
grep: .cpan/Metadata: binary file matches
grep: .ollama/models/blobs/sha256-1278394b693672ac2799eadc9a83fd98259a6a88a40acfb1dcaa6c6fc895a606: binary file matches
grep: .git/objects/52/8f277e48ce196d53944b34c4a440eed0cee09f: binary file matchesgrep -r omni
grep: .cpan/Metadata: binary file matches
grep: .ollama/models/blobs/sha256-1278394b693672ac2799eadc9a83fd98259a6a88a40acfb1dcaa6c6fc895a606: binary file matches
grep: .git/objects/52/8f277e48ce196d53944b34c4a440eed0cee09f: binary file matches
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/clap_complete_nushell-4.6.0/Cargo.lock: "omnipath",
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/clap_complete_nushell-4.6.0/Cargo.lock:name = "omnipath"
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/chacha/asm/chacha-x86_64.pl:.type      se_handler,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/chacha/asm/chacha-x86_64.pl:.type      ssse3_handler,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/chacha/asm/chacha-x86_64.pl:.type      full_handler,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/cipher/asm/chacha20_poly1305_x86_64.pl:.type poly_hash_ad_internal,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/aes-gcm-avx2-x86_64.pl:.type $funcname,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/aesni-gcm-x86_64.pl:.type   _aesni_ctr32_ghash_6x,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/aesni-gcm-x86_64.pl:.type   aesni_gcm_decrypt,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/aesni-gcm-x86_64.pl:.type   _aesni_ctr32_6x,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/aesni-gcm-x86_64.pl:.type   aesni_gcm_encrypt,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/aesni-gcm-x86_64.pl:.type   aesni_gcm_encrypt,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/aesni-gcm-x86_64.pl:.type   aesni_gcm_decrypt,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/aesni-x86_64.pl:.type       _aesni_${dir}rypt2,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/aesni-x86_64.pl:.type       _aesni_${dir}rypt3,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/aesni-x86_64.pl:.type       _aesni_${dir}rypt4,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/aesni-x86_64.pl:.type       _aesni_${dir}rypt6,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/aesni-x86_64.pl:.type       _aesni_${dir}rypt8,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/aesni-x86_64.pl:# are used. Note that it's declared "abi-omnipotent", which means that
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/aesni-x86_64.pl:.type       ${PREFIX}_set_encrypt_key_base,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/aesni-x86_64.pl:.type       ${PREFIX}_set_encrypt_key_alt,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/aesni-x86_64.pl:.type       ctr_xts_se_handler,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/ghash-x86_64.pl:.type       gcm_init_clmul,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/ghash-x86_64.pl:.type       gcm_ghash_clmul,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/ghash-x86_64.pl:.type       gcm_init_avx,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/ghash-x86_64.pl:.type       gcm_ghash_avx,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/vpaes-x86_64.pl:.type       _vpaes_encrypt_core,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/vpaes-x86_64.pl:.type       _vpaes_encrypt_core_2x,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/vpaes-x86_64.pl:.type       _vpaes_schedule_core,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/vpaes-x86_64.pl:.type       _vpaes_schedule_round,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/vpaes-x86_64.pl:.type       _vpaes_schedule_transform,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/vpaes-x86_64.pl:.type       _vpaes_schedule_mangle,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/vpaes-x86_64.pl:.type       _vpaes_preheat,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/aes/asm/vpaes-x86_64.pl:.type       se_handler,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/bn/asm/x86_64-mont.pl:.type mul_handler,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/bn/asm/x86_64-mont.pl:.type sqr_handler,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/bn/asm/x86_64-mont5.pl:.type        mul4x_internal,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/bn/asm/x86_64-mont5.pl:.type        bn_sqr8x_internal,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/bn/asm/x86_64-mont5.pl:.type        __bn_post4x_internal,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/bn/asm/x86_64-mont5.pl:.type        mulx4x_internal,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/bn/asm/x86_64-mont5.pl:.type        bn_sqrx8x_internal,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/bn/asm/x86_64-mont5.pl:.type        __bn_postx4x_internal,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/bn/asm/x86_64-mont5.pl:.type        bn_scatter5,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/bn/asm/x86_64-mont5.pl:.type        bn_gather5,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/bn/asm/x86_64-mont5.pl:.type        mul_handler,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/ec/asm/p256-x86_64-asm.pl:.type     __ecp_nistz256_mul_montq,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/ec/asm/p256-x86_64-asm.pl:.type     __ecp_nistz256_sqr_montq,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/ec/asm/p256-x86_64-asm.pl:.type     __ecp_nistz256_mul_montx,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/ec/asm/p256-x86_64-asm.pl:.type     __ecp_nistz256_sqr_montx,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/ec/asm/p256-x86_64-asm.pl:.type     ecp_nistz256_select_w5_nohw,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/ec/asm/p256-x86_64-asm.pl:.type     ecp_nistz256_select_w7_nohw,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/ec/asm/p256-x86_64-asm.pl:.type     ecp_nistz256_select_w5_avx2,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/ec/asm/p256-x86_64-asm.pl:.type     ecp_nistz256_select_w7_avx2,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/ec/asm/p256-x86_64-asm.pl:.type     __ecp_nistz256_add_toq,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/ec/asm/p256-x86_64-asm.pl:.type     __ecp_nistz256_sub_fromq,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/ec/asm/p256-x86_64-asm.pl:.type     __ecp_nistz256_subq,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/ec/asm/p256-x86_64-asm.pl:.type     __ecp_nistz256_mul_by_2q,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/ec/asm/p256-x86_64-asm.pl:.type     __ecp_nistz256_add_tox,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/ec/asm/p256-x86_64-asm.pl:.type     __ecp_nistz256_sub_fromx,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/ec/asm/p256-x86_64-asm.pl:.type     __ecp_nistz256_subx,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/ec/asm/p256-x86_64-asm.pl:.type     __ecp_nistz256_mul_by_2x,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/ec/asm/p256-x86_64-asm.pl:.type     short_handler,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/ec/asm/p256-x86_64-asm.pl:.type     full_handler,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/sha/asm/sha512-x86_64.pl:.type      se_handler,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/fipsmodule/sha/asm/sha512-x86_64.pl:.type      shaext_handler,\@abi-omnipotent
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/perlasm/x86_64-xlate.pl:#    ".type name,@abi-omnipotent" instead.
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/perlasm/x86_64-xlate.pl:#    larger than 6, then you *have to* write "abi-omnipotent" code,
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/perlasm/x86_64-xlate.pl:    # Additionally, this only supports @abi-omnipotent functions. It is
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/perlasm/x86_64-xlate.pl:           die "SEH directives can only be used with \@abi-omnipotent";
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/perlasm/x86_64-xlate.pl:                                   } elsif ($type eq "\@abi-omnipotent") {
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/perlasm/x86_64-xlate.pl:                                   $$line =~ s/\@abi\-omnipotent/\@function/;
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/perlasm/x86_64-xlate.pl:# omnipotent_function:.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/perlasm/x86_64-xlate.pl:                                   $$line =~ s/\@abi\-omnipotent/\@function/;
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/ring-0.17.14/crypto/perlasm/x86_64-xlate.pl:# omnipotent_function:
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/platform-info-2.1.0/src/platform/windows.rs:/// `file_path` ~ if empty or `None`, default to the full path of "kernel32.dll" (a known, omnipresent, system file)
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/zip-7.2.0/src/read.rs:        let mut reader = ZipArchive::new(Cursor::new(include_bytes!("../tests/data/omni.ja")))?;
.cargo/registry/src/index.crates.io-1949cf8c6b5b557f/zip-8.5.1/src/read/zip_archive.rs:            ZipArchive::new(Cursor::new(include_bytes!("../../tests/data/omni.ja"))).unwrap();
grep: .gradle/caches/9.6.1/generated-gradle-jars/gradle-api-9.6.1.jar: binary file matches
0 commit comments
Comments
0
 (0)
Comment
You're not receiving notifications from this thread.
