# Joern Workshop

This workshop consists of 3 modules covering various concepts around Interactive Code Analysis using [Joern](http://joern.io). We use VLC v3.0.12 as the primary target application along with a few memory allocation examples present in this repo. The workshop outline is as follows:

1. **`Familiarization`: CPG and Joern Quickstart** : Understand what Code Property graph (CPG) is and how Joern can create one
2. **`Module 1`: Code Navigation & Insights** : Basic navigation (searching functions, types, call-sites) and obtaining insights about code and rule violations using Joern
2. **`Module 2`: Hunting Bugs** : Explore and learn about possible memory allocation related bugs
3. **`Module 3`: Finding Vulnerabilities in VLC** : Start developing queries for hunting bugs in VLC
4. **`Activity`: Open-ended Bug Hunt**: Use Joern To find _possible vulnerabilties_ in VLC (one close case and one recent disclosure) or open-ended search in any other tool with Q& A support


## Workshop Guide
Use the workshop presentation which also doubles as a step by step modular workshop guide: [`RSA-LAB2-R08.pdf`](RSA-LAB2-R08.pdf) The various modules are marked in the slides and contain all the commands presented in the workshop. You can directly copy/paste and run them on the Joern shell. This repo also contains scripts that are discussed in Module 3

## Preparation

* Clone Workshop Repo
  * `git clone https://github.com/joernio/workshops`
  * `cd workshops/2021-RSA` 
  * `apt install source-highlight graphviz unzip`

* Download  Joern and install it
  * `wget https://github.com/joernio/joern/releases/latest/download/joern-install.sh`
  * `chmod +x ./joern-install.sh`
  * `sudo ./joern-install.sh`

* Download VLC v3.0.12 source and extract in workshop directory
  * `wget http://get.videolan.org/vlc/3.0.12/vlc-3.0.12.tar.xz`
  * `tar -xvf vlc-3.0.12.tar.xz`

* Machine Requirements
  * At least 5-7GB free RAM (close as many browser tabs as possible, pkill slack etc)
  * At least 4 CPUs (preferably modern)
  * OpenJDK 1.8+

## Important Links

* Joern Docs: https://docs.joern.io
* Query Database: https://queries.joern.io

## Support Channel
Live support during workshop is provided in the `#rsa-lab2-r08` channel on the Joern.io Discord server 