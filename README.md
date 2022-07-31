# linux-profile

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

**RESOURCES**
- GitHub: https://github.com/MyLinuxProfile/linux-profile-pypi
- Docs:   https://linuxprofile.com
