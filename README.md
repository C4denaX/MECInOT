# MECInOT: A Multi-Access Edge Computing and Industrial Internet of Things Emulator for the modelling and study of cybersecurity threads


MECInOT is emulator for the design and deployment of different kind of scenarios which involve IIoT and MEC technologies.

### Pre-requisites

- Host with Linux Distribution (Ubuntu, Debian, Fedora, Linux Mint...) with the last [Docker/Docker-Compose](https://docs.docker.com/engine/install/centos/ "Docker/Docker-Compose") installed

- openLEON virtual machine which is avaliable on their own [website](https://openleon.networks.imdea.org/ "website")

### Installation

- On both hosts clone this repository with the following command:

```console
git clone https://github.com/C4denaX/MECInOT.git
```
- It is recommend first launch openLEON MEC topology to do that, the steps to follow are:
```console
cd mininet/custom
sudo python datacenterTest.py
```
To access to a specific host
```console
xterm hX (X is a number between 0-63, which are the Edge Server host which deploy Mininet)
```
Once in the host, it is possible to access to the repository pulled and run the specific service.

- On Linux Host, where the IIoT topology and Docker-Compose will be run, firstly it is neccesary to establish communication with MEC private network with a new network route:

```console
sudo ip route add 10.0.0.0/12 via <openLEON_IP_machine> dev <interface>

to run an specific pre-made scenario the steps are:
```console
cd directory_to_dockercomposefile.yml
docker-compose up
docker-compose exec attacker_node_name bash (to access to the bash of the malicious machine)
```
