ansible-role-linux-users-helper
===============================

[travis-badge]: https://img.shields.io/travis/9fv/ansible-role-linux-users-helper/master.svg?label=TravisCI
[travis-badge-url]: https://travis-ci.org/9fv/ansible-role-linux-users-helper

An [Ansible](https://www.ansible.com) An Ansible role to help managing users on Linux systems.

[![TravisCI Build Status][travis-badge]][travis-badge-url]

## Table of Contents

* [Synopsis](#synopsis)
* [Usage](#usage)
* [Installation](#installation)
* [Tests](#tests)
* [Compatibility](#compatibility)
* [Issues](#issues)
* [Contributing](#contributing)
* [Credits](#credits)
* [History](#history)
* [License](#license)

## <a name="synopsis"> Synopsis

An [Ansible](https://www.ansible.com) An Ansible role to help managing users on Linux systems.

## <a name="usage"> Usage

Add a list of users into vars as below:

```yaml
role_users_helper:
  users:
    - username: user1
      password: mysecretpassword
      state: present
    - username: user2
      password: mysecretpassword
      shell: /bin/sh
    - username: user3
      password: mysecretpassword
      state: absent
```

**Recommanded:** Please encrypt your passwords into an [Ansible Vault](https://docs.ansible.com/ansible/2.6/user_guide/vault.html) for better security.

Create a `playbook.yml`

```yaml
- hosts: all
  tasks:
    - import_role:
        name: 9fv_io.linux_users_helper
```

Run the playbook:

```bash
ansible-playbook -i inventory playbook.yml -vvv
```

## <a name="installation"> Installation

```bash
ansible-galaxy install 9fv_io.linux_users_helper
```

## <a name="test"> Tests

Please install prealably [Molecule](https://molecule.readthedocs.io/en/latest/):

```bash
pip install molecule
```

Then run:

```bash
molecule --debug test
```

## <a name="compatibility"> Compatibility

* [Ansible](https://www.ansible.com) >= v2.6
* Supposedly all distributions and GNU / Linux versions.

## <a name="issues"> Issues

Feel free to [submit issues](https://github.com/9fv/ansible-role-linux-users-helper/issues) and enhancement requests.

## <a name="contributing"> Contributing

Please refer to project's style guidelines and guidelines for submitting patches and additions. In general, we follow the "fork-and-pull" Git workflow.

 1. **Fork** the repo on GitHub
 2. **Clone** the project to your own machine
 3. **Commit** changes to your own branch
 4. **Push** your work back up to your fork
 5. Submit a **Pull request** so that we can review your changes

**NOTE**: Be sure to merge the latest from "upstream" before making a pull request!

## <a name="credits"> Credits

### Thanks to the developers of the very useful dependencies...

* [Ansible](https://github.com/ansible/ansible)
* [Ansible Galaxy](https://github.com/ansible/galaxy)
* [Molecule](https://github.com/metacloud/molecule)

## <a name="history"> History

Please refer to [the changelog file](CHANGELOG.md).

## <a name="license"> License

>
> [The MIT License](https://opensource.org/licenses/MIT)
>
> Copyright (c) 2018 [SAS 9 Février](https://9fevrier.com/)
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
>AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.
>
