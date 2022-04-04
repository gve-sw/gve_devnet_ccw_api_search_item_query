# gve_devnet_ccw_api_search_item_query
prototype script that queries product items from CCW APIs


## Contacts
* Jorge Banegas

## Solution Components
* CCW APIs 
* CCW SearchItem API call


## Installation/Configuration

(optional) This first step is optional if the user wants to leverage a virtual environment to install python packages

```shell
pip install virtualenv
virtualenv env
source env/bin/activate
```

Install python dependencies 

```shell
pip install -r requirements.txt
```
Include configuration information inside the config.py file. Reference to this [documentation](https://apidocs-prod.cisco.com/explore;category=6083723925042e9035f6a74f;sgroup=6083723a25042e9035f6a756;epname=608372fb25042e9035f6a78c;isTestMode=on) for more details on how to authenticate. 

    client_id=""
    client_secret=""
    grant_type="password"
    username="email@domain.com"
    password=""
    
Edit the body.xml which is the soap envelope to make the API call. Reference to this [documentation](https://www.cisco.com/E-Learning/gbo-ccw/cdc_bulk/Cisco_Commerce_B2B_Implementation_Guides/Access_Authorization/CreateToken_API/CCW_API_Generate_Token_IG.pdf) on how to go about editing the envelope. 

## Usage

To launch script:


    $ python main.py
    
An ouput file called output.xml will be created displaying the query response. 

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.
