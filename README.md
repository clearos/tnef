# tnef

Forked version of tnef with ClearOS changes applied

* git clone git+ssh://git@github.com/clearos/tnef.git
* cd tnef
* git checkout epel7
* git remote add upstream git://pkgs.fedoraproject.org/tnef.git
* git pull upstream epel7
* git checkout clear7
* git merge --no-commit epel7
* git commit
