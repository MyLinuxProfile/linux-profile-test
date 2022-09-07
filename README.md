# linux-profile
![GitHub Org's stars](https://img.shields.io/github/stars/MyLinuxProfile?label=LinuxProfile&style=flat-square)
![GitHub](https://img.shields.io/github/license/MyLinuxProfile/linux-profile?color=black&style=flat-square)
![GitHub last commit](https://img.shields.io/github/last-commit/MyLinuxProfile/linux-profile?style=flat-square)
![GitHub Pipenv locked Python version](https://img.shields.io/github/pipenv/locked/python-version/MyLinuxProfile/linux-profile?style=flat-square)

# Introduction
Linux Profile is a linux profile management tool.


### Characteristics and objectives for the project:
- Saving your current plasma customization
    - Theme
    - Window decoration
    - Colors
    - Icons
    - Wallpapers
    - Layout disposition
    - Widgets
- Saving configurations
    - Alias
    - Scripts
    - Packages
- Save and restore your latte-dock customization per save
- Explort and import customizations. For transfer to another computer or backup them.

# Help

## Commands

| #      | Command                        | Argument              | Param           |
|--------|:-------------------------------|:----------------------|:----------------|
| 01     | ``linux_profile init``         | ``login``, ``create`` |--email --token  |
| 02     | ``linux_profile commit``       | ``all``               |                 |
| 03     | ``linux_profile pull``         | ``all``               |                 |
| 04     | ``linux_profile push``         | ``all``               |                 |
| 05     | ``linux_profile apply``        | ``all``               |                 |

## Description
- 01 - Initial configuration of profile files and server connection.
  - **Example**: 
    - ``linux_profile init login --email email@linuxprofile.com --token WKB62dMYod``
    - ``linux_profile init create --email email@linuxprofile.com``
- 02 - Saves the current computer settings in the local configuration file.
  - **Example**: 
    - ``linux_profile commit all``
- 03 - It pulls all the settings from the cloud and saves it to the local settings.
  - **Example**: 
    - ``linux_profile pull all``
- 04 - Push all local settings to the cloud.
  - **Example**: 
    - ``linux_profile push all``
- 05 - Applies computer profile settings based on local information.
  - **Example**: 
    - ``linux_profile apply all``

## Download

| Method  | Command                                                                                                    |
|-------- |:-----------------------------------------------------------------------------------------------------------|
| Git     | ``git clone https://github.com/MyLinuxProfile/linux-profile.git ~/.linux_profile --branch master``         |

**RESOURCES**
- GitHub: https://github.com/MyLinuxProfile/linux-profile
- Docs:   https://linuxprofile.com
