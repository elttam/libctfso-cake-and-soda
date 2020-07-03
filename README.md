# Overview

libctfso-cake-and-soda is a bundle of Linux CTF challenges requiring
reverse engineering and some crypto knowledge to solve.

Works out of the box on my machine, YMMV - PR's welcome.

# Prerequisites

To use this bundle you should have [Vagrant](https://www.vagrantup.com)
installed along with one of the following hypervisors:

* Virtualbox
* Hyper-V
* Parallels
* libvirt+QEMU
* VMWare Desktop (should work but not tested)

If you know what you're doing and prefer to manage deployment yourself, you can
simply run the [Ansible](https://www.ansible.com/)
[playbook](./ansible/site.yml) on a [Ubuntu Xenial
amd64](http://releases.ubuntu.com/xenial/) target.

## Notes

If you are using Parallels or libvirt+QEMU, please ensure you have `rsync`
installed locally.

If this is your first time using Vagrant with libvirt, please run `vagrant
plugin install vagrant-libvirt`.

If this is your first time using Vagrant with Parallels, please run `vagrant
plugin install vagrant-parallels`.

If this is your first time using Vagrant with Hyper-V, please run all commands
from an Administrator console. In addition, you will be asked to enter your
Windows username/password to enable shared folder support for provisioning.

# Usage

The following command will download a Ubuntu 16.04 VM template from VagrantHub,
create a new virtual machine for 'libctfso-cake-and-soda', and build/install
challenges under the `/challenges` directory of the VM:

**Note:** This can take a while the first time you run it depending on your host
specs and internet connection.

```sh
vagrant up
```

You can re-provision anytime with:

```sh
vagrant provision
```

You can connect to the virtual machine with:

```sh
vagrant ssh
```

This will login to the virtual machine using the 'vagrant' user account,
which has `sudo` privileges so that you can install any additional packages that
you want.

You can stop the virtual machine with:

```sh
vagrant halt
```

And delete the virtual machine with:

```sh
vagrant destroy
```

# Challenges

You should switch to the 'hahn' user account (password = 'hahn') when you are
ready to play:

```sh
su - hahn
```

All challenges can be found under the `/challenges/` directory.

Difficulty estimates are relative to other challenges in this bundle.

---

**Title:** coca-cola  
**Category:** Crypto  
**Flag:** `libctf{d8d07554-c34c-4944-96ae-d7e285391694}`  
**Relative Difficulty:** Easy  

---

**Title:** dr-pepper  
**Category:** Crypto  
**Flag:** `libctf{2946adf1-cd78-4346-8b07-aa84c8cf7279}`  
**Relative Difficulty:** Easy  

---

**Title:** mcarthur-river  
**Category:** Reversing  
**Flag:** `libctf{dc11f7e1-599e-4ca2-8c15-940247455aaa}`  
**Relative Difficulty:** Easy  

---

**Title:** olympic-dam  
**Category:** Reversing  
**Flag:** `libctf{8eb6767f-9440-44da-9c3a-57cb210f441e}`  
**Relative Difficulty:** Medium  

---

**Title:** ranger  
**Category:** Reversing  
**Flag:** `libctf{16ebc76c-37ce-4f20-8a01-e3343653a5fb}`  
**Relative Difficulty:** Medium  

---

**Title:** arlit  
**Category:** Reversing  
**Flag:** `libctf{5910c360-5d46-41f9-b1ab-eb2f2df03ea5}`  
**Relative Difficulty:** Hard  

---

# Hints

Each challenge directory should have everything you need to figure out a plan of
attack. Looking at the source code in the repo will ruin the challenge.

