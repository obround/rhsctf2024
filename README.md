# CTF 2024
## Overview
On March 15, Cybersecurity Club at RHS held a Capture the Flag event. This repository contains the source code for the CTF's website on which the problems were solved.

Special thanks to https://render.com/ for hosting our website, database, and supporting services.

## Hosting on Render
 1. You will need to split up this repository into two: one for problem #4 and one for the website
 2. For problem #4 migrate the Dockerfile in `ctf/` to a seperate repository along with the `problem_4.jar`
 3. Create a seperate web service for problem #4
 4. Create a postgresql database on Render
 5. Replace all instances `REDACTED` with the respective URLs

## Building Locally
Certain strings in the code containing things like database URLs have been replaces with `REDACTED`:
 1. The problem #4 websocket URL will be a localhost (check what `websocketd` prints out when run)
 2. You will need a postgresql database to store the users
 3. If you don't have access to a postgres instance, you can either migrate django `ctfdb` to sqlite, or remove any storage and retrival of user information

Afterwards, run the following to build:
```
docker-compose up --build
```

## Gallery
<img width="1440" src="https://github.com/obround/rhsctf2024/assets/75817213/369e3844-5cdc-4df8-aac4-c945d9efc7a1">
<img width="1440" src="https://github.com/obround/rhsctf2024/assets/75817213/33609d2b-ed91-4241-b2ed-d4bfbec593a6">
<img width="1440" src="https://github.com/obround/rhsctf2024/assets/75817213/ae0e1148-ddc9-49ab-bc31-2ca361f26198">
<img width="1440" src="https://github.com/obround/rhsctf2024/assets/75817213/4af6acde-86d8-46ce-8876-252328d98868">
<img width="1440"  src="https://github.com/obround/rhsctf2024/assets/75817213/a26ec0cc-3506-423d-8dca-620a42b535da">
<img width="1440" src="https://github.com/obround/rhsctf2024/assets/75817213/d39fe050-e49b-469b-a1a9-15a7b754b48f">
<img width="1440" src="https://github.com/obround/rhsctf2024/assets/75817213/883d1095-f7a9-4079-8192-f50d8f3d0ac1">
