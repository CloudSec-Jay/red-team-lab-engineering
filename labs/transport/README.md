# Transport trust lab

The archived OpenSSL lab defines an isolated `192.168.100.0/24` network with three roles: a root CA, a TLS server, and an mTLS client. Its purpose is to compare server-only TLS with mutual authentication and examine trust failures without internet exposure.

The source includes CA, server-certificate, client-certificate, and VM-provisioning scripts. This repository records the design as `source-lab`; it does not claim a current successful run because no evidence bundle was migrated.

The next run should capture certificate metadata, handshake results, expected rejection without a client certificate, synchronized timestamps, and teardown confirmation. Private keys must never enter the evidence directory.
